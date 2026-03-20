"""SVG illustrations for sections 09-35"""

# ===== 09: S/R =====
SVG_09 = '''<svg viewBox="0 0 500 300" width="100%" style="max-width:620px">
<line x1="40" y1="20" x2="40" y2="280" stroke="#888" stroke-width="1.5"/>
<line x1="40" y1="280" x2="480" y2="280" stroke="#888" stroke-width="1.5"/>
<line x1="40" y1="80" x2="460" y2="80" stroke="#c0392b" stroke-width="2" stroke-dasharray="8,4"/>
<text x="465" y="78" font-size="13" fill="#c0392b" font-weight="700">レジスタンス</text>
<line x1="40" y1="200" x2="460" y2="200" stroke="#27ae60" stroke-width="2" stroke-dasharray="8,4"/>
<text x="465" y="198" font-size="13" fill="#27ae60" font-weight="700">サポート</text>
<polyline points="60,220 100,190 130,210 170,180 200,205 240,85 270,100 300,75 330,95 360,82 400,90 430,78" stroke="#2e86c1" stroke-width="2.5" fill="none"/>
<circle cx="240" cy="85" r="6" fill="#c0392b"/><text x="248" y="72" font-size="11" fill="#c0392b" font-weight="600">反発</text>
<circle cx="300" cy="75" r="6" fill="#c0392b"/><text x="308" y="62" font-size="11" fill="#c0392b" font-weight="600">反発</text>
<circle cx="100" cy="190" r="6" fill="#27ae60"/><text x="108" y="185" font-size="11" fill="#27ae60" font-weight="600">反発</text>
<circle cx="200" cy="205" r="6" fill="#27ae60"/><text x="208" y="222" font-size="11" fill="#27ae60" font-weight="600">反発</text>
<rect x="35" y="70" width="430" height="140" fill="#2e86c1" opacity="0.04" rx="4"/>
<text x="260" y="150" text-anchor="middle" font-size="14" fill="#555" font-weight="600">レンジ（取引ゾーン）</text>
</svg>'''

# ===== 10: Indicators =====
SVG_10 = '''<svg viewBox="0 0 500 300" width="100%" style="max-width:620px">
<rect x="30" y="10" width="440" height="170" rx="8" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="50" y="30" font-size="11" fill="#888">価格チャート</text>
<polyline points="50,120 90,100 120,130 160,90 200,110 240,70 280,85 320,60 360,75 400,50 440,65" stroke="#2c3e50" stroke-width="2" fill="none"/>
<polyline points="50,130 90,120 120,125 160,110 200,115 240,100 280,95 320,85 360,80 400,75 440,70" stroke="#d4a537" stroke-width="1.5" fill="none" stroke-dasharray="4,2"/>
<text x="445" y="68" font-size="10" fill="#d4a537">20 EMA</text>
<polyline points="50,140 90,135 120,132 160,125 200,120 240,115 280,110 320,105 360,100 400,95 440,90" stroke="#c0392b" stroke-width="1.5" fill="none" stroke-dasharray="4,2"/>
<text x="445" y="88" font-size="10" fill="#c0392b">200 SMA</text>
<rect x="30" y="195" width="440" height="95" rx="8" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="50" y="215" font-size="11" fill="#888">RSI (14)</text>
<line x1="50" y1="225" x2="450" y2="225" stroke="#c0392b" stroke-width="0.8" stroke-dasharray="3,3"/><text x="455" y="228" font-size="9" fill="#c0392b">70</text>
<line x1="50" y1="260" x2="450" y2="260" stroke="#27ae60" stroke-width="0.8" stroke-dasharray="3,3"/><text x="455" y="263" font-size="9" fill="#27ae60">30</text>
<polyline points="50,250 90,240 120,255 160,230 200,245 240,220 280,225 320,215 360,228 400,222 440,232" stroke="#8e44ad" stroke-width="2" fill="none"/>
</svg>'''

# ===== 11: Chart Patterns =====
SVG_11 = '''<svg viewBox="0 0 500 280" width="100%" style="max-width:620px">
<text x="130" y="20" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">ヘッドアンドショルダー</text>
<polyline points="30,180 70,120 100,160 150,60 190,150 230,110 260,180" stroke="#2c3e50" stroke-width="2.5" fill="none"/>
<line x1="30" y1="160" x2="260" y2="160" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="6,3"/>
<text x="265" y="158" font-size="11" fill="#c0392b" font-weight="600">ネックライン</text>
<text x="70" y="115" text-anchor="middle" font-size="10" fill="#888">左肩</text>
<text x="150" y="52" text-anchor="middle" font-size="10" fill="#888">頭</text>
<text x="230" y="105" text-anchor="middle" font-size="10" fill="#888">右肩</text>
<path d="M260,180 L260,230" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#ard)"/>

<text x="400" y="20" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">ダブルトップ</text>
<polyline points="300,180 340,70 370,130 410,70 440,180" stroke="#2c3e50" stroke-width="2.5" fill="none"/>
<line x1="300" y1="130" x2="470" y2="130" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="6,3"/>
<text x="340" y="62" text-anchor="middle" font-size="10" fill="#888">Top1</text>
<text x="410" y="62" text-anchor="middle" font-size="10" fill="#888">Top2</text>
<text x="475" y="128" font-size="11" fill="#c0392b" font-weight="600">ネックライン</text>

<text x="130" y="260" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="600">ブルフラッグ ↑</text>
<polyline points="40,250 70,210 60,215 90,218 80,222 110,225 140,195" stroke="#27ae60" stroke-width="2" fill="none"/>
<text x="400" y="260" text-anchor="middle" font-size="13" fill="#2e86c1" font-weight="600">トライアングル △</text>
<polyline points="310,230 340,210 350,235 380,215 390,232 420,220" stroke="#2e86c1" stroke-width="2" fill="none"/>
<line x1="310" y1="240" x2="430" y2="225" stroke="#888" stroke-width="1" stroke-dasharray="3,2"/>
<line x1="310" y1="205" x2="430" y2="218" stroke="#888" stroke-width="1" stroke-dasharray="3,2"/>
<defs><marker id="ard" markerWidth="8" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#c0392b"/></marker></defs>
</svg>'''

# ===== 12: Fibonacci =====
SVG_12 = '''<svg viewBox="0 0 500 300" width="100%" style="max-width:620px">
<line x1="60" y1="20" x2="60" y2="280" stroke="#888" stroke-width="1.5"/>
<polyline points="80,260 150,250 200,60 250,145 300,50" stroke="#2c3e50" stroke-width="2.5" fill="none"/>
<line x1="190" y1="60" x2="420" y2="60" stroke="#0a2f5c" stroke-width="1" stroke-dasharray="4,3"/><text x="425" y="64" font-size="12" fill="#0a2f5c" font-weight="700">0% (高値)</text>
<line x1="190" y1="137" x2="420" y2="137" stroke="#d4a537" stroke-width="1.5" stroke-dasharray="4,3"/><text x="425" y="141" font-size="12" fill="#d4a537" font-weight="700">38.2%</text>
<line x1="190" y1="160" x2="420" y2="160" stroke="#2e86c1" stroke-width="1.5" stroke-dasharray="4,3"/><text x="425" y="164" font-size="12" fill="#2e86c1" font-weight="700">50.0%</text>
<line x1="190" y1="184" x2="420" y2="184" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="4,3"/><text x="425" y="188" font-size="12" fill="#e74c3c" font-weight="700">61.8%</text>
<line x1="190" y1="260" x2="420" y2="260" stroke="#0a2f5c" stroke-width="1" stroke-dasharray="4,3"/><text x="425" y="264" font-size="12" fill="#0a2f5c" font-weight="700">100% (安値)</text>
<circle cx="250" cy="145" r="8" fill="#d4a537" opacity="0.8"/>
<text x="260" y="135" font-size="12" fill="#d4a537" font-weight="700">反発ポイント</text>
<rect x="60" y="275" width="360" height="22" rx="4" fill="#e8f0fe"/>
<text x="240" y="291" text-anchor="middle" font-size="12" fill="#0a2f5c" font-weight="600">61.8%（黄金比）が最も注目されるレベル</text>
</svg>'''

# ===== 13: MTF =====
SVG_13 = '''<svg viewBox="0 0 500 280" width="100%" style="max-width:620px">
<rect x="30" y="15" width="440" height="70" rx="10" fill="#0a2f5c"/>
<text x="250" y="42" text-anchor="middle" fill="#d4a537" font-size="16" font-weight="700">上位時間軸（日足）── トレンド方向の確認</text>
<text x="250" y="65" text-anchor="middle" fill="#8b949e" font-size="12">「今は上昇トレンドか下降トレンドか？」</text>
<path d="M250,85 L250,100" stroke="#d4a537" stroke-width="2" marker-end="url(#am)"/>
<rect x="30" y="105" width="440" height="70" rx="10" fill="#1a3c6e"/>
<text x="250" y="132" text-anchor="middle" fill="#d4a537" font-size="16" font-weight="700">中位時間軸（4H足）── セットアップの発見</text>
<text x="250" y="155" text-anchor="middle" fill="#8b949e" font-size="12">「S/R・フィボ・パターンは出ているか？」</text>
<path d="M250,175 L250,190" stroke="#d4a537" stroke-width="2" marker-end="url(#am)"/>
<rect x="30" y="195" width="440" height="70" rx="10" fill="#2e86c1"/>
<text x="250" y="222" text-anchor="middle" fill="#fff" font-size="16" font-weight="700">下位時間軸（15分足）── エントリータイミング</text>
<text x="250" y="245" text-anchor="middle" fill="#d6eaf8" font-size="12">「ローソク足の反転確認 → エントリー実行」</text>
<defs><marker id="am" markerWidth="10" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L10,3.5 L0,7Z" fill="#d4a537"/></marker></defs>
</svg>'''

# ===== 14: Elliott Wave =====
SVG_14 = '''<svg viewBox="0 0 500 280" width="100%" style="max-width:620px">
<polyline points="40,240 100,180 80,200 180,60 140,130 220,40 280,160 240,120 320,80 360,200" stroke="#2c3e50" stroke-width="2.5" fill="none"/>
<circle cx="40" cy="240" r="5" fill="#0a2f5c"/><text x="30" y="258" font-size="13" fill="#0a2f5c" font-weight="700">0</text>
<circle cx="100" cy="180" r="5" fill="#27ae60"/><text x="105" y="175" font-size="13" fill="#27ae60" font-weight="700">1</text>
<circle cx="80" cy="200" r="5" fill="#c0392b"/><text x="65" y="215" font-size="13" fill="#c0392b" font-weight="700">2</text>
<circle cx="180" cy="60" r="5" fill="#27ae60"/><text x="185" y="52" font-size="13" fill="#27ae60" font-weight="700">3</text>
<circle cx="140" cy="130" r="5" fill="#c0392b"/><text x="125" y="145" font-size="13" fill="#c0392b" font-weight="700">4</text>
<circle cx="220" cy="40" r="5" fill="#27ae60"/><text x="225" y="32" font-size="13" fill="#27ae60" font-weight="700">5</text>
<circle cx="280" cy="160" r="5" fill="#8e44ad"/><text x="285" y="155" font-size="13" fill="#8e44ad" font-weight="700">A</text>
<circle cx="240" cy="120" r="5" fill="#8e44ad"/><text x="225" y="115" font-size="13" fill="#8e44ad" font-weight="700">B</text>
<circle cx="320" cy="80" r="5" fill="#8e44ad"/><text x="325" y="72" font-size="13" fill="#8e44ad" font-weight="700">C</text>
<rect x="350" y="30" width="140" height="45" rx="6" fill="#27ae60" opacity="0.15" stroke="#27ae60" stroke-width="1"/>
<text x="420" y="50" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="700">推進波（1-5）</text>
<text x="420" y="66" text-anchor="middle" font-size="10" fill="#27ae60">トレンド方向</text>
<rect x="350" y="85" width="140" height="45" rx="6" fill="#8e44ad" opacity="0.15" stroke="#8e44ad" stroke-width="1"/>
<text x="420" y="105" text-anchor="middle" font-size="12" fill="#8e44ad" font-weight="700">修正波（ABC）</text>
<text x="420" y="121" text-anchor="middle" font-size="10" fill="#8e44ad">調整方向</text>
</svg>'''

# ===== 15-19: Compact illustrations =====
SVG_15 = '''<svg viewBox="0 0 500 260" width="100%" style="max-width:620px">
<text x="250" y="20" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">ガートレーパターン（XABCD）</text>
<polyline points="60,200 160,50 120,130 220,30 180,160" stroke="#2c3e50" stroke-width="2.5" fill="none"/>
<circle cx="60" cy="200" r="5" fill="#0a2f5c"/><text x="45" y="218" font-size="14" fill="#0a2f5c" font-weight="700">X</text>
<circle cx="160" cy="50" r="5" fill="#0a2f5c"/><text x="165" y="42" font-size="14" fill="#0a2f5c" font-weight="700">A</text>
<circle cx="120" cy="130" r="5" fill="#0a2f5c"/><text x="105" y="145" font-size="14" fill="#0a2f5c" font-weight="700">B</text>
<circle cx="220" cy="30" r="5" fill="#0a2f5c"/><text x="228" y="25" font-size="14" fill="#0a2f5c" font-weight="700">C</text>
<circle cx="180" cy="160" r="6" fill="#d4a537"/><text x="190" y="175" font-size="14" fill="#d4a537" font-weight="700">D (PRZ)</text>
<rect x="160" y="145" width="55" height="30" rx="4" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="90" y="105" font-size="10" fill="#888">61.8%</text>
<text x="185" y="105" font-size="10" fill="#888">78.6%</text>
<rect x="280" y="40" width="190" height="80" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="375" y="65" text-anchor="middle" font-size="13" fill="#0a2f5c" font-weight="700">PRZ（反転ゾーン）</text>
<text x="375" y="85" text-anchor="middle" font-size="11" fill="#555">複数フィボが収束する</text>
<text x="375" y="105" text-anchor="middle" font-size="11" fill="#555">ポイントでエントリー</text>
</svg>'''

SVG_16 = '''<svg viewBox="0 0 500 260" width="100%" style="max-width:620px">
<text x="250" y="22" text-anchor="middle" font-size="15" fill="#2c3e50" font-weight="700">ワイコフ・蓄積（Accumulation）スキーマティック</text>
<polyline points="30,60 80,100 100,140 90,180 110,190 95,210 80,200 120,150 160,130 200,90 250,70 300,50 350,40 420,30 470,20" stroke="#2c3e50" stroke-width="2" fill="none"/>
<line x1="70" y1="200" x2="300" y2="200" stroke="#27ae60" stroke-width="1.5" stroke-dasharray="5,3"/>
<rect x="70" y="120" width="230" height="85" rx="6" fill="#27ae60" opacity="0.06" stroke="#27ae60" stroke-width="1" stroke-dasharray="4,3"/>
<text x="185" y="145" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="600">蓄積レンジ（Accumulation）</text>
<circle cx="95" cy="210" r="5" fill="#d4a537"/><text x="95" y="232" text-anchor="middle" font-size="11" fill="#d4a537" font-weight="700">Spring</text>
<text x="95" y="246" text-anchor="middle" font-size="9" fill="#888">ダマシの下抜け</text>
<path d="M300,50 L470,20" stroke="#27ae60" stroke-width="3" opacity="0.4"/>
<text x="400" y="55" font-size="12" fill="#27ae60" font-weight="700">マークアップ ↑</text>
</svg>'''

SVG_17 = '''<svg viewBox="0 0 500 260" width="100%" style="max-width:620px">
<text x="130" y="20" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">板情報（DOM）</text>
<rect x="30" y="30" width="200" height="200" rx="8" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<rect x="40" y="45" width="80" height="22" rx="3" fill="#27ae60" opacity="0.7"/><text x="80" y="61" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">120 lot</text><text x="145" y="61" font-size="12" fill="#555">1.0805</text>
<rect x="40" y="72" width="110" height="22" rx="3" fill="#27ae60" opacity="0.7"/><text x="95" y="88" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">180 lot</text><text x="175" y="88" font-size="12" fill="#555">1.0804</text>
<rect x="40" y="99" width="150" height="22" rx="3" fill="#27ae60" opacity="0.9"/><text x="115" y="115" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">250 lot</text><text x="205" y="115" font-size="12" fill="#555" font-weight="700">1.0803</text>
<rect x="40" y="130" width="90" height="22" rx="3" fill="#c0392b" opacity="0.7"/><text x="85" y="146" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">140 lot</text><text x="145" y="146" font-size="12" fill="#555">1.0802</text>
<rect x="40" y="157" width="70" height="22" rx="3" fill="#c0392b" opacity="0.7"/><text x="75" y="173" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">100 lot</text><text x="145" y="173" font-size="12" fill="#555">1.0801</text>
<rect x="40" y="184" width="50" height="22" rx="3" fill="#c0392b" opacity="0.5"/><text x="65" y="200" text-anchor="middle" fill="#fff" font-size="11" font-weight="600">60 lot</text><text x="145" y="200" font-size="12" fill="#555">1.0800</text>
<text x="80" y="228" text-anchor="middle" font-size="10" fill="#27ae60" font-weight="600">買い（Bid）</text>
<text x="165" y="228" text-anchor="middle" font-size="10" fill="#c0392b" font-weight="600">売り（Ask）</text>
<rect x="270" y="30" width="200" height="100" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="370" y="55" text-anchor="middle" font-size="13" fill="#0a2f5c" font-weight="700">オーダーフローの要点</text>
<text x="370" y="78" text-anchor="middle" font-size="11" fill="#555">バーの長さ ＝ 注文量</text>
<text x="370" y="98" text-anchor="middle" font-size="11" fill="#555">大量注文 ＝ S/Rの存在</text>
<text x="370" y="118" text-anchor="middle" font-size="11" fill="#555">リアルタイムの需給を可視化</text>
</svg>'''

SVG_18 = '''<svg viewBox="0 0 500 260" width="100%" style="max-width:620px">
<line x1="60" y1="20" x2="60" y2="240" stroke="#888" stroke-width="1.5"/>
<text x="30" y="130" text-anchor="middle" font-size="11" fill="#888" transform="rotate(-90,30,130)">価格</text>
<rect x="65" y="30" width="30" height="15" rx="2" fill="#2e86c1" opacity="0.3"/>
<rect x="65" y="50" width="60" height="15" rx="2" fill="#2e86c1" opacity="0.4"/>
<rect x="65" y="70" width="100" height="15" rx="2" fill="#2e86c1" opacity="0.5"/>
<rect x="65" y="90" width="160" height="15" rx="2" fill="#2e86c1" opacity="0.6"/>
<rect x="65" y="110" width="250" height="15" rx="2" fill="#d4a537" opacity="0.9"/>
<rect x="65" y="130" width="200" height="15" rx="2" fill="#2e86c1" opacity="0.7"/>
<rect x="65" y="150" width="120" height="15" rx="2" fill="#2e86c1" opacity="0.5"/>
<rect x="65" y="170" width="80" height="15" rx="2" fill="#2e86c1" opacity="0.4"/>
<rect x="65" y="190" width="40" height="15" rx="2" fill="#2e86c1" opacity="0.3"/>
<text x="325" y="123" font-size="14" fill="#d4a537" font-weight="700">← POC（最大出来高）</text>
<line x1="65" y1="85" x2="330" y2="85" stroke="#27ae60" stroke-width="1" stroke-dasharray="4,3"/>
<text x="335" y="89" font-size="11" fill="#27ae60" font-weight="600">VAH</text>
<line x1="65" y1="155" x2="330" y2="155" stroke="#27ae60" stroke-width="1" stroke-dasharray="4,3"/>
<text x="335" y="159" font-size="11" fill="#27ae60" font-weight="600">VAL</text>
<rect x="60" y="85" width="5" height="70" fill="#27ae60" opacity="0.2"/>
<text x="350" y="180" font-size="12" fill="#555">Value Area (70%)</text>
</svg>'''

SVG_19 = '''<svg viewBox="0 0 500 250" width="100%" style="max-width:620px">
<rect x="180" y="10" width="140" height="50" rx="10" fill="#0a2f5c"/>
<text x="250" y="42" text-anchor="middle" fill="#d4a537" font-size="15" font-weight="700">市場間の相関</text>
<rect x="20" y="100" width="110" height="45" rx="8" fill="#27ae60"/><text x="75" y="128" text-anchor="middle" fill="#fff" font-size="13" font-weight="600">株式 ↑</text>
<rect x="150" y="100" width="110" height="45" rx="8" fill="#2e86c1"/><text x="205" y="128" text-anchor="middle" fill="#fff" font-size="13" font-weight="600">金利 ↑</text>
<rect x="280" y="100" width="110" height="45" rx="8" fill="#d4a537"/><text x="335" y="128" text-anchor="middle" fill="#0a2f5c" font-size="13" font-weight="600">USD ↑</text>
<rect x="410" y="100" width="80" height="45" rx="8" fill="#c0392b"/><text x="450" y="128" text-anchor="middle" fill="#fff" font-size="13" font-weight="600">金 ↓</text>
<path d="M130,122 L148,122" stroke="#555" stroke-width="1.5" marker-end="url(#ai)"/>
<path d="M260,122 L278,122" stroke="#555" stroke-width="1.5" marker-end="url(#ai)"/>
<path d="M390,122 L408,122" stroke="#555" stroke-width="1.5" marker-end="url(#ai)"/>
<rect x="20" y="175" width="220" height="55" rx="8" fill="#27ae60" opacity="0.1" stroke="#27ae60" stroke-width="1"/>
<text x="130" y="198" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="700">リスクオン</text>
<text x="130" y="218" text-anchor="middle" font-size="11" fill="#555">AUD↑ NZD↑ 株↑ 新興国↑</text>
<rect x="260" y="175" width="220" height="55" rx="8" fill="#c0392b" opacity="0.1" stroke="#c0392b" stroke-width="1"/>
<text x="370" y="198" text-anchor="middle" font-size="13" fill="#c0392b" font-weight="700">リスクオフ</text>
<text x="370" y="218" text-anchor="middle" font-size="11" fill="#555">JPY↑ CHF↑ 金↑ 米国債↑</text>
<defs><marker id="ai" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#555"/></marker></defs>
</svg>'''

# ===== 20-25: Fundamental & Sentiment =====
SVG_20 = '''<svg viewBox="0 0 500 240" width="100%" style="max-width:620px">
<rect x="20" y="10" width="140" height="100" rx="10" fill="#c0392b" opacity="0.9"/>
<text x="90" y="40" text-anchor="middle" fill="#fff" font-size="16" font-weight="800">NFP</text>
<text x="90" y="60" text-anchor="middle" fill="#fadbd8" font-size="11">雇用統計</text>
<text x="90" y="80" text-anchor="middle" fill="#fadbd8" font-size="11">毎月第一金曜</text>
<text x="90" y="98" text-anchor="middle" fill="#fff" font-size="10">インパクト ★★★</text>
<rect x="180" y="10" width="140" height="100" rx="10" fill="#d4a537" opacity="0.9"/>
<text x="250" y="40" text-anchor="middle" fill="#0a2f5c" font-size="16" font-weight="800">CPI</text>
<text x="250" y="60" text-anchor="middle" fill="#0a2f5c" font-size="11">消費者物価指数</text>
<text x="250" y="80" text-anchor="middle" fill="#0a2f5c" font-size="11">インフレ指標</text>
<text x="250" y="98" text-anchor="middle" fill="#0a2f5c" font-size="10">インパクト ★★★</text>
<rect x="340" y="10" width="140" height="100" rx="10" fill="#2e86c1" opacity="0.9"/>
<text x="410" y="40" text-anchor="middle" fill="#fff" font-size="16" font-weight="800">GDP</text>
<text x="410" y="60" text-anchor="middle" fill="#d6eaf8" font-size="11">国内総生産</text>
<text x="410" y="80" text-anchor="middle" fill="#d6eaf8" font-size="11">四半期発表</text>
<text x="410" y="98" text-anchor="middle" fill="#fff" font-size="10">インパクト ★★☆</text>
<rect x="20" y="130" width="460" height="45" rx="8" fill="#e8f0fe"/>
<text x="250" y="158" text-anchor="middle" font-size="14" fill="#0a2f5c" font-weight="700">重要なのは数値そのものではなく「市場予想との差」</text>
<rect x="20" y="190" width="140" height="35" rx="6" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="90" y="213" text-anchor="middle" font-size="12" fill="#555" font-weight="600">PMI（50が分岐点）</text>
<rect x="180" y="190" width="140" height="35" rx="6" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="250" y="213" text-anchor="middle" font-size="12" fill="#555" font-weight="600">小売売上高</text>
<rect x="340" y="190" width="140" height="35" rx="6" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<text x="410" y="213" text-anchor="middle" font-size="12" fill="#555" font-weight="600">消費者信頼感</text>
</svg>'''

SVG_21 = '''<svg viewBox="0 0 500 240" width="100%" style="max-width:620px">
<rect x="150" y="5" width="200" height="50" rx="10" fill="#0a2f5c"/>
<text x="250" y="36" text-anchor="middle" fill="#d4a537" font-size="16" font-weight="700">中央銀行</text>
<path d="M200,55 L120,90" stroke="#d4a537" stroke-width="2"/><path d="M300,55 L380,90" stroke="#d4a537" stroke-width="2"/>
<rect x="40" y="90" width="160" height="50" rx="8" fill="#27ae60"/>
<text x="120" y="112" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">利上げ（タカ派）</text>
<text x="120" y="130" text-anchor="middle" fill="#d5f5e3" font-size="12">→ 通貨高</text>
<rect x="300" y="90" width="160" height="50" rx="8" fill="#c0392b"/>
<text x="380" y="112" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">利下げ（ハト派）</text>
<text x="380" y="130" text-anchor="middle" fill="#fadbd8" font-size="12">→ 通貨安</text>
<rect x="40" y="165" width="200" height="60" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="140" y="190" text-anchor="middle" font-size="12" fill="#0a2f5c" font-weight="700">QE（量的緩和）</text>
<text x="140" y="210" text-anchor="middle" font-size="11" fill="#555">資金供給→金利↓→通貨安</text>
<rect x="260" y="165" width="200" height="60" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="360" y="190" text-anchor="middle" font-size="12" fill="#0a2f5c" font-weight="700">QT（量的引締め）</text>
<text x="360" y="210" text-anchor="middle" font-size="11" fill="#555">資金回収→金利↑→通貨高</text>
</svg>'''

# Generic concept diagrams for remaining sections
SVG_22 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="20" y="10" width="220" height="80" rx="10" fill="#c0392b" opacity="0.1" stroke="#c0392b" stroke-width="1.5"/>
<text x="130" y="38" text-anchor="middle" font-size="15" fill="#c0392b" font-weight="700">地政学イベント</text>
<text x="130" y="60" text-anchor="middle" font-size="11" fill="#555">戦争・選挙・制裁・貿易戦争</text>
<text x="130" y="78" text-anchor="middle" font-size="11" fill="#555">→ ボラティリティ急上昇</text>
<rect x="260" y="10" width="220" height="80" rx="10" fill="#27ae60" opacity="0.1" stroke="#27ae60" stroke-width="1.5"/>
<text x="370" y="38" text-anchor="middle" font-size="15" fill="#27ae60" font-weight="700">最善の対応</text>
<text x="370" y="60" text-anchor="middle" font-size="11" fill="#555">サイズ縮小 or ノーポジション</text>
<text x="370" y="78" text-anchor="middle" font-size="11" fill="#555">不確実性が高い時は参加しない</text>
<path d="M240,50 L258,50" stroke="#d4a537" stroke-width="2.5" marker-end="url(#an)"/>
<rect x="20" y="110" width="460" height="70" rx="10" fill="#e8f0fe"/>
<text x="250" y="140" text-anchor="middle" font-size="14" fill="#0a2f5c" font-weight="700">リスクオフ → 安全資産（JPY・CHF・金・米国債）が買われる</text>
<text x="250" y="165" text-anchor="middle" font-size="12" fill="#555">初動は感情的反応 → その後、合理的評価に移行する傾向</text>
<defs><marker id="an" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#d4a537"/></marker></defs>
</svg>'''

SVG_23 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="10" y="10" width="110" height="80" rx="8" fill="#0a2f5c"/><text x="65" y="42" text-anchor="middle" fill="#d4a537" font-size="20" font-weight="800">USD</text><text x="65" y="65" text-anchor="middle" fill="#8b949e" font-size="10">基軸通貨</text><text x="65" y="80" text-anchor="middle" fill="#8b949e" font-size="9">全取引の88%</text>
<rect x="130" y="10" width="110" height="80" rx="8" fill="#2e86c1"/><text x="185" y="42" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">EUR</text><text x="185" y="65" text-anchor="middle" fill="#d6eaf8" font-size="10">20カ国統一</text><text x="185" y="80" text-anchor="middle" fill="#d6eaf8" font-size="9">ECB</text>
<rect x="250" y="10" width="110" height="80" rx="8" fill="#c0392b"/><text x="305" y="42" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">JPY</text><text x="305" y="65" text-anchor="middle" fill="#fadbd8" font-size="10">安全通貨</text><text x="305" y="80" text-anchor="middle" fill="#fadbd8" font-size="9">超低金利</text>
<rect x="370" y="10" width="110" height="80" rx="8" fill="#8e44ad"/><text x="425" y="42" text-anchor="middle" fill="#fff" font-size="20" font-weight="800">GBP</text><text x="425" y="65" text-anchor="middle" fill="#d2b4de" font-size="10">高ボラ</text><text x="425" y="80" text-anchor="middle" fill="#d2b4de" font-size="9">ロンドン市場</text>
<rect x="70" y="110" width="110" height="70" rx="8" fill="#27ae60"/><text x="125" y="140" text-anchor="middle" fill="#fff" font-size="18" font-weight="800">AUD</text><text x="125" y="160" text-anchor="middle" fill="#d5f5e3" font-size="10">資源国・鉄鉱石</text>
<rect x="200" y="110" width="110" height="70" rx="8" fill="#d4a537"/><text x="255" y="140" text-anchor="middle" fill="#0a2f5c" font-size="18" font-weight="800">CAD</text><text x="255" y="160" text-anchor="middle" fill="#0a2f5c" font-size="10">原油相関</text>
<rect x="330" y="110" width="110" height="70" rx="8" fill="#1a3c6e"/><text x="385" y="140" text-anchor="middle" fill="#fff" font-size="18" font-weight="800">CHF</text><text x="385" y="160" text-anchor="middle" fill="#8b949e" font-size="10">安全通貨・介入</text>
</svg>'''

# Sections 24-35: Reusable concept SVGs
SVG_24 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<text x="250" y="22" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">COTレポート ── 大口投機家のポジション</text>
<rect x="30" y="35" width="440" height="30" rx="4" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
<rect x="30" y="35" width="300" height="30" rx="4" fill="#27ae60" opacity="0.7"/><text x="180" y="55" text-anchor="middle" fill="#fff" font-size="12" font-weight="600">ネットロング（強気）</text>
<rect x="330" y="35" width="140" height="30" rx="4" fill="#c0392b" opacity="0.7"/><text x="400" y="55" text-anchor="middle" fill="#fff" font-size="12" font-weight="600">ネットショート</text>
<text x="250" y="88" text-anchor="middle" font-size="12" fill="#555">↑ 極端に偏ると → 反転のシグナル</text>
<rect x="30" y="105" width="215" height="75" rx="8" fill="#27ae60" opacity="0.1" stroke="#27ae60" stroke-width="1"/>
<text x="138" y="130" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="700">Large Speculators</text>
<text x="138" y="150" text-anchor="middle" font-size="11" fill="#555">ヘッジファンド等</text>
<text x="138" y="168" text-anchor="middle" font-size="11" fill="#555">トレンドフォロー型</text>
<rect x="255" y="105" width="215" height="75" rx="8" fill="#2e86c1" opacity="0.1" stroke="#2e86c1" stroke-width="1"/>
<text x="363" y="130" text-anchor="middle" font-size="13" fill="#2e86c1" font-weight="700">Commercials</text>
<text x="363" y="150" text-anchor="middle" font-size="11" fill="#555">実需筋（企業ヘッジ）</text>
<text x="363" y="168" text-anchor="middle" font-size="11" fill="#555">トレンドに逆行傾向</text>
</svg>'''

SVG_25 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<text x="250" y="22" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">リテールセンチメント ── 逆指標として活用</text>
<rect x="30" y="35" width="440" height="30" rx="4" fill="#f8f9fa"/>
<rect x="30" y="35" width="350" height="30" rx="4" fill="#27ae60" opacity="0.7"/><text x="205" y="55" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">80% ロング（個人）</text>
<rect x="380" y="35" width="90" height="30" rx="4" fill="#c0392b" opacity="0.7"/><text x="425" y="55" text-anchor="middle" fill="#fff" font-size="12">20%</text>
<path d="M250,75 L250,95" stroke="#c0392b" stroke-width="2" marker-end="url(#as)"/>
<text x="250" y="115" text-anchor="middle" font-size="16" fill="#c0392b" font-weight="700">→ 下落の確率が高い</text>
<rect x="30" y="135" width="200" height="50" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="130" y="157" text-anchor="middle" font-size="12" fill="#0a2f5c" font-weight="700">VIX 10-15 = 安定</text>
<text x="130" y="175" text-anchor="middle" font-size="12" fill="#0a2f5c">VIX 30+ = 恐怖</text>
<rect x="250" y="135" width="220" height="50" rx="8" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/>
<text x="360" y="157" text-anchor="middle" font-size="12" fill="#0a2f5c" font-weight="700">3点セットで判断</text>
<text x="360" y="175" text-anchor="middle" font-size="12" fill="#0a2f5c">COT + リテール + VIX</text>
<defs><marker id="as" markerWidth="8" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#c0392b"/></marker></defs>
</svg>'''

SVG_26 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="20" y="10" width="460" height="80" rx="10" fill="#0a2f5c"/>
<text x="250" y="40" text-anchor="middle" fill="#d4a537" font-size="16" font-weight="700">ポジションサイズの計算式</text>
<text x="250" y="68" text-anchor="middle" fill="#fff" font-size="18" font-weight="600">（口座残高 × リスク%）÷（SL幅 × pip価値）= ロット</text>
<rect x="20" y="110" width="140" height="75" rx="8" fill="#27ae60" opacity="0.15" stroke="#27ae60" stroke-width="1"/>
<text x="90" y="135" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="700">口座: 100万円</text>
<text x="90" y="155" text-anchor="middle" font-size="12" fill="#555">リスク: 1%</text>
<text x="90" y="172" text-anchor="middle" font-size="12" fill="#555">= 1万円</text>
<rect x="180" y="110" width="140" height="75" rx="8" fill="#2e86c1" opacity="0.15" stroke="#2e86c1" stroke-width="1"/>
<text x="250" y="135" text-anchor="middle" font-size="13" fill="#2e86c1" font-weight="700">SL: 30 pips</text>
<text x="250" y="155" text-anchor="middle" font-size="12" fill="#555">pip価値: ¥1000</text>
<text x="250" y="172" text-anchor="middle" font-size="12" fill="#555">= ¥30,000</text>
<rect x="340" y="110" width="140" height="75" rx="8" fill="#d4a537" opacity="0.2" stroke="#d4a537" stroke-width="2"/>
<text x="410" y="140" text-anchor="middle" font-size="15" fill="#d4a537" font-weight="800">= 0.33 lot</text>
<text x="410" y="165" text-anchor="middle" font-size="12" fill="#555">適正ポジション</text>
</svg>'''

SVG_27 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<line x1="60" y1="20" x2="60" y2="170" stroke="#888" stroke-width="1.5"/>
<line x1="60" y1="170" x2="460" y2="170" stroke="#888" stroke-width="1.5"/>
<rect x="80" y="130" width="50" height="40" rx="4" fill="#c0392b" opacity="0.8"/><text x="105" y="155" text-anchor="middle" fill="#fff" font-size="10" font-weight="600">SL 20</text>
<rect x="80" y="50" width="50" height="80" rx="4" fill="#27ae60" opacity="0.8"/><text x="105" y="95" text-anchor="middle" fill="#fff" font-size="10" font-weight="600">TP 60</text>
<text x="105" y="185" text-anchor="middle" font-size="12" fill="#555" font-weight="600">RRR 1:3</text>
<rect x="200" y="30" width="270" height="70" rx="8" fill="#e8f0fe"/>
<text x="335" y="55" text-anchor="middle" font-size="14" fill="#0a2f5c" font-weight="700">勝率30%でもRRR 1:3なら利益が出る</text>
<text x="335" y="78" text-anchor="middle" font-size="12" fill="#555">期待値 = (0.3 × 60) - (0.7 × 20) = +4 /トレード</text>
<rect x="200" y="115" width="270" height="50" rx="8" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="1"/>
<text x="335" y="138" text-anchor="middle" font-size="13" fill="#d4a537" font-weight="700">期待値がプラス = 長期的に利益が出る戦略</text>
<text x="335" y="155" text-anchor="middle" font-size="11" fill="#555">最低100トレードのデータで算出する</text>
</svg>'''

SVG_28 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<line x1="60" y1="20" x2="60" y2="180" stroke="#888" stroke-width="1.5"/>
<polyline points="80,150 120,140 160,130 200,100 220,95 250,80 280,75 300,70" stroke="#2c3e50" stroke-width="2" fill="none"/>
<circle cx="200" cy="100" r="6" fill="#2e86c1"/><text x="210" y="95" font-size="12" fill="#2e86c1" font-weight="700">エントリー</text>
<line x1="60" y1="150" x2="350" y2="150" stroke="#c0392b" stroke-width="2" stroke-dasharray="6,3"/>
<text x="355" y="148" font-size="12" fill="#c0392b" font-weight="700">SL（構造ベース）</text>
<line x1="60" y1="50" x2="350" y2="50" stroke="#27ae60" stroke-width="2" stroke-dasharray="6,3"/>
<text x="355" y="48" font-size="12" fill="#27ae60" font-weight="700">TP1（次のS/R）</text>
<line x1="60" y1="30" x2="350" y2="30" stroke="#27ae60" stroke-width="1" stroke-dasharray="4,3" opacity="0.5"/>
<text x="355" y="28" font-size="11" fill="#27ae60" opacity="0.7">TP2（トレーリング）</text>
<rect x="62" y="50" width="6" height="100" rx="2" fill="#27ae60" opacity="0.1"/>
<text x="65" y="105" font-size="10" fill="#27ae60" transform="rotate(-90,65,105)">利益</text>
<rect x="62" y="100" width="6" height="50" rx="2" fill="#c0392b" opacity="0.1"/>
</svg>'''

SVG_29 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<line x1="40" y1="180" x2="460" y2="180" stroke="#888" stroke-width="1"/>
<line x1="40" y1="20" x2="40" y2="180" stroke="#888" stroke-width="1"/>
<text x="20" y="100" text-anchor="middle" font-size="10" fill="#888" transform="rotate(-90,20,100)">口座残高</text>
<polyline points="50,40 100,35 150,45 180,42 210,60 230,100 250,90 280,95 300,110 330,105 360,100 390,95 420,90 450,85" stroke="#2e86c1" stroke-width="2.5" fill="none"/>
<line x1="180" y1="42" x2="300" y2="42" stroke="#d4a537" stroke-width="1" stroke-dasharray="4,3"/>
<text x="310" y="40" font-size="10" fill="#d4a537">ピーク</text>
<path d="M230,100 L230,42" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="3,2"/>
<text x="235" y="75" font-size="11" fill="#c0392b" font-weight="700">DD</text>
<rect x="60" y="140" width="380" height="30" rx="6" fill="#e8f0fe"/>
<text x="250" y="160" text-anchor="middle" font-size="13" fill="#0a2f5c" font-weight="700">50%のDD → 回復に100%の利益が必要 → 目標: DD 20%以内</text>
</svg>'''

SVG_30 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="20" y="10" width="110" height="80" rx="10" fill="#c0392b" opacity="0.15" stroke="#c0392b" stroke-width="1.5"/>
<text x="75" y="42" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">恐怖</text>
<text x="75" y="62" text-anchor="middle" font-size="10" fill="#555">Fear</text>
<text x="75" y="80" text-anchor="middle" font-size="9" fill="#888">エントリーできない</text>
<rect x="140" y="10" width="110" height="80" rx="10" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="1.5"/>
<text x="195" y="42" text-anchor="middle" font-size="14" fill="#d4a537" font-weight="700">欲望</text>
<text x="195" y="62" text-anchor="middle" font-size="10" fill="#555">Greed</text>
<text x="195" y="80" text-anchor="middle" font-size="9" fill="#888">ロット過大</text>
<rect x="260" y="10" width="110" height="80" rx="10" fill="#2e86c1" opacity="0.15" stroke="#2e86c1" stroke-width="1.5"/>
<text x="315" y="42" text-anchor="middle" font-size="14" fill="#2e86c1" font-weight="700">希望</text>
<text x="315" y="62" text-anchor="middle" font-size="10" fill="#555">Hope</text>
<text x="315" y="80" text-anchor="middle" font-size="9" fill="#888">SLを外す</text>
<rect x="380" y="10" width="110" height="80" rx="10" fill="#8e44ad" opacity="0.15" stroke="#8e44ad" stroke-width="1.5"/>
<text x="435" y="42" text-anchor="middle" font-size="14" fill="#8e44ad" font-weight="700">後悔</text>
<text x="435" y="62" text-anchor="middle" font-size="10" fill="#555">Regret</text>
<text x="435" y="80" text-anchor="middle" font-size="9" fill="#888">追いかける</text>
<rect x="20" y="110" width="470" height="70" rx="10" fill="#e8f0fe"/>
<text x="255" y="138" text-anchor="middle" font-size="15" fill="#0a2f5c" font-weight="700">対策: ルーティン + チェックリスト + 損失上限 + ジャーナル</text>
<text x="255" y="163" text-anchor="middle" font-size="12" fill="#555">感情をゼロにするのは不可能 → 管理する仕組みを作る</text>
</svg>'''

SVG_31 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="20" y="10" width="220" height="80" rx="10" fill="#c0392b" opacity="0.1" stroke="#c0392b" stroke-width="1.5"/>
<text x="130" y="38" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">損失回避バイアス</text>
<text x="130" y="58" text-anchor="middle" font-size="12" fill="#555">損失の痛み = 利益の喜びの2倍</text>
<text x="130" y="78" text-anchor="middle" font-size="12" fill="#c0392b" font-weight="600">→ 利小損大の元凶</text>
<rect x="260" y="10" width="220" height="80" rx="10" fill="#2e86c1" opacity="0.1" stroke="#2e86c1" stroke-width="1.5"/>
<text x="370" y="38" text-anchor="middle" font-size="14" fill="#2e86c1" font-weight="700">確証バイアス</text>
<text x="370" y="58" text-anchor="middle" font-size="12" fill="#555">信念に合う情報だけ集める</text>
<text x="370" y="78" text-anchor="middle" font-size="12" fill="#2e86c1" font-weight="600">→ 反証データを無視</text>
<rect x="20" y="110" width="460" height="70" rx="10" fill="#27ae60" opacity="0.1" stroke="#27ae60" stroke-width="1.5"/>
<text x="250" y="138" text-anchor="middle" font-size="15" fill="#27ae60" font-weight="700">対策: ルールベースの戦略 + SL/TP自動設定 + ジャーナル</text>
<text x="250" y="163" text-anchor="middle" font-size="12" fill="#555">「感覚」ではなく「数字」で判断。システムでバイアスから守る</text>
</svg>'''

SVG_32 = '''<svg viewBox="0 0 500 220" width="100%" style="max-width:620px">
<text x="250" y="22" text-anchor="middle" font-size="15" fill="#2c3e50" font-weight="700">トレーダーの1日のルーティン</text>
<rect x="20" y="35" width="90" height="70" rx="8" fill="#0a2f5c"/><text x="65" y="62" text-anchor="middle" fill="#d4a537" font-size="11" font-weight="700">プレマーケット</text><text x="65" y="80" text-anchor="middle" fill="#8b949e" font-size="9">カレンダー確認</text><text x="65" y="92" text-anchor="middle" fill="#8b949e" font-size="9">S/Rマーキング</text>
<path d="M112,70 L128,70" stroke="#d4a537" stroke-width="1.5" marker-end="url(#ar2)"/>
<rect x="130" y="35" width="90" height="70" rx="8" fill="#2e86c1"/><text x="175" y="62" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">チェックリスト</text><text x="175" y="80" text-anchor="middle" fill="#d6eaf8" font-size="9">全条件確認</text><text x="175" y="92" text-anchor="middle" fill="#d6eaf8" font-size="9">エントリー判断</text>
<path d="M222,70 L238,70" stroke="#d4a537" stroke-width="1.5" marker-end="url(#ar2)"/>
<rect x="240" y="35" width="90" height="70" rx="8" fill="#27ae60"/><text x="285" y="62" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">トレード実行</text><text x="285" y="80" text-anchor="middle" fill="#d5f5e3" font-size="9">SL/TP設定</text><text x="285" y="92" text-anchor="middle" fill="#d5f5e3" font-size="9">ルール遵守</text>
<path d="M332,70 L348,70" stroke="#d4a537" stroke-width="1.5" marker-end="url(#ar2)"/>
<rect x="350" y="35" width="90" height="70" rx="8" fill="#d4a537"/><text x="395" y="62" text-anchor="middle" fill="#0a2f5c" font-size="11" font-weight="700">ジャーナル</text><text x="395" y="80" text-anchor="middle" fill="#0a2f5c" font-size="9">結果・感情記録</text><text x="395" y="92" text-anchor="middle" fill="#0a2f5c" font-size="9">改善点メモ</text>
<rect x="20" y="125" width="420" height="40" rx="8" fill="#e8f0fe"/>
<text x="230" y="150" text-anchor="middle" font-size="13" fill="#0a2f5c" font-weight="700">週次/月次レビュー → パフォーマンスを定量評価 → 改善</text>
<defs><marker id="ar2" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill="#d4a537"/></marker></defs>
</svg>'''

SVG_33 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="20" y="10" width="460" height="45" rx="8" fill="#0a2f5c"/>
<text x="250" y="38" text-anchor="middle" fill="#d4a537" font-size="16" font-weight="700">トレーディングプラン = 全判断ルールの設計図</text>
<rect x="20" y="70" width="145" height="55" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="93" y="92" text-anchor="middle" font-size="11" fill="#0a2f5c" font-weight="700">市場・時間軸</text><text x="93" y="110" text-anchor="middle" font-size="10" fill="#555">何を・いつ取引</text>
<rect x="177" y="70" width="145" height="55" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="250" y="92" text-anchor="middle" font-size="11" fill="#0a2f5c" font-weight="700">エントリー/イグジット</text><text x="250" y="110" text-anchor="middle" font-size="10" fill="#555">条件・SL・TP</text>
<rect x="335" y="70" width="145" height="55" rx="6" fill="#e8f0fe" stroke="#2e86c1" stroke-width="1"/><text x="408" y="92" text-anchor="middle" font-size="11" fill="#0a2f5c" font-weight="700">リスク管理</text><text x="408" y="110" text-anchor="middle" font-size="10" fill="#555">1%ルール・上限</text>
<rect x="20" y="140" width="460" height="45" rx="8" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="1.5"/>
<text x="250" y="168" text-anchor="middle" font-size="13" fill="#d4a537" font-weight="700">プランに従ったが負けた = 良いトレード / 従わず勝った = 悪いトレード</text>
</svg>'''

SVG_34 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<text x="250" y="22" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="700">バックテスト評価指標</text>
<rect x="20" y="35" width="145" height="65" rx="8" fill="#27ae60" opacity="0.15" stroke="#27ae60" stroke-width="1"/>
<text x="93" y="58" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="700">プロフィットファクター</text>
<text x="93" y="78" text-anchor="middle" font-size="18" fill="#27ae60" font-weight="800">≥ 1.5</text>
<rect x="177" y="35" width="145" height="65" rx="8" fill="#2e86c1" opacity="0.15" stroke="#2e86c1" stroke-width="1"/>
<text x="250" y="58" text-anchor="middle" font-size="13" fill="#2e86c1" font-weight="700">最大ドローダウン</text>
<text x="250" y="78" text-anchor="middle" font-size="18" fill="#2e86c1" font-weight="800">≤ 20%</text>
<rect x="335" y="35" width="145" height="65" rx="8" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="1"/>
<text x="408" y="58" text-anchor="middle" font-size="13" fill="#d4a537" font-weight="700">サンプル数</text>
<text x="408" y="78" text-anchor="middle" font-size="18" fill="#d4a537" font-weight="800">≥ 100</text>
<rect x="20" y="115" width="460" height="65" rx="8" fill="#c0392b" opacity="0.08" stroke="#c0392b" stroke-width="1"/>
<text x="250" y="140" text-anchor="middle" font-size="14" fill="#c0392b" font-weight="700">カーブフィッティングに注意</text>
<text x="250" y="162" text-anchor="middle" font-size="12" fill="#555">結果が「良すぎる」場合は過学習の疑い → ウォークフォワード検証で確認</text>
</svg>'''

SVG_35 = '''<svg viewBox="0 0 500 200" width="100%" style="max-width:620px">
<rect x="10" y="10" width="150" height="80" rx="8" fill="#27ae60" opacity="0.15" stroke="#27ae60" stroke-width="1.5"/>
<text x="85" y="38" text-anchor="middle" font-size="13" fill="#27ae60" font-weight="700">ブレイクアウト</text>
<text x="85" y="58" text-anchor="middle" font-size="10" fill="#555">レンジ突破</text>
<text x="85" y="75" text-anchor="middle" font-size="10" fill="#555">RRR: 高</text>
<rect x="175" y="10" width="150" height="80" rx="8" fill="#2e86c1" opacity="0.15" stroke="#2e86c1" stroke-width="1.5"/>
<text x="250" y="38" text-anchor="middle" font-size="13" fill="#2e86c1" font-weight="700">プルバック</text>
<text x="250" y="58" text-anchor="middle" font-size="10" fill="#555">押し目/戻り</text>
<text x="250" y="75" text-anchor="middle" font-size="10" fill="#555">勝率: 高</text>
<rect x="340" y="10" width="150" height="80" rx="8" fill="#d4a537" opacity="0.15" stroke="#d4a537" stroke-width="1.5"/>
<text x="415" y="38" text-anchor="middle" font-size="13" fill="#d4a537" font-weight="700">ミーンリバージョン</text>
<text x="415" y="58" text-anchor="middle" font-size="10" fill="#555">平均回帰</text>
<text x="415" y="75" text-anchor="middle" font-size="10" fill="#555">レンジ専用</text>
<rect x="10" y="110" width="480" height="70" rx="10" fill="#e8f0fe"/>
<text x="250" y="138" text-anchor="middle" font-size="15" fill="#0a2f5c" font-weight="700">最良の戦略 = 自分が一貫して実行できる戦略</text>
<text x="250" y="163" text-anchor="middle" font-size="12" fill="#555">性格・生活スタイル・リスク許容度に合う1つを徹底的にマスターする</text>
</svg>'''

# Map section number to SVG
SVGS = {
    "09": SVG_09, "10": SVG_10, "11": SVG_11, "12": SVG_12, "13": SVG_13,
    "14": SVG_14, "15": SVG_15, "16": SVG_16, "17": SVG_17, "18": SVG_18,
    "19": SVG_19, "20": SVG_20, "21": SVG_21, "22": SVG_22, "23": SVG_23,
    "24": SVG_24, "25": SVG_25, "26": SVG_26, "27": SVG_27, "28": SVG_28,
    "29": SVG_29, "30": SVG_30, "31": SVG_31, "32": SVG_32, "33": SVG_33,
    "34": SVG_34, "35": SVG_35,
}
