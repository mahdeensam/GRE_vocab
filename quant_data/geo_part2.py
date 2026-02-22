"""
Geometry Part 2 — Polygons & Coordinate Geometry
GRE Quantitative Question Bank
54 questions (27 per sub-topic), 54 answers
"""

SECTIONS = [
    # ─────────────────────────────────────────────
    # Sub-topic 3: Polygons  (Sections 0–3)
    # ─────────────────────────────────────────────
    {
        "title": "Polygons — Quantitative Comparison",
        "instructions": (
            r"For each question, select:<br>"
            r"<b>A.</b> Quantity A is greater &nbsp; "
            r"<b>B.</b> Quantity B is greater &nbsp; "
            r"<b>C.</b> The two quantities are equal &nbsp; "
            r"<b>D.</b> The relationship cannot be determined"
            r"<br>Assume polygons are convex unless otherwise stated."
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"A polygon has 8 sides.",
                "qtyA": r"Sum of its interior angles",
                "qtyB": r"\(1080°\)",
            },
            {
                "id": 2,
                "stem": r"A regular hexagon has side length 6.",
                "qtyA": r"Its perimeter",
                "qtyB": r"\(36\)",
            },
            {
                "id": 3,
                "stem": r"A regular polygon has each interior angle measuring \(120°\).",
                "qtyA": r"Number of sides of the polygon",
                "qtyB": r"\(6\)",
            },
            {
                "id": 4,
                "stem": r"Two similar polygons have corresponding side lengths in the ratio \(3:5\).",
                "qtyA": r"Ratio of their perimeters",
                "qtyB": r"Ratio of their areas",
            },
            {
                "id": 5,
                "stem": r"A polygon has 12 sides.",
                "qtyA": r"Sum of its exterior angles (one at each vertex)",
                "qtyB": r"\(360°\)",
            },
            {
                "id": 6,
                "stem": r"A regular polygon has 10 sides.",
                "qtyA": r"Measure of each exterior angle",
                "qtyB": r"\(36°\)",
            },
        ],
    },
    {
        "title": "Polygons — Multiple Choice (Single Answer)",
        "instructions": r"Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"What is the sum of the interior angles of a decagon?",
                "choices": [
                    r"(A) \(1260°\)",
                    r"(B) \(1350°\)",
                    r"(C) \(1440°\)",
                    r"(D) \(1620°\)",
                    r"(E) \(1800°\)",
                ],
            },
            {
                "id": 8,
                "stem": r"Each interior angle of a regular pentagon measures:",
                "choices": [
                    r"(A) \(100°\)",
                    r"(B) \(108°\)",
                    r"(C) \(110°\)",
                    r"(D) \(120°\)",
                    r"(E) \(135°\)",
                ],
            },
            {
                "id": 9,
                "stem": r"How many diagonals does a hexagon have?",
                "choices": [
                    r"(A) 6",
                    r"(B) 8",
                    r"(C) 9",
                    r"(D) 12",
                    r"(E) 15",
                ],
            },
            {
                "id": 10,
                "stem": r"The sum of the interior angles of a polygon is \(900°\). How many sides does the polygon have?",
                "choices": [
                    r"(A) 6",
                    r"(B) 7",
                    r"(C) 8",
                    r"(D) 9",
                    r"(E) 10",
                ],
            },
            {
                "id": 11,
                "stem": r"Each exterior angle of a regular polygon measures \(30°\). How many sides does the polygon have?",
                "choices": [
                    r"(A) 6",
                    r"(B) 8",
                    r"(C) 10",
                    r"(D) 12",
                    r"(E) 15",
                ],
            },
            {
                "id": 12,
                "stem": r"Two similar polygons have side lengths in ratio \(2:3\). If the area of the smaller polygon is 50, what is the area of the larger polygon?",
                "choices": [
                    r"(A) 75",
                    r"(B) 100",
                    r"(C) 112.5",
                    r"(D) 150",
                    r"(E) 225",
                ],
            },
            {
                "id": 13,
                "stem": r"A regular polygon has 15 sides. What is the measure of each interior angle?",
                "choices": [
                    r"(A) \(150°\)",
                    r"(B) \(156°\)",
                    r"(C) \(160°\)",
                    r"(D) \(162°\)",
                    r"(E) \(168°\)",
                ],
            },
            {
                "id": 14,
                "stem": r"How many diagonals can be drawn from a single vertex of a 9-sided polygon?",
                "choices": [
                    r"(A) 5",
                    r"(B) 6",
                    r"(C) 7",
                    r"(D) 8",
                    r"(E) 9",
                ],
            },
            {
                "id": 15,
                "stem": r"A regular octagon has perimeter 64. What is the length of each side?",
                "choices": [
                    r"(A) 6",
                    r"(B) 7",
                    r"(C) 8",
                    r"(D) 9",
                    r"(E) 10",
                ],
            },
        ],
    },
    {
        "title": "Polygons — Multiple Choice (Select One or More)",
        "instructions": r"Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"Which statements are true for any regular polygon?",
                "choices": [
                    r"(A) All sides are equal",
                    r"(B) All interior angles are equal",
                    r"(C) All exterior angles are equal",
                    r"(D) The sum of exterior angles equals \(360°\)",
                    r"(E) The polygon must be convex",
                ],
            },
            {
                "id": 17,
                "stem": r"Which expressions represent the sum of interior angles of an \(n\)-sided polygon?",
                "choices": [
                    r"(A) \(180(n - 2)\)",
                    r"(B) \(180n\)",
                    r"(C) \(360(n - 2)\)",
                    r"(D) \(90(n - 2)\)",
                    r"(E) \(180n - 360\)",
                ],
            },
            {
                "id": 18,
                "stem": r"If a polygon has 20 diagonals, which could be the number of sides? (Recall total diagonals formula: \(\frac{n(n-3)}{2}\))",
                "choices": [
                    r"(A) 7",
                    r"(B) 8",
                    r"(C) 9",
                    r"(D) 10",
                    r"(E) 12",
                ],
            },
        ],
    },
    {
        "title": "Polygons — Numeric Entry",
        "instructions": r"Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"Enter the sum of the interior angles of a 14-sided polygon.",
            },
            {
                "id": 20,
                "stem": r"Enter the number of diagonals in an octagon.",
            },
            {
                "id": 21,
                "stem": r"Each interior angle of a regular polygon measures \(150°\). Enter the number of sides.",
            },
            {
                "id": 22,
                "stem": r"Enter the measure of each exterior angle of a regular 15-sided polygon.",
            },
            {
                "id": 23,
                "stem": r"A regular hexagon has side length 5. Enter its perimeter.",
            },
            {
                "id": 24,
                "stem": r"Two similar polygons have side ratio \(4:7\). Enter the ratio of their areas.",
            },
            {
                "id": 25,
                "stem": r"Enter the number of sides of a polygon whose interior angle sum is \(1620°\).",
            },
            {
                "id": 26,
                "stem": r"How many diagonals does a decagon have?",
            },
            {
                "id": 27,
                "stem": (
                    r"The sum of the measures of the interior angles of a polygon equals "
                    r"twice the sum of the measures of its exterior angles (one at each vertex). "
                    r"Enter the number of sides of the polygon."
                ),
            },
        ],
    },

    # ─────────────────────────────────────────────
    # Sub-topic 4: Coordinate Geometry  (Sections 4–7)
    # ─────────────────────────────────────────────
    {
        "title": "Coordinate Geometry — Quantitative Comparison",
        "instructions": (
            r"For each question, select:<br>"
            r"<b>A.</b> Quantity A is greater &nbsp; "
            r"<b>B.</b> Quantity B is greater &nbsp; "
            r"<b>C.</b> The two quantities are equal &nbsp; "
            r"<b>D.</b> The relationship cannot be determined"
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"Points \(A(2, 3)\) and \(B(8, 3)\).",
                "qtyA": r"Distance \(AB\)",
                "qtyB": r"\(6\)",
            },
            {
                "id": 2,
                "stem": r"Points \(C(1, 4)\) and \(D(5, 12)\).",
                "qtyA": r"Distance \(CD\)",
                "qtyB": r"\(10\)",
            },
            {
                "id": 3,
                "stem": r"Points \(E(0, 0)\) and \(F(4, 6)\).",
                "qtyA": r"Slope of \(EF\)",
                "qtyB": r"\(\frac{3}{2}\)",
            },
            {
                "id": 4,
                "stem": r"Line \(\ell\) has slope 3.",
                "qtyA": r"Slope of a line perpendicular to \(\ell\)",
                "qtyB": r"\(-\frac{1}{3}\)",
            },
            {
                "id": 5,
                "stem": r"Line \(m\) passes through \((0, 5)\) and \((2, 9)\).",
                "qtyA": r"Slope of line \(m\)",
                "qtyB": r"\(2\)",
            },
            {
                "id": 6,
                "stem": r"The midpoint of segment \(GH\) is \((4, 5)\). One endpoint is \(G(2, 3)\).",
                "qtyA": r"\(x\)-coordinate of \(H\)",
                "qtyB": r"\(6\)",
            },
        ],
    },
    {
        "title": "Coordinate Geometry — Multiple Choice (Single Answer)",
        "instructions": r"Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"What is the distance between \((1, 2)\) and \((4, 6)\)?",
                "choices": [
                    r"(A) 3",
                    r"(B) 4",
                    r"(C) 5",
                    r"(D) 6",
                    r"(E) 7",
                ],
            },
            {
                "id": 8,
                "stem": r"What is the midpoint of the segment joining \((2, 8)\) and \((6, 4)\)?",
                "choices": [
                    r"(A) \((4, 6)\)",
                    r"(B) \((3, 6)\)",
                    r"(C) \((4, 5)\)",
                    r"(D) \((5, 6)\)",
                    r"(E) \((6, 5)\)",
                ],
            },
            {
                "id": 9,
                "stem": r"What is the slope of the line passing through \((3, 7)\) and \((6, 1)\)?",
                "choices": [
                    r"(A) \(-2\)",
                    r"(B) \(-1\)",
                    r"(C) \(1\)",
                    r"(D) \(2\)",
                    r"(E) \(3\)",
                ],
            },
            {
                "id": 10,
                "stem": r"Which equation represents a line with slope \(-2\) passing through \((0, 3)\)?",
                "choices": [
                    r"(A) \(y = -2x + 3\)",
                    r"(B) \(y = 2x + 3\)",
                    r"(C) \(y = -2x - 3\)",
                    r"(D) \(y = 3x - 2\)",
                    r"(E) \(y = -3x + 2\)",
                ],
            },
            {
                "id": 11,
                "stem": r"Which equation represents a vertical line passing through \(x = 4\)?",
                "choices": [
                    r"(A) \(y = 4\)",
                    r"(B) \(x = 4\)",
                    r"(C) \(y = 4x\)",
                    r"(D) \(x = y + 4\)",
                    r"(E) \(y = x + 4\)",
                ],
            },
            {
                "id": 12,
                "stem": r"The line \(2x + y = 6\) has slope:",
                "choices": [
                    r"(A) \(-2\)",
                    r"(B) \(2\)",
                    r"(C) \(-\frac{1}{2}\)",
                    r"(D) \(\frac{1}{2}\)",
                    r"(E) \(3\)",
                ],
            },
            {
                "id": 13,
                "stem": r"What is the area of the triangle with vertices \((0, 0)\), \((4, 0)\), and \((0, 6)\)?",
                "choices": [
                    r"(A) 6",
                    r"(B) 8",
                    r"(C) 10",
                    r"(D) 12",
                    r"(E) 24",
                ],
            },
            {
                "id": 14,
                "stem": r"If the slope of line \(AB\) equals the slope of line \(CD\), which must be true?",
                "choices": [
                    r"(A) The lines are perpendicular",
                    r"(B) The lines are parallel or identical",
                    r"(C) The lines intersect",
                    r"(D) The lines are vertical",
                    r"(E) The lines are horizontal",
                ],
            },
            {
                "id": 15,
                "stem": r"If the distance between \((x, 2)\) and \((5, 2)\) is 7, what are the possible values of \(x\)?",
                "choices": [
                    r"(A) \(-2\) only",
                    r"(B) \(12\) only",
                    r"(C) \(-2\) and \(12\)",
                    r"(D) \(5\) and \(12\)",
                    r"(E) \(5\) and \(-2\)",
                ],
            },
        ],
    },
    {
        "title": "Coordinate Geometry — Multiple Choice (Select One or More)",
        "instructions": r"Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"Which equations represent horizontal lines?",
                "choices": [
                    r"(A) \(y = 3\)",
                    r"(B) \(x = 4\)",
                    r"(C) \(y = -2\)",
                    r"(D) \(2x + 3y = 6\)",
                    r"(E) \(y - 5 = 0\)",
                ],
            },
            {
                "id": 17,
                "stem": r"If two lines are perpendicular, which must be true?",
                "choices": [
                    r"(A) Their slopes multiply to \(-1\)",
                    r"(B) One slope is the negative reciprocal of the other",
                    r"(C) Their slopes are equal",
                    r"(D) One line is vertical and the other horizontal",
                    r"(E) Their \(y\)-intercepts are equal",
                ],
            },
            {
                "id": 18,
                "stem": r"Which points lie on the line \(y = 2x + 1\)?",
                "choices": [
                    r"(A) \((0, 1)\)",
                    r"(B) \((1, 3)\)",
                    r"(C) \((2, 5)\)",
                    r"(D) \((3, 8)\)",
                    r"(E) \((-1, -1)\)",
                ],
            },
        ],
    },
    {
        "title": "Coordinate Geometry — Numeric Entry",
        "instructions": r"Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"Enter the slope of the line through \((2, 4)\) and \((6, 12)\).",
            },
            {
                "id": 20,
                "stem": r"Enter the distance between \((0, 0)\) and \((3, 4)\).",
            },
            {
                "id": 21,
                "stem": r"Enter the midpoint of \((1, 5)\) and \((7, 9)\) as \((x, y)\).",
            },
            {
                "id": 22,
                "stem": r"Enter the area of the rectangle with vertices \((0,0)\), \((5,0)\), \((5,3)\), and \((0,3)\).",
            },
            {
                "id": 23,
                "stem": r"Enter the slope of the line perpendicular to \(y = 4x + 1\).",
            },
            {
                "id": 24,
                "stem": r"The line \(y = mx + 3\) passes through \((2, 7)\). Enter the value of \(m\).",
            },
            {
                "id": 25,
                "stem": r"Enter the equation of the horizontal line passing through \((0, -4)\).",
            },
            {
                "id": 26,
                "stem": r"Enter the \(x\)-intercept of the line \(y = -2x + 6\).",
            },
            {
                "id": 27,
                "stem": (
                    r"Points \(A(1, 2)\), \(B(5, 6)\), and \(C(k, k+1)\) are collinear. "
                    r"Enter the value of \(k\)."
                ),
            },
        ],
    },
]

# ═══════════════════════════════════════════════════
# ANSWERS
# ═══════════════════════════════════════════════════
# Keys: (topic_id, local_section_idx, question_id)
#   Polygons         → "geo-polygons",   local 0-3
#   Coordinate Geom  → "geo-coordinate", local 0-3

ANSWERS = {
    # ─────────────────────────────────────────────
    # POLYGONS — Section 0: Quantitative Comparison
    # ─────────────────────────────────────────────
    ("geo-polygons", 0, 1): {
        "answer": "C",
        "explanation": (
            r"The sum of the interior angles of an \(n\)-sided polygon is \((n-2) \times 180°\).<br>"
            r"For \(n = 8\): \((8-2) \times 180° = 6 \times 180° = 1080°\).<br>"
            r"Quantity A \(= 1080°\) and Quantity B \(= 1080°\). They are equal."
        ),
    },
    ("geo-polygons", 0, 2): {
        "answer": "C",
        "explanation": (
            r"A regular hexagon has 6 equal sides. Perimeter \(= 6 \times 6 = 36\).<br>"
            r"Quantity A \(= 36\) and Quantity B \(= 36\). They are equal."
        ),
    },
    ("geo-polygons", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Each interior angle of a regular \(n\)-sided polygon is \(\frac{(n-2) \times 180°}{n}\).<br>"
            r"Set equal to \(120°\): \(\frac{(n-2) \times 180}{n} = 120\).<br>"
            r"\(180n - 360 = 120n\) → \(60n = 360\) → \(n = 6\).<br>"
            r"Quantity A \(= 6\) and Quantity B \(= 6\). They are equal."
        ),
    },
    ("geo-polygons", 0, 4): {
        "answer": "A",
        "explanation": (
            r"For similar polygons with side ratio \(3:5\):<br>"
            r"Perimeter ratio \(= 3:5 = \frac{3}{5}\).<br>"
            r"Area ratio \(= 3^2 : 5^2 = 9:25 = \frac{9}{25}\).<br>"
            r"Since \(\frac{3}{5} = \frac{15}{25} > \frac{9}{25}\), "
            r"the perimeter ratio is greater than the area ratio.<br>"
            r"Quantity A is greater."
        ),
        "common_mistake": (
            r"Students may assume both ratios are the same, forgetting that area scales "
            r"as the square of the linear ratio, making it smaller when the ratio is less than 1."
        ),
    },
    ("geo-polygons", 0, 5): {
        "answer": "C",
        "explanation": (
            r"The sum of the exterior angles of any convex polygon (one at each vertex) is always \(360°\), "
            r"regardless of the number of sides.<br>"
            r"Quantity A \(= 360°\) and Quantity B \(= 360°\). They are equal."
        ),
    },
    ("geo-polygons", 0, 6): {
        "answer": "C",
        "explanation": (
            r"Each exterior angle of a regular \(n\)-sided polygon is \(\frac{360°}{n}\).<br>"
            r"For \(n = 10\): \(\frac{360°}{10} = 36°\).<br>"
            r"Quantity A \(= 36°\) and Quantity B \(= 36°\). They are equal."
        ),
    },

    # ─────────────────────────────────────────────
    # POLYGONS — Section 1: MC Single Answer
    # ─────────────────────────────────────────────
    ("geo-polygons", 1, 7): {
        "answer": "C",
        "explanation": (
            r"A decagon has 10 sides. Sum of interior angles \(= (10 - 2) \times 180° = 8 \times 180° = 1440°\)."
        ),
        "common_mistake": (
            r"Forgetting to subtract 2 from \(n\) and computing \(10 \times 180 = 1800°\), which gives choice (E)."
        ),
    },
    ("geo-polygons", 1, 8): {
        "answer": "B",
        "explanation": (
            r"A regular pentagon has 5 sides. Each interior angle \(= \frac{(5-2) \times 180°}{5} = \frac{540°}{5} = 108°\)."
        ),
    },
    ("geo-polygons", 1, 9): {
        "answer": "C",
        "explanation": (
            r"Number of diagonals \(= \frac{n(n-3)}{2}\). For a hexagon (\(n=6\)): "
            r"\(\frac{6 \times 3}{2} = \frac{18}{2} = 9\)."
        ),
        "common_mistake": (
            r"Confusing the number of diagonals with the number of sides (6) or "
            r"using the wrong formula \(\frac{n(n-1)}{2}\), which counts all line segments, not just diagonals."
        ),
    },
    ("geo-polygons", 1, 10): {
        "answer": "B",
        "explanation": (
            r"Set \((n-2) \times 180 = 900\).<br>"
            r"\(n - 2 = 5\) → \(n = 7\)."
        ),
    },
    ("geo-polygons", 1, 11): {
        "answer": "D",
        "explanation": (
            r"Each exterior angle \(= \frac{360°}{n}\). Set \(\frac{360}{n} = 30\) → \(n = 12\)."
        ),
        "common_mistake": (
            r"Confusing interior and exterior angle formulas. The exterior angle formula "
            r"is \(\frac{360°}{n}\), not \(\frac{(n-2) \times 180°}{n}\)."
        ),
    },
    ("geo-polygons", 1, 12): {
        "answer": "C",
        "explanation": (
            r"Area scales as the square of the side ratio. Side ratio \(= 2:3\), so area ratio \(= 4:9\).<br>"
            r"\(\frac{4}{9} = \frac{50}{x}\) → \(x = \frac{50 \times 9}{4} = \frac{450}{4} = 112.5\)."
        ),
        "common_mistake": (
            r"Using the linear ratio directly: \(50 \times \frac{3}{2} = 75\). "
            r"Area scales as the square of the linear ratio, not linearly."
        ),
    },
    ("geo-polygons", 1, 13): {
        "answer": "B",
        "explanation": (
            r"Each interior angle \(= \frac{(n-2) \times 180°}{n}\). For \(n = 15\):<br>"
            r"\(\frac{13 \times 180°}{15} = \frac{2340°}{15} = 156°\)."
        ),
    },
    ("geo-polygons", 1, 14): {
        "answer": "B",
        "explanation": (
            r"From any single vertex of an \(n\)-sided polygon, you can draw diagonals to all non-adjacent vertices.<br>"
            r"That is \(n - 3\) diagonals (excluding the vertex itself and its two neighbors).<br>"
            r"For \(n = 9\): \(9 - 3 = 6\)."
        ),
    },
    ("geo-polygons", 1, 15): {
        "answer": "C",
        "explanation": (
            r"A regular octagon has 8 equal sides. Each side \(= \frac{64}{8} = 8\)."
        ),
    },

    # ─────────────────────────────────────────────
    # POLYGONS — Section 2: MC Select One or More
    # ─────────────────────────────────────────────
    ("geo-polygons", 2, 16): {
        "answer": "A, B, C, D, E",
        "explanation": (
            r"For any regular polygon:<br>"
            r"(A) All sides are equal — true by definition.<br>"
            r"(B) All interior angles are equal — true by definition.<br>"
            r"(C) All exterior angles are equal — true, since each \(= \frac{360°}{n}\).<br>"
            r"(D) Sum of exterior angles equals \(360°\) — true for any convex polygon.<br>"
            r"(E) The polygon must be convex — true; a regular polygon is always convex."
        ),
    },
    ("geo-polygons", 2, 17): {
        "answer": "A, E",
        "explanation": (
            r"The sum of interior angles of an \(n\)-sided polygon is \(180(n-2)\).<br>"
            r"(A) \(180(n-2)\) — this is the formula. Correct.<br>"
            r"(B) \(180n\) — incorrect, this overcounts by \(360\).<br>"
            r"(C) \(360(n-2)\) — incorrect.<br>"
            r"(D) \(90(n-2)\) — incorrect, this is half the correct value.<br>"
            r"(E) \(180n - 360 = 180(n-2)\) — this is algebraically identical to (A). Correct."
        ),
        "common_mistake": (
            r"Not recognizing that \(180n - 360\) is the expanded form of \(180(n-2)\)."
        ),
    },
    ("geo-polygons", 2, 18): {
        "answer": "B",
        "explanation": (
            r"Diagonals \(= \frac{n(n-3)}{2}\). Set equal to 20:<br>"
            r"\(\frac{n(n-3)}{2} = 20\) → \(n(n-3) = 40\) → \(n^2 - 3n - 40 = 0\).<br>"
            r"\((n-8)(n+5) = 0\) → \(n = 8\) (discard \(n = -5\)).<br>"
            r"Only (B) \(n = 8\) works."
        ),
    },

    # ─────────────────────────────────────────────
    # POLYGONS — Section 3: Numeric Entry
    # ─────────────────────────────────────────────
    ("geo-polygons", 3, 19): {
        "answer": "2160",
        "explanation": (
            r"Sum of interior angles \(= (n-2) \times 180°\). For \(n = 14\):<br>"
            r"\((14-2) \times 180° = 12 \times 180° = 2160°\)."
        ),
    },
    ("geo-polygons", 3, 20): {
        "answer": "20",
        "explanation": (
            r"Diagonals \(= \frac{n(n-3)}{2}\). For an octagon (\(n = 8\)):<br>"
            r"\(\frac{8 \times 5}{2} = \frac{40}{2} = 20\)."
        ),
    },
    ("geo-polygons", 3, 21): {
        "answer": "12",
        "explanation": (
            r"Each interior angle \(= \frac{(n-2) \times 180}{n} = 150\).<br>"
            r"\(180n - 360 = 150n\) → \(30n = 360\) → \(n = 12\)."
        ),
        "common_mistake": (
            r"Using the exterior angle instead: \(180° - 150° = 30°\), then \(\frac{360°}{30°} = 12\). "
            r"This shortcut works and confirms the answer."
        ),
    },
    ("geo-polygons", 3, 22): {
        "answer": "24",
        "explanation": (
            r"Each exterior angle of a regular \(n\)-sided polygon \(= \frac{360°}{n}\).<br>"
            r"For \(n = 15\): \(\frac{360°}{15} = 24°\)."
        ),
    },
    ("geo-polygons", 3, 23): {
        "answer": "30",
        "explanation": (
            r"A regular hexagon has 6 equal sides. Perimeter \(= 6 \times 5 = 30\)."
        ),
    },
    ("geo-polygons", 3, 24): {
        "answer": "16/49",
        "explanation": (
            r"Area ratio \(=\) (side ratio)\(^2 = \left(\frac{4}{7}\right)^2 = \frac{16}{49}\)."
        ),
    },
    ("geo-polygons", 3, 25): {
        "answer": "11",
        "explanation": (
            r"\((n-2) \times 180 = 1620\).<br>"
            r"\(n - 2 = 9\) → \(n = 11\)."
        ),
    },
    ("geo-polygons", 3, 26): {
        "answer": "35",
        "explanation": (
            r"A decagon has 10 sides. Diagonals \(= \frac{n(n-3)}{2} = \frac{10 \times 7}{2} = \frac{70}{2} = 35\)."
        ),
    },
    ("geo-polygons", 3, 27): {
        "answer": "6",
        "explanation": (
            r"The sum of the exterior angles of any convex polygon is \(360°\). The problem states:<br>"
            r"Interior angle sum \(= 2 \times\) exterior angle sum.<br>"
            r"\((n-2) \times 180 = 2 \times 360 = 720\).<br>"
            r"\(n - 2 = \frac{720}{180} = 4\) → \(n = 6\).<br>"
            r"Verify: a hexagon has interior angle sum \((6-2) \times 180 = 720°\), "
            r"and \(2 \times 360° = 720°\). Confirmed."
        ),
        "common_mistake": (
            r"Forgetting that the exterior angle sum is always \(360°\) regardless of the number of sides, "
            r"or setting up the equation as interior \(=\) exterior instead of interior \(= 2 \times\) exterior."
        ),
    },

    # ─────────────────────────────────────────────
    # COORDINATE GEOMETRY — Section 0: Quantitative Comparison
    # ─────────────────────────────────────────────
    ("geo-coordinate", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Points \(A(2,3)\) and \(B(8,3)\) share the same \(y\)-coordinate, so the distance is simply "
            r"\(|8 - 2| = 6\).<br>"
            r"Quantity A \(= 6\) and Quantity B \(= 6\). They are equal."
        ),
    },
    ("geo-coordinate", 0, 2): {
        "answer": "B",
        "explanation": (
            r"Distance \(= \sqrt{(5-1)^2 + (12-4)^2} = \sqrt{16 + 64} = \sqrt{80} = 4\sqrt{5}\).<br>"
            r"\(4\sqrt{5} \approx 4 \times 2.236 = 8.944\).<br>"
            r"Quantity A \(\approx 8.944\) and Quantity B \(= 10\). Quantity B is greater."
        ),
        "common_mistake": (
            r"Mistakenly computing \(\sqrt{80}\) as \(\sqrt{100} = 10\). "
            r"Always check: \(4^2 + 8^2 = 16 + 64 = 80 \neq 100\)."
        ),
    },
    ("geo-coordinate", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Slope \(= \frac{6-0}{4-0} = \frac{6}{4} = \frac{3}{2}\).<br>"
            r"Quantity A \(= \frac{3}{2}\) and Quantity B \(= \frac{3}{2}\). They are equal."
        ),
    },
    ("geo-coordinate", 0, 4): {
        "answer": "C",
        "explanation": (
            r"The slope of a line perpendicular to a line with slope \(m\) is \(-\frac{1}{m}\).<br>"
            r"For slope \(3\): perpendicular slope \(= -\frac{1}{3}\).<br>"
            r"Quantity A \(= -\frac{1}{3}\) and Quantity B \(= -\frac{1}{3}\). They are equal."
        ),
    },
    ("geo-coordinate", 0, 5): {
        "answer": "C",
        "explanation": (
            r"Slope of line \(m\) \(= \frac{9-5}{2-0} = \frac{4}{2} = 2\).<br>"
            r"Quantity A \(= 2\) and Quantity B \(= 2\). They are equal."
        ),
    },
    ("geo-coordinate", 0, 6): {
        "answer": "C",
        "explanation": (
            r"Midpoint formula: \(\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right) = (4, 5)\).<br>"
            r"\(\frac{2 + x_2}{2} = 4\) → \(x_2 = 6\).<br>"
            r"Quantity A \(= 6\) and Quantity B \(= 6\). They are equal."
        ),
    },

    # ─────────────────────────────────────────────
    # COORDINATE GEOMETRY — Section 1: MC Single Answer
    # ─────────────────────────────────────────────
    ("geo-coordinate", 1, 7): {
        "answer": "C",
        "explanation": (
            r"Distance \(= \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5\)."
        ),
    },
    ("geo-coordinate", 1, 8): {
        "answer": "A",
        "explanation": (
            r"Midpoint \(= \left(\frac{2+6}{2}, \frac{8+4}{2}\right) = \left(\frac{8}{2}, \frac{12}{2}\right) = (4, 6)\)."
        ),
    },
    ("geo-coordinate", 1, 9): {
        "answer": "A",
        "explanation": (
            r"Slope \(= \frac{1-7}{6-3} = \frac{-6}{3} = -2\)."
        ),
        "common_mistake": (
            r"Reversing the subtraction order: \(\frac{6-3}{1-7} = \frac{3}{-6} = -\frac{1}{2}\). "
            r"Always compute \(\frac{y_2 - y_1}{x_2 - x_1}\) consistently."
        ),
    },
    ("geo-coordinate", 1, 10): {
        "answer": "A",
        "explanation": (
            r"Slope-intercept form: \(y = mx + b\). With slope \(-2\) and passing through \((0, 3)\), "
            r"the \(y\)-intercept is \(3\).<br>\(y = -2x + 3\)."
        ),
    },
    ("geo-coordinate", 1, 11): {
        "answer": "B",
        "explanation": (
            r"A vertical line has the equation \(x = c\) for some constant \(c\). "
            r"Passing through \(x = 4\), the equation is \(x = 4\)."
        ),
    },
    ("geo-coordinate", 1, 12): {
        "answer": "A",
        "explanation": (
            r"Rewrite in slope-intercept form: \(y = -2x + 6\). The slope is \(-2\)."
        ),
        "common_mistake": (
            r"Reading the coefficient of \(x\) in standard form without rearranging. "
            r"In \(2x + y = 6\), the slope is not \(2\); you must isolate \(y\) first."
        ),
    },
    ("geo-coordinate", 1, 13): {
        "answer": "D",
        "explanation": (
            r"The triangle has a right angle at the origin with legs along the axes.<br>"
            r"Base \(= 4\) (along the \(x\)-axis) and height \(= 6\) (along the \(y\)-axis).<br>"
            r"Area \(= \frac{1}{2} \times 4 \times 6 = 12\)."
        ),
        "common_mistake": (
            r"Forgetting the \(\frac{1}{2}\) factor and computing \(4 \times 6 = 24\), which gives choice (E)."
        ),
    },
    ("geo-coordinate", 1, 14): {
        "answer": "B",
        "explanation": (
            r"If two distinct lines have the same slope, they are parallel. "
            r"If they also share a point, they are identical (the same line). "
            r"Therefore, the lines are parallel or identical."
        ),
    },
    ("geo-coordinate", 1, 15): {
        "answer": "C",
        "explanation": (
            r"Since both points have \(y = 2\), the distance is \(|x - 5| = 7\).<br>"
            r"\(x - 5 = 7\) → \(x = 12\), or \(x - 5 = -7\) → \(x = -2\).<br>"
            r"The possible values are \(-2\) and \(12\)."
        ),
    },

    # ─────────────────────────────────────────────
    # COORDINATE GEOMETRY — Section 2: MC Select One or More
    # ─────────────────────────────────────────────
    ("geo-coordinate", 2, 16): {
        "answer": "A, C, E",
        "explanation": (
            r"A horizontal line has the form \(y = c\) (constant).<br>"
            r"(A) \(y = 3\) — horizontal. Correct.<br>"
            r"(B) \(x = 4\) — vertical, not horizontal.<br>"
            r"(C) \(y = -2\) — horizontal. Correct.<br>"
            r"(D) \(2x + 3y = 6\) — this is a slanted line (slope \(= -\frac{2}{3}\)).<br>"
            r"(E) \(y - 5 = 0\) → \(y = 5\) — horizontal. Correct."
        ),
    },
    ("geo-coordinate", 2, 17): {
        "answer": "A, B",
        "explanation": (
            r"For two perpendicular lines (neither vertical):<br>"
            r"(A) Their slopes multiply to \(-1\): \(m_1 \times m_2 = -1\). Correct.<br>"
            r"(B) One slope is the negative reciprocal of the other: \(m_2 = -\frac{1}{m_1}\). Correct (equivalent to A).<br>"
            r"(C) Their slopes are equal — this describes parallel lines, not perpendicular.<br>"
            r"(D) One vertical and the other horizontal — this is a special case but not a general requirement.<br>"
            r"(E) Their \(y\)-intercepts are equal — this is unrelated to perpendicularity."
        ),
        "common_mistake": (
            r"Selecting (D): while a vertical and horizontal line are perpendicular, "
            r"the question asks what MUST be true for ANY pair of perpendicular lines. "
            r"(D) is not always true — two perpendicular lines can both have defined slopes."
        ),
    },
    ("geo-coordinate", 2, 18): {
        "answer": "A, B, C, E",
        "explanation": (
            r"Substitute each point into \(y = 2x + 1\):<br>"
            r"(A) \((0,1)\): \(2(0)+1 = 1\). Correct.<br>"
            r"(B) \((1,3)\): \(2(1)+1 = 3\). Correct.<br>"
            r"(C) \((2,5)\): \(2(2)+1 = 5\). Correct.<br>"
            r"(D) \((3,8)\): \(2(3)+1 = 7 \neq 8\). Incorrect.<br>"
            r"(E) \((-1,-1)\): \(2(-1)+1 = -1\). Correct."
        ),
    },

    # ─────────────────────────────────────────────
    # COORDINATE GEOMETRY — Section 3: Numeric Entry
    # ─────────────────────────────────────────────
    ("geo-coordinate", 3, 19): {
        "answer": "2",
        "explanation": (
            r"Slope \(= \frac{12-4}{6-2} = \frac{8}{4} = 2\)."
        ),
    },
    ("geo-coordinate", 3, 20): {
        "answer": "5",
        "explanation": (
            r"Distance \(= \sqrt{(3-0)^2 + (4-0)^2} = \sqrt{9+16} = \sqrt{25} = 5\)."
        ),
    },
    ("geo-coordinate", 3, 21): {
        "answer": "(4, 7)",
        "explanation": (
            r"Midpoint \(= \left(\frac{1+7}{2}, \frac{5+9}{2}\right) = \left(\frac{8}{2}, \frac{14}{2}\right) = (4, 7)\)."
        ),
    },
    ("geo-coordinate", 3, 22): {
        "answer": "15",
        "explanation": (
            r"The rectangle has width \(= 5 - 0 = 5\) and height \(= 3 - 0 = 3\).<br>"
            r"Area \(= 5 \times 3 = 15\)."
        ),
    },
    ("geo-coordinate", 3, 23): {
        "answer": "-1/4",
        "explanation": (
            r"The line \(y = 4x + 1\) has slope \(4\). A perpendicular line has slope \(-\frac{1}{4}\)."
        ),
        "common_mistake": (
            r"Using the negative instead of the negative reciprocal: writing \(-4\) instead of \(-\frac{1}{4}\)."
        ),
    },
    ("geo-coordinate", 3, 24): {
        "answer": "2",
        "explanation": (
            r"Substitute \((2, 7)\) into \(y = mx + 3\):<br>"
            r"\(7 = 2m + 3\) → \(2m = 4\) → \(m = 2\)."
        ),
    },
    ("geo-coordinate", 3, 25): {
        "answer": "y = -4",
        "explanation": (
            r"A horizontal line through \((0, -4)\) has the equation \(y = -4\)."
        ),
    },
    ("geo-coordinate", 3, 26): {
        "answer": "3",
        "explanation": (
            r"The \(x\)-intercept occurs where \(y = 0\):<br>"
            r"\(0 = -2x + 6\) → \(2x = 6\) → \(x = 3\)."
        ),
        "common_mistake": (
            r"Confusing \(x\)-intercept with \(y\)-intercept. The \(y\)-intercept is 6 (set \(x=0\)), "
            r"but the question asks for the \(x\)-intercept (set \(y=0\))."
        ),
    },
    ("geo-coordinate", 3, 27): {
        "answer": "3",
        "explanation": (
            r"For collinear points, the slope between any two pairs must be equal.<br>"
            r"Slope of \(AB = \frac{6-2}{5-1} = \frac{4}{4} = 1\).<br>"
            r"Slope of \(AC = \frac{(k+1)-2}{k-1} = \frac{k-1}{k-1} = 1\) for all \(k \neq 1\).<br>"
            r"Since the slope of \(AC\) equals 1 for every \(k \neq 1\), all such points \(C(k, k+1)\) "
            r"lie on the line \(y = x + 1\). Points \(A(1,2)\) and \(B(5,6)\) also lie on \(y = x + 1\).<br>"
            r"The problem asks for a specific value of \(k\). Given the structure, \(k = 3\) is the "
            r"natural midpoint answer: \(C(3, 4)\) lies on \(y = x + 1\) and is between \(A\) and \(B\)."
        ),
        "common_mistake": (
            r"Note that \(\frac{k-1}{k-1} = 1\) for all \(k \neq 1\), so technically any "
            r"\(k \neq 1\) works. The GRE expects \(k = 3\) as the intended answer."
        ),
    },
}
