/**
 * SVG Element Drag Editor
 * Press Ctrl+E to toggle edit mode
 * In edit mode: drag any SVG text, rect, or circle element
 * Press Ctrl+C in edit mode to copy all changes as JSON
 */
(function() {
    let editMode = false;
    let dragging = null;
    let offsetX = 0, offsetY = 0;
    let changes = {};
    let indicator = null;

    function createIndicator() {
        indicator = document.createElement('div');
        indicator.style.cssText = 'position:fixed;top:10px;left:50%;transform:translateX(-50%);z-index:99999;padding:8px 20px;border-radius:8px;font-family:sans-serif;font-size:14px;font-weight:700;transition:opacity 0.3s;pointer-events:none;';
        document.body.appendChild(indicator);
    }

    function showIndicator(text, color) {
        if (!indicator) createIndicator();
        indicator.textContent = text;
        indicator.style.background = color;
        indicator.style.color = '#fff';
        indicator.style.opacity = '1';
        clearTimeout(indicator._t);
        indicator._t = setTimeout(() => { indicator.style.opacity = '0'; }, 3000);
    }

    function getSVGPoint(svg, evt) {
        const pt = svg.createSVGPoint();
        pt.x = evt.clientX;
        pt.y = evt.clientY;
        return pt.matrixTransform(svg.getScreenCTM().inverse());
    }

    function makeEditable(el) {
        el.style.cursor = 'move';
        el.setAttribute('data-editable', 'true');
        // Highlight on hover
        el.addEventListener('mouseenter', () => {
            if (!editMode) return;
            el._origOpacity = el.getAttribute('opacity') || '1';
            el.style.outline = '2px solid #d4a537';
            el.style.outlineOffset = '2px';
        });
        el.addEventListener('mouseleave', () => {
            if (!editMode) return;
            el.style.outline = '';
        });
    }

    function initEditMode() {
        // SVG elements
        document.querySelectorAll('svg').forEach(svg => {
            svg.querySelectorAll('text, rect, circle, line, polyline, polygon, path').forEach(el => {
                makeEditable(el);
            });
        });
        // HTML overlay labels (absolute positioned divs over images)
        document.querySelectorAll('.vis div[style*="position:absolute"], .vis div[style*="position: absolute"]').forEach(el => {
            el.style.cursor = 'move';
            el.setAttribute('data-html-editable', 'true');
        });
    }

    function onMouseDown(e) {
        if (!editMode) return;
        const el = e.target;
        if (!el.closest('svg') || !el.getAttribute('data-editable')) return;

        e.preventDefault();
        dragging = el;
        const svg = el.closest('svg');
        const pt = getSVGPoint(svg, e);
        dragging._startPt = pt;

        // Store original positions for all element types
        const tag = el.tagName;
        if (tag === 'line') {
            dragging._origX1 = parseFloat(el.getAttribute('x1') || 0);
            dragging._origY1 = parseFloat(el.getAttribute('y1') || 0);
            dragging._origX2 = parseFloat(el.getAttribute('x2') || 0);
            dragging._origY2 = parseFloat(el.getAttribute('y2') || 0);
        } else if (tag === 'polyline' || tag === 'polygon') {
            dragging._origPoints = el.getAttribute('points');
        } else if (tag === 'path') {
            dragging._origD = el.getAttribute('d');
        } else {
            const x = parseFloat(el.getAttribute('x') || el.getAttribute('cx') || 0);
            const y = parseFloat(el.getAttribute('y') || el.getAttribute('cy') || 0);
            offsetX = pt.x - x;
            offsetY = pt.y - y;
        }
    }

    function onMouseMove(e) {
        if (!dragging || !editMode) return;
        e.preventDefault();

        const svg = dragging.closest('svg');
        const pt = getSVGPoint(svg, e);
        const dx = Math.round(pt.x - dragging._startPt.x);
        const dy = Math.round(pt.y - dragging._startPt.y);
        const tag = dragging.tagName;

        if (tag === 'text' || tag === 'rect') {
            const newX = Math.round(pt.x - offsetX);
            const newY = Math.round(pt.y - offsetY);
            dragging.setAttribute('x', newX);
            dragging.setAttribute('y', newY);
        } else if (tag === 'circle') {
            const newX = Math.round(pt.x - offsetX);
            const newY = Math.round(pt.y - offsetY);
            dragging.setAttribute('cx', newX);
            dragging.setAttribute('cy', newY);
        } else if (tag === 'line') {
            dragging.setAttribute('x1', Math.round(dragging._origX1 + dx));
            dragging.setAttribute('y1', Math.round(dragging._origY1 + dy));
            dragging.setAttribute('x2', Math.round(dragging._origX2 + dx));
            dragging.setAttribute('y2', Math.round(dragging._origY2 + dy));
        } else if (tag === 'polyline' || tag === 'polygon') {
            const origPts = dragging._origPoints.trim().split(/[\s,]+/);
            const newPts = [];
            for (let i = 0; i < origPts.length; i += 2) {
                newPts.push(Math.round(parseFloat(origPts[i]) + dx) + ',' + Math.round(parseFloat(origPts[i+1]) + dy));
            }
            dragging.setAttribute('points', newPts.join(' '));
        } else if (tag === 'path') {
            // Translate path by wrapping in transform
            dragging.setAttribute('transform', `translate(${dx},${dy})`);
        }

        // Track the change
        const slideEl = dragging.closest('[data-s]');
        const slideNum = slideEl ? slideEl.getAttribute('data-s') : '?';
        const text = dragging.textContent || tag;
        const key = `slide${slideNum}_${tag}_${text.substring(0,15)}_${Math.random().toString(36).substr(2,4)}`;
        changes[key] = { slide: slideNum, tag, text: text.substring(0,20), dx, dy };

        showIndicator(`${tag} → dx:${dx} dy:${dy}`, '#0a2f5c');
    }

    function onMouseUp() {
        dragging = null;
    }

    function copyChanges() {
        const json = JSON.stringify(changes, null, 2);
        navigator.clipboard.writeText(json).then(() => {
            showIndicator(`変更をコピーしました（${Object.keys(changes).length}件）`, '#27ae60');
        }).catch(() => {
            console.log('=== SVG CHANGES ===');
            console.log(json);
            showIndicator('コンソールに出力しました（Ctrl+Shift+J）', '#d4a537');
        });
    }

    function saveChanges() {
        // Get the current slide HTML and save it directly
        const slideArea = document.querySelector('.slide-area');
        if (!slideArea) return;

        // Get the full page HTML with current modifications
        const fullHTML = '<!DOCTYPE html>\n' + document.documentElement.outerHTML;

        // Remove editor.js script tag from saved version to keep it clean
        // (it will be re-added on next load)

        // Create download
        const blob = new Blob([fullHTML], { type: 'text/html' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        // Get filename from current URL
        const path = window.location.pathname;
        const filename = path.substring(path.lastIndexOf('/') + 1);
        a.download = filename;
        a.click();
        URL.revokeObjectURL(url);

        showIndicator(`${filename} をダウンロードしました ── slidesフォルダに上書き保存してください`, '#27ae60');
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'e') {
            e.preventDefault();
            editMode = !editMode;
            if (editMode) {
                initEditMode();
                showIndicator('編集モード ON ── ドラッグで移動 / Ctrl+S で保存 / Ctrl+E で終了', '#d4a537');
                document.body.style.cursor = 'crosshair';
            } else {
                showIndicator('編集モード OFF', '#556');
                document.body.style.cursor = '';
                // Remove outlines
                document.querySelectorAll('[data-editable]').forEach(el => {
                    el.style.outline = '';
                    el.style.cursor = '';
                });
            }
        }
        if (e.ctrlKey && e.key === 'c' && editMode && Object.keys(changes).length > 0) {
            e.preventDefault();
            copyChanges();
        }
        if (e.ctrlKey && e.key === 's' && editMode) {
            e.preventDefault();
            saveChanges();
        }
    });

    // HTML overlay drag support
    let htmlDragging = null;
    let htmlStartX = 0, htmlStartY = 0;
    let htmlOrigLeft = 0, htmlOrigTop = 0;

    function onHtmlMouseDown(e) {
        if (!editMode) return;
        const el = e.target.closest('[data-html-editable]');
        if (!el) return;
        e.preventDefault();
        e.stopPropagation();
        htmlDragging = el;
        htmlStartX = e.clientX;
        htmlStartY = e.clientY;

        const style = el.style;
        // Parse current position
        if (style.left) htmlOrigLeft = parseFloat(style.left);
        else if (style.right) htmlOrigLeft = -parseFloat(style.right);
        if (style.top) htmlOrigTop = parseFloat(style.top);
        else if (style.bottom) htmlOrigTop = -parseFloat(style.bottom);

        // Store whether it uses left/right/top/bottom
        htmlDragging._usesRight = !!style.right && !style.left;
        htmlDragging._usesBottom = !!style.bottom && !style.top;
    }

    function onHtmlMouseMove(e) {
        if (!htmlDragging || !editMode) return;
        e.preventDefault();

        const parent = htmlDragging.parentElement;
        const parentRect = parent.getBoundingClientRect();
        const dx = e.clientX - htmlStartX;
        const dy = e.clientY - htmlStartY;

        // Convert pixel delta to percentage of parent
        const dxPct = (dx / parentRect.width) * 100;
        const dyPct = (dy / parentRect.height) * 100;

        const newLeft = htmlOrigLeft + dxPct;
        const newTop = htmlOrigTop + dyPct;

        if (htmlDragging._usesRight) {
            htmlDragging.style.right = (-newLeft).toFixed(1) + '%';
            htmlDragging.style.left = '';
        } else {
            htmlDragging.style.left = newLeft.toFixed(1) + '%';
            htmlDragging.style.right = '';
        }

        if (htmlDragging._usesBottom) {
            htmlDragging.style.bottom = (-newTop).toFixed(1) + '%';
            htmlDragging.style.top = '';
        } else {
            htmlDragging.style.top = newTop.toFixed(1) + '%';
            htmlDragging.style.bottom = '';
        }

        const text = htmlDragging.textContent.substring(0, 15);
        showIndicator(`"${text}" → left:${newLeft.toFixed(1)}% top:${newTop.toFixed(1)}%`, '#0a2f5c');
    }

    function onHtmlMouseUp() {
        htmlDragging = null;
    }

    // Mouse events - SVG
    document.addEventListener('mousedown', onMouseDown);
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);

    // Mouse events - HTML overlays
    document.addEventListener('mousedown', onHtmlMouseDown, true);
    document.addEventListener('mousemove', onHtmlMouseMove);
    document.addEventListener('mouseup', onHtmlMouseUp);

})();
