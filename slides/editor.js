/**
 * URIKAI Slide Editor v2
 * Ctrl+E: 編集モード ON/OFF
 * 編集モード中:
 *   - テキスト/画像/SVG要素をドラッグで移動
 *   - テキストをダブルクリックで編集
 *   - 画像の角をドラッグでリサイズ
 *   - Delete/Backspaceで選択要素を削除
 *   - Ctrl+S で保存（HTMLダウンロード）
 *   - Ctrl+Z で直前の操作を元に戻す
 */
(function() {
    let editMode = false;
    let selected = null;
    let dragging = null;
    let resizing = null;
    let startX, startY, origX, origY, origW, origH;
    let undoStack = [];
    let indicator = null;
    let toolbar = null;

    // ===== Indicator =====
    function showMsg(text, color, duration) {
        if (!indicator) {
            indicator = document.createElement('div');
            indicator.style.cssText = 'position:fixed;top:10px;left:50%;transform:translateX(-50%);z-index:99999;padding:8px 24px;border-radius:8px;font-family:sans-serif;font-size:14px;font-weight:700;pointer-events:none;transition:opacity 0.3s;';
            document.body.appendChild(indicator);
        }
        indicator.textContent = text;
        indicator.style.background = color || '#0a2f5c';
        indicator.style.color = '#fff';
        indicator.style.opacity = '1';
        clearTimeout(indicator._t);
        indicator._t = setTimeout(() => indicator.style.opacity = '0', duration || 3000);
    }

    // ===== Toolbar =====
    function createToolbar() {
        if (toolbar) return;
        toolbar = document.createElement('div');
        toolbar.id = 'editor-toolbar';
        toolbar.style.cssText = 'position:fixed;bottom:20px;left:50%;transform:translateX(-50%);z-index:99998;display:flex;gap:8px;padding:10px 16px;background:#1a1a2e;border:2px solid #d4a537;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.5);font-family:sans-serif;';
        toolbar.innerHTML = `
            <span style="color:#d4a537;font-size:13px;font-weight:700;margin-right:8px;line-height:32px;">編集モード</span>
            <button data-action="save" style="padding:6px 16px;background:#27ae60;color:#fff;border:none;border-radius:6px;font-size:12px;font-weight:700;cursor:pointer;">💾 保存 (Ctrl+S)</button>
            <button data-action="undo" style="padding:6px 16px;background:#2e86c1;color:#fff;border:none;border-radius:6px;font-size:12px;font-weight:700;cursor:pointer;">↩ 戻す (Ctrl+Z)</button>
            <button data-action="delete" style="padding:6px 16px;background:#e74c3c;color:#fff;border:none;border-radius:6px;font-size:12px;font-weight:700;cursor:pointer;">🗑 削除 (Del)</button>
            <button data-action="exit" style="padding:6px 16px;background:#556;color:#fff;border:none;border-radius:6px;font-size:12px;font-weight:700;cursor:pointer;">✕ 終了 (Ctrl+E)</button>
        `;
        document.body.appendChild(toolbar);
        toolbar.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                if (action === 'save') saveHTML();
                else if (action === 'undo') undo();
                else if (action === 'delete') deleteSelected();
                else if (action === 'exit') toggleEdit();
            });
        });
    }

    function removeToolbar() {
        if (toolbar) { toolbar.remove(); toolbar = null; }
    }

    // ===== Edit Mode =====
    function toggleEdit() {
        editMode = !editMode;
        if (editMode) {
            createToolbar();
            initEditable();
            showMsg('編集モード ON ── ドラッグ移動 / ダブルクリック編集 / 画像角でリサイズ', '#d4a537', 4000);
        } else {
            removeToolbar();
            clearSelection();
            document.querySelectorAll('.editor-handle').forEach(h => h.remove());
            document.querySelectorAll('[data-editable]').forEach(el => {
                el.style.outline = '';
                el.style.cursor = '';
            });
            showMsg('編集モード OFF', '#556', 2000);
        }
    }

    function initEditable() {
        // All elements inside slides that can be edited
        document.querySelectorAll('.slide').forEach(slide => {
            // Text elements
            slide.querySelectorAll('li, .pbox, h2, .srow .lbl, .srow .val, p').forEach(el => {
                el.setAttribute('data-editable', 'text');
                el.style.cursor = 'move';
            });
            // Images
            slide.querySelectorAll('img').forEach(el => {
                el.setAttribute('data-editable', 'image');
                el.style.cursor = 'move';
                el.draggable = false;
            });
            // SVG elements
            slide.querySelectorAll('svg text, svg rect, svg circle, svg line, svg polyline').forEach(el => {
                el.setAttribute('data-editable', 'svg');
                el.style.cursor = 'move';
            });
            // Absolute positioned divs (overlay labels)
            slide.querySelectorAll('div[style*="position:absolute"], div[style*="position: absolute"]').forEach(el => {
                el.setAttribute('data-editable', 'overlay');
                el.style.cursor = 'move';
            });
        });
    }

    // ===== Selection =====
    function selectElement(el) {
        clearSelection();
        selected = el;
        const type = el.getAttribute('data-editable');
        if (type === 'image') {
            el.style.outline = '3px solid #d4a537';
            addResizeHandles(el);
        } else if (type === 'svg') {
            el.style.outline = '2px solid #d4a537';
        } else {
            el.style.outline = '2px dashed #d4a537';
            el.style.outlineOffset = '2px';
        }
    }

    function clearSelection() {
        if (selected) {
            selected.style.outline = '';
            selected.style.outlineOffset = '';
        }
        document.querySelectorAll('.editor-handle').forEach(h => h.remove());
        selected = null;
    }

    // ===== Resize Handles for Images =====
    function addResizeHandles(img) {
        document.querySelectorAll('.editor-handle').forEach(h => h.remove());
        const parent = img.offsetParent || img.parentElement;

        ['nw','ne','sw','se'].forEach(pos => {
            const handle = document.createElement('div');
            handle.className = 'editor-handle';
            handle.dataset.pos = pos;
            handle.style.cssText = `position:absolute;width:14px;height:14px;background:#d4a537;border:2px solid #fff;border-radius:3px;cursor:${pos}-resize;z-index:99997;`;

            const rect = img.getBoundingClientRect();
            const pRect = parent.getBoundingClientRect();

            if (pos.includes('n')) handle.style.top = (rect.top - pRect.top - 7) + 'px';
            else handle.style.top = (rect.bottom - pRect.top - 7) + 'px';
            if (pos.includes('w')) handle.style.left = (rect.left - pRect.left - 7) + 'px';
            else handle.style.left = (rect.right - pRect.left - 7) + 'px';

            parent.style.position = 'relative';
            parent.appendChild(handle);

            handle.addEventListener('mousedown', (e) => {
                e.preventDefault();
                e.stopPropagation();
                resizing = { img, pos, startX: e.clientX, startY: e.clientY };
                origW = img.offsetWidth;
                origH = img.offsetHeight;
                saveUndo(img, 'resize');
            });
        });
    }

    // ===== Drag =====
    function onMouseDown(e) {
        if (!editMode) return;

        const el = e.target.closest('[data-editable]');
        if (!el) { clearSelection(); return; }

        e.preventDefault();
        selectElement(el);
        dragging = el;
        startX = e.clientX;
        startY = e.clientY;

        const type = el.getAttribute('data-editable');
        if (type === 'svg') {
            const svg = el.closest('svg');
            const pt = svg.createSVGPoint();
            pt.x = e.clientX; pt.y = e.clientY;
            const svgPt = pt.matrixTransform(svg.getScreenCTM().inverse());
            origX = parseFloat(el.getAttribute('x') || el.getAttribute('cx') || el.getAttribute('x1') || 0);
            origY = parseFloat(el.getAttribute('y') || el.getAttribute('cy') || el.getAttribute('y1') || 0);
            dragging._svgStart = svgPt;
            if (el.tagName === 'line') {
                dragging._origX2 = parseFloat(el.getAttribute('x2'));
                dragging._origY2 = parseFloat(el.getAttribute('y2'));
            }
            if (el.tagName === 'polyline') {
                dragging._origPoints = el.getAttribute('points');
            }
        } else if (type === 'overlay') {
            origX = parseFloat(el.style.left) || 0;
            origY = parseFloat(el.style.top) || 0;
        } else if (type === 'image') {
            const rect = el.getBoundingClientRect();
            origX = rect.left;
            origY = rect.top;
        }

        saveUndo(el, 'move');
    }

    function onMouseMove(e) {
        // Handle resize
        if (resizing) {
            e.preventDefault();
            const dx = e.clientX - resizing.startX;
            const dy = e.clientY - resizing.startY;
            let newW = origW;

            if (resizing.pos.includes('e')) newW = origW + dx;
            else if (resizing.pos.includes('w')) newW = origW - dx;

            newW = Math.max(50, newW);
            resizing.img.style.maxWidth = newW + 'px';
            resizing.img.style.width = newW + 'px';
            resizing.img.style.height = 'auto';

            // Update handles
            addResizeHandles(resizing.img);
            showMsg(`画像サイズ: ${newW}px`, '#0a2f5c', 1000);
            return;
        }

        if (!dragging || !editMode) return;
        e.preventDefault();

        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        const type = dragging.getAttribute('data-editable');

        if (type === 'svg') {
            const svg = dragging.closest('svg');
            const pt = svg.createSVGPoint();
            pt.x = e.clientX; pt.y = e.clientY;
            const svgPt = pt.matrixTransform(svg.getScreenCTM().inverse());
            const sdx = svgPt.x - dragging._svgStart.x;
            const sdy = svgPt.y - dragging._svgStart.y;

            const tag = dragging.tagName;
            if (tag === 'text' || tag === 'rect') {
                dragging.setAttribute('x', Math.round(origX + sdx));
                dragging.setAttribute('y', Math.round(origY + sdy));
            } else if (tag === 'circle') {
                dragging.setAttribute('cx', Math.round(origX + sdx));
                dragging.setAttribute('cy', Math.round(origY + sdy));
            } else if (tag === 'line') {
                dragging.setAttribute('x1', Math.round(origX + sdx));
                dragging.setAttribute('y1', Math.round(origY + sdy));
                dragging.setAttribute('x2', Math.round(dragging._origX2 + sdx));
                dragging.setAttribute('y2', Math.round(dragging._origY2 + sdy));
            } else if (tag === 'polyline') {
                const pts = dragging._origPoints.trim().split(/[\s,]+/);
                const newPts = [];
                for (let i = 0; i < pts.length; i += 2) {
                    newPts.push(Math.round(parseFloat(pts[i]) + sdx) + ',' + Math.round(parseFloat(pts[i+1]) + sdy));
                }
                dragging.setAttribute('points', newPts.join(' '));
            }
        } else if (type === 'overlay') {
            const parent = dragging.parentElement.getBoundingClientRect();
            const newLeft = origX + (dx / parent.width) * 100;
            const newTop = origY + (dy / parent.height) * 100;
            dragging.style.left = newLeft.toFixed(1) + '%';
            dragging.style.top = newTop.toFixed(1) + '%';
            dragging.style.right = '';
            dragging.style.bottom = '';
        } else if (type === 'image') {
            // Move image by adjusting margin
            dragging.style.marginLeft = dx + 'px';
            dragging.style.marginTop = dy + 'px';
        }
    }

    function onMouseUp() {
        dragging = null;
        resizing = null;
    }

    // ===== Double-click to Edit Text =====
    function onDblClick(e) {
        if (!editMode) return;
        const el = e.target.closest('[data-editable="text"], [data-editable="overlay"]');
        if (!el) return;

        e.preventDefault();
        saveUndo(el, 'edit');

        el.contentEditable = true;
        el.focus();
        el.style.outline = '2px solid #27ae60';
        el.style.background = 'rgba(39,174,96,0.1)';

        const finish = () => {
            el.contentEditable = false;
            el.style.background = '';
            selectElement(el);
            el.removeEventListener('blur', finish);
        };
        el.addEventListener('blur', finish);

        // Also handle Enter key to finish editing
        el.addEventListener('keydown', (ev) => {
            if (ev.key === 'Enter' && !ev.shiftKey) {
                ev.preventDefault();
                el.blur();
            }
        }, { once: true });

        showMsg('テキスト編集中 ── Enterで確定', '#27ae60', 3000);
    }

    // Also support SVG text editing
    function onSvgDblClick(e) {
        if (!editMode) return;
        const el = e.target;
        if (el.tagName !== 'text' || !el.closest('svg')) return;

        e.preventDefault();
        saveUndo(el, 'edit');

        const newText = prompt('テキストを編集:', el.textContent);
        if (newText !== null) {
            el.textContent = newText;
        }
    }

    // ===== Delete =====
    function deleteSelected() {
        if (!selected) return;
        saveUndo(selected, 'delete');
        selected.style.display = 'none';
        showMsg('要素を非表示にしました（Ctrl+Zで戻す）', '#e74c3c', 3000);
        clearSelection();
    }

    // ===== Undo =====
    function saveUndo(el, action) {
        undoStack.push({
            el,
            action,
            html: el.outerHTML,
            display: el.style.display,
            attrs: {
                x: el.getAttribute && el.getAttribute('x'),
                y: el.getAttribute && el.getAttribute('y'),
                cx: el.getAttribute && el.getAttribute('cx'),
                cy: el.getAttribute && el.getAttribute('cy'),
                style: el.getAttribute && el.getAttribute('style'),
                points: el.getAttribute && el.getAttribute('points'),
            },
            maxWidth: el.style.maxWidth,
            width: el.style.width,
            marginLeft: el.style.marginLeft,
            marginTop: el.style.marginTop,
        });
        if (undoStack.length > 50) undoStack.shift();
    }

    function undo() {
        if (undoStack.length === 0) { showMsg('元に戻せる操作がありません', '#556', 2000); return; }
        const state = undoStack.pop();
        const el = state.el;

        if (state.action === 'delete') {
            el.style.display = state.display || '';
        } else if (state.action === 'resize') {
            el.style.maxWidth = state.maxWidth;
            el.style.width = state.width;
        } else if (state.action === 'move') {
            if (state.attrs.x !== null && el.setAttribute) el.setAttribute('x', state.attrs.x);
            if (state.attrs.y !== null && el.setAttribute) el.setAttribute('y', state.attrs.y);
            if (state.attrs.cx !== null && el.setAttribute) el.setAttribute('cx', state.attrs.cx);
            if (state.attrs.cy !== null && el.setAttribute) el.setAttribute('cy', state.attrs.cy);
            if (state.attrs.points !== null && el.setAttribute) el.setAttribute('points', state.attrs.points);
            if (state.attrs.style !== null && el.setAttribute) el.setAttribute('style', state.attrs.style);
            el.style.marginLeft = state.marginLeft || '';
            el.style.marginTop = state.marginTop || '';
        } else if (state.action === 'edit') {
            el.outerHTML = state.html;
        }

        showMsg('元に戻しました', '#2e86c1', 2000);
    }

    // ===== Save =====
    function saveHTML() {
        const fullHTML = '<!DOCTYPE html>\n' + document.documentElement.outerHTML;
        const blob = new Blob([fullHTML], { type: 'text/html' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        const path = window.location.pathname;
        a.download = path.substring(path.lastIndexOf('/') + 1);
        a.click();
        URL.revokeObjectURL(url);
        showMsg('保存しました ── slidesフォルダに上書きしてください', '#27ae60', 4000);
    }

    // ===== Keyboard =====
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'e') { e.preventDefault(); toggleEdit(); }
        if (e.ctrlKey && e.key === 's' && editMode) { e.preventDefault(); saveHTML(); }
        if (e.ctrlKey && e.key === 'z' && editMode) { e.preventDefault(); undo(); }
        if ((e.key === 'Delete' || e.key === 'Backspace') && editMode && selected && !selected.isContentEditable) {
            e.preventDefault(); deleteSelected();
        }
    });

    // ===== Mouse Events =====
    document.addEventListener('mousedown', onMouseDown);
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
    document.addEventListener('dblclick', onDblClick);
    document.addEventListener('dblclick', onSvgDblClick);

})();
