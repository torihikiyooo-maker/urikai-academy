#!/usr/bin/env python3
"""
Generate ALL chart images for URIKAI Trading Academy using matplotlib
All text/labels are baked into the PNG images
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib_fontja
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

plt.style.use('dark_background')
OUT = "/mnt/c/Users/konog/.claude/urikai-academy/slides/img"
os.makedirs(OUT, exist_ok=True)

# Colors
G='#27ae60'; R='#e74c3c'; GOLD='#d4a537'; BLUE='#2e86c1'
BG='#131c2b'; GRID='#1e3045'; TM='#8b949e'; PURPLE='#8e44ad'

def dc(ax, x, o, h, l, c, w=0.6):
    """Draw candlestick"""
    col = G if c>=o else R
    bl,bh = min(o,c), max(o,c)
    ax.plot([x,x],[l,bl], color=col, lw=1.2)
    ax.plot([x,x],[bh,h], color=col, lw=1.2)
    ax.add_patch(patches.FancyBboxPatch((x-w/2,bl),w,max(bh-bl,0.0001),
        boxstyle="round,pad=0.01",fc=col,ec=col))

def mk(figsize=(10,5.6)):
    """Make chart"""
    fig,ax = plt.subplots(1,1,figsize=figsize,facecolor=BG)
    ax.set_facecolor(BG); ax.grid(True,color=GRID,lw=0.5,alpha=0.5)
    ax.tick_params(colors=TM,labelsize=8)
    for s in ax.spines.values(): s.set_color(GRID)
    return fig,ax

def save(fig, name):
    plt.tight_layout()
    plt.savefig(f'{OUT}/{name}', dpi=150, bbox_inches='tight', facecolor=BG, edgecolor='none')
    plt.close()
    print(f"  OK: {name}")

np.random.seed(42)

# ===== 08: ローソク足パターン =====

# 08-2: 単体パターン6種
fig, axes = plt.subplots(1, 6, figsize=(14, 4), facecolor=BG)
patterns = [
    ("同時線\nDoji", [(100,101,99,100.05)]),
    ("ハンマー\nHammer", [(100,100.5,97,100.3)]),
    ("流れ星\nShooting Star", [(100,103,99.8,99.9)]),
    ("大陽線\nMarubozu", [(98,103,97.8,102.8)]),
    ("大陰線\nMarubozu", [(103,103.2,97.8,98)]),
    ("コマ\nSpinning Top", [(100,102,98,100.2)]),
]
for ax, (name, data) in zip(axes, patterns):
    ax.set_facecolor(BG)
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    for o,h,l,c in data:
        dc(ax, 0, o, h, l, c, 0.8)
    col = G if data[0][3]>=data[0][0] else (R if data[0][3]<data[0][0] else TM)
    if "同時" in name: col = TM
    if "コマ" in name: col = TM
    ax.set_title(name, fontsize=11, color=col, fontweight='bold', pad=8)
    ax.set_xlim(-1.5, 1.5)
plt.suptitle('単体ローソク足パターン', fontsize=14, color=GOLD, fontweight='bold', y=1.02)
save(fig, '08-2.png')

# 08-3: モーニングスター & イブニングスター
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), facecolor=BG)
for ax in [ax1, ax2]:
    ax.set_facecolor(BG); ax.grid(True,color=GRID,lw=0.3,alpha=0.3)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color(GRID)

# Morning Star
dc(ax1, 0, 105, 106, 98, 99, 1.2)
dc(ax1, 2, 99.5, 100, 97.5, 98, 0.8)
dc(ax1, 4, 98.5, 106, 98, 105, 1.2)
ax1.annotate('', xy=(5.5,105), xytext=(5.5,99), arrowprops=dict(arrowstyle='->', color=G, lw=2.5))
ax1.set_title('モーニングスター（強気反転）', fontsize=13, color=G, fontweight='bold', pad=10)
ax1.text(0, 107, '大陰線', fontsize=9, color=R, ha='center')
ax1.text(2, 107, '小実体', fontsize=9, color=TM, ha='center')
ax1.text(4, 107, '大陽線', fontsize=9, color=G, ha='center')
ax1.set_xlim(-2, 7)

# Evening Star
dc(ax2, 0, 99, 98, 106, 105, 1.2)
dc(ax2, 2, 105, 107, 104.5, 106, 0.8)
dc(ax2, 4, 105.5, 106, 98, 99, 1.2)
ax2.annotate('', xy=(5.5,99), xytext=(5.5,105), arrowprops=dict(arrowstyle='->', color=R, lw=2.5))
ax2.set_title('イブニングスター（弱気反転）', fontsize=13, color=R, fontweight='bold', pad=10)
ax2.text(0, 96.5, '大陽線', fontsize=9, color=G, ha='center')
ax2.text(2, 96.5, '小実体', fontsize=9, color=TM, ha='center')
ax2.text(4, 96.5, '大陰線', fontsize=9, color=R, ha='center')
ax2.set_xlim(-2, 7)
save(fig, '08-3.png')

# 08-4: エンゴルフィング
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), facecolor=BG)
for ax in [ax1, ax2]:
    ax.set_facecolor(BG); ax.grid(True,color=GRID,lw=0.3,alpha=0.3)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color(GRID)

# Bullish Engulfing
dc(ax1, 0, 104, 105, 100, 101, 1.0)
dc(ax1, 2, 100.5, 106, 99.5, 105.5, 1.4)
ax1.set_title('強気エンゴルフィング', fontsize=13, color=G, fontweight='bold', pad=10)
ax1.text(0, 106.5, '陰線', fontsize=10, color=R, ha='center')
ax1.text(2, 106.5, '陽線（包み込む）', fontsize=10, color=G, ha='center')
ax1.annotate('', xy=(3.5,105.5), xytext=(3.5,101), arrowprops=dict(arrowstyle='->', color=G, lw=2, alpha=0.5))
ax1.set_xlim(-2, 5)

# Bearish Engulfing
dc(ax2, 0, 100, 105, 99.5, 104, 1.0)
dc(ax2, 2, 104.5, 105.5, 98.5, 99, 1.4)
ax2.set_title('弱気エンゴルフィング', fontsize=13, color=R, fontweight='bold', pad=10)
ax2.text(0, 96.5, '陽線', fontsize=10, color=G, ha='center')
ax2.text(2, 96.5, '陰線（包み込む）', fontsize=10, color=R, ha='center')
ax2.annotate('', xy=(3.5,99), xytext=(3.5,104), arrowprops=dict(arrowstyle='->', color=R, lw=2, alpha=0.5))
ax2.set_xlim(-2, 5)
save(fig, '08-4.png')

# ===== 09: S/R (already done as 09-1-new, 09-2-new) =====
# Rename existing
for old, new in [('09-1-new.png','09-1.png'), ('09-2-new.png','09-2.png'), ('08-1-new.png','08-1.png')]:
    old_p = f'{OUT}/{old}'
    new_p = f'{OUT}/{new}'
    if os.path.exists(old_p):
        if os.path.exists(new_p): os.remove(new_p)
        os.rename(old_p, new_p)
        print(f"  Renamed: {old} → {new}")

# 09-3: ロールリバーサル
fig, ax = mk()
n = 30
# Price above support, breaks below, retests, falls
ohlc = []
price = 108
for i in range(n):
    if i < 8:  # Above support, declining
        move = np.random.uniform(-0.8, 0.3)
    elif i < 10:  # Bounce at 105
        move = np.random.uniform(0.2, 1.0)
        price = max(price, 105.2)
    elif i < 14:  # Break below 105
        move = np.random.uniform(-1.5, -0.3)
    elif i < 18:  # Retest from below
        move = np.random.uniform(0.3, 1.2)
    elif i == 18:  # Rejection at 105
        move = -0.5
        price = min(price, 105.3)
    else:  # Fall away
        move = np.random.uniform(-1.5, -0.2)
    o = price; c = price + move
    h = max(o,c) + np.random.uniform(0.1,0.6); l = min(o,c) - np.random.uniform(0.1,0.6)
    ohlc.append((o,h,l,c)); price = c

for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.6)

ax.axhline(y=105, color=BLUE, lw=2, ls='--', alpha=0.7)
ax.axhspan(104.7, 105.3, alpha=0.06, color=BLUE)

# Phase labels
ax.text(4, 109.5, 'サポートとして機能', fontsize=11, color=G, fontweight='bold', ha='center',
    bbox=dict(boxstyle='round,pad=0.3', fc=G, alpha=0.15))
ax.text(12, 101, '下方ブレイク ↓', fontsize=11, color=R, fontweight='bold', ha='center',
    bbox=dict(boxstyle='round,pad=0.3', fc=R, alpha=0.15))
ax.text(17, 106.5, 'リテスト', fontsize=11, color=GOLD, fontweight='bold', ha='center',
    bbox=dict(boxstyle='round,pad=0.3', fc=GOLD, alpha=0.2))
ax.text(24, 98, 'レジスタンスとして反落 ↓', fontsize=11, color=R, fontweight='bold', ha='center',
    bbox=dict(boxstyle='round,pad=0.3', fc=R, alpha=0.15))

ax.text(n+1, 105, 'S/R ライン', fontsize=10, color=BLUE, fontweight='bold', va='center')
ax.set_xlim(-1, n+6); ax.set_xticks([])
plt.title('ロールリバーサル（S/R転換）', fontsize=14, color=GOLD, fontweight='bold', pad=10)
save(fig, '09-3.png')

# ===== 10: インジケーター =====

# 10-1: MA ゴールデンクロス
fig, ax = mk()
n = 35
price = 100
ohlc = []
for i in range(n):
    if i<12: trend=-0.15
    elif i<18: trend=np.random.uniform(-0.05,0.05)
    else: trend=0.2
    noise = np.random.uniform(-0.3,0.3)
    o=price; c=price+trend+noise
    h=max(o,c)+np.random.uniform(0.05,0.3); l=min(o,c)-np.random.uniform(0.05,0.3)
    ohlc.append((o,h,l,c)); price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.6)
closes = [c for _,_,_,c in ohlc]
def sma(d,p):
    r=[]
    for i in range(len(d)):
        s=d[max(0,i-p+1):i+1]; r.append(sum(s)/len(s))
    return r
ma5=sma(closes,5); ma15=sma(closes,15)
ax.plot(range(n),ma5,color=GOLD,lw=2.5,label='短期MA (5)')
ax.plot(range(n),ma15,color=R,lw=2,ls='--',label='長期MA (15)')
# Find cross
for i in range(1,n):
    if ma5[i-1]<=ma15[i-1] and ma5[i]>ma15[i]:
        ax.annotate('ゴールデンクロス', xy=(i,ma5[i]), xytext=(i+3,ma5[i]+1.5),
            fontsize=12, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', fc=GOLD, alpha=0.2))
        break
ax.legend(loc='upper left',fontsize=10,facecolor=BG,edgecolor=GRID)
ax.set_xticks([])
plt.title('移動平均線 ── ゴールデンクロス', fontsize=14, color=GOLD, fontweight='bold', pad=10)
save(fig, '10-1.png')

# 10-2: RSI ダイバージェンス
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,6), facecolor=BG, gridspec_kw={'height_ratios':[2,1]})
for ax in [ax1,ax2]:
    ax.set_facecolor(BG); ax.grid(True,color=GRID,lw=0.3,alpha=0.3)
    for s in ax.spines.values(): s.set_color(GRID)
    ax.tick_params(colors=TM,labelsize=7)

n=25
price=100; ohlc=[]
for i in range(n):
    if i<10: move=np.random.uniform(0.1,0.6)
    elif i<15: move=np.random.uniform(-0.4,0.2)
    elif i<22: move=np.random.uniform(0.05,0.5)
    else: move=np.random.uniform(-0.8,-0.1)
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.05,0.3);l=min(o,c)-np.random.uniform(0.05,0.3)
    ohlc.append((o,h,l,c)); price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax1,i,o,h,l,c,0.6)
ax1.set_xticks([]); ax1.set_title('価格: 高値更新', fontsize=10, color=TM, loc='left')
# Higher high line on price
ax1.plot([9,21],[max(h for _,h,_,_ in ohlc[8:11]),max(h for _,h,_,_ in ohlc[19:23])],
    color=GOLD, lw=1.5, ls='--', alpha=0.6)

# RSI
rsi_vals = [50]
for i in range(1,n):
    if i<10: rsi_vals.append(min(78,rsi_vals[-1]+np.random.uniform(1,4)))
    elif i<15: rsi_vals.append(max(42,rsi_vals[-1]-np.random.uniform(1,3)))
    elif i<22: rsi_vals.append(min(68,rsi_vals[-1]+np.random.uniform(0.5,2.5)))  # Lower high!
    else: rsi_vals.append(max(32,rsi_vals[-1]-np.random.uniform(2,5)))
ax2.plot(range(n),rsi_vals,color=PURPLE,lw=2)
ax2.axhline(70,color=R,lw=0.8,ls='--',alpha=0.5)
ax2.axhline(30,color=G,lw=0.8,ls='--',alpha=0.5)
ax2.set_ylim(20,85); ax2.set_xticks([])
ax2.set_title('RSI: 高値切り下げ（ダイバージェンス）', fontsize=10, color=TM, loc='left')
ax2.text(n+0.5,70,'70',fontsize=8,color=R,va='center')
ax2.text(n+0.5,30,'30',fontsize=8,color=G,va='center')
# Lower high line on RSI
ax2.plot([9,21],[max(rsi_vals[8:11]),max(rsi_vals[19:23])],
    color=GOLD, lw=1.5, ls='--', alpha=0.6)
ax2.text(15,75,'ダイバージェンス',fontsize=11,color=GOLD,fontweight='bold',ha='center',
    bbox=dict(boxstyle='round,pad=0.3',fc=GOLD,alpha=0.15))
plt.suptitle('RSI ── ダイバージェンスの検出',fontsize=14,color=GOLD,fontweight='bold')
save(fig, '10-2.png')

# 10-3: MACD
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,6), facecolor=BG, gridspec_kw={'height_ratios':[2,1]})
for ax in [ax1,ax2]:
    ax.set_facecolor(BG); ax.grid(True,color=GRID,lw=0.3,alpha=0.3)
    for s in ax.spines.values(): s.set_color(GRID)
    ax.tick_params(colors=TM,labelsize=7)
n=30; price=100; ohlc=[]
for i in range(n):
    if i<10: trend=-0.1
    elif i<15: trend=0
    else: trend=0.15
    noise=np.random.uniform(-0.3,0.3)
    o=price;c=price+trend+noise;h=max(o,c)+np.random.uniform(0.05,0.2);l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c)); price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax1,i,o,h,l,c,0.6)
ax1.set_xticks([])
closes=[c for _,_,_,c in ohlc]
def ema(d,p):
    r=[d[0]]; k=2/(p+1)
    for i in range(1,len(d)): r.append(d[i]*k+r[-1]*(1-k))
    return r
e12=ema(closes,12); e26=ema(closes,26)
macd_l=[e12[i]-e26[i] for i in range(n)]
sig=ema(macd_l,9)
hist=[macd_l[i]-sig[i] for i in range(n)]
for i in range(n):
    col=G if hist[i]>=0 else R
    ax2.bar(i,hist[i],color=col,alpha=0.5,width=0.7)
ax2.plot(range(n),macd_l,color=BLUE,lw=2,label='MACD')
ax2.plot(range(n),sig,color=R,lw=1.5,ls='--',label='シグナル')
ax2.axhline(0,color=TM,lw=0.5,ls='--',alpha=0.3)
ax2.legend(loc='upper left',fontsize=9,facecolor=BG,edgecolor=GRID)
ax2.set_xticks([])
plt.suptitle('MACD ── シグナルクロスとヒストグラム',fontsize=14,color=GOLD,fontweight='bold')
save(fig, '10-3.png')

# 10-4: ボリンジャーバンド
fig, ax = mk()
n=35; price=100; ohlc=[]
for i in range(n):
    if i<15: vol=0.15
    elif i==15: vol=1.0  # breakout
    else: vol=0.4
    move=np.random.uniform(-vol,vol)
    if i>=15: move+=0.15  # uptrend after breakout
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.02,vol*0.3);l=min(o,c)-np.random.uniform(0.02,vol*0.3)
    ohlc.append((o,h,l,c)); price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.5)
closes=[c for _,_,_,c in ohlc]
period=10
mid_b,up_b,lo_b=[],[],[]
for i in range(n):
    w=closes[max(0,i-period+1):i+1]; m=sum(w)/len(w)
    std=(sum((x-m)**2 for x in w)/len(w))**0.5
    mid_b.append(m); up_b.append(m+2*std); lo_b.append(m-2*std)
ax.plot(range(n),mid_b,color=GOLD,lw=1.5,label='ミドル(SMA)')
ax.plot(range(n),up_b,color=BLUE,lw=1.2,label='±2σ')
ax.plot(range(n),lo_b,color=BLUE,lw=1.2)
ax.fill_between(range(n),up_b,lo_b,alpha=0.05,color=BLUE)
ax.text(7,max(closes[:15])+0.5,'スクイーズ',fontsize=11,color=GOLD,fontweight='bold',ha='center',
    bbox=dict(boxstyle='round,pad=0.3',fc=GOLD,alpha=0.15))
ax.text(25,max(closes[15:])+0.5,'バンドウォーク',fontsize=11,color=G,fontweight='bold',ha='center',
    bbox=dict(boxstyle='round,pad=0.3',fc=G,alpha=0.15))
ax.legend(loc='lower left',fontsize=9,facecolor=BG,edgecolor=GRID)
ax.set_xticks([])
plt.title('ボリンジャーバンド ── スクイーズ → ブレイクアウト',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '10-4.png')

# 10-5: ATR
fig, (ax1,ax2) = plt.subplots(2,1,figsize=(10,5.5),facecolor=BG,gridspec_kw={'height_ratios':[2,1]})
for ax in [ax1,ax2]:
    ax.set_facecolor(BG);ax.grid(True,color=GRID,lw=0.3,alpha=0.3)
    for s in ax.spines.values(): s.set_color(GRID)
    ax.tick_params(colors=TM,labelsize=7)
n=28;price=100;ohlc=[]
for i in range(n):
    if i<12: vol=0.15
    elif i<20: vol=0.8
    else: vol=0.25
    move=np.random.uniform(-vol,vol)
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.02,vol*0.4);l=min(o,c)-np.random.uniform(0.02,vol*0.4)
    ohlc.append((o,h,l,c)); price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax1,i,o,h,l,c,0.6)
ax1.set_xticks([]); ax1.set_title('価格',fontsize=9,color=TM,loc='left')
# ATR
trs=[]
for i in range(n):
    o,h,l,c=ohlc[i]
    if i==0: trs.append(h-l)
    else:
        pc=ohlc[i-1][3]; trs.append(max(h-l,abs(h-pc),abs(l-pc)))
atr=[trs[0]]
for i in range(1,n): atr.append((atr[-1]*13+trs[i])/14)
ax2.plot(range(n),atr,color=GOLD,lw=2.5)
ax2.fill_between(range(n),0,atr,alpha=0.1,color=GOLD)
ax2.set_xticks([]); ax2.set_title('ATR (14)',fontsize=9,color=TM,loc='left')
spike_i=np.argmax(atr)
ax2.annotate('ATR急上昇\nボラティリティ拡大',xy=(spike_i,atr[spike_i]),xytext=(spike_i+4,atr[spike_i]*0.9),
    fontsize=10,color=GOLD,fontweight='bold',arrowprops=dict(arrowstyle='->',color=GOLD,lw=1.5),
    bbox=dict(boxstyle='round,pad=0.3',fc=GOLD,alpha=0.15))
plt.suptitle('ATR ── ボラティリティの可視化',fontsize=14,color=GOLD,fontweight='bold')
save(fig, '10-5.png')

# ===== 11: チャートパターン =====

# 11-1: ヘッドアンドショルダー
fig, ax = mk()
n=35; price=100; ohlc=[]
phases = [(5,0.5),(3,-0.3),(5,0.8),(5,-0.7),(3,0.4),(4,-0.3),(5,-0.6)]
for count, trend in phases:
    for _ in range(count):
        move=trend+np.random.uniform(-0.2,0.2)
        o=price;c=price+move;h=max(o,c)+np.random.uniform(0.05,0.25);l=min(o,c)-np.random.uniform(0.05,0.25)
        ohlc.append((o,h,l,c));price=c
ohlc=ohlc[:n]
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.6)

# Neckline
neck_y = min(ohlc[7][2], ohlc[17][2])
ax.axhline(y=neck_y, color=R, lw=1.5, ls='--', alpha=0.6)
ax.text(n+0.5, neck_y, 'ネックライン', fontsize=10, color=R, fontweight='bold', va='center')
ax.text(4, max(h for _,h,_,_ in ohlc[3:7])+0.3, '左肩', fontsize=10, color=TM, ha='center',
    bbox=dict(boxstyle='round,pad=0.2',fc=BG,ec=TM,lw=0.5))
ax.text(12, max(h for _,h,_,_ in ohlc[8:16])+0.3, '頭', fontsize=11, color=GOLD, ha='center', fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.2',fc=GOLD,alpha=0.2))
ax.text(22, max(h for _,h,_,_ in ohlc[18:25])+0.3, '右肩', fontsize=10, color=TM, ha='center',
    bbox=dict(boxstyle='round,pad=0.2',fc=BG,ec=TM,lw=0.5))
ax.set_xlim(-1,n+5); ax.set_xticks([])
plt.title('ヘッドアンドショルダー（H&S）── 反転パターン',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '11-1.png')

# 11-2: ダブルトップ
fig, ax = mk()
n=25; price=100; ohlc=[]
for i in range(n):
    if i<7: move=np.random.uniform(0.2,0.7)
    elif i<10: move=np.random.uniform(-0.5,-0.1)
    elif i<17: move=np.random.uniform(0.15,0.6)
    else: move=np.random.uniform(-0.7,-0.1)
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.05,0.2);l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c));price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.6)
top1=max(h for _,h,_,_ in ohlc[5:8])
top2=max(h for _,h,_,_ in ohlc[14:18])
ax.plot([6],[top1],'v',color=R,markersize=10)
ax.plot([15],[top2],'v',color=R,markersize=10)
ax.text(6,top1+0.4,'Top 1',fontsize=10,color=R,ha='center',fontweight='bold')
ax.text(15,top2+0.4,'Top 2',fontsize=10,color=R,ha='center',fontweight='bold')
neck=min(l for _,_,l,_ in ohlc[8:11])
ax.axhline(y=neck,color=R,lw=1.5,ls='--',alpha=0.6)
ax.text(n+0.5,neck,'ネックライン',fontsize=10,color=R,fontweight='bold',va='center')
ax.set_xlim(-1,n+5); ax.set_xticks([])
plt.title('ダブルトップ（M型）── 反転パターン',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '11-2.png')

# 11-3: ブルフラッグ
fig, ax = mk()
n=20; price=100; ohlc=[]
for i in range(n):
    if i<5: move=np.random.uniform(0.6,1.2)  # Flagpole
    elif i<13: move=np.random.uniform(-0.15,0.05)  # Flag
    else: move=np.random.uniform(0.5,1.0)  # Breakout
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.05,0.2);l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c));price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.7)
# Flag channel
flag_h = [max(o,c) for o,_,_,c in ohlc[5:13]]
flag_l = [min(o,c) for o,_,_,c in ohlc[5:13]]
z_h = np.polyfit(range(8), flag_h, 1)
z_l = np.polyfit(range(8), flag_l, 1)
fx = np.array([-0.5, 8.5])
ax.plot(fx+5, z_h[0]*fx+z_h[1], color=GOLD, lw=1.5, ls='--', alpha=0.6)
ax.plot(fx+5, z_l[0]*fx+z_l[1], color=GOLD, lw=1.5, ls='--', alpha=0.6)
ax.text(2, max(h for _,h,_,_ in ohlc[:5])+0.3, 'フラッグポール', fontsize=10, color=G, fontweight='bold', ha='center')
ax.text(9, min(l for _,_,l,_ in ohlc[5:13])-0.5, 'フラッグ', fontsize=10, color=GOLD, fontweight='bold', ha='center')
ax.text(16, max(h for _,h,_,_ in ohlc[13:])+0.3, 'ブレイク ↑', fontsize=11, color=G, fontweight='bold', ha='center',
    bbox=dict(boxstyle='round,pad=0.3',fc=G,alpha=0.15))
ax.set_xlim(-1,n+1); ax.set_xticks([])
plt.title('ブルフラッグ ── 継続パターン',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '11-3.png')

# 11-4: アセンディングトライアングル
fig, ax = mk()
n=25; price=100; ohlc=[]; resistance=104
for i in range(n):
    target_low = 100 + i*0.15  # Rising support
    if i%4 < 2:
        move = np.random.uniform(0.3,0.8)
        c = min(price+move, resistance+np.random.uniform(-0.2,0.2))
    else:
        move = np.random.uniform(-0.6,-0.1)
        c = max(price+move, target_low)
    o=price; h=max(o,c)+np.random.uniform(0.05,0.2); l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c)); price=c
# Breakout
for i in range(3):
    o=price;c=price+np.random.uniform(0.5,1.0);h=c+0.2;l=o-0.1
    ohlc.append((o,h,l,c));price=c
n=len(ohlc)
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.6)
ax.axhline(y=resistance, color=R, lw=1.5, ls='--', alpha=0.6)
# Rising support line
lows = [l for _,_,l,_ in ohlc[:25]]
low_idx = [i for i in range(25) if i%4>=2]
if len(low_idx)>=2:
    z=np.polyfit(low_idx[:6],[lows[j] for j in low_idx[:6]],1)
    sx=np.array([0,24]); ax.plot(sx,z[0]*sx+z[1],color=G,lw=1.5,ls='--',alpha=0.6)
ax.text(n-2,max(h for _,h,_,_ in ohlc[-3:])+0.3,'ブレイク ↑',fontsize=11,color=G,fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.3',fc=G,alpha=0.15))
ax.text(n+1,resistance,'レジスタンス',fontsize=9,color=R,fontweight='bold',va='center')
ax.set_xlim(-1,n+5); ax.set_xticks([])
plt.title('アセンディングトライアングル',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '11-4.png')

# ===== 12: フィボナッチ =====
fig, ax = mk()
n=30; price=100; ohlc=[]
# Uptrend
for i in range(15):
    move=np.random.uniform(0.2,0.6); o=price;c=price+move
    h=max(o,c)+np.random.uniform(0.05,0.2);l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c));price=c
swing_high = price
swing_low = 100
# Retracement to 61.8%
ret_target = swing_high - (swing_high-swing_low)*0.618
for i in range(8):
    target = swing_high - (swing_high-ret_target)*(i+1)/8
    move = target - price + np.random.uniform(-0.1,0.1)
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.05,0.15);l=min(o,c)-np.random.uniform(0.05,0.15)
    ohlc.append((o,h,l,c));price=c
# Bounce
for i in range(7):
    move=np.random.uniform(0.3,0.7);o=price;c=price+move
    h=max(o,c)+np.random.uniform(0.05,0.2);l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c));price=c
n=len(ohlc)
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.55)

# Fib levels
fibs = [(0,'0% (高値)',GOLD), (0.236,'23.6%',TM), (0.382,'38.2%',BLUE),
        (0.5,'50%',TM), (0.618,'61.8%',R), (1.0,'100% (安値)',GOLD)]
for ratio, label, color in fibs:
    y = swing_high - (swing_high-swing_low)*ratio
    ax.axhline(y=y, color=color, lw=1 if ratio in [0,1] else 1.2, ls='--', alpha=0.5)
    ax.text(n+0.5, y, label, fontsize=9, color=color, fontweight='bold', va='center')

# Highlight 61.8% bounce
ret_y = swing_high - (swing_high-swing_low)*0.618
ax.annotate('61.8%で反発 ↑', xy=(22, ret_y), xytext=(24, ret_y-1),
    fontsize=11, color=GOLD, fontweight='bold',
    arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
    bbox=dict(boxstyle='round,pad=0.3', fc=GOLD, alpha=0.2))

ax.set_xlim(-1, n+8); ax.set_xticks([])
plt.title('フィボナッチリトレースメント',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '12-1.png')

# ===== 14: エリオット波動 =====
fig, ax = mk((12,6))
# Build specific wave structure
ohlc = []
price = 100
segments = [
    (5, 0.4, ''),    # Wave 0→1 up
    (3, -0.25, ''),   # Wave 1→2 down
    (8, 0.6, ''),    # Wave 2→3 up (strongest)
    (4, -0.2, ''),    # Wave 3→4 down
    (5, 0.35, ''),   # Wave 4→5 up
    (5, -0.5, ''),    # Wave A down
    (3, 0.3, ''),    # Wave B up
    (5, -0.45, ''),   # Wave C down
]
for count, trend, _ in segments:
    for j in range(count):
        move = trend + np.random.uniform(-0.1, 0.1)
        o=price;c=price+move;h=max(o,c)+np.random.uniform(0.03,0.15);l=min(o,c)-np.random.uniform(0.03,0.15)
        ohlc.append((o,h,l,c));price=c
n=len(ohlc)
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.55)

# Wave labels
wave_points = [
    (0, ohlc[0][2], '0', GOLD),
    (5, max(h for _,h,_,_ in ohlc[3:6]), '1', G),
    (8, min(l for _,_,l,_ in ohlc[6:9]), '2', R),
    (16, max(h for _,h,_,_ in ohlc[12:17]), '3', G),
    (20, min(l for _,_,l,_ in ohlc[18:21]), '4', R),
    (25, max(h for _,h,_,_ in ohlc[22:26]), '5', G),
    (30, min(l for _,_,l,_ in ohlc[27:31]), 'A', PURPLE),
    (33, max(h for _,h,_,_ in ohlc[31:34]), 'B', PURPLE),
    (38, min(l for _,_,l,_ in ohlc[35:min(39,n)]), 'C', PURPLE),
]
for x, y, label, color in wave_points:
    if x >= n: continue
    offset = 0.5 if label in ['1','3','5','B'] else -0.5
    ax.annotate(label, xy=(x, y), xytext=(x, y+offset),
        fontsize=14, color=color, fontweight='bold', ha='center',
        bbox=dict(boxstyle='circle,pad=0.3', fc=color, alpha=0.2, ec=color))

# Legend
ax.text(n+1, max(h for _,h,_,_ in ohlc)-1, '推進波（1-5）', fontsize=11, color=G, fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.3',fc=G,alpha=0.1))
ax.text(n+1, max(h for _,h,_,_ in ohlc)-2.5, '修正波（ABC）', fontsize=11, color=PURPLE, fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.3',fc=PURPLE,alpha=0.1))

ax.set_xlim(-1, n+8); ax.set_xticks([])
plt.title('エリオット波動 ── 推進5波 ＋ 修正ABC',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '14-1.png')

# ===== 16: ワイコフ蓄積 =====
fig, ax = mk((12,5.5))
ohlc=[]; price=110
# Downtrend
for i in range(6): move=np.random.uniform(-0.8,-0.2);o=price;c=price+move;h=max(o,c)+0.15;l=min(o,c)-0.15;ohlc.append((o,h,l,c));price=c
# Selling climax
for i in range(2): move=np.random.uniform(-1.5,-0.5);o=price;c=price+move;h=max(o,c)+0.2;l=min(o,c)-0.3;ohlc.append((o,h,l,c));price=c
# Range
range_low = price
for i in range(16):
    move=np.random.uniform(-0.3,0.3);o=price;c=price+move;h=max(o,c)+0.1;l=min(o,c)-0.1
    c=max(c,range_low-0.5);c=min(c,range_low+2.5)
    ohlc.append((o,h,l,c));price=c
# Spring (break below then snap back)
o=price;c=price-0.8;h=max(o,c)+0.1;l=c-0.5;ohlc.append((o,h,l,c));price=c
o=price;c=price+1.5;h=c+0.2;l=o-0.1;ohlc.append((o,h,l,c));price=c
# Markup
for i in range(10): move=np.random.uniform(0.2,0.8);o=price;c=price+move;h=max(o,c)+0.15;l=min(o,c)-0.1;ohlc.append((o,h,l,c));price=c
n=len(ohlc)
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.55)

# Range lines
ax.axhline(y=range_low-0.3,color=G,lw=1.2,ls='--',alpha=0.5)
ax.axhline(y=range_low+2.5,color=TM,lw=1,ls='--',alpha=0.3)
ax.axhspan(range_low-0.3,range_low+2.5,alpha=0.03,color=G)

# Labels
ax.text(3,111,'下落トレンド',fontsize=10,color=R,fontweight='bold')
ax.text(7,min(l for _,_,l,_ in ohlc[6:8])-0.5,'SC',fontsize=10,color=R,fontweight='bold',ha='center',
    bbox=dict(boxstyle='round,pad=0.2',fc=R,alpha=0.15))
ax.text(16,range_low+3,'蓄積レンジ',fontsize=11,color=G,fontweight='bold',ha='center',
    bbox=dict(boxstyle='round,pad=0.3',fc=G,alpha=0.1))
spring_i = 24
ax.annotate('Spring',xy=(spring_i,min(l for _,_,l,_ in ohlc[24:26])),
    xytext=(spring_i,min(l for _,_,l,_ in ohlc[24:26])-1.5),
    fontsize=12,color=GOLD,fontweight='bold',ha='center',
    arrowprops=dict(arrowstyle='->',color=GOLD,lw=2),
    bbox=dict(boxstyle='round,pad=0.3',fc=GOLD,alpha=0.2))
ax.text(32,max(h for _,h,_,_ in ohlc[26:])+0.3,'マークアップ ↑',fontsize=11,color=G,fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.3',fc=G,alpha=0.15))
ax.set_xlim(-1,n+2); ax.set_xticks([])
plt.title('ワイコフ蓄積スキーマティック',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '16-1.png')

# ===== 28: SL/TP =====
fig, ax = mk()
n=20; price=100; ohlc=[]
for i in range(n):
    if i<5: move=np.random.uniform(-0.3,0.1)
    elif i<15: move=np.random.uniform(0.2,0.6)
    else: move=np.random.uniform(0.1,0.4)
    o=price;c=price+move;h=max(o,c)+np.random.uniform(0.05,0.2);l=min(o,c)-np.random.uniform(0.05,0.2)
    ohlc.append((o,h,l,c));price=c
for i,(o,h,l,c) in enumerate(ohlc): dc(ax,i,o,h,l,c,0.6)

entry_price = ohlc[5][3]
sl_price = entry_price - 1.5
tp_price = entry_price + 3.0

ax.axhline(y=entry_price, color=BLUE, lw=1.5, ls='-', alpha=0.6)
ax.axhline(y=sl_price, color=R, lw=2, ls='--', alpha=0.7)
ax.axhline(y=tp_price, color=G, lw=2, ls='--', alpha=0.7)
ax.axhspan(sl_price, entry_price, alpha=0.05, color=R)
ax.axhspan(entry_price, tp_price, alpha=0.05, color=G)

ax.text(n+0.5, entry_price, 'エントリー', fontsize=10, color=BLUE, fontweight='bold', va='center')
ax.text(n+0.5, sl_price, 'ストップロス（SL）', fontsize=10, color=R, fontweight='bold', va='center')
ax.text(n+0.5, tp_price, 'テイクプロフィット（TP）', fontsize=10, color=G, fontweight='bold', va='center')
ax.text(n+0.5, (entry_price+tp_price)/2, 'RR 1:2', fontsize=11, color=GOLD, fontweight='bold', va='center',
    bbox=dict(boxstyle='round,pad=0.3',fc=GOLD,alpha=0.15))

ax.set_xlim(-1, n+10); ax.set_xticks([])
plt.title('SL / TP の配置',fontsize=14,color=GOLD,fontweight='bold',pad=10)
save(fig, '28-1.png')

print("\n===== ALL CHARTS GENERATED =====")
