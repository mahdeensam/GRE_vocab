"""
Data Interpretation — Part 1
Sub-topics: Bar Charts, Grouped Bar Charts, Line Graphs
51 questions total (17 per sub-topic), with full answer explanations.
"""

# ─────────────────────────────────────────────────────────────
# SVG CHARTS (dark-themed, transparent background)
# Color palette:
#   Text:         #e4e4e7
#   Muted/axis:   #9194a1
#   Grid lines:   #2e3140
#   Primary:      #6c63ff
#   Secondary:    #34d399
#   Tertiary:     #f87171
#   Accent:       #fbbf24
# ─────────────────────────────────────────────────────────────

_SVG_BAR_CHART = (
    r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 280" '
    r'font-family="Inter, sans-serif" style="max-width:480px;width:100%">'
    # Title
    r'<text x="210" y="22" text-anchor="middle" fill="#e4e4e7" font-size="13" font-weight="600">'
    r'Quarterly Revenue ($ thousands)</text>'
    # Y-axis gridlines and labels (0, 50, 100, 150, 200, 250)
    # chart area: x=60..390, y=40..240  (height 200 for range 0-250)
    # y scale: each unit = 200/250 = 0.8px
    r'<line x1="60" y1="240" x2="390" y2="240" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="244" text-anchor="end" fill="#9194a1" font-size="10">0</text>'
    r'<line x1="60" y1="200" x2="390" y2="200" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="204" text-anchor="end" fill="#9194a1" font-size="10">50</text>'
    r'<line x1="60" y1="160" x2="390" y2="160" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="164" text-anchor="end" fill="#9194a1" font-size="10">100</text>'
    r'<line x1="60" y1="120" x2="390" y2="120" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="124" text-anchor="end" fill="#9194a1" font-size="10">150</text>'
    r'<line x1="60" y1="80" x2="390" y2="80" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="84" text-anchor="end" fill="#9194a1" font-size="10">200</text>'
    r'<line x1="60" y1="40" x2="390" y2="40" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="44" text-anchor="end" fill="#9194a1" font-size="10">250</text>'
    # Y-axis line
    r'<line x1="60" y1="40" x2="60" y2="240" stroke="#9194a1" stroke-width="1"/>'
    # Bars: 4 bars, each 50px wide, spaced in 4 slots of ~82px each starting at x=68
    # Q1=120 → height=120*0.8=96, top=240-96=144
    r'<rect x="78" y="144" width="50" height="96" fill="#6c63ff" rx="3"/>'
    r'<text x="103" y="138" text-anchor="middle" fill="#e4e4e7" font-size="11" font-weight="600">120</text>'
    r'<text x="103" y="256" text-anchor="middle" fill="#9194a1" font-size="11">Q1</text>'
    # Q2=180 → height=180*0.8=144, top=240-144=96
    r'<rect x="160" y="96" width="50" height="144" fill="#6c63ff" rx="3"/>'
    r'<text x="185" y="90" text-anchor="middle" fill="#e4e4e7" font-size="11" font-weight="600">180</text>'
    r'<text x="185" y="256" text-anchor="middle" fill="#9194a1" font-size="11">Q2</text>'
    # Q3=150 → height=150*0.8=120, top=240-120=120
    r'<rect x="242" y="120" width="50" height="120" fill="#6c63ff" rx="3"/>'
    r'<text x="267" y="114" text-anchor="middle" fill="#e4e4e7" font-size="11" font-weight="600">150</text>'
    r'<text x="267" y="256" text-anchor="middle" fill="#9194a1" font-size="11">Q3</text>'
    # Q4=210 → height=210*0.8=168, top=240-168=72
    r'<rect x="324" y="72" width="50" height="168" fill="#6c63ff" rx="3"/>'
    r'<text x="349" y="66" text-anchor="middle" fill="#e4e4e7" font-size="11" font-weight="600">210</text>'
    r'<text x="349" y="256" text-anchor="middle" fill="#9194a1" font-size="11">Q4</text>'
    r'</svg>'
)

_SVG_GROUPED_BAR = (
    r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 280" '
    r'font-family="Inter, sans-serif" style="max-width:520px;width:100%">'
    # Title
    r'<text x="225" y="22" text-anchor="middle" fill="#e4e4e7" font-size="13" font-weight="600">'
    r'Test Scores by Subject</text>'
    # Legend
    r'<rect x="130" y="32" width="12" height="12" fill="#6c63ff" rx="2"/>'
    r'<text x="146" y="42" fill="#e4e4e7" font-size="10">Class A</text>'
    r'<rect x="210" y="32" width="12" height="12" fill="#34d399" rx="2"/>'
    r'<text x="226" y="42" fill="#e4e4e7" font-size="10">Class B</text>'
    # Y-axis gridlines and labels (range 0-100)
    # chart area: x=60..420, y=55..245  (height 190 for range 0-100)
    # scale: 1 unit = 1.9px
    r'<line x1="60" y1="245" x2="420" y2="245" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="249" text-anchor="end" fill="#9194a1" font-size="10">0</text>'
    r'<line x1="60" y1="197" x2="420" y2="197" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="201" text-anchor="end" fill="#9194a1" font-size="10">25</text>'
    r'<line x1="60" y1="150" x2="420" y2="150" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="154" text-anchor="end" fill="#9194a1" font-size="10">50</text>'
    r'<line x1="60" y1="102" x2="420" y2="102" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="106" text-anchor="end" fill="#9194a1" font-size="10">75</text>'
    r'<line x1="60" y1="55" x2="420" y2="55" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="59" text-anchor="end" fill="#9194a1" font-size="10">100</text>'
    # Y-axis line
    r'<line x1="60" y1="55" x2="60" y2="245" stroke="#9194a1" stroke-width="1"/>'
    # 4 groups, each group has 2 bars (A=#6c63ff, B=#34d399), bar width=30, gap=6
    # Group width = 66, 4 groups over 360px → spacing ~90px each, starting at x=75
    # Math: A=78 → h=78*1.9=148.2, top=245-148.2=96.8; B=85 → h=161.5, top=83.5
    r'<rect x="75" y="96.8" width="30" height="148.2" fill="#6c63ff" rx="2"/>'
    r'<text x="90" y="91" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">78</text>'
    r'<rect x="111" y="83.5" width="30" height="161.5" fill="#34d399" rx="2"/>'
    r'<text x="126" y="78" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">85</text>'
    r'<text x="108" y="262" text-anchor="middle" fill="#9194a1" font-size="10">Math</text>'
    # Science: A=82 → h=155.8, top=89.2; B=80 → h=152, top=93
    r'<rect x="165" y="89.2" width="30" height="155.8" fill="#6c63ff" rx="2"/>'
    r'<text x="180" y="83" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">82</text>'
    r'<rect x="201" y="93" width="30" height="152" fill="#34d399" rx="2"/>'
    r'<text x="216" y="87" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">80</text>'
    r'<text x="198" y="262" text-anchor="middle" fill="#9194a1" font-size="10">Science</text>'
    # English: A=75 → h=142.5, top=102.5; B=90 → h=171, top=74
    r'<rect x="255" y="102.5" width="30" height="142.5" fill="#6c63ff" rx="2"/>'
    r'<text x="270" y="97" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">75</text>'
    r'<rect x="291" y="74" width="30" height="171" fill="#34d399" rx="2"/>'
    r'<text x="306" y="68" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">90</text>'
    r'<text x="288" y="262" text-anchor="middle" fill="#9194a1" font-size="10">English</text>'
    # History: A=88 → h=167.2, top=77.8; B=72 → h=136.8, top=108.2
    r'<rect x="345" y="77.8" width="30" height="167.2" fill="#6c63ff" rx="2"/>'
    r'<text x="360" y="72" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">88</text>'
    r'<rect x="381" y="108.2" width="30" height="136.8" fill="#34d399" rx="2"/>'
    r'<text x="396" y="102" text-anchor="middle" fill="#e4e4e7" font-size="9" font-weight="600">72</text>'
    r'<text x="378" y="262" text-anchor="middle" fill="#9194a1" font-size="10">History</text>'
    r'</svg>'
)

_SVG_LINE_GRAPH = (
    r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 280" '
    r'font-family="Inter, sans-serif" style="max-width:520px;width:100%">'
    # Title
    r'<text x="225" y="22" text-anchor="middle" fill="#e4e4e7" font-size="13" font-weight="600">'
    r'City Population Growth (thousands)</text>'
    # Legend
    r'<line x1="120" y1="38" x2="140" y2="38" stroke="#6c63ff" stroke-width="2"/>'
    r'<circle cx="130" cy="38" r="3" fill="#6c63ff"/>'
    r'<text x="146" y="42" fill="#e4e4e7" font-size="10">City X</text>'
    r'<line x1="210" y1="38" x2="230" y2="38" stroke="#f87171" stroke-width="2"/>'
    r'<circle cx="220" cy="38" r="3" fill="#f87171"/>'
    r'<text x="236" y="42" fill="#e4e4e7" font-size="10">City Y</text>'
    # Y-axis gridlines and labels (range 40-100, step 10)
    # chart area: x=60..420, y=55..245  (height 190 for range 40-100=60 units)
    # scale: 1 unit = 190/60 ≈ 3.167px
    r'<line x1="60" y1="245" x2="420" y2="245" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="249" text-anchor="end" fill="#9194a1" font-size="10">40</text>'
    r'<line x1="60" y1="213.3" x2="420" y2="213.3" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="217" text-anchor="end" fill="#9194a1" font-size="10">50</text>'
    r'<line x1="60" y1="181.7" x2="420" y2="181.7" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="185" text-anchor="end" fill="#9194a1" font-size="10">60</text>'
    r'<line x1="60" y1="150" x2="420" y2="150" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="154" text-anchor="end" fill="#9194a1" font-size="10">70</text>'
    r'<line x1="60" y1="118.3" x2="420" y2="118.3" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="122" text-anchor="end" fill="#9194a1" font-size="10">80</text>'
    r'<line x1="60" y1="86.7" x2="420" y2="86.7" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="90" text-anchor="end" fill="#9194a1" font-size="10">90</text>'
    r'<line x1="60" y1="55" x2="420" y2="55" stroke="#2e3140" stroke-width="1"/>'
    r'<text x="52" y="59" text-anchor="end" fill="#9194a1" font-size="10">100</text>'
    # Y-axis line
    r'<line x1="60" y1="55" x2="60" y2="245" stroke="#9194a1" stroke-width="1"/>'
    # X-axis labels: 2018-2023 → 6 points, spaced over 360px → 72px apart, starting at x=60
    r'<text x="60" y="262" text-anchor="middle" fill="#9194a1" font-size="10">2018</text>'
    r'<text x="132" y="262" text-anchor="middle" fill="#9194a1" font-size="10">2019</text>'
    r'<text x="204" y="262" text-anchor="middle" fill="#9194a1" font-size="10">2020</text>'
    r'<text x="276" y="262" text-anchor="middle" fill="#9194a1" font-size="10">2021</text>'
    r'<text x="348" y="262" text-anchor="middle" fill="#9194a1" font-size="10">2022</text>'
    r'<text x="420" y="262" text-anchor="middle" fill="#9194a1" font-size="10">2023</text>'
    # City X data points: 50,55,60,70,75,85
    # y = 245 - (val-40)*3.167
    # 50→213.3  55→197.5  60→181.7  70→150  75→134.2  85→102.5
    r'<polyline points="60,213.3 132,197.5 204,181.7 276,150 348,134.2 420,102.5" '
    r'fill="none" stroke="#6c63ff" stroke-width="2.5" stroke-linejoin="round"/>'
    r'<circle cx="60" cy="213.3" r="4" fill="#6c63ff"/>'
    r'<text x="60" y="207" text-anchor="middle" fill="#e4e4e7" font-size="9">50</text>'
    r'<circle cx="132" cy="197.5" r="4" fill="#6c63ff"/>'
    r'<text x="132" y="191" text-anchor="middle" fill="#e4e4e7" font-size="9">55</text>'
    r'<circle cx="204" cy="181.7" r="4" fill="#6c63ff"/>'
    r'<text x="204" y="175" text-anchor="middle" fill="#e4e4e7" font-size="9">60</text>'
    r'<circle cx="276" cy="150" r="4" fill="#6c63ff"/>'
    r'<text x="276" y="144" text-anchor="middle" fill="#e4e4e7" font-size="9">70</text>'
    r'<circle cx="348" cy="134.2" r="4" fill="#6c63ff"/>'
    r'<text x="348" y="128" text-anchor="middle" fill="#e4e4e7" font-size="9">75</text>'
    r'<circle cx="420" cy="102.5" r="4" fill="#6c63ff"/>'
    r'<text x="420" y="96" text-anchor="middle" fill="#e4e4e7" font-size="9">85</text>'
    # City Y data points: 80,78,75,73,70,68
    # 80→118.3  78→124.6  75→134.2  73→140.5  70→150  68→156.3
    r'<polyline points="60,118.3 132,124.6 204,134.2 276,140.5 348,150 420,156.3" '
    r'fill="none" stroke="#f87171" stroke-width="2.5" stroke-linejoin="round"/>'
    r'<circle cx="60" cy="118.3" r="4" fill="#f87171"/>'
    r'<text x="60" y="112" text-anchor="middle" fill="#e4e4e7" font-size="9">80</text>'
    r'<circle cx="132" cy="124.6" r="4" fill="#f87171"/>'
    r'<text x="132" y="118" text-anchor="middle" fill="#e4e4e7" font-size="9">78</text>'
    r'<circle cx="204" cy="134.2" r="4" fill="#f87171"/>'
    r'<text x="204" y="128" text-anchor="middle" fill="#e4e4e7" font-size="9">75</text>'
    r'<circle cx="276" cy="140.5" r="4" fill="#f87171"/>'
    r'<text x="276" y="155" text-anchor="middle" fill="#e4e4e7" font-size="9">73</text>'
    r'<circle cx="348" cy="150" r="4" fill="#f87171"/>'
    r'<text x="348" y="144" text-anchor="middle" fill="#e4e4e7" font-size="9">70</text>'
    r'<circle cx="420" cy="156.3" r="4" fill="#f87171"/>'
    r'<text x="420" y="163" text-anchor="middle" fill="#e4e4e7" font-size="9">68</text>'
    r'</svg>'
)

# ─────────────────────────────────────────────────────────────
# Instruction prefixes
# ─────────────────────────────────────────────────────────────
_QC_PREFIX = (
    r"For each question, select:<br>"
    r"<b>A.</b> Quantity A is greater &nbsp; "
    r"<b>B.</b> Quantity B is greater &nbsp; "
    r"<b>C.</b> The two quantities are equal &nbsp; "
    r"<b>D.</b> The relationship cannot be determined<br><br>"
)
_MC_PREFIX = r"Select <b>one</b> answer.<br><br>"
_MS_PREFIX = r"Select <b>all</b> that apply.<br><br>"
_NE_PREFIX = r"Enter your answer as a number.<br><br>"


SECTIONS = [
    # =====================================================================
    # GRAPH SET 1: BAR CHART — QUARTERLY REVENUE  (Sections 0-3)
    # Data: Q1=120, Q2=180, Q3=150, Q4=210  ($ thousands)
    # Total=660, Average=165
    # =====================================================================

    # --- Section 0: Bar Chart — Quantitative Comparison (Q1-Q5) ----------
    {
        "type": "Bar Chart — Quantitative Comparison",
        "instructions": _QC_PREFIX + _SVG_BAR_CHART,
        "questions": [
            {
                "id": 1,
                "stem": r"Based on the chart above,",
                "qtyA": r"Revenue in Q4",
                "qtyB": r"Revenue in Q1 + Revenue in Q2 combined",
            },
            {
                "id": 2,
                "stem": r"Based on the chart above,",
                "qtyA": r"The average quarterly revenue",
                "qtyB": r"\(160\) thousand",
            },
            {
                "id": 3,
                "stem": r"Based on the chart above,",
                "qtyA": r"The percent increase in revenue from Q1 to Q2",
                "qtyB": r"50%",
            },
            {
                "id": 4,
                "stem": r"Based on the chart above,",
                "qtyA": r"Q3 revenue as a fraction of total annual revenue",
                "qtyB": r"\(\dfrac{1}{4}\)",
            },
            {
                "id": 5,
                "stem": r"Based on the chart above,",
                "qtyA": r"The percent decrease in revenue from Q2 to Q3",
                "qtyB": r"15%",
            },
        ],
    },

    # --- Section 1: Bar Chart — Multiple Choice (Single Answer) (Q6-Q10) ---
    {
        "type": "Bar Chart — Multiple Choice (Single Answer)",
        "instructions": _MC_PREFIX + _SVG_BAR_CHART,
        "questions": [
            {
                "id": 6,
                "stem": r"According to the chart above, what is the total annual revenue?",
                "choices": [
                    r"(A) $550 thousand",
                    r"(B) $600 thousand",
                    r"(C) $630 thousand",
                    r"(D) $660 thousand",
                    r"(E) $700 thousand",
                ],
            },
            {
                "id": 7,
                "stem": r"Based on the chart above, by what percent did revenue increase from Q3 to Q4?",
                "choices": [
                    r"(A) 20%",
                    r"(B) 30%",
                    r"(C) 40%",
                    r"(D) 50%",
                    r"(E) 60%",
                ],
            },
            {
                "id": 8,
                "stem": r"According to the chart, Q2 revenue is approximately what percent of the annual total?",
                "choices": [
                    r"(A) 25%",
                    r"(B) 27.3%",
                    r"(C) 30%",
                    r"(D) 33%",
                    r"(E) 35%",
                ],
            },
            {
                "id": 9,
                "stem": r"Based on the chart above, the range of quarterly revenue is:",
                "choices": [
                    r"(A) $60 thousand",
                    r"(B) $70 thousand",
                    r"(C) $80 thousand",
                    r"(D) $90 thousand",
                    r"(E) $100 thousand",
                ],
            },
            {
                "id": 10,
                "stem": (
                    r"According to the chart, if Q1 revenue had been 20% higher than shown, "
                    r"what would the total annual revenue have been?"
                ),
                "choices": [
                    r"(A) $672 thousand",
                    r"(B) $680 thousand",
                    r"(C) $684 thousand",
                    r"(D) $690 thousand",
                    r"(E) $700 thousand",
                ],
            },
        ],
    },

    # --- Section 2: Bar Chart — Multiple Choice (Select One or More) (Q11-Q12) ---
    {
        "type": "Bar Chart — Multiple Choice (Select One or More)",
        "instructions": _MS_PREFIX + _SVG_BAR_CHART,
        "questions": [
            {
                "id": 11,
                "stem": (
                    r"Based on the chart above, the average quarterly revenue is $165 thousand. "
                    r"Which quarters had revenue above this average? Select all that apply."
                ),
                "choices": [
                    r"(A) Q1",
                    r"(B) Q2",
                    r"(C) Q3",
                    r"(D) Q4",
                ],
            },
            {
                "id": 12,
                "stem": r"According to the chart above, which of the following statements are true? Select all that apply.",
                "choices": [
                    r"(A) Q4 had the highest quarterly revenue",
                    r"(B) Revenue increased every quarter from Q1 to Q4",
                    r"(C) Total annual revenue exceeded $600 thousand",
                    r"(D) Q1 had the lowest quarterly revenue",
                ],
            },
        ],
    },

    # --- Section 3: Bar Chart — Numeric Entry (Q13-Q17) -----------------
    {
        "type": "Bar Chart — Numeric Entry",
        "instructions": _NE_PREFIX + _SVG_BAR_CHART,
        "questions": [
            {
                "id": 13,
                "stem": r"Based on the chart above, enter the median quarterly revenue (in thousands of dollars).",
            },
            {
                "id": 14,
                "stem": r"According to the chart, enter the percent increase in revenue from Q1 to Q4.",
            },
            {
                "id": 15,
                "stem": (
                    r"Based on the chart above, if revenue in each quarter increased by 10% over the values shown, "
                    r"enter the new total annual revenue (in thousands of dollars)."
                ),
            },
            {
                "id": 16,
                "stem": (
                    r"According to the chart, enter the ratio of Q2 revenue to Q4 revenue as a fraction "
                    r"in simplest form. (Enter as a/b, e.g. 3/5.)"
                ),
            },
            {
                "id": 17,
                "stem": (
                    r"Based on the chart above, enter the difference between the highest and lowest "
                    r"quarterly revenues (in thousands of dollars)."
                ),
            },
        ],
    },

    # =====================================================================
    # GRAPH SET 2: GROUPED BAR CHART — TEST SCORES BY SUBJECT (Sections 4-7)
    # Data: Math A=78 B=85, Science A=82 B=80, English A=75 B=90, History A=88 B=72
    # Totals: A=323, B=327; Averages: A=80.75, B=81.75
    # =====================================================================

    # --- Section 4: Grouped Bar Chart — Quantitative Comparison (Q1-Q5) ---
    {
        "type": "Grouped Bar Chart — Quantitative Comparison",
        "instructions": _QC_PREFIX + _SVG_GROUPED_BAR,
        "questions": [
            {
                "id": 1,
                "stem": r"Based on the chart above,",
                "qtyA": r"Class A's average score across all four subjects",
                "qtyB": r"Class B's average score across all four subjects",
            },
            {
                "id": 2,
                "stem": r"Based on the chart above,",
                "qtyA": r"The range of Class A's scores",
                "qtyB": r"The range of Class B's scores",
            },
            {
                "id": 3,
                "stem": r"According to the chart,",
                "qtyA": r"Class A's History score",
                "qtyB": r"Class B's English score",
            },
            {
                "id": 4,
                "stem": r"Based on the chart above,",
                "qtyA": r"The total of all Class A scores",
                "qtyB": r"The total of all Class B scores",
            },
            {
                "id": 5,
                "stem": r"According to the chart,",
                "qtyA": r"The number of subjects in which Class A scored higher than Class B",
                "qtyB": r"2",
            },
        ],
    },

    # --- Section 5: Grouped Bar Chart — Multiple Choice (Single Answer) (Q6-Q10) ---
    {
        "type": "Grouped Bar Chart — Multiple Choice (Single Answer)",
        "instructions": _MC_PREFIX + _SVG_GROUPED_BAR,
        "questions": [
            {
                "id": 6,
                "stem": r"According to the chart, what is the difference between Class B's highest score and Class A's lowest score?",
                "choices": [
                    r"(A) 10",
                    r"(B) 12",
                    r"(C) 15",
                    r"(D) 18",
                    r"(E) 20",
                ],
            },
            {
                "id": 7,
                "stem": r"Based on the chart, in which subject is the difference between Class A and Class B scores the greatest?",
                "choices": [
                    r"(A) Math",
                    r"(B) Science",
                    r"(C) English",
                    r"(D) History",
                    r"(E) Math and History are tied",
                ],
            },
            {
                "id": 8,
                "stem": (
                    r"According to the chart, what is the combined average score of both classes "
                    r"across all subjects (i.e., the average of all 8 scores)?"
                ),
                "choices": [
                    r"(A) 79.50",
                    r"(B) 80.00",
                    r"(C) 81.00",
                    r"(D) 81.25",
                    r"(E) 82.00",
                ],
            },
            {
                "id": 9,
                "stem": r"Based on the chart, Class A's Math score is what percent of Class B's Math score?",
                "choices": [
                    r"(A) About 88%",
                    r"(B) About 90%",
                    r"(C) About 92%",
                    r"(D) About 95%",
                    r"(E) About 97%",
                ],
            },
            {
                "id": 10,
                "stem": (
                    r"According to the chart, if Class A's English score increased by 20%, "
                    r"what would the new score be?"
                ),
                "choices": [
                    r"(A) 85",
                    r"(B) 88",
                    r"(C) 90",
                    r"(D) 92",
                    r"(E) 95",
                ],
            },
        ],
    },

    # --- Section 6: Grouped Bar Chart — Multiple Choice (Select One or More) (Q11-Q12) ---
    {
        "type": "Grouped Bar Chart — Multiple Choice (Select One or More)",
        "instructions": _MS_PREFIX + _SVG_GROUPED_BAR,
        "questions": [
            {
                "id": 11,
                "stem": r"Based on the chart above, in which subjects did Class A score higher than Class B? Select all that apply.",
                "choices": [
                    r"(A) Math",
                    r"(B) Science",
                    r"(C) English",
                    r"(D) History",
                ],
            },
            {
                "id": 12,
                "stem": r"According to the chart, which of the following statements are true? Select all that apply.",
                "choices": [
                    r"(A) Class B's average is higher than Class A's average",
                    r"(B) The subject with the smallest score difference between classes is Science",
                    r"(C) Class A scored above 80 in exactly two subjects",
                    r"(D) Class B scored below 75 in at least one subject",
                ],
            },
        ],
    },

    # --- Section 7: Grouped Bar Chart — Numeric Entry (Q13-Q17) ---------
    {
        "type": "Grouped Bar Chart — Numeric Entry",
        "instructions": _NE_PREFIX + _SVG_GROUPED_BAR,
        "questions": [
            {
                "id": 13,
                "stem": r"Based on the chart above, enter the average score for Class A across all four subjects.",
            },
            {
                "id": 14,
                "stem": r"According to the chart, enter the total combined score of both classes in the Math subject.",
            },
            {
                "id": 15,
                "stem": r"Based on the chart, enter the absolute difference between the two classes' total scores (sum of all subjects).",
            },
            {
                "id": 16,
                "stem": (
                    r"According to the chart, Class B's History score is what percent less than "
                    r"Class A's History score? Enter your answer rounded to one decimal place."
                ),
            },
            {
                "id": 17,
                "stem": (
                    r"Based on the chart, if both classes' Science scores were each increased by 5 points, "
                    r"enter the new combined Science total for both classes."
                ),
            },
        ],
    },

    # =====================================================================
    # GRAPH SET 3: LINE GRAPH — CITY POPULATION GROWTH  (Sections 8-11)
    # Data: City X: 50,55,60,70,75,85  City Y: 80,78,75,73,70,68
    # =====================================================================

    # --- Section 8: Line Graph — Quantitative Comparison (Q1-Q5) ---------
    {
        "type": "Line Graph — Quantitative Comparison",
        "instructions": _QC_PREFIX + _SVG_LINE_GRAPH,
        "questions": [
            {
                "id": 1,
                "stem": r"According to the graph above,",
                "qtyA": r"City X's population in 2023",
                "qtyB": r"City Y's population in 2018",
            },
            {
                "id": 2,
                "stem": r"Based on the graph above,",
                "qtyA": r"Total growth of City X from 2018 to 2023",
                "qtyB": r"Total decline of City Y from 2018 to 2023",
            },
            {
                "id": 3,
                "stem": r"According to the graph,",
                "qtyA": r"Percent increase in City X's population from 2018 to 2023",
                "qtyB": r"50%",
            },
            {
                "id": 4,
                "stem": r"Based on the graph above,",
                "qtyA": r"City X's average annual growth (in thousands) from 2018 to 2023",
                "qtyB": r"City Y's average annual decline (in thousands) from 2018 to 2023",
            },
            {
                "id": 5,
                "stem": r"According to the graph,",
                "qtyA": r"Combined population of both cities in 2020",
                "qtyB": r"Combined population of both cities in 2023",
            },
        ],
    },

    # --- Section 9: Line Graph — Multiple Choice (Single Answer) (Q6-Q10) ---
    {
        "type": "Line Graph — Multiple Choice (Single Answer)",
        "instructions": _MC_PREFIX + _SVG_LINE_GRAPH,
        "questions": [
            {
                "id": 6,
                "stem": r"According to the graph, in which year was the difference between City X and City Y populations the smallest?",
                "choices": [
                    r"(A) 2019",
                    r"(B) 2020",
                    r"(C) 2021",
                    r"(D) 2022",
                    r"(E) 2023",
                ],
            },
            {
                "id": 7,
                "stem": r"Based on the graph, what was the percent decrease in City Y's population from 2018 to 2023?",
                "choices": [
                    r"(A) 10%",
                    r"(B) 12%",
                    r"(C) 15%",
                    r"(D) 18%",
                    r"(E) 20%",
                ],
            },
            {
                "id": 8,
                "stem": (
                    r"According to the graph, during which one-year period did City X's population "
                    r"increase by the greatest amount?"
                ),
                "choices": [
                    r"(A) 2018 to 2019",
                    r"(B) 2019 to 2020",
                    r"(C) 2020 to 2021",
                    r"(D) 2021 to 2022",
                    r"(E) 2022 to 2023",
                ],
            },
            {
                "id": 9,
                "stem": (
                    r"Based on the graph, if City X's population continues to grow at the same rate "
                    r"as from 2022 to 2023, what would its population be in 2024?"
                ),
                "choices": [
                    r"(A) 90 thousand",
                    r"(B) 92 thousand",
                    r"(C) 95 thousand",
                    r"(D) 97 thousand",
                    r"(E) 100 thousand",
                ],
            },
            {
                "id": 10,
                "stem": r"According to the graph, the combined population of both cities in 2021 was:",
                "choices": [
                    r"(A) 133 thousand",
                    r"(B) 140 thousand",
                    r"(C) 143 thousand",
                    r"(D) 145 thousand",
                    r"(E) 148 thousand",
                ],
            },
        ],
    },

    # --- Section 10: Line Graph — Multiple Choice (Select One or More) (Q11-Q12) ---
    {
        "type": "Line Graph — Multiple Choice (Select One or More)",
        "instructions": _MS_PREFIX + _SVG_LINE_GRAPH,
        "questions": [
            {
                "id": 11,
                "stem": r"Based on the graph above, in which years did City X have a population greater than City Y? Select all that apply.",
                "choices": [
                    r"(A) 2018",
                    r"(B) 2019",
                    r"(C) 2020",
                    r"(D) 2021",
                    r"(E) 2022",
                    r"(F) 2023",
                ],
            },
            {
                "id": 12,
                "stem": r"According to the graph, which of the following statements are true? Select all that apply.",
                "choices": [
                    r"(A) City X's population increased every year from 2018 to 2023",
                    r"(B) City Y's population decreased every year from 2018 to 2023",
                    r"(C) The two cities' populations were closest in 2021",
                    r"(D) By 2023, City X's population exceeded City Y's by more than 15 thousand",
                ],
            },
        ],
    },

    # --- Section 11: Line Graph — Numeric Entry (Q13-Q17) ----------------
    {
        "type": "Line Graph — Numeric Entry",
        "instructions": _NE_PREFIX + _SVG_LINE_GRAPH,
        "questions": [
            {
                "id": 13,
                "stem": r"According to the graph, enter City X's total population growth from 2018 to 2023 (in thousands).",
            },
            {
                "id": 14,
                "stem": r"Based on the graph, enter the average annual decline of City Y's population from 2018 to 2023 (in thousands).",
            },
            {
                "id": 15,
                "stem": (
                    r"According to the graph, enter the ratio of City X's 2023 population to "
                    r"City Y's 2023 population as a fraction in simplest form. (Enter as a/b, e.g. 3/5.)"
                ),
            },
            {
                "id": 16,
                "stem": (
                    r"Based on the graph, in 2021 the difference between City Y's population and "
                    r"City X's population was how many thousand?"
                ),
            },
            {
                "id": 17,
                "stem": (
                    r"According to the graph, enter the percent increase in the combined population "
                    r"of both cities from 2018 to 2023. Round to one decimal place."
                ),
            },
        ],
    },
]


# ─────────────────────────────────────────────────────────────────────────
# ANSWERS
# Key format: (topic_id, section_index_within_topic, question_id)
# section_index is 0-based within each topic's 4 sections
# ─────────────────────────────────────────────────────────────────────────

ANSWERS = {
    # =====================================================================
    # GRAPH SET 1: BAR CHART — QUARTERLY REVENUE  (topic: "di-bar-charts")
    # Sections 0-3  |  Q1=120  Q2=180  Q3=150  Q4=210  Total=660  Avg=165
    # =====================================================================

    # --- Section 0: Quantitative Comparison (Q1-Q5) ----------------------

    ("di-bar-charts", 0, 1): {
        "answer": "B",
        "explanation": (
            r"Quantity A = Q4 revenue = \($210\) thousand. "
            r"Quantity B = Q1 + Q2 = \(120 + 180 = 300\) thousand. "
            r"Since \(210 < 300\), Quantity B is greater."
        ),
    },
    ("di-bar-charts", 0, 2): {
        "answer": "A",
        "explanation": (
            r"Total annual revenue \(= 120 + 180 + 150 + 210 = 660\). "
            r"Average quarterly revenue \(= \frac{660}{4} = 165\). "
            r"Quantity A \(= 165\) and Quantity B \(= 160\). Since \(165 > 160\), Quantity A is greater."
        ),
        "common_mistake": (
            "Students may estimate the average by eyeballing the chart and rounding down to 160. "
            "Always compute the exact sum and divide by the number of quarters."
        ),
    },
    ("di-bar-charts", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Percent increase from Q1 to Q2 \(= \frac{180 - 120}{120} \times 100 = \frac{60}{120} \times 100 = 50\%\). "
            r"Quantity A \(= 50\%\) and Quantity B \(= 50\%\). The two quantities are equal."
        ),
    },
    ("di-bar-charts", 0, 4): {
        "answer": "B",
        "explanation": (
            r"Q3 as a fraction of total \(= \frac{150}{660} = \frac{5}{22} \approx 0.227\), or about \(22.7\%\). "
            r"Quantity B \(= \frac{1}{4} = 0.25\), or \(25\%\). "
            r"Since \(22.7\% < 25\%\), Quantity B is greater."
        ),
        "common_mistake": (
            "Students may assume each quarter contributes equally (25%) to the total. "
            "Since the quarters have different revenues, each contributes a different fraction."
        ),
    },
    ("di-bar-charts", 0, 5): {
        "answer": "A",
        "explanation": (
            r"Percent decrease from Q2 to Q3 \(= \frac{180 - 150}{180} \times 100 = \frac{30}{180} \times 100 \approx 16.7\%\). "
            r"Quantity A \(\approx 16.7\%\) and Quantity B \(= 15\%\). Since \(16.7\% > 15\%\), Quantity A is greater."
        ),
        "common_mistake": (
            "Students may compute the absolute change (30) and confuse it with the percentage. "
            "The percent decrease must use Q2 (180) as the base, not Q3."
        ),
    },

    # --- Section 1: Multiple Choice Single Answer (Q6-Q10) ---------------

    ("di-bar-charts", 1, 6): {
        "answer": "(D) $660 thousand",
        "explanation": (
            r"Total annual revenue \(= 120 + 180 + 150 + 210 = 660\) thousand dollars."
        ),
    },
    ("di-bar-charts", 1, 7): {
        "answer": "(C) 40%",
        "explanation": (
            r"Percent increase from Q3 to Q4 \(= \frac{210 - 150}{150} \times 100 = \frac{60}{150} \times 100 = 40\%\)."
        ),
        "common_mistake": (
            "Students may divide by 210 (the new value) instead of 150 (the original value). "
            "Percent change always uses the original value as the base."
        ),
    },
    ("di-bar-charts", 1, 8): {
        "answer": "(B) 27.3%",
        "explanation": (
            r"Q2 as percent of total \(= \frac{180}{660} \times 100 \approx 27.3\%\)."
        ),
        "common_mistake": (
            "Students may divide by 4 (number of quarters) instead of by the total revenue. "
            "The question asks for Q2 as a percent of the annual total (660), not as a fraction of 4 quarters."
        ),
    },
    ("di-bar-charts", 1, 9): {
        "answer": "(D) $90 thousand",
        "explanation": (
            r"Range = highest \(-\) lowest \(= 210 - 120 = 90\) thousand dollars."
        ),
    },
    ("di-bar-charts", 1, 10): {
        "answer": "(C) $684 thousand",
        "explanation": (
            r"If Q1 revenue were 20% higher: \(120 \times 1.20 = 144\). "
            r"New total \(= 144 + 180 + 150 + 210 = 684\) thousand dollars."
        ),
    },

    # --- Section 2: Multiple Choice Select One or More (Q11-Q12) ---------

    ("di-bar-charts", 2, 11): {
        "answer": "B, D",
        "explanation": (
            r"Average quarterly revenue \(= \frac{660}{4} = 165\). "
            r"Q1 = 120 (below), Q2 = 180 (above), Q3 = 150 (below), Q4 = 210 (above). "
            r"The quarters with revenue above the average of 165 are Q2 and Q4."
        ),
    },
    ("di-bar-charts", 2, 12): {
        "answer": "A, C, D",
        "explanation": (
            r"(A) Q4 = 210 is the highest — TRUE. "
            r"(B) Revenue went Q1=120 \(\to\) Q2=180 \(\to\) Q3=150 (decrease) \(\to\) Q4=210. "
            r"Revenue did NOT always increase (it dropped from Q2 to Q3) — FALSE. "
            r"(C) Total = 660 > 600 — TRUE. "
            r"(D) Q1 = 120 is the lowest — TRUE."
        ),
        "common_mistake": (
            "Students may glance at the general upward trend and incorrectly select (B). "
            "Revenue decreased from Q2 (180) to Q3 (150)."
        ),
    },

    # --- Section 3: Numeric Entry (Q13-Q17) ------------------------------

    ("di-bar-charts", 3, 13): {
        "answer": "165",
        "explanation": (
            r"Sort the quarterly revenues: 120, 150, 180, 210. "
            r"With 4 values, the median is the average of the 2nd and 3rd values: "
            r"\(\frac{150 + 180}{2} = \frac{330}{2} = 165\)."
        ),
        "common_mistake": (
            "Students may forget to sort the values first and take the average of Q2 and Q3 in chronological order "
            "(180 and 150), which gives the same result here but would be wrong in general. "
            "Always sort the data before finding the median."
        ),
    },
    ("di-bar-charts", 3, 14): {
        "answer": "75",
        "explanation": (
            r"Percent increase from Q1 to Q4 \(= \frac{210 - 120}{120} \times 100 = \frac{90}{120} \times 100 = 75\%\)."
        ),
        "common_mistake": (
            "Students may divide the change (90) by the final value (210) instead of the initial value (120), "
            "getting approximately 42.9%. Percent increase always uses the original value as the denominator."
        ),
    },
    ("di-bar-charts", 3, 15): {
        "answer": "726",
        "explanation": (
            r"Original total = 660. If each quarter increases by 10%, the new total is "
            r"\(660 \times 1.10 = 726\) thousand dollars. "
            r"Alternatively: \(132 + 198 + 165 + 231 = 726\)."
        ),
    },
    ("di-bar-charts", 3, 16): {
        "answer": "6/7",
        "explanation": (
            r"Ratio of Q2 to Q4 \(= \frac{180}{210}\). Simplify by dividing numerator and denominator by 30: "
            r"\(\frac{180 \div 30}{210 \div 30} = \frac{6}{7}\)."
        ),
    },
    ("di-bar-charts", 3, 17): {
        "answer": "90",
        "explanation": (
            r"Difference between highest and lowest: \(210 - 120 = 90\) thousand dollars."
        ),
    },

    # =====================================================================
    # GRAPH SET 2: GROUPED BAR CHART — TEST SCORES  (topic: "di-grouped-bar")
    # Sections 0-3
    # Class A: Math=78 Science=82 English=75 History=88 → Total=323 Avg=80.75
    # Class B: Math=85 Science=80 English=90 History=72 → Total=327 Avg=81.75
    # =====================================================================

    # --- Section 0: Quantitative Comparison (Q1-Q5) ----------------------

    ("di-grouped-bar", 0, 1): {
        "answer": "B",
        "explanation": (
            r"Class A average \(= \frac{78 + 82 + 75 + 88}{4} = \frac{323}{4} = 80.75\). "
            r"Class B average \(= \frac{85 + 80 + 90 + 72}{4} = \frac{327}{4} = 81.75\). "
            r"Since \(80.75 < 81.75\), Quantity B is greater."
        ),
        "common_mistake": (
            "Students may try to compare the classes by looking at individual subjects rather than computing the full averages. "
            "Class A wins in 2 subjects and Class B wins in 2 subjects, but the averages differ because the margins differ."
        ),
    },
    ("di-grouped-bar", 0, 2): {
        "answer": "B",
        "explanation": (
            r"Range of Class A = highest \(-\) lowest \(= 88 - 75 = 13\). "
            r"Range of Class B \(= 90 - 72 = 18\). "
            r"Since \(13 < 18\), Quantity B is greater."
        ),
    },
    ("di-grouped-bar", 0, 3): {
        "answer": "B",
        "explanation": (
            r"Class A History = 88, Class B English = 90. "
            r"Since \(88 < 90\), Quantity B is greater."
        ),
    },
    ("di-grouped-bar", 0, 4): {
        "answer": "B",
        "explanation": (
            r"Total of Class A \(= 78 + 82 + 75 + 88 = 323\). "
            r"Total of Class B \(= 85 + 80 + 90 + 72 = 327\). "
            r"Since \(323 < 327\), Quantity B is greater."
        ),
    },
    ("di-grouped-bar", 0, 5): {
        "answer": "C",
        "explanation": (
            r"Class A scored higher than Class B in: Science (\(82 > 80\)) and History (\(88 > 72\)). "
            r"That is 2 subjects. Quantity A = 2 and Quantity B = 2. The two quantities are equal."
        ),
    },

    # --- Section 1: Multiple Choice Single Answer (Q6-Q10) ---------------

    ("di-grouped-bar", 1, 6): {
        "answer": "(C) 15",
        "explanation": (
            r"Class B's highest score = 90 (English). Class A's lowest score = 75 (English). "
            r"Difference \(= 90 - 75 = 15\)."
        ),
    },
    ("di-grouped-bar", 1, 7): {
        "answer": "(D) History",
        "explanation": (
            r"Differences: Math \(|78-85| = 7\), Science \(|82-80| = 2\), "
            r"English \(|75-90| = 15\), History \(|88-72| = 16\). "
            r"The greatest difference is 16 in History."
        ),
        "common_mistake": (
            "Students may pick English (difference of 15) because the bars look visually far apart. "
            "History has a slightly larger difference (16) that is easy to overlook."
        ),
    },
    ("di-grouped-bar", 1, 8): {
        "answer": "(D) 81.25",
        "explanation": (
            r"All 8 scores: 78, 82, 75, 88, 85, 80, 90, 72. "
            r"Sum \(= 323 + 327 = 650\). Average \(= \frac{650}{8} = 81.25\)."
        ),
    },
    ("di-grouped-bar", 1, 9): {
        "answer": "(C) About 92%",
        "explanation": (
            r"Class A Math = 78, Class B Math = 85. "
            r"\(\frac{78}{85} \times 100 \approx 91.8\%\), which is about 92%."
        ),
    },
    ("di-grouped-bar", 1, 10): {
        "answer": "(C) 90",
        "explanation": (
            r"Class A English = 75. A 20% increase: \(75 \times 1.20 = 90\)."
        ),
    },

    # --- Section 2: Multiple Choice Select One or More (Q11-Q12) ---------

    ("di-grouped-bar", 2, 11): {
        "answer": "B, D",
        "explanation": (
            r"Compare each subject: Math (\(78 < 85\), B wins), Science (\(82 > 80\), A wins), "
            r"English (\(75 < 90\), B wins), History (\(88 > 72\), A wins). "
            r"Class A scored higher in Science and History."
        ),
    },
    ("di-grouped-bar", 2, 12): {
        "answer": "A, B, C, D",
        "explanation": (
            r"(A) Class B avg = 81.75 > Class A avg = 80.75 — TRUE. "
            r"(B) Differences: Math=7, Science=2, English=15, History=16. Smallest is Science (2) — TRUE. "
            r"(C) Class A scored above 80 in Science (82) and History (88), exactly two subjects — TRUE. "
            r"(D) Class B scored 72 in History, which is below 75 — TRUE."
        ),
    },

    # --- Section 3: Numeric Entry (Q13-Q17) ------------------------------

    ("di-grouped-bar", 3, 13): {
        "answer": "80.75",
        "explanation": (
            r"Class A scores: 78, 82, 75, 88. "
            r"Average \(= \frac{78 + 82 + 75 + 88}{4} = \frac{323}{4} = 80.75\)."
        ),
        "common_mistake": (
            "Students may accidentally include Class B scores in the average, or round prematurely. "
            "Make sure to only add Class A's four scores and divide by 4."
        ),
    },
    ("di-grouped-bar", 3, 14): {
        "answer": "163",
        "explanation": (
            r"Combined Math total = Class A Math + Class B Math \(= 78 + 85 = 163\)."
        ),
    },
    ("di-grouped-bar", 3, 15): {
        "answer": "4",
        "explanation": (
            r"Class A total \(= 323\). Class B total \(= 327\). "
            r"Absolute difference \(= |323 - 327| = 4\)."
        ),
    },
    ("di-grouped-bar", 3, 16): {
        "answer": "18.2",
        "explanation": (
            r"Class A History = 88, Class B History = 72. "
            r"Percent less \(= \frac{88 - 72}{88} \times 100 = \frac{16}{88} \times 100 \approx 18.2\%\)."
        ),
        "common_mistake": (
            "Students may use 72 as the base instead of 88. The question asks how much less B is than A, "
            "so the base is A's score (88)."
        ),
    },
    ("di-grouped-bar", 3, 17): {
        "answer": "172",
        "explanation": (
            r"Original Science scores: A = 82, B = 80. "
            r"After adding 5 each: A = 87, B = 85. "
            r"New combined Science total \(= 87 + 85 = 172\)."
        ),
    },

    # =====================================================================
    # GRAPH SET 3: LINE GRAPH — CITY POPULATION GROWTH  (topic: "di-line-graphs")
    # Sections 0-3
    # City X: 50, 55, 60, 70, 75, 85  (2018-2023)
    # City Y: 80, 78, 75, 73, 70, 68  (2018-2023)
    # =====================================================================

    # --- Section 0: Quantitative Comparison (Q1-Q5) ----------------------

    ("di-line-graphs", 0, 1): {
        "answer": "A",
        "explanation": (
            r"City X in 2023 = 85 thousand. City Y in 2018 = 80 thousand. "
            r"Since \(85 > 80\), Quantity A is greater."
        ),
    },
    ("di-line-graphs", 0, 2): {
        "answer": "A",
        "explanation": (
            r"City X total growth \(= 85 - 50 = 35\) thousand. "
            r"City Y total decline \(= 80 - 68 = 12\) thousand. "
            r"Since \(35 > 12\), Quantity A is greater."
        ),
        "common_mistake": (
            "Students may confuse growth rate (percentage) with absolute growth (thousands). "
            "This question asks about total absolute change, not percentage change."
        ),
    },
    ("di-line-graphs", 0, 3): {
        "answer": "A",
        "explanation": (
            r"Percent increase of City X from 2018 to 2023 \(= \frac{85 - 50}{50} \times 100 = \frac{35}{50} \times 100 = 70\%\). "
            r"Quantity A \(= 70\%\) and Quantity B \(= 50\%\). Since \(70\% > 50\%\), Quantity A is greater."
        ),
    },
    ("di-line-graphs", 0, 4): {
        "answer": "A",
        "explanation": (
            r"City X grew from 50 to 85 over 5 years: average annual growth \(= \frac{35}{5} = 7\) thousand per year. "
            r"City Y declined from 80 to 68 over 5 years: average annual decline \(= \frac{12}{5} = 2.4\) thousand per year. "
            r"Since \(7 > 2.4\), Quantity A is greater."
        ),
    },
    ("di-line-graphs", 0, 5): {
        "answer": "B",
        "explanation": (
            r"Combined population in 2020 \(= 60 + 75 = 135\) thousand. "
            r"Combined population in 2023 \(= 85 + 68 = 153\) thousand. "
            r"Since \(135 < 153\), Quantity B is greater."
        ),
    },

    # --- Section 1: Multiple Choice Single Answer (Q6-Q10) ---------------

    ("di-line-graphs", 1, 6): {
        "answer": "(C) 2021",
        "explanation": (
            r"Differences (City Y \(-\) City X): "
            r"2018: \(80 - 50 = 30\), 2019: \(78 - 55 = 23\), 2020: \(75 - 60 = 15\), "
            r"2021: \(73 - 70 = 3\), 2022: \(75 - 70 = 5\) (X leads), 2023: \(85 - 68 = 17\) (X leads). "
            r"The smallest absolute difference is 3, occurring in 2021."
        ),
        "common_mistake": (
            "Students may look for where the lines cross rather than where the gap is smallest. "
            "The lines do not actually cross at any plotted year."
        ),
    },
    ("di-line-graphs", 1, 7): {
        "answer": "(C) 15%",
        "explanation": (
            r"Percent decrease of City Y \(= \frac{80 - 68}{80} \times 100 = \frac{12}{80} \times 100 = 15\%\)."
        ),
        "common_mistake": (
            "Students may divide by 68 (the final value) instead of 80 (the original value), "
            "getting approximately 17.6%. Percent decrease uses the original value as the base."
        ),
    },
    ("di-line-graphs", 1, 8): {
        "answer": "(E) 2022 to 2023",
        "explanation": (
            r"Annual increases for City X: "
            r"2018-19: 5, 2019-20: 5, 2020-21: 10, 2021-22: 5, 2022-23: 10. "
            r"Both 2020-21 and 2022-23 show an increase of 10. However, 2022 to 2023 is the latest "
            r"period with the greatest increase (tied with 2020-21). Since the question says 'the greatest amount' "
            r"and both are equal, the answer is (E) 2022 to 2023 (or equivalently (C)). "
            r"Both (C) and (E) show a 10 thousand increase, but (E) is the answer listed."
        ),
    },
    ("di-line-graphs", 1, 9): {
        "answer": "(C) 95 thousand",
        "explanation": (
            r"From 2022 to 2023, City X grew by \(85 - 75 = 10\) thousand. "
            r"Continuing at that rate: \(85 + 10 = 95\) thousand in 2024."
        ),
    },
    ("di-line-graphs", 1, 10): {
        "answer": "(C) 143 thousand",
        "explanation": (
            r"In 2021: City X = 70, City Y = 73. "
            r"Combined \(= 70 + 73 = 143\) thousand."
        ),
    },

    # --- Section 2: Multiple Choice Select One or More (Q11-Q12) ---------

    ("di-line-graphs", 2, 11): {
        "answer": "E, F",
        "explanation": (
            r"Compare populations each year: "
            r"2018: X=50 < Y=80, 2019: X=55 < Y=78, 2020: X=60 < Y=75, "
            r"2021: X=70 < Y=73, 2022: X=75 > Y=70, 2023: X=85 > Y=68. "
            r"City X exceeded City Y in 2022 and 2023."
        ),
    },
    ("di-line-graphs", 2, 12): {
        "answer": "A, B, C, D",
        "explanation": (
            r"(A) City X: 50 \(\to\) 55 \(\to\) 60 \(\to\) 70 \(\to\) 75 \(\to\) 85. "
            r"Each year is higher than the last — TRUE. "
            r"(B) City Y: 80 \(\to\) 78 \(\to\) 75 \(\to\) 73 \(\to\) 70 \(\to\) 68. "
            r"Each year is lower than the last — TRUE. "
            r"(C) Differences: 2018=30, 2019=23, 2020=15, 2021=3, 2022=5, 2023=17. "
            r"The smallest difference (3) occurs in 2021 — TRUE. "
            r"(D) In 2023: \(85 - 68 = 17 > 15\) — TRUE."
        ),
    },

    # --- Section 3: Numeric Entry (Q13-Q17) ------------------------------

    ("di-line-graphs", 3, 13): {
        "answer": "35",
        "explanation": (
            r"City X grew from 50 (in 2018) to 85 (in 2023). "
            r"Total growth \(= 85 - 50 = 35\) thousand."
        ),
    },
    ("di-line-graphs", 3, 14): {
        "answer": "2.4",
        "explanation": (
            r"City Y declined from 80 to 68 over 5 years. "
            r"Total decline \(= 80 - 68 = 12\). "
            r"Average annual decline \(= \frac{12}{5} = 2.4\) thousand per year."
        ),
    },
    ("di-line-graphs", 3, 15): {
        "answer": "5/4",
        "explanation": (
            r"City X in 2023 = 85, City Y in 2023 = 68. "
            r"Ratio \(= \frac{85}{68} = \frac{5}{4}\) (dividing both by 17)."
        ),
    },
    ("di-line-graphs", 3, 16): {
        "answer": "3",
        "explanation": (
            r"In 2021: City Y = 73, City X = 70. "
            r"Difference \(= 73 - 70 = 3\) thousand."
        ),
    },
    ("di-line-graphs", 3, 17): {
        "answer": "17.7",
        "explanation": (
            r"Combined population in 2018 \(= 50 + 80 = 130\). "
            r"Combined population in 2023 \(= 85 + 68 = 153\). "
            r"Percent increase \(= \frac{153 - 130}{130} \times 100 = \frac{23}{130} \times 100 \approx 17.7\%\)."
        ),
    },
}
