"""
Data Interpretation Part 2 — Pie Charts, Data Tables, Combined Charts
Each data set has 17 questions split across 4 section types (QC, MC Single, MC Multi, Numeric Entry).
"""

# ─── SVG helper: Pie Chart ──────────────────────────────────────────────
import math as _math

def _pie_svg():
    """Build an SVG pie chart for Monthly Budget Allocation."""
    cx, cy, r = 180, 160, 100
    slices = [
        ("Rent",      35,  "#6c63ff"),
        ("Food",      20,  "#34d399"),
        ("Transport", 15,  "#f87171"),
        ("Utilities", 10,  "#fbbf24"),
        ("Savings",   12,  "#60a5fa"),
        ("Other",      8,  "#8b83ff"),
    ]

    paths = []
    cumulative = 0
    for name, pct, color in slices:
        start_angle = cumulative * 3.6          # degrees
        end_angle   = (cumulative + pct) * 3.6
        # SVG arcs start from 12‑o'clock (−90°) and go clockwise
        sa_rad = _math.radians(start_angle - 90)
        ea_rad = _math.radians(end_angle - 90)
        x1 = cx + r * _math.cos(sa_rad)
        y1 = cy + r * _math.sin(sa_rad)
        x2 = cx + r * _math.cos(ea_rad)
        y2 = cy + r * _math.sin(ea_rad)
        large = 1 if (end_angle - start_angle) > 180 else 0
        paths.append(
            f'<path d="M {cx},{cy} L {x1:.1f},{y1:.1f} '
            f'A {r},{r} 0 {large} 1 {x2:.1f},{y2:.1f} Z" '
            f'fill="{color}" stroke="#181926" stroke-width="1.5"/>'
        )
        # label at mid-angle
        mid_rad = _math.radians((start_angle + end_angle) / 2 - 90)
        lx = cx + (r + 18) * _math.cos(mid_rad)
        ly = cy + (r + 18) * _math.sin(mid_rad)
        paths.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" fill="#e4e4e7" '
            f'font-size="9" text-anchor="middle" '
            f'dominant-baseline="middle">{pct}%</text>'
        )
        cumulative += pct

    # legend
    legend_x, legend_y = 310, 60
    legend_items = []
    for i, (name, pct, color) in enumerate(slices):
        yy = legend_y + i * 22
        legend_items.append(
            f'<rect x="{legend_x}" y="{yy}" width="12" height="12" '
            f'rx="2" fill="{color}"/>'
            f'<text x="{legend_x + 18}" y="{yy + 10}" fill="#e4e4e7" '
            f'font-size="10">{name} ({pct}%)</text>'
        )

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 300" '
        'style="max-width:450px;width:100%;">'
        '<text x="225" y="24" fill="#e4e4e7" font-size="13" '
        'font-weight="700" text-anchor="middle">'
        'Monthly Budget Allocation (Total: $5,000)</text>'
        + "".join(paths)
        + "".join(legend_items)
        + '</svg>'
    )


def _combined_svg():
    """Build an SVG combined bar + line chart for Factory Production & Cost."""
    data = [
        ("Jan", 500, 12.0),
        ("Feb", 600, 11.0),
        ("Mar", 700, 10.0),
        ("Apr", 650, 10.5),
        ("May", 800,  9.0),
        ("Jun", 750,  9.5),
    ]
    # layout
    left, right, top, bottom = 55, 400, 45, 255
    w = right - left
    h = bottom - top
    n = len(data)
    bar_w = w / n
    # left y-axis: 0-1000 (units)
    # right y-axis: 8-13 (cost)
    def uy(v):            # units → y
        return bottom - (v / 1000) * h
    def cy(v):            # cost → y
        return bottom - ((v - 8) / 5) * h

    bars = []
    dots = []
    line_pts = []
    for i, (month, units, cost) in enumerate(data):
        bx = left + i * bar_w + bar_w * 0.15
        bw = bar_w * 0.5
        by = uy(units)
        bh = bottom - by
        bars.append(
            f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" '
            f'height="{bh:.1f}" fill="#6c63ff" rx="2" opacity="0.9"/>'
        )
        # month label
        bars.append(
            f'<text x="{left + i * bar_w + bar_w / 2:.1f}" '
            f'y="{bottom + 16}" fill="#9194a1" font-size="10" '
            f'text-anchor="middle">{month}</text>'
        )
        # cost dot + line
        dx = left + i * bar_w + bar_w / 2
        dy = cy(cost)
        line_pts.append(f"{dx:.1f},{dy:.1f}")
        dots.append(
            f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="4" '
            f'fill="#f87171" stroke="#181926" stroke-width="1"/>'
        )

    # grid lines (horizontal)
    grids = []
    for v in range(0, 1001, 200):
        y = uy(v)
        grids.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" '
            f'stroke="#2e3140" stroke-width="0.7"/>'
        )
        grids.append(
            f'<text x="{left - 6}" y="{y + 3:.1f}" fill="#9194a1" '
            f'font-size="9" text-anchor="end">{v}</text>'
        )
    # right y-axis labels
    for v_raw in [8, 9, 10, 11, 12, 13]:
        y = cy(v_raw)
        grids.append(
            f'<text x="{right + 6}" y="{y + 3:.1f}" fill="#9194a1" '
            f'font-size="9" text-anchor="start">${v_raw}</text>'
        )

    polyline = (
        f'<polyline points="{" ".join(line_pts)}" fill="none" '
        f'stroke="#f87171" stroke-width="2.5"/>'
    )

    legend = (
        '<rect x="140" y="6" width="10" height="10" fill="#6c63ff" rx="2"/>'
        '<text x="154" y="15" fill="#e4e4e7" font-size="10">Units Produced</text>'
        '<rect x="260" y="6" width="10" height="10" fill="#f87171" rx="2"/>'
        '<text x="274" y="15" fill="#e4e4e7" font-size="10">Cost per Unit ($)</text>'
    )

    # axis lines
    axes = (
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" '
        f'stroke="#9194a1" stroke-width="1"/>'
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" '
        f'stroke="#9194a1" stroke-width="1"/>'
        f'<line x1="{right}" y1="{top}" x2="{right}" y2="{bottom}" '
        f'stroke="#9194a1" stroke-width="1"/>'
    )

    # axis titles
    axis_titles = (
        '<text x="20" y="150" fill="#9194a1" font-size="10" '
        'text-anchor="middle" transform="rotate(-90,20,150)">Units</text>'
        '<text x="435" y="150" fill="#9194a1" font-size="10" '
        'text-anchor="middle" transform="rotate(90,435,150)">Cost ($)</text>'
    )

    title = (
        '<text x="225" y="30" fill="#e4e4e7" font-size="13" '
        'font-weight="700" text-anchor="middle">'
        'Factory Production &amp; Cost per Unit</text>'
    )

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 300" '
        'style="max-width:450px;width:100%;">'
        + title + legend + "".join(grids) + axes + axis_titles
        + "".join(bars) + polyline + "".join(dots)
        + '</svg>'
    )


# ── Pre-build the SVG / HTML strings ────────────────────────────────────
_PIE_SVG = _pie_svg()
_TABLE_HTML = (
    '<table style="width:100%;border-collapse:collapse;color:#e4e4e7;font-size:.9rem;margin:1rem 0;">'
    '<caption style="font-weight:700;margin-bottom:.5rem;font-size:1rem;">Student Test Scores by Subject (out of 100)</caption>'
    '<thead><tr style="border-bottom:2px solid #6c63ff;">'
    '<th style="padding:.5rem;text-align:left;color:#9194a1;">Student</th>'
    '<th style="padding:.5rem;text-align:center;color:#9194a1;">Math</th>'
    '<th style="padding:.5rem;text-align:center;color:#9194a1;">Verbal</th>'
    '<th style="padding:.5rem;text-align:center;color:#9194a1;">Writing</th>'
    '<th style="padding:.5rem;text-align:center;color:#9194a1;">Average</th>'
    '</tr></thead><tbody>'
    '<tr style="border-bottom:1px solid #2e3140;"><td style="padding:.5rem;">Alex</td><td style="text-align:center;">85</td><td style="text-align:center;">72</td><td style="text-align:center;">90</td><td style="text-align:center;">82.3</td></tr>'
    '<tr style="border-bottom:1px solid #2e3140;"><td style="padding:.5rem;">Blake</td><td style="text-align:center;">92</td><td style="text-align:center;">88</td><td style="text-align:center;">76</td><td style="text-align:center;">85.3</td></tr>'
    '<tr style="border-bottom:1px solid #2e3140;"><td style="padding:.5rem;">Casey</td><td style="text-align:center;">78</td><td style="text-align:center;">95</td><td style="text-align:center;">82</td><td style="text-align:center;">85.0</td></tr>'
    '<tr style="border-bottom:1px solid #2e3140;"><td style="padding:.5rem;">Dana</td><td style="text-align:center;">95</td><td style="text-align:center;">80</td><td style="text-align:center;">88</td><td style="text-align:center;">87.7</td></tr>'
    '<tr style="border-bottom:1px solid #2e3140;"><td style="padding:.5rem;">Evan</td><td style="text-align:center;">70</td><td style="text-align:center;">90</td><td style="text-align:center;">75</td><td style="text-align:center;">78.3</td></tr>'
    '</tbody></table>'
)
_COMBINED_SVG = _combined_svg()


# =====================================================================
# SECTIONS  (12 sections: 4 per data set)
# =====================================================================
SECTIONS = [
    # ==================================================================
    # DATA SET 4 — Pie Chart: Monthly Budget Allocation  (sections 0-3)
    # ==================================================================

    # ── Section 0: QC ────────────────────────────────────────────────
    {
        "title": r"Pie Chart — Quantitative Comparison",
        "topic_id": "di-pie-charts",
        "instructions": (
            r"Use the pie chart below to answer each question.<br>"
            r"<b>A.</b> Quantity A is greater &nbsp; "
            r"<b>B.</b> Quantity B is greater &nbsp; "
            r"<b>C.</b> The two quantities are equal &nbsp; "
            r"<b>D.</b> The relationship cannot be determined"
            r"<br><br>" + _PIE_SVG
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"Based on the chart above,",
                "qtyA": r"Amount spent on Rent",
                "qtyB": r"Amount spent on Food and Transport combined",
            },
            {
                "id": 2,
                "stem": r"Based on the chart above,",
                "qtyA": r"Central angle for the Rent sector",
                "qtyB": r"\(120°\)",
            },
            {
                "id": 3,
                "stem": r"Based on the chart above,",
                "qtyA": r"Savings as a fraction of total budget",
                "qtyB": r"\(\dfrac{1}{8}\)",
            },
            {
                "id": 4,
                "stem": r"Based on the chart above,",
                "qtyA": r"Ratio of Food spending to Utilities spending",
                "qtyB": r"\(2\)",
            },
            {
                "id": 5,
                "stem": r"Based on the chart above,",
                "qtyA": r"Combined percentage of the top 3 categories",
                "qtyB": r"\(70\%\)",
            },
        ],
    },

    # ── Section 1: MC Single ─────────────────────────────────────────
    {
        "title": r"Pie Chart — Multiple Choice (Single Answer)",
        "topic_id": "di-pie-charts",
        "instructions": (
            r"Use the pie chart below to answer each question. "
            r"Select <b>one</b> answer."
            r"<br><br>" + _PIE_SVG
        ),
        "questions": [
            {
                "id": 6,
                "stem": r"What central angle (in degrees) represents the Food sector in the chart above?",
                "choices": [
                    r"(A) 60°",
                    r"(B) 72°",
                    r"(C) 80°",
                    r"(D) 90°",
                    r"(E) 100°",
                ],
            },
            {
                "id": 7,
                "stem": r"If Rent increases by 10% of its current amount and the total budget stays the same, what is the new Rent amount?",
                "choices": [
                    r"(A) $1,825",
                    r"(B) $1,900",
                    r"(C) $1,925",
                    r"(D) $1,950",
                    r"(E) $2,000",
                ],
            },
            {
                "id": 8,
                "stem": r"Based on the chart above, spending on Transport and Utilities combined equals what fraction of Rent spending?",
                "choices": [
                    r"(A) \(\dfrac{5}{7}\)",
                    r"(B) \(\dfrac{1}{2}\)",
                    r"(C) \(\dfrac{3}{7}\)",
                    r"(D) \(\dfrac{5}{14}\)",
                    r"(E) \(\dfrac{1}{4}\)",
                ],
            },
            {
                "id": 9,
                "stem": r"If the total monthly budget increases to $6,000 and the Rent percentage stays at 35%, how much goes to Rent?",
                "choices": [
                    r"(A) $1,750",
                    r"(B) $1,800",
                    r"(C) $2,000",
                    r"(D) $2,100",
                    r"(E) $2,400",
                ],
            },
            {
                "id": 10,
                "stem": r"Based on the chart above, which category is closest to \(\dfrac{1}{6}\) of the total budget?",
                "choices": [
                    r"(A) Food",
                    r"(B) Transport",
                    r"(C) Utilities",
                    r"(D) Savings",
                    r"(E) Other",
                ],
            },
        ],
    },

    # ── Section 2: MC Multi ──────────────────────────────────────────
    {
        "title": r"Pie Chart — Multiple Choice (Select One or More)",
        "topic_id": "di-pie-charts",
        "instructions": (
            r"Use the pie chart below to answer each question. "
            r"Select <b>all</b> that apply."
            r"<br><br>" + _PIE_SVG
        ),
        "questions": [
            {
                "id": 11,
                "stem": r"Based on the chart above, which categories individually account for more than $600 per month?",
                "choices": [
                    r"(A) Rent",
                    r"(B) Food",
                    r"(C) Transport",
                    r"(D) Utilities",
                    r"(E) Savings",
                    r"(F) Other",
                ],
            },
            {
                "id": 12,
                "stem": r"Based on the chart above, which of the following statements are true?",
                "choices": [
                    r"(A) Savings spending exceeds Utilities spending",
                    r"(B) Other is the smallest category",
                    r"(C) Rent accounts for more than \(\dfrac{1}{3}\) of the total budget",
                    r"(D) Food + Other = Transport + Savings",
                ],
            },
        ],
    },

    # ── Section 3: Numeric Entry ─────────────────────────────────────
    {
        "title": r"Pie Chart — Numeric Entry",
        "topic_id": "di-pie-charts",
        "instructions": (
            r"Use the pie chart below to answer each question. "
            r"Enter your answer as a number."
            r"<br><br>" + _PIE_SVG
        ),
        "questions": [
            {
                "id": 13,
                "stem": r"Enter the central angle (in degrees, rounded to the nearest whole number) for the Savings sector in the chart above.",
            },
            {
                "id": 14,
                "stem": r"If the amount spent on Food decreases by 25%, enter the new Food amount in dollars.",
            },
            {
                "id": 15,
                "stem": r"Based on the chart above, enter the amount (in dollars) saved monthly.",
            },
            {
                "id": 16,
                "stem": r"Enter the total spending (in dollars) on all categories other than Rent and Food.",
            },
            {
                "id": 17,
                "stem": r"If the total budget is reduced by 20% but all category percentages stay the same, enter the new Transport amount in dollars.",
            },
        ],
    },

    # ==================================================================
    # DATA SET 5 — Data Table: Student Performance  (sections 4-7)
    # ==================================================================

    # ── Section 4 (local 0): QC ──────────────────────────────────────
    {
        "title": r"Data Table — Quantitative Comparison",
        "topic_id": "di-tables",
        "instructions": (
            r"Use the table below to answer each question.<br>"
            r"<b>A.</b> Quantity A is greater &nbsp; "
            r"<b>B.</b> Quantity B is greater &nbsp; "
            r"<b>C.</b> The two quantities are equal &nbsp; "
            r"<b>D.</b> The relationship cannot be determined"
            r"<br><br>" + _TABLE_HTML
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"Based on the table above,",
                "qtyA": r"The highest Math score among all students",
                "qtyB": r"The highest Verbal score among all students",
            },
            {
                "id": 2,
                "stem": r"Based on the table above,",
                "qtyA": r"Dana's average score",
                "qtyB": r"Blake's average score",
            },
            {
                "id": 3,
                "stem": r"Based on the table above,",
                "qtyA": r"Range of Math scores",
                "qtyB": r"Range of Writing scores",
            },
            {
                "id": 4,
                "stem": r"Based on the table above,",
                "qtyA": r"Class average in Math",
                "qtyB": r"Class average in Verbal",
            },
            {
                "id": 5,
                "stem": r"Based on the table above,",
                "qtyA": r"Evan's total score across all three subjects",
                "qtyB": r"\(240\)",
            },
        ],
    },

    # ── Section 5 (local 1): MC Single ───────────────────────────────
    {
        "title": r"Data Table — Multiple Choice (Single Answer)",
        "topic_id": "di-tables",
        "instructions": (
            r"Use the table below to answer each question. "
            r"Select <b>one</b> answer."
            r"<br><br>" + _TABLE_HTML
        ),
        "questions": [
            {
                "id": 6,
                "stem": r"Based on the table above, what is the median Math score?",
                "choices": [
                    r"(A) 70",
                    r"(B) 78",
                    r"(C) 85",
                    r"(D) 92",
                    r"(E) 95",
                ],
            },
            {
                "id": 7,
                "stem": r"Based on the table above, which student has the greatest difference between their highest and lowest subject scores?",
                "choices": [
                    r"(A) Alex",
                    r"(B) Blake",
                    r"(C) Casey",
                    r"(D) Dana",
                    r"(E) Evan",
                ],
            },
            {
                "id": 8,
                "stem": r"Based on the table above, what is the class average Writing score?",
                "choices": [
                    r"(A) 78.2",
                    r"(B) 80.0",
                    r"(C) 82.2",
                    r"(D) 84.0",
                    r"(E) 85.0",
                ],
            },
            {
                "id": 9,
                "stem": r"Based on the table above, Alex's Math score is what percent of Dana's Math score?",
                "choices": [
                    r"(A) 85%",
                    r"(B) approximately 89%",
                    r"(C) 90%",
                    r"(D) approximately 92%",
                    r"(E) 95%",
                ],
            },
            {
                "id": 10,
                "stem": r"Based on the table above, if Casey's Writing score increased by 10 points, what would Casey's new average be?",
                "choices": [
                    r"(A) 86.7",
                    r"(B) 87.0",
                    r"(C) 88.3",
                    r"(D) 89.0",
                    r"(E) 91.7",
                ],
            },
        ],
    },

    # ── Section 6 (local 2): MC Multi ────────────────────────────────
    {
        "title": r"Data Table — Multiple Choice (Select One or More)",
        "topic_id": "di-tables",
        "instructions": (
            r"Use the table below to answer each question. "
            r"Select <b>all</b> that apply."
            r"<br><br>" + _TABLE_HTML
        ),
        "questions": [
            {
                "id": 11,
                "stem": r"Based on the table above, which students scored higher in Verbal than in Math?",
                "choices": [
                    r"(A) Alex",
                    r"(B) Blake",
                    r"(C) Casey",
                    r"(D) Dana",
                    r"(E) Evan",
                ],
            },
            {
                "id": 12,
                "stem": r"Based on the table above, which of the following statements are true?",
                "choices": [
                    r"(A) Dana has the highest average score",
                    r"(B) The class average in Verbal is higher than in Writing",
                    r"(C) Every student scored at least 70 in every subject",
                    r"(D) Blake's Writing score is the lowest Writing score in the class",
                ],
            },
        ],
    },

    # ── Section 7 (local 3): Numeric Entry ───────────────────────────
    {
        "title": r"Data Table — Numeric Entry",
        "topic_id": "di-tables",
        "instructions": (
            r"Use the table below to answer each question. "
            r"Enter your answer as a number."
            r"<br><br>" + _TABLE_HTML
        ),
        "questions": [
            {
                "id": 13,
                "stem": r"Based on the table above, enter the class average Math score.",
            },
            {
                "id": 14,
                "stem": r"Based on the table above, enter the range of Verbal scores (highest minus lowest).",
            },
            {
                "id": 15,
                "stem": r"Based on the table above, enter Dana's total score across all three subjects.",
            },
            {
                "id": 16,
                "stem": r"Based on the table above, enter the sum of all 15 individual scores (5 students × 3 subjects).",
            },
            {
                "id": 17,
                "stem": r"Based on the table above, enter the median of all five students' average scores.",
            },
        ],
    },

    # ==================================================================
    # DATA SET 6 — Combined Chart: Factory Production & Cost (sections 8-11)
    # ==================================================================

    # ── Section 8 (local 0): QC ──────────────────────────────────────
    {
        "title": r"Combined Chart — Quantitative Comparison",
        "topic_id": "di-combined",
        "instructions": (
            r"Use the chart below to answer each question.<br>"
            r"<b>A.</b> Quantity A is greater &nbsp; "
            r"<b>B.</b> Quantity B is greater &nbsp; "
            r"<b>C.</b> The two quantities are equal &nbsp; "
            r"<b>D.</b> The relationship cannot be determined"
            r"<br><br>" + _COMBINED_SVG
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"Based on the chart above,",
                "qtyA": r"Total units produced in Jan–Mar",
                "qtyB": r"Total units produced in Apr–Jun",
            },
            {
                "id": 2,
                "stem": r"Based on the chart above,",
                "qtyA": r"Total production cost in March",
                "qtyB": r"Total production cost in January",
            },
            {
                "id": 3,
                "stem": r"Based on the chart above,",
                "qtyA": r"Average cost per unit over all 6 months",
                "qtyB": r"\(\$10\)",
            },
            {
                "id": 4,
                "stem": r"Based on the chart above,",
                "qtyA": r"Percent increase in production from January to May",
                "qtyB": r"\(50\%\)",
            },
            {
                "id": 5,
                "stem": r"Based on the chart above,",
                "qtyA": r"Total cost in April (units \(\times\) cost per unit)",
                "qtyB": r"Total cost in June (units \(\times\) cost per unit)",
            },
        ],
    },

    # ── Section 9 (local 1): MC Single ───────────────────────────────
    {
        "title": r"Combined Chart — Multiple Choice (Single Answer)",
        "topic_id": "di-combined",
        "instructions": (
            r"Use the chart below to answer each question. "
            r"Select <b>one</b> answer."
            r"<br><br>" + _COMBINED_SVG
        ),
        "questions": [
            {
                "id": 6,
                "stem": r"Based on the chart above, in which month was the total production cost (units × cost per unit) the highest?",
                "choices": [
                    r"(A) January",
                    r"(B) March",
                    r"(C) April",
                    r"(D) May",
                    r"(E) June",
                ],
            },
            {
                "id": 7,
                "stem": r"Based on the chart above, what is the total production cost for all 6 months combined?",
                "choices": [
                    r"(A) $38,750",
                    r"(B) $39,825",
                    r"(C) $40,750",
                    r"(D) $40,950",
                    r"(E) $41,825",
                ],
            },
            {
                "id": 8,
                "stem": r"Based on the chart above, by what percent did the cost per unit decrease from January to May?",
                "choices": [
                    r"(A) 20%",
                    r"(B) 25%",
                    r"(C) 30%",
                    r"(D) 33%",
                    r"(E) 35%",
                ],
            },
            {
                "id": 9,
                "stem": r"Based on the chart above, what is the average number of units produced per month over the 6-month period?",
                "choices": [
                    r"(A) 625",
                    r"(B) 650",
                    r"(C) 667",
                    r"(D) 700",
                    r"(E) 725",
                ],
            },
            {
                "id": 10,
                "stem": r"Based on the chart above, which month shows the greatest month-over-month increase in units produced?",
                "choices": [
                    r"(A) Jan to Feb",
                    r"(B) Feb to Mar",
                    r"(C) Mar to Apr",
                    r"(D) Apr to May",
                    r"(E) May to Jun",
                ],
            },
        ],
    },

    # ── Section 10 (local 2): MC Multi ───────────────────────────────
    {
        "title": r"Combined Chart — Multiple Choice (Select One or More)",
        "topic_id": "di-combined",
        "instructions": (
            r"Use the chart below to answer each question. "
            r"Select <b>all</b> that apply."
            r"<br><br>" + _COMBINED_SVG
        ),
        "questions": [
            {
                "id": 11,
                "stem": r"Based on the chart above, in which months did the total production cost (units × cost per unit) exceed $7,000?",
                "choices": [
                    r"(A) January",
                    r"(B) February",
                    r"(C) March",
                    r"(D) April",
                    r"(E) May",
                    r"(F) June",
                ],
            },
            {
                "id": 12,
                "stem": r"Based on the chart above, which of the following statements are true?",
                "choices": [
                    r"(A) The cost per unit generally decreases as production increases",
                    r"(B) May has both the highest production and the lowest cost per unit",
                    r"(C) Total cost in February is less than total cost in January",
                    r"(D) The range of units produced is 300",
                ],
            },
        ],
    },

    # ── Section 11 (local 3): Numeric Entry ──────────────────────────
    {
        "title": r"Combined Chart — Numeric Entry",
        "topic_id": "di-combined",
        "instructions": (
            r"Use the chart below to answer each question. "
            r"Enter your answer as a number."
            r"<br><br>" + _COMBINED_SVG
        ),
        "questions": [
            {
                "id": 13,
                "stem": r"Based on the chart above, enter the total production cost (in dollars) for February.",
            },
            {
                "id": 14,
                "stem": r"Based on the chart above, enter the total units produced across all 6 months.",
            },
            {
                "id": 15,
                "stem": r"Based on the chart above, enter the difference in total production cost between May and January (in dollars).",
            },
            {
                "id": 16,
                "stem": r"Based on the chart above, enter the percent increase (as a whole number) in production from January to May.",
            },
            {
                "id": 17,
                "stem": r"Based on the chart above, enter the average cost per unit (to one decimal place) across all 6 months.",
            },
        ],
    },
]


# =====================================================================
# ANSWERS  — keyed by (topic_id, local_section_index, question_id)
# =====================================================================
ANSWERS = {
    # ==================================================================
    # DATA SET 4 — Pie Chart  (topic: "di-pie-charts")
    # ==================================================================

    # ── QC (local section 0) ─────────────────────────────────────────
    ("di-pie-charts", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Rent = 35% of $5,000 = $1,750. Food + Transport = 20% + 15% = 35% "
            r"of $5,000 = $1,750. Since \(\$1{,}750 = \$1{,}750\), the two quantities are equal."
        ),
    },
    ("di-pie-charts", 0, 2): {
        "answer": "A",
        "explanation": (
            r"The central angle for Rent is \(35\% \times 360° = 0.35 \times 360° = 126°\). "
            r"Since \(126° > 120°\), Quantity A is greater."
        ),
    },
    ("di-pie-charts", 0, 3): {
        "answer": "B",
        "explanation": (
            r"Savings as a fraction of total = \(\frac{12}{100} = 0.12\). "
            r"Quantity B = \(\frac{1}{8} = 0.125\). "
            r"Since \(0.12 < 0.125\), Quantity B is greater."
        ),
        "common_mistake": (
            r"Rounding 12% to \(\frac{1}{8}\). While close, \(12\% = 0.12\) is strictly "
            r"less than \(\frac{1}{8} = 0.125\)."
        ),
    },
    ("di-pie-charts", 0, 4): {
        "answer": "C",
        "explanation": (
            r"Food = $1,000 and Utilities = $500. "
            r"The ratio is \(\frac{1{,}000}{500} = 2\). "
            r"Quantity B is also 2, so the two quantities are equal."
        ),
    },
    ("di-pie-charts", 0, 5): {
        "answer": "C",
        "explanation": (
            r"The top 3 categories by percentage are Rent (35%), Food (20%), and Transport (15%). "
            r"Combined: \(35 + 20 + 15 = 70\%\). Quantity B is \(70\%\). "
            r"The two quantities are equal."
        ),
    },

    # ── MC Single (local section 1) ──────────────────────────────────
    ("di-pie-charts", 1, 6): {
        "answer": r"(B) 72°",
        "explanation": (
            r"Food is 20% of the budget. The central angle is "
            r"\(20\% \times 360° = 0.20 \times 360° = 72°\)."
        ),
    },
    ("di-pie-charts", 1, 7): {
        "answer": r"(C) $1,925",
        "explanation": (
            r"Current Rent = $1,750. A 10% increase: "
            r"\(\$1{,}750 \times 1.10 = \$1{,}925\)."
        ),
        "common_mistake": (
            r"Computing 10% of the total budget ($500) and adding it to Rent. "
            r"The increase is 10% of the Rent amount, not 10% of the total."
        ),
    },
    ("di-pie-charts", 1, 8): {
        "answer": r"(A) \(\dfrac{5}{7}\)",
        "explanation": (
            r"Transport + Utilities = \(\$750 + \$500 = \$1{,}250\). "
            r"As a fraction of Rent (\$1,750): "
            r"\(\frac{1{,}250}{1{,}750} = \frac{1250}{1750} = \frac{5}{7}\)."
        ),
    },
    ("di-pie-charts", 1, 9): {
        "answer": r"(D) $2,100",
        "explanation": (
            r"New budget = $6,000 with Rent at 35%: "
            r"\(0.35 \times \$6{,}000 = \$2{,}100\)."
        ),
    },
    ("di-pie-charts", 1, 10): {
        "answer": r"(B) Transport",
        "explanation": (
            r"\(\frac{1}{6} \approx 16.67\%\). The category percentages are: "
            r"Food 20%, Transport 15%, Utilities 10%, Savings 12%, Other 8%. "
            r"Transport at 15% is closest to 16.67%."
        ),
    },

    # ── MC Multi (local section 2) ───────────────────────────────────
    ("di-pie-charts", 2, 11): {
        "answer": "A, B, C",
        "explanation": (
            r"Amounts: Rent = \$1,750, Food = \$1,000, Transport = \$750, "
            r"Utilities = \$500, Savings = \$600, Other = \$400. "
            r"Categories exceeding \$600: Rent (\$1,750), Food (\$1,000), "
            r"and Transport (\$750). Savings is exactly \$600, not more than \$600."
        ),
        "common_mistake": (
            r"Including Savings (\$600). The question asks for more than \$600, "
            r"not \$600 or more."
        ),
    },
    ("di-pie-charts", 2, 12): {
        "answer": "A, B, C",
        "explanation": (
            r"(A) Savings (\$600) > Utilities (\$500) — True. "
            r"(B) Other (8%) is the smallest category — True. "
            r"(C) Rent is 35%, and \(\frac{1}{3} \approx 33.3\%\), so \(35\% > 33.3\%\) — True. "
            r"(D) Food + Other = \$1,000 + \$400 = \$1,400. Transport + Savings = "
            r"\$750 + \$600 = \$1,350. Since \(\$1,400 \neq \$1,350\) — False."
        ),
    },

    # ── Numeric Entry (local section 3) ──────────────────────────────
    ("di-pie-charts", 3, 13): {
        "answer": "43",
        "explanation": (
            r"Savings is 12% of the budget. Central angle = "
            r"\(0.12 \times 360° = 43.2°\). Rounded to the nearest whole number: \(43°\)."
        ),
    },
    ("di-pie-charts", 3, 14): {
        "answer": "750",
        "explanation": (
            r"Current Food spending = \$1,000. A 25% decrease: "
            r"\(\$1{,}000 \times (1 - 0.25) = \$1{,}000 \times 0.75 = \$750\)."
        ),
    },
    ("di-pie-charts", 3, 15): {
        "answer": "600",
        "explanation": (
            r"From the chart, Savings = 12% of \$5,000 = \(\$600\)."
        ),
    },
    ("di-pie-charts", 3, 16): {
        "answer": "2250",
        "explanation": (
            r"Total budget = \$5,000. Rent + Food = \$1,750 + \$1,000 = \$2,750. "
            r"Remaining = \$5,000 - \$2,750 = \$2,250."
        ),
    },
    ("di-pie-charts", 3, 17): {
        "answer": "600",
        "explanation": (
            r"New total budget = \(\$5{,}000 \times 0.80 = \$4{,}000\). "
            r"Transport stays at 15%: \(0.15 \times \$4{,}000 = \$600\)."
        ),
    },

    # ==================================================================
    # DATA SET 5 — Data Table  (topic: "di-tables")
    # ==================================================================

    # ── QC (local section 0) ─────────────────────────────────────────
    ("di-tables", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Highest Math score: Dana with 95. Highest Verbal score: Casey with 95. "
            r"Since \(95 = 95\), the two quantities are equal."
        ),
    },
    ("di-tables", 0, 2): {
        "answer": "A",
        "explanation": (
            r"Dana's average = \(\frac{95 + 80 + 88}{3} = \frac{263}{3} \approx 87.7\). "
            r"Blake's average = \(\frac{92 + 88 + 76}{3} = \frac{256}{3} \approx 85.3\). "
            r"Since \(87.7 > 85.3\), Quantity A is greater."
        ),
    },
    ("di-tables", 0, 3): {
        "answer": "A",
        "explanation": (
            r"Math scores: 70, 78, 85, 92, 95. Range = \(95 - 70 = 25\). "
            r"Writing scores: 75, 76, 82, 88, 90. Range = \(90 - 75 = 15\). "
            r"Since \(25 > 15\), Quantity A is greater."
        ),
    },
    ("di-tables", 0, 4): {
        "answer": "B",
        "explanation": (
            r"Class Math average = \(\frac{85 + 92 + 78 + 95 + 70}{5} = \frac{420}{5} = 84\). "
            r"Class Verbal average = \(\frac{72 + 88 + 95 + 80 + 90}{5} = \frac{425}{5} = 85\). "
            r"Since \(84 < 85\), Quantity B is greater."
        ),
    },
    ("di-tables", 0, 5): {
        "answer": "B",
        "explanation": (
            r"Evan's total = \(70 + 90 + 75 = 235\). "
            r"Since \(235 < 240\), Quantity B is greater."
        ),
    },

    # ── MC Single (local section 1) ──────────────────────────────────
    ("di-tables", 1, 6): {
        "answer": r"(C) 85",
        "explanation": (
            r"Math scores sorted: 70, 78, 85, 92, 95. "
            r"The median (middle value of 5) is the 3rd value: 85."
        ),
    },
    ("di-tables", 1, 7): {
        "answer": r"(E) Evan",
        "explanation": (
            r"Differences (highest − lowest): "
            r"Alex: \(90 - 72 = 18\). Blake: \(92 - 76 = 16\). "
            r"Casey: \(95 - 78 = 17\). Dana: \(95 - 80 = 15\). "
            r"Evan: \(90 - 70 = 20\). Evan has the greatest spread of 20."
        ),
    },
    ("di-tables", 1, 8): {
        "answer": r"(C) 82.2",
        "explanation": (
            r"Writing scores: 90, 76, 82, 88, 75. "
            r"Sum = \(90 + 76 + 82 + 88 + 75 = 411\). "
            r"Average = \(\frac{411}{5} = 82.2\)."
        ),
    },
    ("di-tables", 1, 9): {
        "answer": r"(B) approximately 89%",
        "explanation": (
            r"Alex's Math = 85, Dana's Math = 95. "
            r"\(\frac{85}{95} \approx 0.8947 \approx 89\%\)."
        ),
        "common_mistake": (
            r"Choosing 85% by confusing Alex's score with the percentage. "
            r"The question asks for Alex's score as a percent of Dana's, not the score itself."
        ),
    },
    ("di-tables", 1, 10): {
        "answer": r"(C) 88.3",
        "explanation": (
            r"Casey's new scores: Math 78, Verbal 95, Writing \(82 + 10 = 92\). "
            r"New average = \(\frac{78 + 95 + 92}{3} = \frac{265}{3} \approx 88.3\)."
        ),
    },

    # ── MC Multi (local section 2) ───────────────────────────────────
    ("di-tables", 2, 11): {
        "answer": "C, E",
        "explanation": (
            r"Compare Verbal vs Math for each student: "
            r"Alex: 72 < 85 (no). Blake: 88 < 92 (no). "
            r"Casey: 95 > 78 (yes). Dana: 80 < 95 (no). "
            r"Evan: 90 > 70 (yes). Casey and Evan scored higher in Verbal than Math."
        ),
    },
    ("di-tables", 2, 12): {
        "answer": "A, B, C",
        "explanation": (
            r"(A) Dana's average is 87.7, the highest among all students — True. "
            r"(B) Class Verbal average = 85; class Writing average = 82.2. "
            r"Since \(85 > 82.2\) — True. "
            r"(C) Check all scores: the minimum is Evan's Math at 70, which is "
            r"at least 70 — True. "
            r"(D) Writing scores: Alex 90, Blake 76, Casey 82, Dana 88, Evan 75. "
            r"Evan's 75 is the lowest Writing score, not Blake's 76 — False."
        ),
    },

    # ── Numeric Entry (local section 3) ──────────────────────────────
    ("di-tables", 3, 13): {
        "answer": "84",
        "explanation": (
            r"Math scores: 85, 92, 78, 95, 70. "
            r"Sum = \(85 + 92 + 78 + 95 + 70 = 420\). "
            r"Average = \(\frac{420}{5} = 84\)."
        ),
    },
    ("di-tables", 3, 14): {
        "answer": "23",
        "explanation": (
            r"Verbal scores: 72, 88, 95, 80, 90. "
            r"Range = \(95 - 72 = 23\)."
        ),
    },
    ("di-tables", 3, 15): {
        "answer": "263",
        "explanation": (
            r"Dana's scores: Math 95, Verbal 80, Writing 88. "
            r"Total = \(95 + 80 + 88 = 263\)."
        ),
    },
    ("di-tables", 3, 16): {
        "answer": "1256",
        "explanation": (
            r"All scores: Alex \(85+72+90=247\), Blake \(92+88+76=256\), "
            r"Casey \(78+95+82=255\), Dana \(95+80+88=263\), "
            r"Evan \(70+90+75=235\). "
            r"Grand total = \(247+256+255+263+235 = 1{,}256\)."
        ),
    },
    ("di-tables", 3, 17): {
        "answer": "85.0",
        "explanation": (
            r"Student averages: Alex 82.3, Blake 85.3, Casey 85.0, Dana 87.7, Evan 78.3. "
            r"Sorted: 78.3, 82.3, 85.0, 85.3, 87.7. "
            r"The median (3rd value) is \(85.0\)."
        ),
    },

    # ==================================================================
    # DATA SET 6 — Combined Chart  (topic: "di-combined")
    # ==================================================================

    # ── QC (local section 0) ─────────────────────────────────────────
    ("di-combined", 0, 1): {
        "answer": "B",
        "explanation": (
            r"Jan–Mar total = \(500 + 600 + 700 = 1{,}800\) units. "
            r"Apr–Jun total = \(650 + 800 + 750 = 2{,}200\) units. "
            r"Since \(1{,}800 < 2{,}200\), Quantity B is greater."
        ),
    },
    ("di-combined", 0, 2): {
        "answer": "A",
        "explanation": (
            r"Total cost in March = \(700 \times \$10 = \$7{,}000\). "
            r"Total cost in January = \(500 \times \$12 = \$6{,}000\). "
            r"Since \(\$7{,}000 > \$6{,}000\), Quantity A is greater."
        ),
    },
    ("di-combined", 0, 3): {
        "answer": "A",
        "explanation": (
            r"Average cost per unit = \(\frac{12 + 11 + 10 + 10.5 + 9 + 9.5}{6} "
            r"= \frac{62}{6} \approx \$10.33\). "
            r"Since \(\$10.33 > \$10\), Quantity A is greater."
        ),
        "common_mistake": (
            r"Computing a weighted average using units produced. The question asks "
            r"for the simple average of the per-unit costs across the 6 months."
        ),
    },
    ("di-combined", 0, 4): {
        "answer": "A",
        "explanation": (
            r"January production = 500 units, May production = 800 units. "
            r"Percent increase = \(\frac{800 - 500}{500} \times 100\% = "
            r"\frac{300}{500} \times 100\% = 60\%\). "
            r"Since \(60\% > 50\%\), Quantity A is greater."
        ),
    },
    ("di-combined", 0, 5): {
        "answer": "B",
        "explanation": (
            r"Total cost in April = \(650 \times \$10.50 = \$6{,}825\). "
            r"Total cost in June = \(750 \times \$9.50 = \$7{,}125\). "
            r"Since \(\$6{,}825 < \$7{,}125\), Quantity B is greater."
        ),
    },

    # ── MC Single (local section 1) ──────────────────────────────────
    ("di-combined", 1, 6): {
        "answer": r"(D) May",
        "explanation": (
            r"Total costs by month: Jan = \(500 \times 12 = \$6{,}000\), "
            r"Feb = \(600 \times 11 = \$6{,}600\), Mar = \(700 \times 10 = \$7{,}000\), "
            r"Apr = \(650 \times 10.5 = \$6{,}825\), May = \(800 \times 9 = \$7{,}200\), "
            r"Jun = \(750 \times 9.5 = \$7{,}125\). "
            r"May has the highest total cost at \$7,200."
        ),
    },
    ("di-combined", 1, 7): {
        "answer": r"(C) $40,750",
        "explanation": (
            r"Sum of all monthly total costs: "
            r"\(\$6{,}000 + \$6{,}600 + \$7{,}000 + \$6{,}825 + \$7{,}200 + \$7{,}125 "
            r"= \$40{,}750\)."
        ),
    },
    ("di-combined", 1, 8): {
        "answer": r"(B) 25%",
        "explanation": (
            r"Cost per unit: Jan = \$12, May = \$9. "
            r"Percent decrease = \(\frac{12 - 9}{12} \times 100\% = "
            r"\frac{3}{12} \times 100\% = 25\%\)."
        ),
    },
    ("di-combined", 1, 9): {
        "answer": r"(C) 667",
        "explanation": (
            r"Total units = \(500 + 600 + 700 + 650 + 800 + 750 = 4{,}000\). "
            r"Average = \(\frac{4{,}000}{6} \approx 666.7 \approx 667\)."
        ),
    },
    ("di-combined", 1, 10): {
        "answer": r"(D) Apr to May",
        "explanation": (
            r"Month-over-month changes: Jan→Feb: +100, Feb→Mar: +100, "
            r"Mar→Apr: −50, Apr→May: +150, May→Jun: −50. "
            r"The greatest increase is +150 from April to May."
        ),
    },

    # ── MC Multi (local section 2) ───────────────────────────────────
    ("di-combined", 2, 11): {
        "answer": "E, F",
        "explanation": (
            r"Total costs: Jan = \$6,000, Feb = \$6,600, Mar = \$7,000, "
            r"Apr = \$6,825, May = \$7,200, Jun = \$7,125. "
            r"Mar = \$7,000 exactly, which does not exceed \$7,000. "
            r"Only May (\$7,200) and Jun (\$7,125) strictly exceed \$7,000."
        ),
    },
    ("di-combined", 2, 12): {
        "answer": "A, B, D",
        "explanation": (
            r"(A) As production generally increases (500→800), cost per unit decreases "
            r"(\$12→\$9), showing an inverse relationship — True. "
            r"(B) May: 800 units (highest) and \$9/unit (lowest) — True. "
            r"(C) Feb total = \$6,600, Jan total = \$6,000. \$6,600 > \$6,000, "
            r"so Feb is NOT less than Jan — False. "
            r"(D) Range of units = \(800 - 500 = 300\) — True."
        ),
    },

    # ── Numeric Entry (local section 3) ──────────────────────────────
    ("di-combined", 3, 13): {
        "answer": "6600",
        "explanation": (
            r"February: \(600 \text{ units} \times \$11 = \$6{,}600\)."
        ),
    },
    ("di-combined", 3, 14): {
        "answer": "4000",
        "explanation": (
            r"Total units = \(500 + 600 + 700 + 650 + 800 + 750 = 4{,}000\)."
        ),
    },
    ("di-combined", 3, 15): {
        "answer": "1200",
        "explanation": (
            r"May total cost = \(800 \times \$9 = \$7{,}200\). "
            r"Jan total cost = \(500 \times \$12 = \$6{,}000\). "
            r"Difference = \(\$7{,}200 - \$6{,}000 = \$1{,}200\)."
        ),
    },
    ("di-combined", 3, 16): {
        "answer": "60",
        "explanation": (
            r"Percent increase from Jan to May = "
            r"\(\frac{800 - 500}{500} \times 100 = \frac{300}{500} \times 100 = 60\%\). "
            r"Enter 60."
        ),
    },
    ("di-combined", 3, 17): {
        "answer": "10.3",
        "explanation": (
            r"Sum of costs per unit = \(12 + 11 + 10 + 10.5 + 9 + 9.5 = 62\). "
            r"Average = \(\frac{62}{6} \approx 10.333\). Rounded to one decimal place: \(10.3\)."
        ),
    },
}
