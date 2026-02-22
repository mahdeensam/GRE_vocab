"""
Geometry Part 3 — Slopes & Distance + 3D Solids
54 questions (27 per sub-topic), fully corrected from OCR source.
"""

SECTIONS = [
    # ------------------------------------------------------------------ #
    #  Sub-topic 5: Slopes & Distance  (sections 0-3)
    # ------------------------------------------------------------------ #
    {
        "title": "Slopes & Distance \u2014 Quantitative Comparison",
        "topic_id": "geo-slopes-distance",
        "instructions": (
            "For each question, select:<br>"
            "<b>A.</b> Quantity A is greater &nbsp; "
            "<b>B.</b> Quantity B is greater &nbsp; "
            "<b>C.</b> The two quantities are equal &nbsp; "
            "<b>D.</b> The relationship cannot be determined"
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"Points \(A(1, 3)\) and \(B(5, 11)\)",
                "qtyA": r"Slope of \(\overline{AB}\)",
                "qtyB": r"\(2\)",
            },
            {
                "id": 2,
                "stem": r"Points \(C(-2, 4)\) and \(D(4, 4)\)",
                "qtyA": r"Distance \(CD\)",
                "qtyB": r"\(6\)",
            },
            {
                "id": 3,
                "stem": r"Line \(\ell\) passes through \((2, 5)\) and \((6, 1)\).",
                "qtyA": r"Slope of line \(\ell\)",
                "qtyB": r"\(-1\)",
            },
            {
                "id": 4,
                "stem": r"Points \(E(0, 0)\) and \(F(3, 4)\)",
                "qtyA": r"Distance \(EF\)",
                "qtyB": r"\(7\)",
            },
            {
                "id": 5,
                "stem": r"Line \(m\) has slope \(-3\).",
                "qtyA": r"Slope of a line perpendicular to \(m\)",
                "qtyB": r"\(\frac{1}{3}\)",
            },
            {
                "id": 6,
                "stem": r"Points \(G(1, 2)\), \(H(4, 8)\), and \(J(7, 14)\)",
                "qtyA": r"Slope \(\overline{GH}\)",
                "qtyB": r"Slope \(\overline{HJ}\)",
            },
        ],
    },
    {
        "title": "Slopes & Distance \u2014 Multiple Choice (Single Answer)",
        "topic_id": "geo-slopes-distance",
        "instructions": "Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"What is the slope of the line passing through \((4, -1)\) and \((2, 3)\)?",
                "choices": [
                    r"(A) \(-2\)",
                    r"(B) \(-1\)",
                    r"(C) \(1\)",
                    r"(D) \(2\)",
                    r"(E) \(3\)",
                ],
            },
            {
                "id": 8,
                "stem": r"What is the distance between \((-1, 2)\) and \((2, 6)\)?",
                "choices": [
                    r"(A) \(3\)",
                    r"(B) \(4\)",
                    r"(C) \(5\)",
                    r"(D) \(6\)",
                    r"(E) \(7\)",
                ],
            },
            {
                "id": 9,
                "stem": r"Which equation represents a line parallel to \(3x - 2y = 6\)?",
                "choices": [
                    r"(A) \(3x - 2y = 10\)",
                    r"(B) \(2x - 3y = 5\)",
                    r"(C) \(3x + 2y = 6\)",
                    r"(D) \(y = 3x - 2\)",
                    r"(E) \(y = -3x + 2\)",
                ],
            },
            {
                "id": 10,
                "stem": r"Which equation represents a line perpendicular to \(y = 2x + 1\)?",
                "choices": [
                    r"(A) \(y = -2x + 1\)",
                    r"(B) \(y = \frac{1}{2}x + 3\)",
                    r"(C) \(y = -\frac{1}{2}x + 4\)",
                    r"(D) \(y = 2x - 3\)",
                    r"(E) \(y = -x + 2\)",
                ],
            },
            {
                "id": 11,
                "stem": r"What is the distance between \((a, b)\) and \((a + 3, b)\)?",
                "choices": [
                    r"(A) \(3\)",
                    r"(B) \(\sqrt{3}\)",
                    r"(C) \(6\)",
                    r"(D) \(\sqrt{9 + b^2}\)",
                    r"(E) Cannot be determined",
                ],
            },
            {
                "id": 12,
                "stem": r"If the slope of a line is undefined, which must be true?",
                "choices": [
                    r"(A) The line is horizontal",
                    r"(B) The line is vertical",
                    r"(C) The line passes through the origin",
                    r"(D) The \(y\)-values are constant",
                    r"(E) The \(x\)-values increase",
                ],
            },
            {
                "id": 13,
                "stem": r"What is the slope of the line through \((0, 0)\) and \((k, 2k)\), where \(k \neq 0\)?",
                "choices": [
                    r"(A) \(0\)",
                    r"(B) \(1\)",
                    r"(C) \(2\)",
                    r"(D) \(k\)",
                    r"(E) \(\frac{1}{2}\)",
                ],
            },
            {
                "id": 14,
                "stem": r"If the distance between \((1, 2)\) and \((x, 2)\) is \(8\), what are the possible values of \(x\)?",
                "choices": [
                    r"(A) \(9\) only",
                    r"(B) \(-7\) only",
                    r"(C) \(9\) and \(-7\)",
                    r"(D) \(-7\) and \(9\)",
                    r"(E) \(1\) and \(9\)",
                ],
            },
            {
                "id": 15,
                "stem": r"Points \(A(2, 3)\), \(B(6, 7)\), and \(C(10, 11)\) are:",
                "choices": [
                    r"(A) Collinear",
                    r"(B) Form a right triangle",
                    r"(C) Form an equilateral triangle",
                    r"(D) Form an isosceles triangle",
                    r"(E) Cannot be determined",
                ],
            },
        ],
    },
    {
        "title": "Slopes & Distance \u2014 Multiple Choice (Select One or More)",
        "topic_id": "geo-slopes-distance",
        "instructions": "Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"Which statements about slope are true?",
                "choices": [
                    r"(A) A horizontal line has slope \(0\)",
                    r"(B) A vertical line has slope \(0\)",
                    r"(C) Parallel lines have equal slopes",
                    r"(D) Perpendicular slopes multiply to \(-1\) (when defined)",
                    r"(E) A line with positive slope rises left to right",
                ],
            },
            {
                "id": 17,
                "stem": r"Which pairs of points form a segment with length \(5\)?",
                "choices": [
                    r"(A) \((0, 0)\) and \((3, 4)\)",
                    r"(B) \((1, 2)\) and \((4, 6)\)",
                    r"(C) \((2, 3)\) and \((2, 8)\)",
                    r"(D) \((-1, -1)\) and \((2, 3)\)",
                    r"(E) \((5, 5)\) and \((8, 9)\)",
                ],
            },
            {
                "id": 18,
                "stem": r"If two lines are perpendicular and one is vertical, which must be true?",
                "choices": [
                    r"(A) The other line is horizontal",
                    r"(B) The other line has slope \(0\)",
                    r"(C) The other line is also vertical",
                    r"(D) The slopes multiply to \(-1\)",
                    r"(E) The other line has undefined slope",
                ],
            },
        ],
    },
    {
        "title": "Slopes & Distance \u2014 Numeric Entry",
        "topic_id": "geo-slopes-distance",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"Enter the slope of the line through \((1, 4)\) and \((5, 12)\).",
            },
            {
                "id": 20,
                "stem": r"Enter the distance between \((0, 0)\) and \((6, 8)\).",
            },
            {
                "id": 21,
                "stem": r"Enter the distance between \((3, 7)\) and \((3, -5)\).",
            },
            {
                "id": 22,
                "stem": r"Enter the slope of the line perpendicular to \(4x + 2y = 8\).",
            },
            {
                "id": 23,
                "stem": r"The line \(y = mx - 2\) passes through \((3, 4)\). Enter the value of \(m\).",
            },
            {
                "id": 24,
                "stem": r"Enter the distance between \((a, b)\) and \((a + 6, b + 8)\).",
            },
            {
                "id": 25,
                "stem": r"Points \(A(1, 1)\), \(B(4, 5)\), and \(C(7, 9)\) are collinear. Enter the slope of line \(AC\).",
            },
            {
                "id": 26,
                "stem": r"Enter the equation of the vertical line passing through \((-3, 5)\).",
            },
            {
                "id": 27,
                "stem": (
                    r"Points \(A(2, 3)\), \(B(6, 7)\), and \(C(x, y)\) lie on the same line. "
                    r"If \(x = 10\), enter the value of \(y\)."
                ),
            },
        ],
    },

    # ------------------------------------------------------------------ #
    #  Sub-topic 6: 3D Solids  (sections 4-7)
    # ------------------------------------------------------------------ #
    {
        "title": "3D Solids \u2014 Quantitative Comparison",
        "topic_id": "geo-3d-solids",
        "instructions": (
            "For each question, select:<br>"
            "<b>A.</b> Quantity A is greater &nbsp; "
            "<b>B.</b> Quantity B is greater &nbsp; "
            "<b>C.</b> The two quantities are equal &nbsp; "
            "<b>D.</b> The relationship cannot be determined"
            "<br>Assume all solids are right solids unless otherwise stated."
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"A cube has side length \(4\).",
                "qtyA": r"Volume of the cube",
                "qtyB": r"\(64\)",
            },
            {
                "id": 2,
                "stem": r"A rectangular solid has dimensions \(2\), \(3\), and \(4\).",
                "qtyA": r"Volume",
                "qtyB": r"Surface area",
            },
            {
                "id": 3,
                "stem": r"A cylinder has radius \(3\) and height \(5\).",
                "qtyA": r"Volume",
                "qtyB": r"\(45\pi\)",
            },
            {
                "id": 4,
                "stem": r"The edge length of a cube is doubled.",
                "qtyA": r"The volume",
                "qtyB": r"\(4\) times the original volume",
            },
            {
                "id": 5,
                "stem": r"A sphere has radius \(r\).",
                "qtyA": r"Volume",
                "qtyB": r"Surface area",
            },
            {
                "id": 6,
                "stem": r"A rectangular solid has dimensions \(3\), \(4\), and \(12\).",
                "qtyA": r"Length of the space diagonal",
                "qtyB": r"\(13\)",
            },
        ],
    },
    {
        "title": "3D Solids \u2014 Multiple Choice (Single Answer)",
        "topic_id": "geo-3d-solids",
        "instructions": "Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"What is the volume of a rectangular solid with dimensions \(5\), \(6\), and \(8\)?",
                "choices": [
                    r"(A) \(19\)",
                    r"(B) \(40\)",
                    r"(C) \(120\)",
                    r"(D) \(240\)",
                    r"(E) \(480\)",
                ],
            },
            {
                "id": 8,
                "stem": r"What is the surface area of a cube with side length \(7\)?",
                "choices": [
                    r"(A) \(147\)",
                    r"(B) \(196\)",
                    r"(C) \(294\)",
                    r"(D) \(343\)",
                    r"(E) \(686\)",
                ],
            },
            {
                "id": 9,
                "stem": r"What is the volume of a cylinder with radius \(4\) and height \(10\)?",
                "choices": [
                    r"(A) \(40\pi\)",
                    r"(B) \(80\pi\)",
                    r"(C) \(120\pi\)",
                    r"(D) \(160\pi\)",
                    r"(E) \(200\pi\)",
                ],
            },
            {
                "id": 10,
                "stem": r"A cube has volume \(125\). What is its surface area?",
                "choices": [
                    r"(A) \(25\)",
                    r"(B) \(75\)",
                    r"(C) \(100\)",
                    r"(D) \(150\)",
                    r"(E) \(300\)",
                ],
            },
            {
                "id": 11,
                "stem": r"What is the length of the space diagonal of a cube with side length \(6\)?",
                "choices": [
                    r"(A) \(6\)",
                    r"(B) \(6\sqrt{2}\)",
                    r"(C) \(6\sqrt{3}\)",
                    r"(D) \(12\)",
                    r"(E) \(18\)",
                ],
            },
            {
                "id": 12,
                "stem": r"A rectangular prism has base area \(12\) and height \(5\). What is its volume?",
                "choices": [
                    r"(A) \(17\)",
                    r"(B) \(30\)",
                    r"(C) \(48\)",
                    r"(D) \(60\)",
                    r"(E) \(120\)",
                ],
            },
            {
                "id": 13,
                "stem": (
                    r"If the radius of a cylinder is tripled and the height remains constant, "
                    r"how does the volume change?"
                ),
                "choices": [
                    r"(A) Triples",
                    r"(B) Doubles",
                    r"(C) Increases ninefold",
                    r"(D) Increases sixfold",
                    r"(E) Remains the same",
                ],
            },
            {
                "id": 14,
                "stem": (
                    r"A cube is inscribed in a sphere. If the cube has side length \(2\), "
                    r"what is the diameter of the sphere?"
                ),
                "choices": [
                    r"(A) \(2\)",
                    r"(B) \(2\sqrt{2}\)",
                    r"(C) \(2\sqrt{3}\)",
                    r"(D) \(4\)",
                    r"(E) \(4\sqrt{3}\)",
                ],
            },
            {
                "id": 15,
                "stem": r"A rectangular solid has volume \(96\) and base area \(12\). What is the height?",
                "choices": [
                    r"(A) \(4\)",
                    r"(B) \(6\)",
                    r"(C) \(8\)",
                    r"(D) \(10\)",
                    r"(E) \(12\)",
                ],
            },
        ],
    },
    {
        "title": "3D Solids \u2014 Multiple Choice (Select One or More)",
        "topic_id": "geo-3d-solids",
        "instructions": "Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If all dimensions of a solid are multiplied by \(2\), which must be true?",
                "choices": [
                    r"(A) Surface area doubles",
                    r"(B) Surface area quadruples",
                    r"(C) Volume doubles",
                    r"(D) Volume increases eightfold",
                    r"(E) The space diagonal doubles",
                ],
            },
            {
                "id": 17,
                "stem": r"Which formulas represent volume?",
                "choices": [
                    r"(A) \(lwh\)",
                    r"(B) \(\pi r^2 h\)",
                    r"(C) \(\frac{4}{3}\pi r^3\)",
                    r"(D) \(2\pi r h\)",
                    r"(E) \(6s^2\)",
                ],
            },
            {
                "id": 18,
                "stem": r"Which statements about cubes must be true?",
                "choices": [
                    r"(A) All faces are squares",
                    r"(B) All edges are equal",
                    r"(C) Surface area equals \(6\) times one face",
                    r"(D) Volume equals side length squared",
                    r"(E) The space diagonal equals side length times \(\sqrt{3}\)",
                ],
            },
        ],
    },
    {
        "title": "3D Solids \u2014 Numeric Entry",
        "topic_id": "geo-3d-solids",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"Enter the volume of a cube with side length \(9\).",
            },
            {
                "id": 20,
                "stem": r"Enter the surface area of a rectangular solid with dimensions \(2\), \(5\), and \(7\).",
            },
            {
                "id": 21,
                "stem": r"Enter the volume of a cylinder with radius \(5\) and height \(12\).",
            },
            {
                "id": 22,
                "stem": r"Enter the length of the space diagonal of a rectangular solid with dimensions \(2\), \(3\), and \(6\).",
            },
            {
                "id": 23,
                "stem": r"A sphere has radius \(4\). Enter its volume.",
            },
            {
                "id": 24,
                "stem": r"A rectangular prism has dimensions \(4\), \(6\), and \(10\). Enter its surface area.",
            },
            {
                "id": 25,
                "stem": r"If a cube has surface area \(150\), enter its side length.",
            },
            {
                "id": 26,
                "stem": r"If the radius of a sphere is doubled, by what factor does its volume increase?",
            },
            {
                "id": 27,
                "stem": (
                    r"A rectangular solid has dimensions \(x\), \(2x\), and \(3x\). "
                    r"If its volume is \(162\), enter the value of \(x\)."
                ),
            },
        ],
    },
]

# ====================================================================== #
#  ANSWERS
# ====================================================================== #

ANSWERS = {
    # ------------------------------------------------------------------ #
    #  Slopes & Distance  —  QC  (local section 0)
    # ------------------------------------------------------------------ #
    ("geo-slopes-distance", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Slope of \(\overline{AB} = \frac{11 - 3}{5 - 1} = \frac{8}{4} = 2\). "
            r"Quantity B is also \(2\). The two quantities are equal."
        ),
    },
    ("geo-slopes-distance", 0, 2): {
        "answer": "C",
        "explanation": (
            r"Both points share \(y = 4\), so the segment is horizontal. "
            r"Distance \(= |4 - (-2)| = 6\). Quantity B is \(6\). Equal."
        ),
    },
    ("geo-slopes-distance", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Slope \(= \frac{1 - 5}{6 - 2} = \frac{-4}{4} = -1\). "
            r"Quantity B is \(-1\). The two quantities are equal."
        ),
    },
    ("geo-slopes-distance", 0, 4): {
        "answer": "B",
        "explanation": (
            r"Distance \(EF = \sqrt{(3-0)^2 + (4-0)^2} = \sqrt{9 + 16} = \sqrt{25} = 5\). "
            r"Since \(5 < 7\), Quantity B is greater."
        ),
        "common_mistake": (
            "Adding the coordinates instead of using the distance formula: "
            "3 + 4 = 7 would incorrectly give answer C."
        ),
    },
    ("geo-slopes-distance", 0, 5): {
        "answer": "C",
        "explanation": (
            r"The slope of a line perpendicular to a line with slope \(-3\) is "
            r"\(-\frac{1}{-3} = \frac{1}{3}\). Quantity B is \(\frac{1}{3}\). Equal."
        ),
    },
    ("geo-slopes-distance", 0, 6): {
        "answer": "C",
        "explanation": (
            r"Slope \(\overline{GH} = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2\). "
            r"Slope \(\overline{HJ} = \frac{14 - 8}{7 - 4} = \frac{6}{3} = 2\). "
            r"Both slopes equal \(2\), so the quantities are equal."
        ),
        "common_mistake": (
            "Rushing the arithmetic or misreading the coordinates. "
            "Always compute each slope carefully before comparing."
        ),
    },

    # ------------------------------------------------------------------ #
    #  Slopes & Distance  —  MC Single  (local section 1)
    # ------------------------------------------------------------------ #
    ("geo-slopes-distance", 1, 7): {
        "answer": "A",
        "explanation": (
            r"Slope \(= \frac{3 - (-1)}{2 - 4} = \frac{4}{-2} = -2\). The answer is (A)."
        ),
    },
    ("geo-slopes-distance", 1, 8): {
        "answer": "C",
        "explanation": (
            r"Distance \(= \sqrt{(2 - (-1))^2 + (6 - 2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5\). "
            r"The answer is (C)."
        ),
    },
    ("geo-slopes-distance", 1, 9): {
        "answer": "A",
        "explanation": (
            r"Rewrite \(3x - 2y = 6\) as \(y = \frac{3}{2}x - 3\); slope is \(\frac{3}{2}\). "
            r"A parallel line must have the same slope. \(3x - 2y = 10\) rewrites to "
            r"\(y = \frac{3}{2}x - 5\), which has slope \(\frac{3}{2}\). The answer is (A)."
        ),
        "common_mistake": (
            "Confusing parallel (same slope) with perpendicular (negative reciprocal). "
            "Choice (D) has slope 3, not 3/2."
        ),
    },
    ("geo-slopes-distance", 1, 10): {
        "answer": "C",
        "explanation": (
            r"The given line has slope \(2\). A perpendicular line has slope "
            r"\(-\frac{1}{2}\). Only \(y = -\frac{1}{2}x + 4\) matches. The answer is (C)."
        ),
        "common_mistake": (
            "Choosing (A) by simply negating the slope to get -2. "
            "Perpendicular requires the negative reciprocal, not just the negative."
        ),
    },
    ("geo-slopes-distance", 1, 11): {
        "answer": "A",
        "explanation": (
            r"Both points share the same \(y\)-coordinate \(b\), so the segment is horizontal. "
            r"Distance \(= |(a + 3) - a| = 3\). The answer is (A)."
        ),
    },
    ("geo-slopes-distance", 1, 12): {
        "answer": "B",
        "explanation": (
            r"An undefined slope means the denominator \(\Delta x = 0\), i.e., the line is vertical. "
            r"The answer is (B)."
        ),
        "common_mistake": (
            "Confusing undefined slope (vertical) with zero slope (horizontal). "
            "A horizontal line has slope 0, not undefined."
        ),
    },
    ("geo-slopes-distance", 1, 13): {
        "answer": "C",
        "explanation": (
            r"Slope \(= \frac{2k - 0}{k - 0} = \frac{2k}{k} = 2\). "
            r"The \(k\) cancels because \(k \neq 0\). The answer is (C)."
        ),
    },
    ("geo-slopes-distance", 1, 14): {
        "answer": "C",
        "explanation": (
            r"Same \(y\)-coordinates, so distance \(= |x - 1| = 8\). "
            r"Thus \(x - 1 = 8\) or \(x - 1 = -8\), giving \(x = 9\) or \(x = -7\). "
            r"The answer is (C)."
        ),
        "common_mistake": (
            "Only finding the positive solution x = 9 and choosing (A). "
            "Absolute value equations always have two cases."
        ),
    },
    ("geo-slopes-distance", 1, 15): {
        "answer": "A",
        "explanation": (
            r"Slope \(\overline{AB} = \frac{7 - 3}{6 - 2} = 1\). "
            r"Slope \(\overline{BC} = \frac{11 - 7}{10 - 6} = 1\). "
            r"Equal slopes through a common point means the points are collinear. The answer is (A)."
        ),
    },

    # ------------------------------------------------------------------ #
    #  Slopes & Distance  —  MC Multi  (local section 2)
    # ------------------------------------------------------------------ #
    ("geo-slopes-distance", 2, 16): {
        "answer": "A, C, D, E",
        "explanation": (
            r"(A) True: horizontal lines have slope \(0\). "
            r"(B) False: vertical lines have undefined slope, not \(0\). "
            r"(C) True: parallel lines share the same slope. "
            r"(D) True: perpendicular slopes satisfy \(m_1 \cdot m_2 = -1\) when both are defined. "
            r"(E) True: positive slope means the line rises from left to right."
        ),
        "common_mistake": (
            "Including (B). Vertical lines have undefined slope, not zero slope. "
            "Zero slope belongs to horizontal lines."
        ),
    },
    ("geo-slopes-distance", 2, 17): {
        "answer": "A, B, C, D, E",
        "explanation": (
            r"(A) \(\sqrt{(3-0)^2 + (4-0)^2} = \sqrt{9 + 16} = 5\). Yes. "
            r"(B) \(\sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = 5\). Yes. "
            r"(C) Same \(x\)-coordinate, so distance \(= |8 - 3| = 5\). Yes. "
            r"(D) \(\sqrt{(2-(-1))^2 + (3-(-1))^2} = \sqrt{9 + 16} = 5\). Yes. "
            r"(E) \(\sqrt{(8-5)^2 + (9-5)^2} = \sqrt{9 + 16} = 5\). Yes. "
            r"All five pairs form segments of length \(5\)."
        ),
    },
    ("geo-slopes-distance", 2, 18): {
        "answer": "A, B",
        "explanation": (
            r"If one line is vertical, a perpendicular line must be horizontal. "
            r"(A) True: a horizontal line is perpendicular to a vertical line. "
            r"(B) True: a horizontal line has slope \(0\). "
            r"(C) False: two vertical lines are parallel, not perpendicular. "
            r"(D) False: the vertical line has undefined slope, so the product is not defined. "
            r"(E) False: the other line has slope \(0\), not undefined."
        ),
    },

    # ------------------------------------------------------------------ #
    #  Slopes & Distance  —  Numeric Entry  (local section 3)
    # ------------------------------------------------------------------ #
    ("geo-slopes-distance", 3, 19): {
        "answer": "2",
        "explanation": (
            r"Slope \(= \frac{12 - 4}{5 - 1} = \frac{8}{4} = 2\)."
        ),
    },
    ("geo-slopes-distance", 3, 20): {
        "answer": "10",
        "explanation": (
            r"Distance \(= \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\)."
        ),
    },
    ("geo-slopes-distance", 3, 21): {
        "answer": "12",
        "explanation": (
            r"Both points share \(x = 3\), so the segment is vertical. "
            r"Distance \(= |7 - (-5)| = 12\)."
        ),
    },
    ("geo-slopes-distance", 3, 22): {
        "answer": "0.5",
        "explanation": (
            r"Rewrite \(4x + 2y = 8\) as \(y = -2x + 4\); slope is \(-2\). "
            r"Perpendicular slope \(= -\frac{1}{-2} = \frac{1}{2} = 0.5\)."
        ),
        "common_mistake": (
            "Forgetting to take the negative reciprocal. The perpendicular slope is 1/2, not -2 or 2."
        ),
    },
    ("geo-slopes-distance", 3, 23): {
        "answer": "2",
        "explanation": (
            r"Substitute \((3, 4)\): \(4 = 3m - 2\), so \(3m = 6\), giving \(m = 2\)."
        ),
    },
    ("geo-slopes-distance", 3, 24): {
        "answer": "10",
        "explanation": (
            r"Distance \(= \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). "
            r"The variables \(a\) and \(b\) cancel in the differences."
        ),
    },
    ("geo-slopes-distance", 3, 25): {
        "answer": "4/3",
        "explanation": (
            r"Slope of \(\overline{AC} = \frac{9 - 1}{7 - 1} = \frac{8}{6} = \frac{4}{3}\). "
            r"Alternatively, slope \(\overline{AB} = \frac{5-1}{4-1} = \frac{4}{3}\), confirming collinearity."
        ),
        "common_mistake": (
            "Inverting the slope formula to get 3/4 instead of 4/3. "
            "Remember: slope = rise/run = (y2 - y1)/(x2 - x1)."
        ),
    },
    ("geo-slopes-distance", 3, 26): {
        "answer": "x = -3",
        "explanation": (
            r"A vertical line has the form \(x = c\). Since it passes through \((-3, 5)\), "
            r"the equation is \(x = -3\)."
        ),
    },
    ("geo-slopes-distance", 3, 27): {
        "answer": "11",
        "explanation": (
            r"Slope \(\overline{AB} = \frac{7 - 3}{6 - 2} = \frac{4}{4} = 1\). "
            r"Since the points are collinear, slope from \(A\) to \(C\) is also \(1\): "
            r"\(\frac{y - 3}{10 - 2} = 1\), so \(y - 3 = 8\), giving \(y = 11\)."
        ),
        "common_mistake": (
            "Using the wrong pair of points to compute the slope. "
            "Always verify with a second pair to confirm collinearity."
        ),
    },

    # ------------------------------------------------------------------ #
    #  3D Solids  —  QC  (local section 0)
    # ------------------------------------------------------------------ #
    ("geo-3d-solids", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Volume of a cube with side \(4\) is \(4^3 = 64\). "
            r"Quantity B is \(64\). The two quantities are equal."
        ),
    },
    ("geo-3d-solids", 0, 2): {
        "answer": "B",
        "explanation": (
            r"Volume \(= 2 \times 3 \times 4 = 24\). "
            r"Surface area \(= 2(2 \cdot 3 + 3 \cdot 4 + 2 \cdot 4) = 2(6 + 12 + 8) = 2(26) = 52\). "
            r"Since \(24 < 52\), Quantity B is greater."
        ),
        "common_mistake": (
            "Assuming volume is always larger than surface area for rectangular solids. "
            "For small dimensions, surface area can exceed volume."
        ),
    },
    ("geo-3d-solids", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Volume of a cylinder \(= \pi r^2 h = \pi(3)^2(5) = 45\pi\). "
            r"Quantity B is \(45\pi\). The two quantities are equal."
        ),
    },
    ("geo-3d-solids", 0, 4): {
        "answer": "A",
        "explanation": (
            r"If the edge is doubled, the new volume is \((2s)^3 = 8s^3\), which is \(8\) times the original. "
            r"Quantity B says \(4\) times. Since \(8 > 4\), Quantity A is greater."
        ),
        "common_mistake": (
            "Confusing the scaling factor for volume (cubed) with surface area (squared). "
            "Doubling edge length multiplies volume by 8, not 4."
        ),
    },
    ("geo-3d-solids", 0, 5): {
        "answer": "D",
        "explanation": (
            r"Volume \(= \frac{4}{3}\pi r^3\) and surface area \(= 4\pi r^2\). "
            r"For \(r = 1\): volume \(= \frac{4}{3}\pi < 4\pi\) (B is greater). "
            r"For \(r = 6\): volume \(= 288\pi > 144\pi\) (A is greater). "
            r"The relationship depends on \(r\), so it cannot be determined."
        ),
        "common_mistake": (
            "Assuming the comparison is always the same regardless of r. "
            "Testing two different values of r reveals the relationship changes."
        ),
    },
    ("geo-3d-solids", 0, 6): {
        "answer": "C",
        "explanation": (
            r"Space diagonal \(= \sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13\). "
            r"Quantity B is \(13\). The two quantities are equal."
        ),
    },

    # ------------------------------------------------------------------ #
    #  3D Solids  —  MC Single  (local section 1)
    # ------------------------------------------------------------------ #
    ("geo-3d-solids", 1, 7): {
        "answer": "D",
        "explanation": (
            r"Volume \(= 5 \times 6 \times 8 = 240\). The answer is (D)."
        ),
    },
    ("geo-3d-solids", 1, 8): {
        "answer": "C",
        "explanation": (
            r"Surface area of a cube \(= 6s^2 = 6(7)^2 = 6 \times 49 = 294\). The answer is (C)."
        ),
    },
    ("geo-3d-solids", 1, 9): {
        "answer": "D",
        "explanation": (
            r"Volume \(= \pi r^2 h = \pi(4)^2(10) = 160\pi\). The answer is (D)."
        ),
    },
    ("geo-3d-solids", 1, 10): {
        "answer": "D",
        "explanation": (
            r"Volume \(= s^3 = 125\), so \(s = 5\). "
            r"Surface area \(= 6s^2 = 6(25) = 150\). The answer is (D)."
        ),
        "common_mistake": (
            "Forgetting to find the side length first. Volume 125 gives s = 5, not s = 125."
        ),
    },
    ("geo-3d-solids", 1, 11): {
        "answer": "C",
        "explanation": (
            r"Space diagonal of a cube \(= s\sqrt{3} = 6\sqrt{3}\). The answer is (C)."
        ),
    },
    ("geo-3d-solids", 1, 12): {
        "answer": "D",
        "explanation": (
            r"Volume \(= \text{base area} \times \text{height} = 12 \times 5 = 60\). The answer is (D)."
        ),
    },
    ("geo-3d-solids", 1, 13): {
        "answer": "C",
        "explanation": (
            r"Original volume \(= \pi r^2 h\). New volume \(= \pi (3r)^2 h = 9\pi r^2 h\). "
            r"The volume increases ninefold. The answer is (C)."
        ),
        "common_mistake": (
            "Thinking tripling the radius triples the volume. "
            "Radius is squared in the formula, so tripling it multiplies volume by 9."
        ),
    },
    ("geo-3d-solids", 1, 14): {
        "answer": "C",
        "explanation": (
            r"The space diagonal of the cube is the diameter of the sphere. "
            r"Space diagonal \(= s\sqrt{3} = 2\sqrt{3}\). The answer is (C)."
        ),
    },
    ("geo-3d-solids", 1, 15): {
        "answer": "C",
        "explanation": (
            r"Height \(= \frac{\text{Volume}}{\text{Base area}} = \frac{96}{12} = 8\). The answer is (C)."
        ),
    },

    # ------------------------------------------------------------------ #
    #  3D Solids  —  MC Multi  (local section 2)
    # ------------------------------------------------------------------ #
    ("geo-3d-solids", 2, 16): {
        "answer": "B, D, E",
        "explanation": (
            r"(A) False: surface area scales by \(2^2 = 4\), not \(2\). "
            r"(B) True: surface area quadruples (\(\times 4\)). "
            r"(C) False: volume scales by \(2^3 = 8\), not \(2\). "
            r"(D) True: volume increases eightfold (\(\times 8\)). "
            r"(E) True: the diagonal is a linear measure, so it doubles."
        ),
    },
    ("geo-3d-solids", 2, 17): {
        "answer": "A, B, C",
        "explanation": (
            r"(A) \(lwh\) is the volume of a rectangular solid. Correct. "
            r"(B) \(\pi r^2 h\) is the volume of a cylinder. Correct. "
            r"(C) \(\frac{4}{3}\pi r^3\) is the volume of a sphere. Correct. "
            r"(D) \(2\pi r h\) is the lateral surface area of a cylinder, not volume. Incorrect. "
            r"(E) \(6s^2\) is the surface area of a cube, not volume. Incorrect."
        ),
        "common_mistake": (
            "Confusing lateral surface area of a cylinder (2*pi*r*h) with its volume (pi*r^2*h). "
            "Also confusing cube surface area (6s^2) with volume (s^3)."
        ),
    },
    ("geo-3d-solids", 2, 18): {
        "answer": "A, B, C, E",
        "explanation": (
            r"(A) True: all six faces of a cube are squares. "
            r"(B) True: all 12 edges of a cube are equal. "
            r"(C) True: surface area \(= 6s^2 = 6 \times (\text{area of one face})\). "
            r"(D) False: volume \(= s^3\) (cubed, not squared). "
            r"(E) True: space diagonal \(= s\sqrt{3}\)."
        ),
    },

    # ------------------------------------------------------------------ #
    #  3D Solids  —  Numeric Entry  (local section 3)
    # ------------------------------------------------------------------ #
    ("geo-3d-solids", 3, 19): {
        "answer": "729",
        "explanation": (
            r"Volume \(= 9^3 = 729\)."
        ),
    },
    ("geo-3d-solids", 3, 20): {
        "answer": "118",
        "explanation": (
            r"Surface area \(= 2(2 \cdot 5 + 5 \cdot 7 + 2 \cdot 7) = 2(10 + 35 + 14) = 2(59) = 118\)."
        ),
    },
    ("geo-3d-solids", 3, 21): {
        "answer": "300pi",
        "explanation": (
            r"Volume \(= \pi r^2 h = \pi(5)^2(12) = 300\pi\)."
        ),
    },
    ("geo-3d-solids", 3, 22): {
        "answer": "7",
        "explanation": (
            r"Space diagonal \(= \sqrt{2^2 + 3^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7\)."
        ),
    },
    ("geo-3d-solids", 3, 23): {
        "answer": "256pi/3",
        "explanation": (
            r"Volume \(= \frac{4}{3}\pi r^3 = \frac{4}{3}\pi(4)^3 = \frac{4}{3}\pi(64) = \frac{256\pi}{3}\)."
        ),
    },
    ("geo-3d-solids", 3, 24): {
        "answer": "248",
        "explanation": (
            r"Surface area \(= 2(4 \cdot 6 + 6 \cdot 10 + 4 \cdot 10) = 2(24 + 60 + 40) = 2(124) = 248\)."
        ),
    },
    ("geo-3d-solids", 3, 25): {
        "answer": "5",
        "explanation": (
            r"Surface area \(= 6s^2 = 150\), so \(s^2 = 25\), giving \(s = 5\)."
        ),
    },
    ("geo-3d-solids", 3, 26): {
        "answer": "8",
        "explanation": (
            r"Volume \(= \frac{4}{3}\pi r^3\). Doubling \(r\): "
            r"\(\frac{4}{3}\pi (2r)^3 = \frac{4}{3}\pi \cdot 8r^3 = 8 \times \frac{4}{3}\pi r^3\). "
            r"The volume increases by a factor of \(8\)."
        ),
        "common_mistake": (
            "Using the surface area scaling factor (4) instead of the volume scaling factor (8). "
            "Volume scales as the cube of the linear factor."
        ),
    },
    ("geo-3d-solids", 3, 27): {
        "answer": "3",
        "explanation": (
            r"Volume \(= x \cdot 2x \cdot 3x = 6x^3 = 162\). "
            r"So \(x^3 = 27\), giving \(x = 3\)."
        ),
    },
}
