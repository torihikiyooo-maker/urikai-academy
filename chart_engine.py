"""
SVG Chart Engine - Generates professional trading chart SVGs
All coordinates are mathematically calculated, no hand-positioned elements
"""
import random
import math

class ChartSVG:
    def __init__(self, width=520, height=280, padding=40):
        self.w = width
        self.h = height
        self.pad = padding
        self.elements = []
        self.chart_left = padding
        self.chart_right = width - padding
        self.chart_top = 35
        self.chart_bottom = height - 30
        self.chart_w = self.chart_right - self.chart_left
        self.chart_h = self.chart_bottom - self.chart_top

    def _bg(self):
        s = f'<rect x="0" y="0" width="{self.w}" height="{self.h}" rx="8" fill="#131c2b"/>'
        # Grid lines
        for i in range(5):
            y = self.chart_top + self.chart_h * i / 4
            s += f'<line x1="{self.chart_left}" y1="{y:.0f}" x2="{self.chart_right}" y2="{y:.0f}" stroke="#1e3045" stroke-width="0.5"/>'
        return s

    def _price_to_y(self, price, price_min, price_max):
        """Convert price to Y coordinate (higher price = lower Y)"""
        if price_max == price_min:
            return self.chart_top + self.chart_h / 2
        ratio = (price - price_min) / (price_max - price_min)
        return self.chart_bottom - ratio * self.chart_h

    def _x_at(self, index, total):
        """Get X coordinate for candle at index"""
        spacing = self.chart_w / (total + 1)
        return self.chart_left + spacing * (index + 1)

    def candles(self, ohlc_data, color_override=None):
        """Generate candlestick SVG from OHLC data
        ohlc_data: list of (open, high, low, close) tuples
        """
        if not ohlc_data:
            return ""

        all_prices = []
        for o, h, l, c in ohlc_data:
            all_prices.extend([o, h, l, c])
        pmin = min(all_prices)
        pmax = max(all_prices)
        # Add 5% padding
        margin = (pmax - pmin) * 0.05
        pmin -= margin
        pmax += margin

        n = len(ohlc_data)
        candle_w = max(4, min(12, self.chart_w / n * 0.6))

        parts = []
        for i, (o, h, l, c) in enumerate(ohlc_data):
            x = self._x_at(i, n)
            yo = self._price_to_y(o, pmin, pmax)
            yh = self._price_to_y(h, pmin, pmax)
            yl = self._price_to_y(l, pmin, pmax)
            yc = self._price_to_y(c, pmin, pmax)

            if color_override:
                color = color_override
            else:
                color = "#27ae60" if c >= o else "#e74c3c"

            body_top = min(yo, yc)
            body_bot = max(yo, yc)
            body_h = max(body_bot - body_top, 2)
            hw = candle_w / 2

            # Wick
            parts.append(f'<line x1="{x:.1f}" y1="{yh:.1f}" x2="{x:.1f}" y2="{body_top:.1f}" stroke="{color}" stroke-width="1.2"/>')
            # Body
            parts.append(f'<rect x="{x-hw:.1f}" y="{body_top:.1f}" width="{candle_w:.1f}" height="{body_h:.1f}" fill="{color}" rx="1"/>')
            # Lower wick
            parts.append(f'<line x1="{x:.1f}" y1="{body_bot:.1f}" x2="{x:.1f}" y2="{yl:.1f}" stroke="{color}" stroke-width="1.2"/>')

        return "\n".join(parts), pmin, pmax

    def hline(self, price, pmin, pmax, color="#e74c3c", dash="8,4", label="", label_side="right"):
        """Horizontal line at price level"""
        y = self._price_to_y(price, pmin, pmax)
        s = f'<line x1="{self.chart_left}" y1="{y:.1f}" x2="{self.chart_right}" y2="{y:.1f}" stroke="{color}" stroke-width="1.5" stroke-dasharray="{dash}" opacity="0.7"/>'
        if label:
            if label_side == "right":
                lw = len(label) * 6.5 + 12
                s += f'<rect x="{self.chart_right-lw:.0f}" y="{y-9:.1f}" width="{lw:.0f}" height="18" rx="4" fill="{color}" opacity="0.85"/>'
                s += f'<text x="{self.chart_right-lw/2:.0f}" y="{y+4:.1f}" text-anchor="middle" font-size="10" fill="#fff" font-weight="700">{label}</text>'
            else:
                lw = len(label) * 6.5 + 12
                s += f'<rect x="{self.chart_left:.0f}" y="{y-9:.1f}" width="{lw:.0f}" height="18" rx="4" fill="{color}" opacity="0.85"/>'
                s += f'<text x="{self.chart_left+lw/2:.0f}" y="{y+4:.1f}" text-anchor="middle" font-size="10" fill="#fff" font-weight="700">{label}</text>'
        return s

    def zone(self, price, pmin, pmax, height_price, color="#27ae60"):
        """Semi-transparent zone"""
        y1 = self._price_to_y(price + height_price/2, pmin, pmax)
        y2 = self._price_to_y(price - height_price/2, pmin, pmax)
        return f'<rect x="{self.chart_left}" y="{y1:.1f}" width="{self.chart_w}" height="{y2-y1:.1f}" fill="{color}" opacity="0.06" rx="2"/>'

    def trendline(self, x1_idx, p1, x2_idx, p2, total, pmin, pmax, color="#27ae60", dash=""):
        """Trendline between two price points"""
        xa = self._x_at(x1_idx, total)
        ya = self._price_to_y(p1, pmin, pmax)
        xb = self._x_at(x2_idx, total)
        yb = self._price_to_y(p2, pmin, pmax)
        dashattr = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{color}" stroke-width="2"{dashattr} opacity="0.8"/>'

    def glow_marker(self, x_idx, price, total, pmin, pmax, color="#27ae60"):
        """Glowing circle marker at a specific candle"""
        x = self._x_at(x_idx, total)
        y = self._price_to_y(price, pmin, pmax)
        return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{color}" opacity="0.15"/>'
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{color}"/>')

    def label(self, x_idx, price, total, pmin, pmax, text, color="#d4a537", offset_y=-15):
        """Text label near a point"""
        x = self._x_at(x_idx, total)
        y = self._price_to_y(price, pmin, pmax) + offset_y
        tw = len(text) * 6 + 10
        return (f'<rect x="{x-tw/2:.1f}" y="{y-10:.1f}" width="{tw}" height="16" rx="4" fill="{color}" opacity="0.85"/>'
                f'<text x="{x:.1f}" y="{y+2:.1f}" text-anchor="middle" font-size="9" fill="#0a2f5c" font-weight="700">{text}</text>')

    def title(self, text):
        return f'<text x="{self.w/2}" y="20" text-anchor="middle" font-size="13" fill="#d4a537" font-weight="700">{text}</text>'

    def bottom_note(self, text):
        y = self.h - 10
        # Japanese chars are wider - approx 9px per char
        tw = min(len(text) * 9 + 20, self.w - 20)
        return (f'<rect x="{self.w/2-tw/2:.0f}" y="{y-14:.0f}" width="{tw}" height="20" rx="4" fill="#1e3045"/>'
                f'<text x="{self.w/2}" y="{y:.0f}" text-anchor="middle" font-size="9" fill="#8b949e">{text}</text>')

    def side_panel(self, x, y, width, lines, title_text="", title_color="#d4a537"):
        """Info panel with title and text lines - auto-sizes to fit content"""
        line_h = 17
        h = len(lines) * line_h + (22 if title_text else 5) + 10
        # Auto-calculate width based on longest text (approx 6px per char)
        max_chars = max(len(t) for t, _ in lines)
        if title_text:
            max_chars = max(max_chars, len(title_text))
        auto_w = max(width, max_chars * 7 + 20)
        # Ensure panel stays within SVG bounds
        if x + auto_w > self.w - 5:
            x = self.w - auto_w - 5
        s = f'<rect x="{x}" y="{y}" width="{auto_w}" height="{h}" rx="6" fill="#1e3045"/>'
        cy = y + 16
        if title_text:
            s += f'<text x="{x+auto_w/2}" y="{cy}" text-anchor="middle" font-size="10" fill="{title_color}" font-weight="700">{title_text}</text>'
            cy += 18
        for text, color in lines:
            s += f'<text x="{x+auto_w/2}" y="{cy}" text-anchor="middle" font-size="9" fill="{color}">{text}</text>'
            cy += line_h
        return s

    def legend_panel(self, lines, title_text="", title_color="#d4a537"):
        """Legend panel positioned at bottom-right of chart, never overlapping candles"""
        width = max(len(t) for t, _ in lines) * 7 + 20
        if title_text:
            width = max(width, len(title_text) * 7 + 20)
        line_h = 16
        h = len(lines) * line_h + (20 if title_text else 5) + 8
        x = self.chart_right - width - 5
        y = self.chart_bottom - h - 5
        # Semi-transparent background
        s = f'<rect x="{x}" y="{y}" width="{width}" height="{h}" rx="5" fill="#131c2b" opacity="0.9" stroke="#1e3045" stroke-width="1"/>'
        cy = y + 14
        if title_text:
            s += f'<text x="{x+width/2}" y="{cy}" text-anchor="middle" font-size="9" fill="{title_color}" font-weight="700">{title_text}</text>'
            cy += 16
        for text, color in lines:
            s += f'<text x="{x+width/2}" y="{cy}" text-anchor="middle" font-size="8" fill="{color}">{text}</text>'
            cy += line_h
        return s

    def build(self, *parts):
        content = self._bg() + "\n" + "\n".join(parts)
        return f'<svg viewBox="0 0 {self.w} {self.h}" width="100%" style="max-width:800px">{content}</svg>'


def generate_sr_chart():
    """S/R chart with candles bouncing between support and resistance"""
    chart = ChartSVG(520, 280)

    # Generate OHLC data: price bounces between support (1.0850) and resistance (1.0950)
    support = 1.0850
    resistance = 1.0950
    mid = (support + resistance) / 2

    ohlc = []
    price = support + 0.001
    direction = 1  # 1=up, -1=down
    for i in range(28):
        move = random.uniform(0.0005, 0.0025) * direction
        o = price
        c = price + move
        h = max(o, c) + random.uniform(0.0002, 0.0010)
        l = min(o, c) - random.uniform(0.0002, 0.0010)

        # Bounce at S/R
        if c >= resistance - 0.001:
            direction = -1
            c = min(c, resistance + 0.0005)
        elif c <= support + 0.001:
            direction = 1
            c = max(c, support - 0.0005)

        h = min(h, resistance + 0.002)
        l = max(l, support - 0.002)

        ohlc.append((o, h, l, c))
        price = c

    candles_svg, pmin, pmax = chart.candles(ohlc)

    sr_svg = chart.build(
        chart.title("サポート & レジスタンス ── EUR/USD 4H"),
        chart.zone(resistance, pmin, pmax, 0.0015, "#e74c3c"),
        chart.zone(support, pmin, pmax, 0.0015, "#27ae60"),
        chart.hline(resistance, pmin, pmax, "#e74c3c", "8,4", "レジスタンス"),
        chart.hline(support, pmin, pmax, "#27ae60", "8,4", "サポート"),
        candles_svg,
        chart.bottom_note("サポートとレジスタンスの間で価格が推移する")
    )
    return sr_svg


def generate_trendline_chart():
    """Uptrend with trendline and channel"""
    chart = ChartSVG(520, 280)

    ohlc = []
    base = 1.0800
    for i in range(24):
        trend = i * 0.0008  # upward trend
        noise = random.uniform(-0.002, 0.002)
        # Create swing pattern
        swing = math.sin(i * 0.8) * 0.004

        o = base + trend + swing + noise
        move = random.uniform(-0.0015, 0.0020)
        c = o + move
        h = max(o, c) + random.uniform(0.0003, 0.0010)
        l = min(o, c) - random.uniform(0.0003, 0.0010)
        ohlc.append((o, h, l, c))

    candles_svg, pmin, pmax = chart.candles(ohlc)
    n = len(ohlc)

    # Trendline connecting swing lows (approximate)
    low_prices = [l for _, _, l, _ in ohlc]
    # Find two low points
    low1_idx, low2_idx = 2, 18
    low1_p = min(low_prices[0:6])
    low2_p = min(low_prices[14:22])

    tl = chart.trendline(low1_idx, low1_p, low2_idx, low2_p, n, pmin, pmax, "#27ae60")

    # Parallel channel upper
    offset = 0.006
    tl_upper = chart.trendline(low1_idx, low1_p + offset, low2_idx, low2_p + offset, n, pmin, pmax, "#e74c3c", "6,3")

    return chart.build(
        chart.title("上昇トレンドライン & チャネル"),
        candles_svg,
        tl,
        tl_upper,
        chart.side_panel(10, chart.chart_bottom + 5, 120, [
            ("── サポートライン", "#27ae60"),
            ("- - レジスタンス", "#e74c3c"),
        ], ""),
        chart.bottom_note("安値を結んだラインがサポート、平行線がレジスタンス")
    )


def generate_rsi_chart():
    """Price chart + RSI showing divergence"""
    chart = ChartSVG(520, 280, padding=45)
    chart.chart_bottom = 155  # Upper panel for price
    chart.chart_h = chart.chart_bottom - chart.chart_top

    # Price making higher highs
    ohlc = []
    price = 1.0900
    for i in range(22):
        if i < 8:
            move = random.uniform(0.0005, 0.0025)
        elif i < 12:
            move = random.uniform(-0.002, 0.001)
        elif i < 18:
            move = random.uniform(0.0003, 0.002)
        else:
            move = random.uniform(-0.003, -0.0005)

        o = price
        c = price + move
        h = max(o, c) + random.uniform(0.0002, 0.0008)
        l = min(o, c) - random.uniform(0.0002, 0.0008)
        ohlc.append((o, h, l, c))
        price = c

    candles_svg, pmin, pmax = chart.candles(ohlc)

    # RSI panel (manually drawn below)
    rsi_top = 170
    rsi_bottom = 260
    rsi_h = rsi_bottom - rsi_top

    rsi_parts = []
    # RSI grid
    rsi_parts.append(f'<line x1="{chart.chart_left}" y1="{rsi_top}" x2="{chart.chart_right}" y2="{rsi_top}" stroke="#556" stroke-width="0.8"/>')
    rsi_parts.append(f'<rect x="{chart.chart_left}" y="{rsi_top+3}" width="50" height="14" rx="3" fill="#1e3045"/>')
    rsi_parts.append(f'<text x="{chart.chart_left+25}" y="{rsi_top+13}" text-anchor="middle" font-size="9" fill="#8b949e">RSI (14)</text>')

    # 70/30 lines
    y70 = rsi_top + rsi_h * 0.3
    y30 = rsi_top + rsi_h * 0.7
    rsi_parts.append(f'<line x1="{chart.chart_left}" y1="{y70:.0f}" x2="{chart.chart_right}" y2="{y70:.0f}" stroke="#e74c3c" stroke-width="0.6" stroke-dasharray="3,3" opacity="0.5"/>')
    rsi_parts.append(f'<text x="{chart.chart_right+5}" y="{y70+3:.0f}" font-size="8" fill="#e74c3c">70</text>')
    rsi_parts.append(f'<line x1="{chart.chart_left}" y1="{y30:.0f}" x2="{chart.chart_right}" y2="{y30:.0f}" stroke="#27ae60" stroke-width="0.6" stroke-dasharray="3,3" opacity="0.5"/>')
    rsi_parts.append(f'<text x="{chart.chart_right+5}" y="{y30+3:.0f}" font-size="8" fill="#27ae60">30</text>')

    # RSI line - starts high, makes LOWER high (divergence with price)
    n = len(ohlc)
    rsi_points = []
    rsi_val = 55
    for i in range(n):
        x = chart._x_at(i, n)
        if i < 8:
            rsi_val = min(75, rsi_val + random.uniform(1, 4))
        elif i < 12:
            rsi_val = max(45, rsi_val - random.uniform(1, 3))
        elif i < 18:
            rsi_val = min(65, rsi_val + random.uniform(0.5, 2.5))  # Lower high!
        else:
            rsi_val = max(35, rsi_val - random.uniform(2, 5))

        y = rsi_top + rsi_h * (1 - rsi_val / 100)
        rsi_points.append(f"{x:.1f},{y:.1f}")

    rsi_parts.append(f'<polyline points="{" ".join(rsi_points)}" stroke="#8e44ad" stroke-width="2" fill="none"/>')

    # Divergence label
    rsi_parts.append(chart.side_panel(380, 190, 115, [
        ("価格: 高値更新 ↑", "#27ae60"),
        ("RSI: 高値切下げ ↓", "#e74c3c"),
        ("= ダイバージェンス", "#d4a537"),
    ], "警告シグナル", "#d4a537"))

    return chart.build(
        chart.title("RSI ── ダイバージェンスの検出"),
        f'<rect x="{chart.chart_left}" y="{chart.chart_top-5}" width="50" height="14" rx="3" fill="#1e3045"/><text x="{chart.chart_left+25}" y="{chart.chart_top+5}" text-anchor="middle" font-size="9" fill="#8b949e">価格</text>',
        candles_svg,
        "\n".join(rsi_parts),
    )


def generate_ma_cross_chart():
    """MA Golden Cross chart"""
    chart = ChartSVG(520, 280)

    ohlc = []
    price = 1.0900
    # Downtrend → bottom → uptrend
    for i in range(28):
        if i < 10:
            trend = -0.0012
        elif i < 14:
            trend = random.uniform(-0.0005, 0.0005)
        else:
            trend = 0.0015

        noise = random.uniform(-0.001, 0.001)
        o = price
        c = price + trend + noise
        h = max(o, c) + random.uniform(0.0003, 0.0010)
        l = min(o, c) - random.uniform(0.0003, 0.0010)
        ohlc.append((o, h, l, c))
        price = c

    candles_svg, pmin, pmax = chart.candles(ohlc)
    n = len(ohlc)

    # Calculate actual MAs from close prices
    closes = [c for _, _, _, c in ohlc]

    def sma(data, period):
        result = []
        for i in range(len(data)):
            if i < period - 1:
                result.append(sum(data[:i+1]) / (i+1))
            else:
                result.append(sum(data[i-period+1:i+1]) / period)
        return result

    ma_fast = sma(closes, 5)
    ma_slow = sma(closes, 12)

    # Draw MAs
    fast_points = []
    slow_points = []
    for i in range(n):
        x = chart._x_at(i, n)
        yf = chart._price_to_y(ma_fast[i], pmin, pmax)
        ys = chart._price_to_y(ma_slow[i], pmin, pmax)
        fast_points.append(f"{x:.1f},{yf:.1f}")
        slow_points.append(f"{x:.1f},{ys:.1f}")

    ma_svg = f'<polyline points="{" ".join(fast_points)}" stroke="#d4a537" stroke-width="2" fill="none" opacity="0.9"/>'
    ma_svg += f'<polyline points="{" ".join(slow_points)}" stroke="#e74c3c" stroke-width="1.8" fill="none" opacity="0.6" stroke-dasharray="5,2"/>'

    # Find cross point
    cross_idx = None
    for i in range(1, n):
        if ma_fast[i-1] <= ma_slow[i-1] and ma_fast[i] > ma_slow[i]:
            cross_idx = i
            break

    cross_svg = ""
    if cross_idx:
        cx = chart._x_at(cross_idx, n)
        cy = chart._price_to_y(ma_fast[cross_idx], pmin, pmax)
        cross_svg = f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="12" fill="none" stroke="#d4a537" stroke-width="2" stroke-dasharray="4,2"/>'
        cross_svg += f'<rect x="{cx-45:.0f}" y="{cy+15:.0f}" width="90" height="18" rx="4" fill="#d4a537" opacity="0.9"/>'
        cross_svg += f'<text x="{cx:.0f}" y="{cy+27:.0f}" text-anchor="middle" font-size="10" fill="#0a2f5c" font-weight="700">ゴールデンクロス</text>'

    return chart.build(
        chart.title("移動平均線 ── ゴールデンクロス"),
        candles_svg,
        ma_svg,
        cross_svg,
        chart.side_panel(10, chart.chart_bottom + 5, 110, [
            ("━ 短期MA (5)", "#d4a537"),
            ("╌ 長期MA (12)", "#e74c3c"),
        ], ""),
        chart.bottom_note("短期MAが長期MAを上抜け ＝ 上昇シグナル")
    )


def generate_bb_chart():
    """Bollinger Bands: squeeze → expansion → band walk"""
    chart = ChartSVG(520, 280)

    ohlc = []
    price = 1.0900
    # Tight range (squeeze) → breakout → trend (band walk)
    for i in range(28):
        if i < 12:
            # Squeeze: small moves
            move = random.uniform(-0.0006, 0.0006)
        elif i == 12:
            # Breakout candle
            move = 0.004
        else:
            # Band walk: trending up
            move = random.uniform(0.0005, 0.0025)

        o = price
        c = price + move
        h_range = 0.0004 if i < 12 else 0.001
        h = max(o, c) + random.uniform(0.0001, h_range)
        l = min(o, c) - random.uniform(0.0001, h_range)
        ohlc.append((o, h, l, c))
        price = c

    candles_svg, pmin, pmax = chart.candles(ohlc)
    n = len(ohlc)
    closes = [c for _, _, _, c in ohlc]

    # Calculate BB
    period = 8
    def bb_calc(data, p):
        mid, upper, lower = [], [], []
        for i in range(len(data)):
            window = data[max(0,i-p+1):i+1]
            m = sum(window) / len(window)
            std = (sum((x-m)**2 for x in window) / len(window)) ** 0.5
            mid.append(m)
            upper.append(m + 2 * std)
            lower.append(m - 2 * std)
        return mid, upper, lower

    bb_mid, bb_up, bb_lo = bb_calc(closes, period)

    mid_pts, up_pts, lo_pts = [], [], []
    for i in range(n):
        x = chart._x_at(i, n)
        mid_pts.append(f"{x:.1f},{chart._price_to_y(bb_mid[i], pmin, pmax):.1f}")
        up_pts.append(f"{x:.1f},{chart._price_to_y(bb_up[i], pmin, pmax):.1f}")
        lo_pts.append(f"{x:.1f},{chart._price_to_y(bb_lo[i], pmin, pmax):.1f}")

    # Band fill
    fill_pts = up_pts + list(reversed(lo_pts))

    bb_svg = f'<polygon points="{" ".join(fill_pts)}" fill="#2e86c1" opacity="0.06"/>'
    bb_svg += f'<polyline points="{" ".join(mid_pts)}" stroke="#d4a537" stroke-width="1.5" fill="none" opacity="0.8"/>'
    bb_svg += f'<polyline points="{" ".join(up_pts)}" stroke="#2e86c1" stroke-width="1.2" fill="none" opacity="0.6"/>'
    bb_svg += f'<polyline points="{" ".join(lo_pts)}" stroke="#2e86c1" stroke-width="1.2" fill="none" opacity="0.6"/>'

    # Labels
    squeeze_x = chart._x_at(5, n)
    expand_x = chart._x_at(18, n)

    labels = f'<rect x="{squeeze_x-35:.0f}" y="{chart.chart_bottom+2}" width="70" height="16" rx="4" fill="#1e3045" stroke="#d4a537" stroke-width="0.8"/>'
    labels += f'<text x="{squeeze_x:.0f}" y="{chart.chart_bottom+14}" text-anchor="middle" font-size="9" fill="#d4a537" font-weight="600">スクイーズ</text>'
    labels += f'<rect x="{expand_x-45:.0f}" y="{chart.chart_bottom+2}" width="90" height="16" rx="4" fill="#1e3045" stroke="#27ae60" stroke-width="0.8"/>'
    labels += f'<text x="{expand_x:.0f}" y="{chart.chart_bottom+14}" text-anchor="middle" font-size="9" fill="#27ae60" font-weight="600">エクスパンション</text>'

    return chart.build(
        chart.title("ボリンジャーバンド ── スクイーズ → ブレイクアウト"),
        candles_svg,
        bb_svg,
        labels,
        chart.side_panel(10, chart.chart_bottom + 5, 110, [
            ("━ ミドル(20SMA)", "#d4a537"),
            ("━ ±2σ バンド", "#2e86c1"),
        ], ""),
    )


# Generate and save all charts
if __name__ == "__main__":
    random.seed(42)  # Reproducible

    charts = {
        "sr": generate_sr_chart(),
        "trendline": generate_trendline_chart(),
        "rsi": generate_rsi_chart(),
        "ma_cross": generate_ma_cross_chart(),
        "bb": generate_bb_chart(),
    }

    for name, svg in charts.items():
        print(f"  Generated: {name} ({len(svg)} chars)")

    # Save as JSON for easy import
    import json
    with open("generated_charts.json", "w") as f:
        json.dump(charts, f)

    print(f"\n  Saved {len(charts)} charts to generated_charts.json")
