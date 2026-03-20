#!/usr/bin/env python3
"""Phase 1 (01-07) HTML slides with SVG illustrations"""
import os, html as H

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides")

def wrap(num, title, section_name, total, slides_html, next_title="", quiz_data=None):
    """quiz_data = [(question, optA, optB, correct_index_0or1), ...]"""
    # Quiz slide is inserted before closing
    quiz_slide_num = total - 1
    closing_num = total
    quiz_html = ""
    quiz_js = ""
    if quiz_data:
        qitems = ""
        for i, (q, a, b, ans) in enumerate(quiz_data):
            qitems += f'''<div class="q-item" id="qi{i}"><div class="q-text">Q{i+1}. {q}</div>
<div class="q-opts"><button class="q-btn" onclick="pick({i},0)" id="qb{i}a">{a}</button>
<button class="q-btn" onclick="pick({i},1)" id="qb{i}b">{b}</button></div></div>'''
        quiz_html = f'''<div class="slide quiz" data-s="{quiz_slide_num}"><div class="hdr"><h2>確認テスト ── 3問正解で受講完了</h2></div>
<div class="quiz-body">{qitems}
<button class="quiz-submit" id="qSubmit" onclick="submitQuiz()" disabled>回答を確定する</button>
<div class="quiz-result" id="qResult"></div></div>
<div class="ftr">{H.escape(title)} | URIKAI Trading Academy</div></div>'''
        answers_js = ",".join(str(a) for _,_,_,a in quiz_data)
        quiz_js = f'''
const answers=[{answers_js}];const picks={{}};
function pick(qi,oi){{if(document.getElementById('qSubmit').textContent==='')return;picks[qi]=oi;
document.getElementById('qb'+qi+'a').classList.toggle('selected',oi===0);
document.getElementById('qb'+qi+'b').classList.toggle('selected',oi===1);
if(Object.keys(picks).length===3)document.getElementById('qSubmit').disabled=false;}}
function submitQuiz(){{let score=0;
for(let i=0;i<3;i++){{const btns=[document.getElementById('qb'+i+'a'),document.getElementById('qb'+i+'b')];
btns.forEach(b=>b.disabled=true);
if(picks[i]===answers[i]){{score++;document.getElementById('qi'+i).classList.add('correct');btns[answers[i]].classList.add('right');}}
else{{document.getElementById('qi'+i).classList.add('wrong');btns[picks[i]].classList.add('wrongsel');btns[answers[i]].classList.add('right');}}}}
const r=document.getElementById('qResult');const btn=document.getElementById('qSubmit');
if(score===3){{r.className='quiz-result pass';r.textContent='全問正解！セクション{num} 受講完了';
localStorage.setItem('urikai_done_{num}','true');btn.textContent='';btn.style.display='none';}}
else{{r.className='quiz-result fail';r.textContent=score+'/3 正解 ── 全問正解が必要です';
btn.textContent='もう一度';btn.onclick=()=>location.reload();}}}}'''

    return f'''<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>URIKAI - {H.escape(title)}</title><link rel="stylesheet" href="style.css">
</head><body>
<div class="toolbar"><a href="../index.html">&larr; Back</a><span class="title">Section {num} — {H.escape(title)}</span>
<div class="nav-controls"><button class="nav-btn" id="prevBtn" onclick="nav(-1)">&larr;</button>
<span class="page-info" id="pi">1 / {total}</span>
<button class="nav-btn" id="nextBtn" onclick="nav(1)">&rarr;</button></div></div>
<div class="slide-area">
<div class="slide cover active" data-s="1"><div class="sn">SECTION {num}</div><h1>{H.escape(title)}</h1>
<div class="sub">{H.escape(section_name)}</div><div class="line"></div>
<div class="brand">URIKAI Trading Academy</div></div>
{slides_html}
{quiz_html}
<div class="slide cls" data-s="{total}"><h2>End of Section</h2>
{"<div class='nxt'>Next → "+H.escape(next_title)+"</div>" if next_title else ""}
<div style="width:120px;height:3px;background:#d4a537;margin:2rem auto"></div>
<div style="color:#8b949e;font-size:0.85rem">URIKAI Trading Academy</div></div>
</div><div class="hint">&larr; &rarr; Arrow keys / Space to navigate</div>
<script>
let c=1;const t={total};
function nav(d){{c=Math.max(1,Math.min(t,c+d));document.querySelectorAll('.slide').forEach(s=>s.classList.remove('active'));document.querySelector('[data-s="'+c+'"]').classList.add('active');document.getElementById('pi').textContent=c+' / '+t;document.getElementById('prevBtn').disabled=c===1;document.getElementById('nextBtn').disabled=c===t;}}
document.getElementById('prevBtn').disabled=true;
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' ')nav(1);if(e.key==='ArrowLeft')nav(-1);}});
document.addEventListener('contextmenu',e=>e.preventDefault());
if(sessionStorage.getItem('urikai_auth')!=='true')window.location.href='../index.html';
{quiz_js}
</script></body></html>'''

def cnt(n, title, body_html, footer=""):
    return f'''<div class="slide cnt" data-s="{n}"><div class="hdr"><h2>{title}</h2></div>
<div class="body">{body_html}</div>
<div class="ftr">{footer} | URIKAI Trading Academy</div></div>'''

def cnt_col(n, title, body_html, footer=""):
    return f'''<div class="slide cnt" data-s="{n}"><div class="hdr"><h2>{title}</h2></div>
<div class="body col">{body_html}</div>
<div class="ftr">{footer} | URIKAI Trading Academy</div></div>'''

def li(items):
    return "<div class='txt'><ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"

def li_p(items, point):
    return "<div class='txt'><ul>" + "".join(f"<li>{i}</li>" for i in items) + f"</ul><div class='pbox'>{point}</div></div>"

def vis(svg):
    return f"<div class='vis'>{svg}</div>"

def summary(items):
    rows = "".join(f"<div class='srow'><div class='lbl'>{k}</div><div class='val'>{v}</div></div>" for k,v in items)
    return rows

def tbl(rows):
    h = "<table class='stbl'><tr>" + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr>"
    for r in rows[1:]:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table>"

# ===== SVG Illustrations =====

svg_market_flow = '''<svg viewBox="0 0 500 350" width="100%" style="max-width:620px">
<rect x="150" y="10" width="200" height="55" rx="10" fill="#0a2f5c"/><text x="250" y="45" text-anchor="middle" fill="#fff" font-size="18" font-weight="700">金融市場</text>
<line x1="175" y1="65" x2="100" y2="110" stroke="#d4a537" stroke-width="2"/><line x1="325" y1="65" x2="400" y2="110" stroke="#d4a537" stroke-width="2"/>
<rect x="20" y="110" width="170" height="50" rx="8" fill="#27ae60"/><text x="105" y="142" text-anchor="middle" fill="#fff" font-size="16" font-weight="600">資金の出し手</text><text x="105" y="160" text-anchor="middle" fill="#d5f5e3" font-size="11">投資家・貯蓄者</text>
<rect x="310" y="110" width="170" height="50" rx="8" fill="#2e86c1"/><text x="395" y="142" text-anchor="middle" fill="#fff" font-size="16" font-weight="600">資金の受け手</text><text x="395" y="160" text-anchor="middle" fill="#d6eaf8" font-size="11">企業・政府</text>
<path d="M190,155 Q250,130 310,145" stroke="#d4a537" stroke-width="2.5" fill="none" marker-end="url(#ga)"/>
<path d="M310,160 Q250,185 190,155" stroke="#888" stroke-width="1.5" fill="none" stroke-dasharray="5,3" marker-end="url(#gb)"/>
<text x="250" y="128" text-anchor="middle" font-size="12" fill="#d4a537" font-weight="600">資金</text>
<text x="250" y="192" text-anchor="middle" font-size="11" fill="#888">リターン</text>
<rect x="30" y="210" width="100" height="40" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="80" y="235" text-anchor="middle" fill="#0a2f5c" font-size="12" font-weight="600">価格発見</text>
<rect x="145" y="210" width="100" height="40" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="195" y="235" text-anchor="middle" fill="#0a2f5c" font-size="12" font-weight="600">流動性提供</text>
<rect x="260" y="210" width="100" height="40" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="310" y="235" text-anchor="middle" fill="#0a2f5c" font-size="12" font-weight="600">リスク移転</text>
<rect x="375" y="210" width="100" height="40" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="425" y="235" text-anchor="middle" fill="#0a2f5c" font-size="12" font-weight="600">資本配分</text>
<text x="250" y="285" text-anchor="middle" font-size="14" fill="#555" font-weight="600">金融市場の4つの機能</text>
<defs><marker id="ga" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#d4a537"/></marker>
<marker id="gb" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#888"/></marker></defs>
</svg>'''

svg_market_types = '''<svg viewBox="0 0 520 320" width="100%" style="max-width:620px">
<g transform="translate(10,10)">
<rect x="0" y="0" width="155" height="90" rx="10" fill="#0a2f5c"/><text x="78" y="32" text-anchor="middle" fill="#d4a537" font-size="28" font-weight="800">$7.5T</text><text x="78" y="55" text-anchor="middle" fill="#fff" font-size="15" font-weight="600">FX市場</text><text x="78" y="75" text-anchor="middle" fill="#8b949e" font-size="11">1日の取引量</text>
<rect x="175" y="0" width="155" height="90" rx="10" fill="#1a3c6e"/><text x="253" y="32" text-anchor="middle" fill="#d4a537" font-size="22" font-weight="800">$200B</text><text x="253" y="55" text-anchor="middle" fill="#fff" font-size="15" font-weight="600">株式市場</text><text x="253" y="75" text-anchor="middle" fill="#8b949e" font-size="11">取引所ベース</text>
<rect x="350" y="0" width="155" height="90" rx="10" fill="#2c5f8a"/><text x="428" y="32" text-anchor="middle" fill="#d4a537" font-size="22" font-weight="800">$1T</text><text x="428" y="55" text-anchor="middle" fill="#fff" font-size="15" font-weight="600">債券市場</text><text x="428" y="75" text-anchor="middle" fill="#8b949e" font-size="11">金利のベンチマーク</text>

<rect x="0" y="110" width="155" height="90" rx="10" fill="#2c5f8a"/><text x="78" y="142" text-anchor="middle" fill="#d4a537" font-size="22" font-weight="800">$500B</text><text x="78" y="165" text-anchor="middle" fill="#fff" font-size="15" font-weight="600">商品市場</text><text x="78" y="185" text-anchor="middle" fill="#8b949e" font-size="11">金・原油・農作物</text>
<rect x="175" y="110" width="155" height="90" rx="10" fill="#1a3c6e"/><text x="253" y="142" text-anchor="middle" fill="#d4a537" font-size="22" font-weight="800">$100B</text><text x="253" y="165" text-anchor="middle" fill="#fff" font-size="15" font-weight="600">暗号資産</text><text x="253" y="185" text-anchor="middle" fill="#8b949e" font-size="11">24/7取引</text>
<rect x="350" y="110" width="155" height="90" rx="10" fill="#0a2f5c"/><text x="428" y="142" text-anchor="middle" fill="#d4a537" font-size="18" font-weight="800">数兆$</text><text x="428" y="165" text-anchor="middle" fill="#fff" font-size="15" font-weight="600">デリバティブ</text><text x="428" y="185" text-anchor="middle" fill="#8b949e" font-size="11">先物・オプション</text>
</g>
<rect x="10" y="230" width="500" height="70" rx="10" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="260" y="258" text-anchor="middle" font-size="14" fill="#0a2f5c" font-weight="700">FX市場は株式市場の約37倍の規模 ── 世界最大の金融市場</text>
<rect x="30" y="270" width="460" height="12" rx="4" fill="#eee"/>
<rect x="30" y="270" width="460" height="12" rx="4" fill="#0a2f5c" opacity="0.8"/>
<rect x="30" y="270" width="12" height="12" rx="4" fill="#2e86c1"/>
<text x="260" y="295" text-anchor="middle" font-size="10" fill="#888">FX $7.5T ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 株式 $0.2T</text>
</svg>'''

svg_participants = '''<svg viewBox="0 0 500 340" width="100%" style="max-width:620px">
<polygon points="250,10 420,280 80,280" fill="none" stroke="#d4a537" stroke-width="2" opacity="0.3"/>
<rect x="185" y="25" width="130" height="42" rx="8" fill="#0a2f5c"/><text x="250" y="52" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">中央銀行</text>
<rect x="155" y="82" width="190" height="42" rx="8" fill="#1a3c6e"/><text x="250" y="109" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">商業銀行・投資銀行</text>
<rect x="130" y="140" width="240" height="42" rx="8" fill="#2c5f8a"/><text x="250" y="167" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">ヘッジファンド</text>
<rect x="105" y="198" width="290" height="42" rx="8" fill="#3a7ca5"/><text x="250" y="225" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">機関投資家（年金・保険・運用会社）</text>
<rect x="80" y="255" width="340" height="42" rx="8" fill="#5dade2" opacity="0.8"/><text x="250" y="282" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">個人トレーダー（リテール）≈ 5-6%</text>

<text x="440" y="52" font-size="12" fill="#d4a537" font-weight="600">影響力 大</text>
<text x="440" y="282" font-size="12" fill="#5dade2" font-weight="600">影響力 小</text>
<line x1="435" y1="58" x2="435" y2="268" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>
<path d="M435,60 L435,270" stroke="#888" stroke-width="1" marker-end="url(#ad)"/>
<defs><marker id="ad" markerWidth="8" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#888"/></marker></defs>

<text x="250" y="325" text-anchor="middle" font-size="13" fill="#555" font-weight="600">個人の強み：「参加しない自由」がある</text>
</svg>'''

svg_currency_pair = '''<svg viewBox="0 0 500 300" width="100%" style="max-width:620px">
<rect x="30" y="20" width="180" height="80" rx="12" fill="#27ae60"/><text x="120" y="55" text-anchor="middle" fill="#fff" font-size="22" font-weight="800">EUR</text><text x="120" y="78" text-anchor="middle" fill="#d5f5e3" font-size="13">基軸通貨（Base）</text>
<text x="245" y="70" text-anchor="middle" fill="#d4a537" font-size="36" font-weight="800">/</text>
<rect x="290" y="20" width="180" height="80" rx="12" fill="#2e86c1"/><text x="380" y="55" text-anchor="middle" fill="#fff" font-size="22" font-weight="800">USD</text><text x="380" y="78" text-anchor="middle" fill="#d6eaf8" font-size="13">決済通貨（Quote）</text>

<rect x="120" y="125" width="260" height="50" rx="8" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="250" y="150" text-anchor="middle" font-size="16" fill="#0a2f5c" font-weight="700">EUR/USD = 1.0800</text>
<text x="250" y="167" text-anchor="middle" font-size="12" fill="#888">「1ユーロ = 1.0800ドル」</text>

<rect x="30" y="200" width="210" height="75" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="135" y="225" text-anchor="middle" fill="#0a2f5c" font-size="14" font-weight="700">Pip（ピップ）</text>
<text x="135" y="248" text-anchor="middle" fill="#555" font-size="12">小数点4桁目の変動 = 1pip</text>
<text x="135" y="265" text-anchor="middle" fill="#555" font-size="12">1.0800 → 1.0801 = +1pip</text>

<rect x="260" y="200" width="210" height="75" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="365" y="225" text-anchor="middle" fill="#0a2f5c" font-size="14" font-weight="700">ロットサイズ</text>
<text x="365" y="248" text-anchor="middle" fill="#555" font-size="12">1.0 lot = 100,000通貨</text>
<text x="365" y="265" text-anchor="middle" fill="#555" font-size="12">1pip ≈ $10の損益</text>
</svg>'''

svg_supply_demand = '''<svg viewBox="0 0 500 320" width="100%" style="max-width:620px">
<line x1="60" y1="30" x2="60" y2="260" stroke="#555" stroke-width="2"/><line x1="60" y1="260" x2="460" y2="260" stroke="#555" stroke-width="2"/>
<text x="30" y="150" text-anchor="middle" font-size="13" fill="#555" font-weight="600" transform="rotate(-90,30,150)">価格</text>
<text x="260" y="290" text-anchor="middle" font-size="13" fill="#555" font-weight="600">取引量</text>

<line x1="80" y1="230" x2="420" y2="60" stroke="#27ae60" stroke-width="3"/><text x="430" y="55" font-size="14" fill="#27ae60" font-weight="700">需要</text>
<line x1="80" y1="60" x2="420" y2="230" stroke="#c0392b" stroke-width="3"/><text x="430" y="235" font-size="14" fill="#c0392b" font-weight="700">供給</text>

<circle cx="250" cy="145" r="8" fill="#d4a537"/>
<text x="265" y="138" font-size="14" fill="#d4a537" font-weight="700">均衡価格</text>
<line x1="60" y1="145" x2="245" y2="145" stroke="#d4a537" stroke-width="1" stroke-dasharray="5,3"/>

<rect x="80" y="300" width="380" height="20" rx="4" fill="#e8f0fe"/><text x="270" y="315" text-anchor="middle" font-size="12" fill="#0a2f5c" font-weight="600">需要 ＞ 供給 → 価格上昇 ｜ 供給 ＞ 需要 → 価格下落</text>
</svg>'''

svg_order_types = '''<svg viewBox="0 0 520 310" width="100%" style="max-width:640px">
<line x1="60" y1="20" x2="60" y2="270" stroke="#888" stroke-width="1.5"/>
<text x="50" y="15" text-anchor="end" font-size="11" fill="#888">価格</text>

<line x1="55" y1="60" x2="480" y2="60" stroke="#c0392b" stroke-width="1" stroke-dasharray="6,3" opacity="0.5"/>
<text x="485" y="63" font-size="12" fill="#c0392b">Sell Limit</text>
<rect x="65" y="48" width="120" height="24" rx="5" fill="#c0392b" opacity="0.15" stroke="#c0392b" stroke-width="1"/><text x="125" y="65" text-anchor="middle" font-size="11" fill="#c0392b" font-weight="600">現在価格より上で売り</text>

<line x1="55" y1="110" x2="480" y2="110" stroke="#2e86c1" stroke-width="1" stroke-dasharray="6,3" opacity="0.5"/>
<text x="485" y="113" font-size="12" fill="#2e86c1">Buy Stop</text>
<rect x="65" y="98" width="120" height="24" rx="5" fill="#2e86c1" opacity="0.15" stroke="#2e86c1" stroke-width="1"/><text x="125" y="115" text-anchor="middle" font-size="11" fill="#2e86c1" font-weight="600">現在価格より上で買い</text>

<rect x="55" y="148" width="180" height="34" rx="6" fill="#d4a537" opacity="0.2" stroke="#d4a537" stroke-width="2"/>
<text x="145" y="170" text-anchor="middle" font-size="16" fill="#d4a537" font-weight="800">現在の市場価格</text>

<line x1="55" y1="210" x2="480" y2="210" stroke="#27ae60" stroke-width="1" stroke-dasharray="6,3" opacity="0.5"/>
<text x="485" y="213" font-size="12" fill="#27ae60">Buy Limit</text>
<rect x="65" y="198" width="120" height="24" rx="5" fill="#27ae60" opacity="0.15" stroke="#27ae60" stroke-width="1"/><text x="125" y="215" text-anchor="middle" font-size="11" fill="#27ae60" font-weight="600">現在価格より下で買い</text>

<line x1="55" y1="250" x2="480" y2="250" stroke="#c0392b" stroke-width="1" stroke-dasharray="6,3" opacity="0.5"/>
<text x="485" y="253" font-size="12" fill="#c0392b">Sell Stop</text>
<rect x="65" y="238" width="120" height="24" rx="5" fill="#c0392b" opacity="0.15" stroke="#c0392b" stroke-width="1"/><text x="125" y="255" text-anchor="middle" font-size="11" fill="#c0392b" font-weight="600">現在価格より下で売り</text>

<rect x="260" y="90" width="170" height="50" rx="8" fill="#0a2f5c"/><text x="345" y="112" text-anchor="middle" fill="#fff" font-size="12" font-weight="600">Stop Loss（SL）</text><text x="345" y="128" text-anchor="middle" fill="#d4a537" font-size="11">= 損失限定の命綱</text>
<rect x="260" y="155" width="170" height="50" rx="8" fill="#27ae60"/><text x="345" y="177" text-anchor="middle" fill="#fff" font-size="12" font-weight="600">Take Profit（TP）</text><text x="345" y="193" text-anchor="middle" fill="#d5f5e3" font-size="11">= 利益確定の目標</text>
</svg>'''

svg_sessions = '''<svg viewBox="0 0 520 300" width="100%" style="max-width:640px">
<rect x="10" y="10" width="500" height="55" rx="8" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="30" y="28" font-size="10" fill="#888">0:00</text><text x="120" y="28" font-size="10" fill="#888">6:00</text><text x="240" y="28" font-size="10" fill="#888">12:00</text><text x="350" y="28" font-size="10" fill="#888">18:00</text><text x="475" y="28" font-size="10" fill="#888">24:00</text>
<rect x="80" y="35" width="150" height="24" rx="5" fill="#c0392b" opacity="0.7"/><text x="155" y="52" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">東京 6:00-15:00</text>
<rect x="230" y="35" width="150" height="24" rx="5" fill="#2e86c1" opacity="0.7"/><text x="305" y="52" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">ロンドン 16:00-1:00</text>
<rect x="330" y="35" width="150" height="24" rx="5" fill="#27ae60" opacity="0.7"/><text x="405" y="52" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">NY 21:00-6:00</text>

<rect x="330" y="35" width="50" height="24" rx="0" fill="#d4a537" opacity="0.4"/>

<rect x="10" y="85" width="240" height="65" rx="8" fill="#c0392b" opacity="0.1" stroke="#c0392b" stroke-width="1"/>
<text x="130" y="108" text-anchor="middle" font-size="16" fill="#c0392b" font-weight="700">東京セッション</text>
<text x="130" y="130" text-anchor="middle" font-size="12" fill="#555">穏やか・レンジ相場 | JPY AUD NZD</text>

<rect x="270" y="85" width="240" height="65" rx="8" fill="#2e86c1" opacity="0.1" stroke="#2e86c1" stroke-width="1"/>
<text x="390" y="108" text-anchor="middle" font-size="16" fill="#2e86c1" font-weight="700">ロンドンセッション</text>
<text x="390" y="130" text-anchor="middle" font-size="12" fill="#555">高ボラ・トレンド | EUR GBP CHF</text>

<rect x="10" y="165" width="240" height="65" rx="8" fill="#27ae60" opacity="0.1" stroke="#27ae60" stroke-width="1"/>
<text x="130" y="188" text-anchor="middle" font-size="16" fill="#27ae60" font-weight="700">NYセッション</text>
<text x="130" y="210" text-anchor="middle" font-size="12" fill="#555">最大流動性・指標発表 | USD CAD</text>

<rect x="270" y="165" width="240" height="65" rx="8" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="2"/>
<text x="390" y="188" text-anchor="middle" font-size="16" fill="#d4a537" font-weight="700">LDN × NY 重複</text>
<text x="390" y="210" text-anchor="middle" font-size="12" fill="#555">21:00-1:00 JST 最も活発</text>

<rect x="10" y="250" width="500" height="35" rx="8" fill="#e8f0fe"/>
<text x="260" y="273" text-anchor="middle" font-size="14" fill="#0a2f5c" font-weight="700">自分のライフスタイルに合ったセッションを「主戦場」にする</text>
</svg>'''

svg_leverage = '''<svg viewBox="0 0 500 280" width="100%" style="max-width:620px">
<rect x="30" y="20" width="120" height="100" rx="10" fill="#27ae60"/><text x="90" y="58" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">証拠金</text><text x="90" y="82" text-anchor="middle" fill="#fff" font-size="24" font-weight="800">1万円</text>
<text x="180" y="75" text-anchor="middle" font-size="28" fill="#d4a537" font-weight="800">×</text>
<rect x="210" y="35" width="80" height="55" rx="10" fill="#d4a537"/><text x="250" y="68" text-anchor="middle" fill="#0a2f5c" font-size="20" font-weight="800">100倍</text>
<text x="315" y="75" text-anchor="middle" font-size="28" fill="#555" font-weight="800">=</text>
<rect x="340" y="20" width="140" height="100" rx="10" fill="#0a2f5c"/><text x="410" y="58" text-anchor="middle" fill="#d4a537" font-size="14" font-weight="700">取引可能額</text><text x="410" y="85" text-anchor="middle" fill="#fff" font-size="22" font-weight="800">100万円</text>

<rect x="30" y="150" width="200" height="55" rx="8" fill="#27ae60" opacity="0.15" stroke="#27ae60" stroke-width="1.5"/>
<text x="130" y="172" text-anchor="middle" font-size="14" fill="#27ae60" font-weight="700">利益も100倍</text>
<text x="130" y="192" text-anchor="middle" font-size="12" fill="#555">+1% → +1万円の利益</text>

<rect x="270" y="150" width="200" height="55" rx="8" fill="#c0392b" opacity="0.15" stroke="#c0392b" stroke-width="1.5"/>
<text x="370" y="172" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">損失も100倍</text>
<text x="370" y="192" text-anchor="middle" font-size="12" fill="#555">-1% → -1万円の損失</text>

<rect x="30" y="225" width="440" height="40" rx="8" fill="#e8f0fe"/><text x="250" y="250" text-anchor="middle" font-size="14" fill="#0a2f5c" font-weight="700">レバレッジは利益も損失も倍増させる ── 管理が生命線</text>
</svg>'''

# ===== Section 01 =====
def gen_01():
    slides = ""
    slides += cnt(2, "金融市場の定義",
        li_p(["金融市場 ＝ お金や金融商品が売買される<strong>「場」</strong>",
              "買い手と売り手が価格を決定する仕組み（オークション方式）",
              "実体経済の資金循環を担う<strong>インフラストラクチャー</strong>",
              "市場がなければ企業は資金調達ができず経済活動が停滞する",
              "世界中の金融市場は相互に連動している"],
             "POINT：金融市場は、資金を必要とする主体と資金を運用したい主体を結びつける場である。")
        + vis(svg_market_flow), "金融市場とは何か")
    slides += cnt(3, "金融市場の4つの機能",
        li_p(["<strong>価格発見</strong>（Price Discovery）── 需要と供給から公正な価格を見つける",
              "<strong>流動性の提供</strong>（Liquidity）── いつでも売買できる環境を作る",
              "<strong>リスク移転</strong>（Risk Transfer）── ヘッジによりリスクを移す",
              "<strong>資本配分</strong>（Capital Allocation）── 有望な事業・国に資金が集まる"],
             "POINT：これら4つの機能が正常に働いている市場ほど、効率的で健全な市場と言える。"), "金融市場とは何か")
    slides += cnt(4, "市場構造と規制",
        li_p(["<strong>一次市場</strong>（Primary）── 新規発行（IPO・新発債）の取引",
              "<strong>二次市場</strong>（Secondary）── 既発の金融商品の流通・売買",
              "トレーダーが参加するのは主に二次市場",
              "<strong>日本：</strong>金融庁（FSA）、証券取引等監視委員会（SESC）",
              "<strong>米国：</strong>SEC（証券取引委員会）、CFTC（商品先物取引委員会）",
              "ブローカー選びでは<strong>規制ライセンスの確認が必須</strong>"],
             "POINT：規制の目的は投資家保護、市場の透明性確保、不正防止。規制されていないブローカーは避ける。"), "金融市場とは何か")
    sm = summary([("定義","資金の出し手と受け手を結ぶ場"),("4つの機能","価格発見・流動性・リスク移転・資本配分"),("市場構造","一次市場（発行）と二次市場（流通）"),("規制","各国の規制当局が市場の公正性を監督")])
    slides += cnt_col(5, "まとめ", sm, "金融市場とは何か")
    quiz = [
        ("金融市場の最も基本的な役割は？", "資金の出し手と受け手を結びつける", "株価を上昇させる", 0),
        ("トレーダーが主に参加するのは？", "一次市場（IPO）", "二次市場（流通）", 1),
        ("金融市場の機能に含まれないものは？", "価格発見", "税金の徴収", 1),
    ]
    return wrap("01","金融市場とは何か","金融市場の定義・役割・仕組み",7, slides, "金融市場の種類", quiz)

# ===== Section 02 =====
def gen_02():
    slides = ""
    slides += cnt(2, "主要な金融市場の全体像",
        li(["<strong>FX（外国為替）</strong>── 世界最大、1日$7.5兆、24時間OTC",
            "<strong>株式市場</strong> ── 企業への投資、取引所ベース",
            "<strong>債券市場</strong> ── 金利のベンチマーク、機関投資家中心",
            "<strong>商品市場</strong> ── 金・原油・農作物、実需+投機",
            "<strong>暗号資産</strong> ── 24/7取引、高ボラティリティ",
            "<strong>デリバティブ</strong> ── 先物・オプション・CFD"])
        + vis(svg_market_types), "金融市場の種類")
    slides += cnt(2+1, "FX市場 ── 世界最大の金融市場",
        li_p(["1日の取引高：<strong>約7.5兆ドル</strong>（2022年BIS調査）",
              "中央集権的な取引所がない → <strong>OTC（相対取引）市場</strong>",
              "24時間取引：東京→ロンドン→ニューヨーク→シドニー",
              "主要ペア：EUR/USD, USD/JPY, GBP/USD, AUD/USD",
              "取引コストが低い（スプレッドが主なコスト）"],
             "POINT：FX市場の巨大な流動性は、個人トレーダーにとって参入障壁の低さと約定力の高さというメリットをもたらす。"), "金融市場の種類")
    slides += cnt(4, "株式・債券・商品市場",
        li(["<strong>株式：</strong>企業の株式をIPOで発行、取引所で売買（東証・NYSE等）",
            "<strong>株式：</strong>リターン ＝ 配当（インカム）＋ 値上がり益（キャピタル）",
            "<strong>債券：</strong>国債・社債。価格と利回りは逆相関（シーソー）",
            "<strong>債券：</strong>国債利回り ＝ あらゆる金利のベンチマーク",
            "<strong>商品：</strong>通貨との相関 AUD←→鉄鉱石、CAD←→原油",
            "<strong>商品：</strong>インフレ指標として重要（特に原油・金）"]), "金融市場の種類")
    slides += cnt(5, "暗号資産・デリバティブ",
        li_p(["<strong>暗号資産：</strong>ブロックチェーン基盤、24/365取引、高ボラティリティ",
              "<strong>暗号資産：</strong>CEX（Binance等）とDEX（分散型）の2種類",
              "<strong>デリバティブ：</strong>原資産から派生した金融商品",
              "<strong>先物</strong> ── 将来の一定日に一定価格で売買する契約",
              "<strong>オプション</strong> ── 売買する「権利」を売買",
              "<strong>CFD</strong> ── 原資産を保有せず価格差で損益確定"],
             "POINT：個人トレーダーが取引するFXの多くは実質的にCFDの一種。"), "金融市場の種類")
    sm = summary([("FX","世界最大、24時間OTC、低コスト"),("株式","取引所ベース、企業価値への投資"),("債券","金利のベンチマーク、全市場に影響"),("商品","実需と投機、インフレ・地政学に敏感"),("暗号資産","24/7、高ボラ、規制発展途上"),("デリバティブ","先物・オプション・CFD")])
    slides += cnt_col(6, "まとめ", sm, "金融市場の種類")
    quiz = [
        ("世界最大の金融市場は？", "株式市場", "FX（外国為替）市場", 1),
        ("債券価格と利回りの関係は？", "逆相関（シーソー）", "正相関（連動）", 0),
        ("CFDとは何か？", "現物を保有して取引する方式", "価格差で損益が確定する差金決済取引", 1),
    ]
    return wrap("02","金融市場の種類","FX・株式・債券・商品・暗号資産・デリバティブ",8, slides, "市場参加者", quiz)

# ===== Section 03 =====
def gen_03():
    slides = ""
    slides += cnt(2, "市場参加者の階層構造",
        li_p(["<strong>中央銀行</strong> ── 金融政策で市場全体の方向性を左右する最上位の存在",
              "<strong>商業銀行/投資銀行</strong> ── インターバンク市場の主役、巨額の取引量",
              "<strong>ヘッジファンド</strong> ── 大きなポジション、高頻度・高レバレッジ戦略",
              "<strong>機関投資家</strong> ── 年金基金、保険会社、運用会社（中長期運用）",
              "<strong>個人トレーダー</strong> ── 全体の約5-6%、ブローカー経由で参加"],
             "POINT：個人トレーダーの取引量は市場全体のごく一部。大手の流れに沿った取引を心がける。")
        + vis(svg_participants), "市場参加者")
    slides += cnt(3, "中央銀行の役割",
        li(["金融政策で<strong>金利を操作</strong> → 通貨の価値を左右する",
            "<strong>量的緩和（QE）</strong>で市場に資金を供給 / <strong>量的引き締め（QT）</strong>で資金を回収",
            "為替介入で直接的に通貨レートに影響を与えることがある",
            "フォワードガイダンスで市場の期待をコントロール",
            "中央銀行の発言・声明ひとつで相場が大きく変動する",
            "主要：<strong>FRB（米）、ECB（欧）、BOJ（日）、BOE（英）</strong>"]), "市場参加者")
    slides += cnt(4, "個人トレーダーの立ち位置",
        li_p(["市場全体に占める割合は<strong>約5-6%</strong>（FX市場の場合）",
              "<strong>情報の非対称性</strong> ── 機関は専用データ・アナリストチームを保有",
              "<strong>資金力の差</strong> ── 機関は数十億〜数兆円規模のポジション",
              "<strong>時間軸の差</strong> ── 機関は中長期、個人は短期が多い傾向",
              "<strong>個人の強み</strong> ── 機動性が高い、取引しない選択ができる"],
             "POINT：個人トレーダーの最大の強みは「参加しない自由」。好条件のときだけ参加できる。"), "市場参加者")
    sm = summary([("中央銀行","金融政策で市場全体の方向性を決定"),("銀行","インターバンク市場で基準価格を形成"),("ヘッジファンド","積極的な戦略で大きなポジションを構築"),("個人トレーダー","全体の5-6%、機動性と選択の自由が武器")])
    slides += cnt_col(5, "まとめ", sm, "市場参加者")
    quiz = [
        ("FX市場で個人トレーダーの取引量は全体の約何%？", "約5-6%", "約30-40%", 0),
        ("金融政策で市場全体の方向性を左右するのは？", "ヘッジファンド", "中央銀行", 1),
        ("個人トレーダーの最大の強みは？", "資金力の大きさ", "参加しない自由がある", 1),
    ]
    return wrap("03","市場参加者","誰がこの市場で取引しているのか",7, slides, "通貨ペアの基礎", quiz)

# ===== Section 04 =====
def gen_04():
    slides = ""
    slides += cnt(2, "通貨ペアとは",
        li_p(["FXは常に<strong>2つの通貨を交換</strong>する取引",
              "EUR/USD → ユーロ（<strong>基軸通貨</strong>）÷ ドル（<strong>決済通貨</strong>）",
              "EUR/USD = 1.0800 → 1ユーロを買うのに1.0800ドル必要",
              "「EUR/USDを買う」＝ ユーロを買ってドルを売る",
              "通貨ペアは<strong>2つの国の経済の相対的な強さ</strong>を表す"],
             "POINT：通貨ペアは2国間の経済の綱引き。強い方が買われ、弱い方が売られる。")
        + vis(svg_currency_pair), "通貨ペアの基礎")
    t = tbl([["分類","代表的なペア","特徴"],["メジャーペア","EUR/USD, USD/JPY, GBP/USD","流動性最高、スプレッド最狭"],["クロス円","EUR/JPY, GBP/JPY, AUD/JPY","日本人に人気、ボラあり"],["マイナーペア","EUR/GBP, AUD/NZD, EUR/CHF","流動性やや低い"],["エキゾチック","USD/TRY, USD/ZAR, USD/MXN","スプレッド広い、高スワップ"]])
    slides += cnt_col(3, "通貨ペアの分類", t, "通貨ペアの基礎")
    slides += cnt(4, "Pips・ロット・スプレッド",
        li_p(["<strong>Pip</strong> ＝ 最小価格変動単位（4桁目 or JPYペアは2桁目）",
              "<strong>スタンダードロット</strong>（1.0）＝ 100,000通貨 → 1pip ≈ $10",
              "<strong>ミニロット</strong>（0.1）＝ 10,000通貨 → 1pip ≈ $1",
              "<strong>マイクロロット</strong>（0.01）＝ 1,000通貨 → 1pip ≈ $0.10",
              "<strong>スプレッド</strong> ＝ Ask - Bid ＝ 毎回の取引コスト",
              "流動性が高い時間帯 → スプレッド縮小、指標発表時 → 拡大"],
             "POINT：スプレッドは実質的な取引手数料。スキャルピングでは収益に直結する。"), "通貨ペアの基礎")
    sm = summary([("通貨ペア","基軸/決済通貨の組み合わせ、2国間の相対評価"),("分類","メジャー・クロス円・マイナー・エキゾチック"),("Pip","最小価格変動単位、利益/損失の計測単位"),("ロット","取引量の単位、リスク管理の基本"),("スプレッド","Bid-Ask差、実質的な取引コスト")])
    slides += cnt_col(5, "まとめ", sm, "通貨ペアの基礎")
    quiz = [
        ("EUR/USDでEURは何と呼ばれる？", "決済通貨（Quote）", "基軸通貨（Base）", 1),
        ("USD/JPYが150.00から150.01に動いた場合、何pip？", "1 pip", "10 pips", 0),
        ("スプレッドとは？", "Ask - Bidの差（取引コスト）", "レバレッジの倍率", 0),
    ]
    return wrap("04","通貨ペアの基礎","FX取引の基本単位を理解する",7, slides, "市場の仕組み", quiz)

# ===== Section 05 =====
def gen_05():
    slides = ""
    slides += cnt(2, "需要と供給 ── 価格変動の原理",
        li_p(["価格が上がる ＝ <strong>買い手 ＞ 売り手</strong>（需要 ＞ 供給）",
              "価格が下がる ＝ <strong>売り手 ＞ 買い手</strong>（供給 ＞ 需要）",
              "すべての値動きはこの<strong>1つの原理</strong>から生まれる",
              "ニュース・指標・テクニカル → すべて需給バランスを変化させる手段",
              "流動性が薄い時間帯 ＝ 少しの売買で大きく変動する"],
             "POINT：あらゆる分析手法は「需要と供給のバランスがどちらに傾くか」を予測するためのツール。")
        + vis(svg_supply_demand), "市場の仕組み")
    slides += cnt(3, "レバレッジとマージン",
        li_p(["<strong>レバレッジ</strong> ＝ 証拠金の何倍もの取引を可能にする仕組み",
              "例：100倍レバレッジ → 1万円で100万円分の取引が可能",
              "<strong>マージン</strong>（証拠金）＝ 取引に必要な担保金",
              "<strong>マージンコール</strong> ＝ 証拠金不足の警告",
              "<strong>ストップアウト</strong> ＝ 証拠金維持率が基準以下で強制決済"],
             "POINT：レバレッジは利益も損失も倍増させる。適正な管理がトレーダーの生存に直結する。")
        + vis(svg_leverage), "市場の仕組み")
    slides += cnt(4, "取引構造・スリッページ・スワップ",
        li(["<strong>取引所取引</strong>（株式・先物）vs <strong>OTC取引</strong>（FX）",
            "<strong>スリッページ</strong> ＝ 注文価格と約定価格のズレ。流動性低下時に拡大",
            "重要指標発表直後はスリッページリスクが最大",
            "<strong>スワップ</strong> ＝ ポジション翌日持越し時の金利差調整",
            "高金利通貨を買い＋低金利通貨を売り → プラススワップ",
            "デイトレーダーは翌日持越さないため基本的にスワップは無関係"]), "市場の仕組み")
    sm = summary([("需給","すべての価格変動は需要と供給で決まる"),("レバレッジ","利益も損失も倍増、管理が生命線"),("取引構造","取引所（株式）vs OTC（FX）"),("スリッページ","注文と約定のズレ、流動性に依存"),("スワップ","ポジション持越し時の金利差調整")])
    slides += cnt_col(5, "まとめ", sm, "市場の仕組み")
    quiz = [
        ("価格が上がる原因は？", "需要 ＞ 供給", "供給 ＞ 需要", 0),
        ("レバレッジ100倍で1万円の証拠金だと取引可能額は？", "10万円", "100万円", 1),
        ("マージンコールとは？", "利益確定の通知", "証拠金不足の警告", 1),
    ]
    return wrap("05","市場の仕組み","価格が動く原理と取引構造",7, slides, "注文の種類", quiz)

# ===== Section 06 =====
def gen_06():
    slides = ""
    slides += cnt(2, "注文タイプの全体像",
        li(["<strong>成行注文（Market）</strong>── 現在の価格で即座に約定",
            "<strong>指値注文（Limit）</strong>── 有利な価格を指定して待つ",
            "<strong>逆指値注文（Stop）</strong>── ブレイクアウト用の注文",
            "<strong>ストップロス（SL）</strong>── 損失を限定する自動決済",
            "<strong>テイクプロフィット（TP）</strong>── 利益確定の自動決済",
            "<strong>トレーリングストップ</strong>── 価格追従型のSL"])
        + vis(svg_order_types), "注文の種類")
    slides += cnt(3, "成行注文・指値注文・逆指値注文",
        li_p(["<strong>成行注文</strong> ＝ 即座に約定。確実だがスリッページの可能性あり",
              "<strong>Buy Limit</strong> ＝ 現在価格より<strong>下</strong>で買い（押し目買い）",
              "<strong>Sell Limit</strong> ＝ 現在価格より<strong>上</strong>で売り（戻り売り）",
              "<strong>Buy Stop</strong> ＝ 現在価格より<strong>上</strong>で買い（上方ブレイク）",
              "<strong>Sell Stop</strong> ＝ 現在価格より<strong>下</strong>で売り（下方ブレイク）"],
             "POINT：Limitは「有利な価格で待つ」、Stopは「ブレイクを追いかける」注文。用途が全く異なる。"), "注文の種類")
    slides += cnt(4, "ストップロス ── リスク管理の生命線",
        li_p(["損失が一定額に達したら<strong>自動的にポジションを決済</strong>する注文",
              "全トレードに<strong>必ず設定すべき</strong>最重要の注文",
              "SLなしのトレード ＝ <strong>リスクが無限大</strong>",
              "「ここを超えたらトレードの根拠が崩れる」ポイントに置く",
              "一度設定したSLを不利な方向に動かしてはならない（<strong>鉄則</strong>）",
              "<strong>テイクプロフィット</strong> ＝ 利益目標で自動決済。感情排除に有効"],
             "POINT：ストップロスはトレーダーの生命保険。設定しない理由は一切ない。"), "注文の種類")
    sm = summary([("成行注文","即座に約定、確実だがスリッページあり"),("指値注文","有利な価格を指定、約定しない可能性あり"),("逆指値注文","ブレイクアウト用、発動後は成行"),("ストップロス","損失限定、全トレードで必須"),("テイクプロフィット","利益確定の自動化、感情排除")])
    slides += cnt_col(5, "まとめ", sm, "注文の種類")
    quiz = [
        ("押し目買いに使う注文タイプは？", "Buy Limit", "Buy Stop", 0),
        ("ストップロス（SL）を設定しないトレードのリスクは？", "少しだけ危険", "リスクが無限大", 1),
        ("ブレイクアウトエントリーに使う注文は？", "指値注文（Limit）", "逆指値注文（Stop）", 1),
    ]
    return wrap("06","注文の種類","取引執行の基本操作を理解する",7, slides, "取引セッションと時間帯", quiz)

# ===== Section 07 =====
def gen_07():
    slides = ""
    slides += cnt(2, "FX市場の24時間サイクル",
        li_p(["FX市場は<strong>月曜早朝〜土曜早朝まで連続稼働</strong>",
              "<strong>3つの主要セッション</strong>がリレー形式で市場を回す",
              "東京セッション → ロンドンセッション → ニューヨークセッション",
              "セッション間の「<strong>オーバーラップ</strong>」が最も活発な時間帯",
              "各セッションごとに主要通貨・ボラティリティが異なる"],
             "POINT：市場は24時間開いているが、「波の大きさ」は時間帯で全く違う。")
        + vis(svg_sessions), "取引セッションと時間帯")
    t = tbl([["セッション","時間（JST）","特徴","主要通貨"],["東京（アジア）","6:00-15:00","穏やか、レンジ相場が多い","JPY, AUD, NZD"],["ロンドン（欧州）","16:00-翌1:00","ボラ増大、トレンド発生","EUR, GBP, CHF"],["ニューヨーク","21:00-翌6:00","最大流動性、指標発表多数","USD, CAD"],["LDN×NY重複","21:00-翌1:00","1日で最も活発","全通貨ペア"]])
    slides += cnt_col(3, "3大セッションの特徴", t, "取引セッションと時間帯")
    slides += cnt(4, "時間帯と戦略の関係",
        li_p(["<strong>東京</strong> → レンジ取引、逆張り戦略が機能しやすい",
              "<strong>ロンドンオープン</strong> → ブレイクアウト戦略が有効",
              "<strong>LDN×NY重複</strong> → トレンドフォロー、モメンタム戦略",
              "<strong>NY午後〜東京前</strong> → 流動性低下、スプレッド拡大に注意",
              "自分のライフスタイルに合ったセッションを<strong>主戦場</strong>にする"],
             "POINT：すべての時間帯で同じ戦略は通用しない。参加する時間帯の特性を理解し、適した戦略を選択する。"), "取引セッションと時間帯")
    sm = summary([("24時間市場","3セッションのリレー方式で世界をカバー"),("東京","穏やか、レンジ、JPY/AUD/NZD"),("ロンドン","高ボラ、トレンド、EUR/GBP/CHF"),("ニューヨーク","最大流動性、米指標発表、USD/CAD"),("オーバーラップ","21:00-1:00が1日で最も活発"),("戦略適合","時間帯に合わせた戦略選択が必須")])
    slides += cnt_col(5, "まとめ", sm, "取引セッションと時間帯")
    quiz = [
        ("1日で最も取引が活発な時間帯は？", "東京セッション単独", "ロンドン×NY重複（21:00-1:00）", 1),
        ("東京セッションの特徴は？", "穏やか、レンジ相場が多い", "トレンドが発生しやすい", 0),
        ("FX取引量の約38%が行われるのは？", "ロンドン市場", "東京市場", 0),
    ]
    return wrap("07","取引セッションと時間帯","市場のリズムを理解する",7, slides, quiz_data=quiz)

# ===== Generate All =====
sections = [
    ("01", gen_01), ("02", gen_02), ("03", gen_03), ("04", gen_04),
    ("05", gen_05), ("06", gen_06), ("07", gen_07),
]

for num, gen_fn in sections:
    html = gen_fn()
    path = os.path.join(DIR, f"{num}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  OK: {num}.html")

print(f"\n  Phase 1 完了: 7ファイル生成")
