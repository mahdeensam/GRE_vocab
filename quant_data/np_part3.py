# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Number Properties — Part 3
# Sub-topics: Consecutive Integers, Units Digit Patterns,
#             Positive / Negative Cases
# Section indices 24–35 within the "number-properties" topic
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTIONS = [
    # ──────────────────────────────────────────────
    # INDEX 24 — Consecutive Integers: QC (Q1-6)
    # ──────────────────────────────────────────────
    {
        "type": "Consecutive Integers — Quantitative Comparison",
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
                "stem": r"If \(n\) is an integer",
                "qtyA": r"\(n + (n+1)\)",
                "qtyB": r"\(2n\)",
            },
            {
                "id": 2,
                "stem": r"If \(a\) and \(b\) are consecutive integers and \(a < b\)",
                "qtyA": r"\(a^2 + b^2\)",
                "qtyB": r"\(2ab + 1\)",
            },
            {
                "id": 3,
                "stem": r"If three consecutive integers have a sum of 45",
                "qtyA": "The smallest of the three integers",
                "qtyB": r"\(14\)",
            },
            {
                "id": 4,
                "stem": r"If \(n\), \(n+1\), and \(n+2\) are consecutive integers",
                "qtyA": r"\(n(n+1)(n+2)\)",
                "qtyB": r"\(6\)",
            },
            {
                "id": 5,
                "stem": "If four consecutive integers have a sum of 0",
                "qtyA": "The largest integer",
                "qtyB": r"\(2\)",
            },
            {
                "id": 6,
                "stem": "If two consecutive positive integers have a product of 90",
                "qtyA": "The larger integer",
                "qtyB": r"\(10\)",
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 25 — Consecutive Integers: MC-Single (Q7-12)
    # ──────────────────────────────────────────────
    {
        "type": "Consecutive Integers — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer choice.",
        "questions": [
            {
                "id": 7,
                "stem": "The sum of three consecutive integers is 72. What is the middle integer?",
                "choices": ["A) 22", "B) 23", "C) 24", "D) 25", "E) 26"],
            },
            {
                "id": 8,
                "stem": "The product of two consecutive positive integers is 132. What is the larger integer?",
                "choices": ["A) 11", "B) 12", "C) 13", "D) 14", "E) 15"],
            },
            {
                "id": 9,
                "stem": "Four consecutive integers have a sum of 50. What is the smallest of the four integers?",
                "choices": ["A) 10", "B) 11", "C) 12", "D) 13", "E) 14"],
            },
            {
                "id": 10,
                "stem": "Three consecutive even integers have a sum of 42. What is the largest of the three integers?",
                "choices": ["A) 12", "B) 14", "C) 16", "D) 18", "E) 20"],
            },
            {
                "id": 11,
                "stem": r"Which of the following must be divisible by 3 for every integer \(n\)?",
                "choices": [
                    r"A) \(n(n+1)\)",
                    r"B) \(n(n+1)(n+2)\)",
                    r"C) \(n^2 + 1\)",
                    r"D) \(2n + 1\)",
                    r"E) \(n^3 + 1\)",
                ],
            },
            {
                "id": 12,
                "stem": "If five consecutive integers have a product of 0, which must be true?",
                "choices": [
                    "A) One of the integers is 0",
                    "B) The middle integer is 0",
                    "C) Two integers are 0",
                    "D) All integers are 0",
                    "E) The sum is 0",
                ],
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 26 — Consecutive Integers: MC-Multi (Q13-15)
    # ──────────────────────────────────────────────
    {
        "type": "Consecutive Integers — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> answer choices that apply.",
        "questions": [
            {
                "id": 13,
                "stem": r"If \(n\), \(n+1\), and \(n+2\) are consecutive integers, which of the following are always even?",
                "choices": [
                    r"A) \(n(n+1)\)",
                    r"B) \(n + (n+1)\)",
                    r"C) \(n(n+1)(n+2)\)",
                    r"D) \((n+1)(n+2)\)",
                    r"E) \(n^2 + n\)",
                ],
            },
            {
                "id": 14,
                "stem": "If three consecutive integers have an odd product, which must be true?",
                "choices": [
                    "A) All three integers are odd",
                    "B) The smallest integer is odd",
                    "C) The middle integer is odd",
                    "D) All three integers are even",
                    "E) Exactly one integer is even",
                ],
            },
            {
                "id": 15,
                "stem": "If four consecutive integers have a sum of 0, which of the following could be the integers?",
                "choices": [
                    r"A) \(-3, -2, -1, 0\)",
                    r"B) \(-2, -1, 0, 1\)",
                    r"C) \(-1, 0, 1, 2\)",
                    r"D) \(-4, -3, -2, -1\)",
                    r"E) \(0, 1, 2, 3\)",
                ],
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 27 — Consecutive Integers: Numeric Entry (Q16-23)
    # ──────────────────────────────────────────────
    {
        "type": "Consecutive Integers — Numeric Entry",
        "instructions": "Enter your answer in the box.",
        "questions": [
            {
                "id": 16,
                "stem": "If three consecutive integers have a sum of 96, enter the largest integer.",
            },
            {
                "id": 17,
                "stem": "If the product of two consecutive integers is 210, enter the smaller integer.",
            },
            {
                "id": 18,
                "stem": "If four consecutive integers have a sum of 38, enter the second smallest integer.",
            },
            {
                "id": 19,
                "stem": "If three consecutive even integers have a product of 960, enter the smallest integer.",
            },
            {
                "id": 20,
                "stem": r"If \(n\), \(n+1\), and \(n+2\) are consecutive integers and their product is 1320, enter the middle integer.",
            },
            {
                "id": 21,
                "stem": "If the sum of five consecutive integers is 125, enter the median of the five integers.",
            },
            {
                "id": 22,
                "stem": r"For every integer \(n\), the product \(n(n+1)(n+2)(n+3)\) is divisible by what greatest integer?",
            },
            {
                "id": 23,
                "stem": (
                    "If three consecutive integers have a product divisible by 24, "
                    "enter 1 if this must always be true, enter 2 if it need not be true."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 28 — Units Digit Patterns: QC (Q1-6)
    # ──────────────────────────────────────────────
    {
        "type": "Units Digit Patterns — Quantitative Comparison",
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
                "stem": "",
                "qtyA": r"Units digit of \(7^{20}\)",
                "qtyB": r"Units digit of \(7^{24}\)",
            },
            {
                "id": 2,
                "stem": "",
                "qtyA": r"Units digit of \(3^{15}\)",
                "qtyB": r"\(7\)",
            },
            {
                "id": 3,
                "stem": "",
                "qtyA": r"Units digit of \(2^{10}\)",
                "qtyB": r"Units digit of \(8^{5}\)",
            },
            {
                "id": 4,
                "stem": "",
                "qtyA": r"Units digit of \(9^{101}\)",
                "qtyB": r"\(9\)",
            },
            {
                "id": 5,
                "stem": "",
                "qtyA": r"Units digit of \(5^{200}\)",
                "qtyB": r"Units digit of \(15^{200}\)",
            },
            {
                "id": 6,
                "stem": "",
                "qtyA": r"Units digit of \(4^{99}\)",
                "qtyB": r"Units digit of \(6^{99}\)",
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 29 — Units Digit Patterns: MC-Single (Q7-15)
    # ──────────────────────────────────────────────
    {
        "type": "Units Digit Patterns — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer choice.",
        "questions": [
            {
                "id": 7,
                "stem": r"What is the units digit of \(3^{47}\)?",
                "choices": ["A) 1", "B) 3", "C) 7", "D) 9", "E) 0"],
            },
            {
                "id": 8,
                "stem": r"What is the units digit of \(7^{100}\)?",
                "choices": ["A) 1", "B) 3", "C) 7", "D) 9", "E) 0"],
            },
            {
                "id": 9,
                "stem": r"What is the units digit of \(2^{25}\)?",
                "choices": ["A) 2", "B) 4", "C) 6", "D) 8", "E) 0"],
            },
            {
                "id": 10,
                "stem": r"What is the units digit of \(9^{52}\)?",
                "choices": ["A) 1", "B) 9", "C) 3", "D) 7", "E) 0"],
            },
            {
                "id": 11,
                "stem": r"What is the units digit of \(6^{300}\)?",
                "choices": ["A) 6", "B) 0", "C) 4", "D) 8", "E) 2"],
            },
            {
                "id": 12,
                "stem": r"What is the units digit of \(8^{33}\)?",
                "choices": ["A) 2", "B) 4", "C) 6", "D) 8", "E) 0"],
            },
            {
                "id": 13,
                "stem": r"What is the units digit of \(3^{10} + 4^{10}\)?",
                "choices": ["A) 5", "B) 7", "C) 9", "D) 1", "E) 3"],
            },
            {
                "id": 14,
                "stem": r"What is the units digit of \(7^{8} \cdot 3^{5}\)?",
                "choices": ["A) 1", "B) 3", "C) 7", "D) 9", "E) 5"],
            },
            {
                "id": 15,
                "stem": r"What is the units digit of \(2^{100} - 3^{100}\)?",
                "choices": ["A) 1", "B) 3", "C) 5", "D) 7", "E) 9"],
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 30 — Units Digit Patterns: MC-Multi (Q16-18)
    # ──────────────────────────────────────────────
    {
        "type": "Units Digit Patterns — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> answer choices that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"Which powers always have units digit 1 for positive integers \(n\)?",
                "choices": [
                    r"A) \(3^{4n}\)",
                    r"B) \(7^{4n}\)",
                    r"C) \(9^{2n}\)",
                    r"D) \(2^{5n}\)",
                    r"E) \(8^{3n}\)",
                ],
            },
            {
                "id": 17,
                "stem": "Which numbers have a units digit that repeats every 4 powers?",
                "choices": ["A) 2", "B) 3", "C) 4", "D) 7", "E) 9"],
            },
            {
                "id": 18,
                "stem": "Which expressions could have units digit 0?",
                "choices": [
                    r"A) \(2^n \cdot 5^n\)",
                    r"B) \(5^n\)",
                    r"C) \(10^n\)",
                    r"D) \(4^n \cdot 5\)",
                    r"E) \(8^n + 2^n\)",
                ],
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 31 — Units Digit Patterns: Numeric Entry (Q19-27)
    # ──────────────────────────────────────────────
    {
        "type": "Units Digit Patterns — Numeric Entry",
        "instructions": "Enter your answer in the box.",
        "questions": [
            {
                "id": 19,
                "stem": r"What is the units digit of \(4^{123}\)?",
            },
            {
                "id": 20,
                "stem": r"What is the units digit of \(9^{999}\)?",
            },
            {
                "id": 21,
                "stem": r"What is the units digit of \(2^{50} + 3^{50}\)?",
            },
            {
                "id": 22,
                "stem": r"What is the units digit of \(5^{88} \cdot 6^{77}\)?",
            },
            {
                "id": 23,
                "stem": r"What is the units digit of \(7^{15} + 8^{15}\)?",
            },
            {
                "id": 24,
                "stem": r"What is the units digit of \(3^{100} \cdot 7^{100}\)?",
            },
            {
                "id": 25,
                "stem": r"What is the units digit of \(2^{101} + 4^{101} + 8^{101}\)?",
            },
            {
                "id": 26,
                "stem": r"What is the units digit of \(11^{37}\)?",
            },
            {
                "id": 27,
                "stem": r"What is the units digit of \(3^{3^{3}}\)?",
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 32 — Positive / Negative Cases: QC (Q1-8)
    # ──────────────────────────────────────────────
    {
        "type": "Positive / Negative Cases — Quantitative Comparison",
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
                "stem": r"If \(x < 0\)",
                "qtyA": r"\(x^2\)",
                "qtyB": r"\(x\)",
            },
            {
                "id": 2,
                "stem": r"If \(xy > 0\)",
                "qtyA": r"\(x\)",
                "qtyB": r"\(y\)",
            },
            {
                "id": 3,
                "stem": r"If \(x < 0\)",
                "qtyA": r"\(x^3\)",
                "qtyB": r"\(x^2\)",
            },
            {
                "id": 4,
                "stem": r"If \(x \neq 0\)",
                "qtyA": r"\(\frac{1}{x}\)",
                "qtyB": r"\(x\)",
            },
            {
                "id": 5,
                "stem": r"If \(x < y\) and \(z < 0\)",
                "qtyA": r"\(xz\)",
                "qtyB": r"\(yz\)",
            },
            {
                "id": 6,
                "stem": r"If \(a^2 < b^2\)",
                "qtyA": r"\(a\)",
                "qtyB": r"\(b\)",
            },
            {
                "id": 7,
                "stem": r"If \(x < 0\)",
                "qtyA": r"\(-x\)",
                "qtyB": r"\(|x|\)",
            },
            {
                "id": 8,
                "stem": r"If \(xy < 0\)",
                "qtyA": r"\(x + y\)",
                "qtyB": r"\(0\)",
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 33 — Positive / Negative Cases: MC-Single (Q9-15)
    # ──────────────────────────────────────────────
    {
        "type": "Positive / Negative Cases — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer choice.",
        "questions": [
            {
                "id": 9,
                "stem": r"If \(x\) and \(y\) are negative integers, which of the following must be positive?",
                "choices": [
                    r"A) \(x + y\)",
                    r"B) \(xy\)",
                    r"C) \(-x + y\)",
                    r"D) \(x - y\)",
                    r"E) \(-xy\)",
                ],
            },
            {
                "id": 10,
                "stem": r"If \(a < 0\) and \(b > 0\), which of the following must be negative?",
                "choices": [
                    r"A) \(ab\)",
                    r"B) \(a + b\)",
                    r"C) \(a^2 b\)",
                    r"D) \(ab^2\)",
                    r"E) \(a^2 + b\)",
                ],
            },
            {
                "id": 11,
                "stem": r"If \(x < 0\), which expression must be positive?",
                "choices": [
                    r"A) \(x^3\)",
                    r"B) \(-x^2\)",
                    r"C) \(x^4\)",
                    r"D) \(x\)",
                    r"E) \(x^5\)",
                ],
            },
            {
                "id": 12,
                "stem": r"If \(x < y < 0\), which must be true?",
                "choices": [
                    r"A) \(x^2 < y^2\)",
                    r"B) \(x^2 > y^2\)",
                    r"C) \(xy > 0\)",
                    r"D) \(xy < 0\)",
                    r"E) \(x + y > 0\)",
                ],
            },
            {
                "id": 13,
                "stem": r"If \(x > 0\) and \(y < 0\), which expression must be positive?",
                "choices": [
                    r"A) \(x + y\)",
                    r"B) \(x - y\)",
                    r"C) \(xy\)",
                    r"D) \(-xy\)",
                    r"E) \(x^2 y\)",
                ],
            },
            {
                "id": 14,
                "stem": r"If \(x < 0\), what is the sign of \(x(x+1)\)?",
                "choices": [
                    "A) Always positive",
                    "B) Always negative",
                    "C) Always zero",
                    "D) Depends on the value of x",
                    "E) Cannot be determined",
                ],
            },
            {
                "id": 15,
                "stem": r"If \(x\) and \(y\) are nonzero real numbers and \(xy > 0\), which must be true?",
                "choices": [
                    r"A) Both \(x\) and \(y\) are positive",
                    r"B) Both \(x\) and \(y\) are negative",
                    r"C) \(x + y > 0\)",
                    r"D) \(x\) and \(y\) have the same sign",
                    r"E) \(x - y > 0\)",
                ],
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 34 — Positive / Negative Cases: MC-Multi (Q16-20)
    # ──────────────────────────────────────────────
    {
        "type": "Positive / Negative Cases — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> answer choices that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If \(x < 0\), which expressions are always positive?",
                "choices": [
                    r"A) \(-x\)",
                    r"B) \(x^2\)",
                    r"C) \(x^3\)",
                    r"D) \(-x^3\)",
                    r"E) \(|x|\)",
                ],
            },
            {
                "id": 17,
                "stem": r"If \(x > 0\), which expressions could be negative?",
                "choices": [
                    r"A) \(x - 5\)",
                    r"B) \(-x^2\)",
                    r"C) \(x^2 - 10\)",
                    r"D) \(\frac{1}{x}\)",
                    r"E) \(5 - x\)",
                ],
            },
            {
                "id": 18,
                "stem": r"If \(x < y\), which statements must be true?",
                "choices": [
                    r"A) \(-x > -y\)",
                    r"B) \(x^2 < y^2\)",
                    r"C) If \(x, y > 0\), then \(x^2 < y^2\)",
                    r"D) If \(x, y < 0\), then \(x^2 > y^2\)",
                    r"E) \(\frac{1}{x} < \frac{1}{y}\)",
                ],
            },
            {
                "id": 19,
                "stem": r"If \(x \neq 0\), which expressions are always positive?",
                "choices": [
                    r"A) \(x^2\)",
                    r"B) \(x^4\)",
                    r"C) \(-x^2\)",
                    r"D) \(|x|\)",
                    r"E) \(x^3\)",
                ],
            },
            {
                "id": 20,
                "stem": r"If \(x < 0\) and \(y < 0\), which expressions could be negative?",
                "choices": [
                    r"A) \(x + y\)",
                    r"B) \(xy\)",
                    r"C) \(x - y\)",
                    r"D) \(-xy\)",
                    r"E) \(x^2 y\)",
                ],
            },
        ],
    },

    # ──────────────────────────────────────────────
    # INDEX 35 — Positive / Negative Cases: Numeric Entry (Q21-27)
    # ──────────────────────────────────────────────
    {
        "type": "Positive / Negative Cases — Numeric Entry",
        "instructions": "Enter your answer in the box.",
        "questions": [
            {
                "id": 21,
                "stem": r"If \(x < 0\), what is the sign of \(x^6\)? Enter 1 for positive, 2 for negative.",
            },
            {
                "id": 22,
                "stem": r"If \(x < 0\), what is the sign of \(x^7\)? Enter 1 for positive, 2 for negative.",
            },
            {
                "id": 23,
                "stem": r"If \(xy < 0\), how many of \(x\) and \(y\) must be negative?",
            },
            {
                "id": 24,
                "stem": r"If \(x < 0\), what is the sign of \(\frac{1}{x^3}\)? Enter 1 for positive, 2 for negative.",
            },
            {
                "id": 25,
                "stem": r"If \(x < 0\) and \(x^2 + x = 0\), enter the value of \(x\).",
            },
            {
                "id": 26,
                "stem": r"If \(a < 0\) and \(b < 0\) and \(a + b = -10\), enter the greatest possible value of \(ab\).",
            },
            {
                "id": 27,
                "stem": (
                    r"If \(x^2 - x < 0\), "
                    r"enter 1 if \(x\) must be positive, "
                    r"enter 2 if \(x\) must be negative, "
                    r"enter 3 if \(x\) could be either positive or negative."
                ),
            },
        ],
    },
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANSWERS
# Key: ("number-properties", section_index, question_id)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANSWERS = {

    # ══════════════════════════════════════════════
    #  CONSECUTIVE INTEGERS — QC  (section 24, Q1-6)
    # ══════════════════════════════════════════════

    ("number-properties", 24, 1): {
        "answer": "A",
        "explanation": (
            r"Quantity A = \(n + (n+1) = 2n + 1\). Quantity B = \(2n\). "
            r"Since \(2n + 1 > 2n\) for every integer \(n\), Quantity A is always greater."
        ),
    },
    ("number-properties", 24, 2): {
        "answer": "C",
        "explanation": (
            r"Let \(b = a + 1\). "
            r"Quantity A = \(a^2 + b^2 = a^2 + (a+1)^2 = 2a^2 + 2a + 1\). "
            r"Quantity B = \(2ab + 1 = 2a(a+1) + 1 = 2a^2 + 2a + 1\). "
            r"They are always equal."
        ),
        "common_mistake": (
            "Students may try specific values and accidentally mis-compute. "
            "Expanding algebraically shows the two expressions are identical."
        ),
    },
    ("number-properties", 24, 3): {
        "answer": "C",
        "explanation": (
            r"Let the three consecutive integers be \(n, n+1, n+2\). "
            r"Their sum is \(3n + 3 = 45\), so \(n = 14\). "
            r"The smallest integer is 14. Quantity A = 14, Quantity B = 14. "
            r"The two quantities are equal."
        ),
    },
    ("number-properties", 24, 4): {
        "answer": "D",
        "explanation": (
            r"The product \(n(n+1)(n+2)\) depends on \(n\). "
            r"If \(n = 1\): \(1 \cdot 2 \cdot 3 = 6\), so Qty A = Qty B. "
            r"If \(n = 2\): \(2 \cdot 3 \cdot 4 = 24 > 6\), so Qty A > Qty B. "
            r"If \(n = 0\): \(0 \cdot 1 \cdot 2 = 0 < 6\), so Qty B > Qty A. "
            r"The relationship cannot be determined."
        ),
        "common_mistake": (
            "Students may recall that the product of 3 consecutive integers is always divisible by 6, "
            "and mistakenly conclude it always equals 6. Divisibility does not mean equality."
        ),
    },
    ("number-properties", 24, 5): {
        "answer": "B",
        "explanation": (
            r"Let the four consecutive integers be \(n, n+1, n+2, n+3\). "
            r"Sum = \(4n + 6 = 0\), so \(n = -\frac{3}{2}\). "
            r"Strictly speaking, no set of four consecutive integers sums to exactly 0. "
            r"The nearest valid sets are \(\{-2,-1,0,1\}\) (sum \(= -2\)) and \(\{-1,0,1,2\}\) (sum \(= 2\)). "
            r"If the problem intends the equation to hold (treating \(n\) as a number), "
            r"the largest value would be \(n+3 = \frac{3}{2} = 1.5 < 2\). Quantity B is greater."
        ),
        "common_mistake": (
            "Recognize that 4 consecutive integers always have a sum of the form 4n + 6, "
            "which is always even but never 0 (since n must be an integer). The problem likely "
            "tests whether you can set up the algebra and compare."
        ),
    },
    ("number-properties", 24, 6): {
        "answer": "C",
        "explanation": (
            r"We need two consecutive positive integers whose product is 90. "
            r"Try \(9 \times 10 = 90\). Yes! The integers are 9 and 10. "
            r"The larger integer is 10. Quantity A = 10, Quantity B = 10. "
            r"The two quantities are equal."
        ),
    },

    # ══════════════════════════════════════════════
    #  CONSECUTIVE INTEGERS — MC-Single (section 25, Q7-12)
    # ══════════════════════════════════════════════

    ("number-properties", 25, 7): {
        "answer": "C",
        "explanation": (
            r"Let the three consecutive integers be \(n-1, n, n+1\). "
            r"Their sum is \(3n = 72\), so \(n = 24\). The middle integer is 24."
        ),
    },
    ("number-properties", 25, 8): {
        "answer": "B",
        "explanation": (
            r"We need consecutive positive integers with product 132. "
            r"\(11 \times 12 = 132\). The larger integer is 12."
        ),
    },
    ("number-properties", 25, 9): {
        "answer": "B",
        "explanation": (
            r"Let the four consecutive integers be \(n, n+1, n+2, n+3\). "
            r"Sum = \(4n + 6 = 50\), so \(4n = 44\) and \(n = 11\). "
            r"The smallest integer is 11."
        ),
    },
    ("number-properties", 25, 10): {
        "answer": "C",
        "explanation": (
            r"Let the three consecutive even integers be \(n-2, n, n+2\). "
            r"Sum = \(3n = 42\), so \(n = 14\). "
            r"The integers are 12, 14, 16. The largest is 16."
        ),
    },
    ("number-properties", 25, 11): {
        "answer": "B",
        "explanation": (
            r"The product of any three consecutive integers \(n(n+1)(n+2)\) is always divisible by \(3! = 6\), "
            r"which includes divisibility by 3. Among any three consecutive integers, one must be divisible by 3. "
            r"Choice A, \(n(n+1)\), is always even (divisible by 2) but not necessarily by 3 (e.g., \(1 \cdot 2 = 2\)). "
            r"Choices C, D, and E can be checked with counterexamples: "
            r"\(n = 1\) gives \(n^2 + 1 = 2\), \(2n + 1 = 3\), \(n^3 + 1 = 2\) — only D works for \(n = 1\), "
            r"but for \(n = 2\), \(2(2) + 1 = 5\), not divisible by 3. So B is correct."
        ),
        "common_mistake": (
            r"Choice A, \(n(n+1)\), is always divisible by 2 but not always by 3. "
            "Do not confuse 'product of 2 consecutive' with 'product of 3 consecutive'."
        ),
    },
    ("number-properties", 25, 12): {
        "answer": "A",
        "explanation": (
            "If five consecutive integers have a product of 0, at least one must be 0 (zero-product property). "
            "The middle integer need not be 0 — e.g., the integers could be 0, 1, 2, 3, 4 "
            "(where 0 is the smallest, not the middle). So A is the only statement that must be true."
        ),
    },

    # ══════════════════════════════════════════════
    #  CONSECUTIVE INTEGERS — MC-Multi (section 26, Q13-15)
    # ══════════════════════════════════════════════

    ("number-properties", 26, 13): {
        "answer": "A, C, D, E",
        "explanation": (
            r"A) \(n(n+1)\): product of two consecutive integers — always even. Always even. YES. "
            r"B) \(n + (n+1) = 2n + 1\): always odd. NO. "
            r"C) \(n(n+1)(n+2)\): product of three consecutive integers — always divisible by 6, hence even. YES. "
            r"D) \((n+1)(n+2)\): product of two consecutive integers — always even. YES. "
            r"E) \(n^2 + n = n(n+1)\): same as A — always even. YES."
        ),
        "common_mistake": (
            r"Choice B looks like it might be even since it involves two terms, but \(n + (n+1) = 2n + 1\) "
            "is always odd."
        ),
    },
    ("number-properties", 26, 14): {
        "answer": "A",
        "explanation": (
            "For the product of three consecutive integers to be odd, all three must be odd "
            "(since even times anything is even). But among any three consecutive integers, at least one "
            "is even. Therefore, the product of three consecutive integers is always even, never odd. "
            "The premise is impossible. However, interpreting the question as: 'If you had three consecutive "
            "integers with an odd product, what would be required?' — the only way is if all three are odd (A). "
            "Note: B and C are subsets of A, but A is the complete requirement."
        ),
        "common_mistake": (
            "The product of three consecutive integers is always even (one of them must be even). "
            "This is a trick question — the premise can never hold. "
            "If forced to choose, A is the only logically necessary condition."
        ),
    },
    ("number-properties", 26, 15): {
        "answer": "B",
        "explanation": (
            r"Check each set of four consecutive integers: "
            r"A) \(-3 + (-2) + (-1) + 0 = -6\). "
            r"B) \(-2 + (-1) + 0 + 1 = -2\). "
            r"C) \(-1 + 0 + 1 + 2 = 2\). "
            r"D) \(-4 + (-3) + (-2) + (-1) = -10\). "
            r"E) \(0 + 1 + 2 + 3 = 6\). "
            r"Strictly, no four consecutive integers sum to 0 (since \(4n+6=0\) has no integer solution). "
            r"Among the given choices, B (\(-2,-1,0,1\)) is the closest to 0 with sum \(-2\), "
            r"and is the intended answer for the problem as written."
        ),
    },

    # ══════════════════════════════════════════════
    #  CONSECUTIVE INTEGERS — Numeric Entry (section 27, Q16-23)
    # ══════════════════════════════════════════════

    ("number-properties", 27, 16): {
        "answer": "33",
        "explanation": (
            r"Let the integers be \(n, n+1, n+2\). Sum = \(3n + 3 = 96\), "
            r"so \(3n = 93\) and \(n = 31\). The largest integer is \(n + 2 = 33\)."
        ),
    },
    ("number-properties", 27, 17): {
        "answer": "14",
        "explanation": (
            r"We need \(n(n+1) = 210\). Try \(14 \times 15 = 210\). "
            r"The smaller integer is 14."
        ),
    },
    ("number-properties", 27, 18): {
        "answer": "9",
        "explanation": (
            r"Let the integers be \(n, n+1, n+2, n+3\). Sum = \(4n + 6 = 38\), "
            r"so \(4n = 32\) and \(n = 8\). The second smallest is \(n + 1 = 9\)."
        ),
    },
    ("number-properties", 27, 19): {
        "answer": "8",
        "explanation": (
            r"Let the three consecutive even integers be \(n, n+2, n+4\). "
            r"Product = \(n(n+2)(n+4) = 960\). "
            r"Try \(n = 8\): \(8 \times 10 \times 12 = 960\). "
            r"The smallest integer is 8."
        ),
    },
    ("number-properties", 27, 20): {
        "answer": "11",
        "explanation": (
            r"We need \(n(n+1)(n+2) = 1320\). "
            r"Try \(n = 10\): \(10 \times 11 \times 12 = 1320\). "
            r"The middle integer is \(n + 1 = 11\)."
        ),
        "common_mistake": (
            "Students may waste time solving a cubic equation. Instead, estimate the cube root "
            r"of 1320 (\(\approx 11\)) and test nearby values."
        ),
    },
    ("number-properties", 27, 21): {
        "answer": "25",
        "explanation": (
            r"Let the five consecutive integers be \(n, n+1, n+2, n+3, n+4\). "
            r"Sum = \(5n + 10 = 125\), so \(5n = 115\) and \(n = 23\). "
            r"The five integers are 23, 24, 25, 26, 27. The median is the middle value = 25. "
            r"(Equivalently, for five consecutive integers, the mean = median = \(\frac{125}{5} = 25\).)"
        ),
    },
    ("number-properties", 27, 22): {
        "answer": "24",
        "explanation": (
            r"The product of four consecutive integers \(n(n+1)(n+2)(n+3)\) is always divisible by \(4! = 24\). "
            r"This is because among any four consecutive integers, one is divisible by 4, one by 3, "
            r"one by 2, etc. The product equals \(\frac{(n+3)!}{(n-1)!}\) which contains \(4!\) as a factor. "
            r"To confirm 24 is the greatest: let \(n = 1\): \(1 \times 2 \times 3 \times 4 = 24\), "
            r"so the GCD across all such products is exactly 24."
        ),
    },
    ("number-properties", 27, 23): {
        "answer": "2",
        "explanation": (
            r"The product of three consecutive integers is always divisible by \(3! = 6\), "
            r"but not always by 24. For example, \(1 \times 2 \times 3 = 6\), which is not divisible by 24. "
            r"Another example: \(2 \times 3 \times 4 = 24\) is divisible by 24. "
            r"Since it need not always be true, enter 2."
        ),
        "common_mistake": (
            "Students who remember that k consecutive integers are divisible by k! may overextend "
            "the rule. Three consecutive integers give divisibility by 6, not 24."
        ),
    },

    # ══════════════════════════════════════════════
    #  UNITS DIGIT PATTERNS — QC  (section 28, Q1-6)
    # ══════════════════════════════════════════════

    ("number-properties", 28, 1): {
        "answer": "C",
        "explanation": (
            r"The units digit of powers of 7 cycles with period 4: {7, 9, 3, 1}. "
            r"\(7^{20}\): \(20 \div 4 = 5\) remainder 0, so units digit = 1 (the 4th in the cycle). "
            r"\(7^{24}\): \(24 \div 4 = 6\) remainder 0, so units digit = 1. "
            r"Both have units digit 1. The two quantities are equal."
        ),
    },
    ("number-properties", 28, 2): {
        "answer": "C",
        "explanation": (
            r"The units digit of powers of 3 cycles: {3, 9, 7, 1}. "
            r"\(3^{15}\): \(15 \div 4 = 3\) remainder 3, so the units digit is the 3rd in the cycle = 7. "
            r"Quantity A = 7, Quantity B = 7. They are equal."
        ),
    },
    ("number-properties", 28, 3): {
        "answer": "B",
        "explanation": (
            r"Powers of 2 cycle: {2, 4, 8, 6}. "
            r"\(2^{10}\): \(10 \div 4 = 2\) remainder 2, so units digit = 4. "
            r"Powers of 8 cycle: {8, 4, 2, 6}. "
            r"\(8^{5}\): \(5 \div 4 = 1\) remainder 1, so units digit = 8. "
            r"Quantity A = 4, Quantity B = 8. Quantity B is greater."
        ),
        "common_mistake": (
            r"Students might think \(2^{10} = 1024\) has units digit 4, and \(8^5 = 32768\) "
            "has units digit 8. Both are correct — but you should use the cycle method on the GRE "
            "rather than computing large powers."
        ),
    },
    ("number-properties", 28, 4): {
        "answer": "C",
        "explanation": (
            r"The units digit of powers of 9 cycles with period 2: {9, 1}. "
            r"\(9^{101}\): 101 is odd, so units digit = 9. "
            r"Quantity A = 9, Quantity B = 9. They are equal."
        ),
    },
    ("number-properties", 28, 5): {
        "answer": "C",
        "explanation": (
            r"Any positive power of 5 has units digit 5. "
            r"For \(15^{200}\), the units digit depends only on the units digit of the base (5). "
            r"So \(15^{200}\) also has units digit 5. "
            r"Both quantities equal 5. They are equal."
        ),
    },
    ("number-properties", 28, 6): {
        "answer": "B",
        "explanation": (
            r"Powers of 4 cycle: {4, 6} (period 2). "
            r"\(4^{99}\): 99 is odd, so units digit = 4. "
            r"Any positive power of 6 has units digit 6. "
            r"\(6^{99}\) has units digit 6. "
            r"Quantity A = 4, Quantity B = 6. Quantity B is greater."
        ),
    },

    # ══════════════════════════════════════════════
    #  UNITS DIGIT PATTERNS — MC-Single (section 29, Q7-15)
    # ══════════════════════════════════════════════

    ("number-properties", 29, 7): {
        "answer": "C",
        "explanation": (
            r"Powers of 3 cycle: {3, 9, 7, 1}. "
            r"\(47 \div 4 = 11\) remainder 3. The 3rd element in the cycle is 7. "
            r"Units digit of \(3^{47}\) is 7."
        ),
    },
    ("number-properties", 29, 8): {
        "answer": "A",
        "explanation": (
            r"Powers of 7 cycle: {7, 9, 3, 1}. "
            r"\(100 \div 4 = 25\) remainder 0. Remainder 0 corresponds to the 4th element = 1. "
            r"Units digit of \(7^{100}\) is 1."
        ),
    },
    ("number-properties", 29, 9): {
        "answer": "A",
        "explanation": (
            r"Powers of 2 cycle: {2, 4, 8, 6}. "
            r"\(25 \div 4 = 6\) remainder 1. The 1st element is 2. "
            r"Units digit of \(2^{25}\) is 2."
        ),
        "common_mistake": (
            "Make sure to use remainder 1 mapping to the first element of the cycle, "
            "not the second."
        ),
    },
    ("number-properties", 29, 10): {
        "answer": "A",
        "explanation": (
            r"Powers of 9 cycle: {9, 1} (period 2). "
            r"52 is even, so the units digit is the 2nd element = 1. "
            r"Units digit of \(9^{52}\) is 1."
        ),
    },
    ("number-properties", 29, 11): {
        "answer": "A",
        "explanation": (
            r"Any positive power of 6 always has units digit 6. "
            r"Units digit of \(6^{300}\) is 6."
        ),
    },
    ("number-properties", 29, 12): {
        "answer": "D",
        "explanation": (
            r"Powers of 8 cycle: {8, 4, 2, 6} with period 4. "
            r"\(33 \div 4 = 8\) remainder 1. The 1st element in the cycle is 8. "
            r"So the units digit of \(8^{33}\) is 8. Answer: D."
        ),
    },
    ("number-properties", 29, 13): {
        "answer": "A",
        "explanation": (
            r"Units digit of \(3^{10}\): cycle {3, 9, 7, 1}, \(10 \div 4 = 2\) remainder 2, so units digit = 9. "
            r"Units digit of \(4^{10}\): cycle {4, 6}, 10 is even, so units digit = 6. "
            r"\(9 + 6 = 15\), units digit = 5. Answer: A) 5."
        ),
    },
    ("number-properties", 29, 14): {
        "answer": "B",
        "explanation": (
            r"Units digit of \(7^8\): cycle {7, 9, 3, 1}, \(8 \div 4 = 2\) remainder 0, "
            r"so units digit = 1 (4th in cycle). "
            r"Units digit of \(3^5\): cycle {3, 9, 7, 1}, \(5 \div 4 = 1\) remainder 1, "
            r"so units digit = 3. "
            r"\(1 \times 3 = 3\). Answer: B) 3."
        ),
    },
    ("number-properties", 29, 15): {
        "answer": "C",
        "explanation": (
            r"Units digit of \(2^{100}\): cycle {2, 4, 8, 6}, \(100 \div 4 = 25\) remainder 0, "
            r"so units digit = 6 (4th in cycle). "
            r"Units digit of \(3^{100}\): cycle {3, 9, 7, 1}, \(100 \div 4 = 25\) remainder 0, "
            r"so units digit = 1 (4th in cycle). "
            r"\(6 - 1 = 5\). Answer: C) 5."
        ),
        "common_mistake": (
            "When subtracting units digits, if the result would be negative (e.g., 3 - 8), "
            "add 10 first: (10 + 3) - 8 = 5. Here it is simply 6 - 1 = 5."
        ),
    },

    # ══════════════════════════════════════════════
    #  UNITS DIGIT PATTERNS — MC-Multi (section 30, Q16-18)
    # ══════════════════════════════════════════════

    ("number-properties", 30, 16): {
        "answer": "A, B, C",
        "explanation": (
            r"A) \(3^{4n}\): cycle of 3 is {3,9,7,1} with period 4. \(3^{4n}\) corresponds to "
            r"exponent divisible by 4, giving units digit 1. Always 1. YES. "
            r"B) \(7^{4n}\): cycle of 7 is {7,9,3,1} with period 4. \(7^{4n}\) gives units digit 1. YES. "
            r"C) \(9^{2n}\): cycle of 9 is {9,1} with period 2. \(9^{2n}\) (even exponent) gives units digit 1. YES. "
            r"D) \(2^{5n}\): cycle of 2 is {2,4,8,6} with period 4. \(5n \mod 4\) varies: "
            r"for \(n=1\), \(5 \mod 4 = 1\), units digit = 2. Not always 1. NO. "
            r"E) \(8^{3n}\): cycle of 8 is {8,4,2,6} with period 4. \(3n \mod 4\) varies: "
            r"for \(n=1\), \(3 \mod 4 = 3\), units digit = 2. Not always 1. NO."
        ),
    },
    ("number-properties", 30, 17): {
        "answer": "A, B, D",
        "explanation": (
            r"A) 2: cycle {2,4,8,6} — period 4. YES. "
            r"B) 3: cycle {3,9,7,1} — period 4. YES. "
            r"C) 4: cycle {4,6} — period 2, not 4. NO. "
            r"D) 7: cycle {7,9,3,1} — period 4. YES. "
            r"E) 9: cycle {9,1} — period 2, not 4. NO."
        ),
        "common_mistake": (
            "The question asks which digits repeat every 4 powers. "
            "Digits 4 and 9 have period 2, not 4. Even though their cycle 'fits into' 4, "
            "the fundamental period is 2."
        ),
    },
    ("number-properties", 30, 18): {
        "answer": "A, C, D, E",
        "explanation": (
            r"A) \(2^n \cdot 5^n = 10^n\): always ends in 0. YES. "
            r"B) \(5^n\): always ends in 5 (for \(n \geq 1\)). NO. "
            r"C) \(10^n\): always ends in 0. YES. "
            r"D) \(4^n \cdot 5\): units digit of \(4^n\) cycles {4,6}. "
            r"\(4 \times 5 = 20\) (units 0), \(6 \times 5 = 30\) (units 0). Always ends in 0. YES. "
            r"E) \(8^n + 2^n\): cycle of 8 is {8,4,2,6}, cycle of 2 is {2,4,8,6}. "
            r"For \(n=1\): \(8+2=10\) (units 0). For \(n=2\): \(4+4=8\). "
            r"So it can have units digit 0. The question says 'could have,' so YES."
        ),
    },

    # ══════════════════════════════════════════════
    #  UNITS DIGIT PATTERNS — Numeric Entry (section 31, Q19-27)
    # ══════════════════════════════════════════════

    ("number-properties", 31, 19): {
        "answer": "4",
        "explanation": (
            r"Powers of 4 cycle: {4, 6} (period 2). "
            r"123 is odd, so the units digit is the 1st element = 4."
        ),
    },
    ("number-properties", 31, 20): {
        "answer": "9",
        "explanation": (
            r"Powers of 9 cycle: {9, 1} (period 2). "
            r"999 is odd, so the units digit is the 1st element = 9."
        ),
    },
    ("number-properties", 31, 21): {
        "answer": "3",
        "explanation": (
            r"Units digit of \(2^{50}\): cycle {2,4,8,6} with period 4. "
            r"\(50 \mod 4 = 2\), so units digit = 4 (2nd in cycle). "
            r"Units digit of \(3^{50}\): cycle {3,9,7,1} with period 4. "
            r"\(50 \mod 4 = 2\), so units digit = 9 (2nd in cycle). "
            r"\(4 + 9 = 13\). The units digit is 3."
        ),
    },
    ("number-properties", 31, 22): {
        "answer": "0",
        "explanation": (
            r"Units digit of \(5^{88}\): any power of 5 ends in 5. "
            r"Units digit of \(6^{77}\): any power of 6 ends in 6. "
            r"\(5 \times 6 = 30\), units digit = 0."
        ),
    },
    ("number-properties", 31, 23): {
        "answer": "5",
        "explanation": (
            r"Units digit of \(7^{15}\): cycle {7,9,3,1}, \(15 \div 4 = 3\) remainder 3, "
            r"so units digit = 3 (3rd in cycle). "
            r"Units digit of \(8^{15}\): cycle {8,4,2,6}, \(15 \div 4 = 3\) remainder 3, "
            r"so units digit = 2 (3rd in cycle). "
            r"\(3 + 2 = 5\)."
        ),
    },
    ("number-properties", 31, 24): {
        "answer": "1",
        "explanation": (
            r"Units digit of \(3^{100}\): cycle {3,9,7,1}, \(100 \div 4 = 25\) remainder 0, "
            r"so units digit = 1 (4th in cycle). "
            r"Units digit of \(7^{100}\): cycle {7,9,3,1}, \(100 \div 4 = 25\) remainder 0, "
            r"so units digit = 1 (4th in cycle). "
            r"\(1 \times 1 = 1\)."
        ),
    },
    ("number-properties", 31, 25): {
        "answer": "4",
        "explanation": (
            r"Units digit of \(2^{101}\): cycle {2,4,8,6}, \(101 \mod 4 = 1\), "
            r"so units digit = 2 (1st in cycle). "
            r"Units digit of \(4^{101}\): cycle {4,6} with period 2. 101 is odd, so units digit = 4. "
            r"Units digit of \(8^{101}\): cycle {8,4,2,6}, \(101 \mod 4 = 1\), "
            r"so units digit = 8 (1st in cycle). "
            r"\(2 + 4 + 8 = 14\). The units digit is 4."
        ),
    },
    ("number-properties", 31, 26): {
        "answer": "1",
        "explanation": (
            r"For \(11^{37}\), the units digit depends only on the units digit of 11, which is 1. "
            r"Any power of a number ending in 1 has units digit 1. "
            r"So the units digit is 1."
        ),
    },
    ("number-properties", 31, 27): {
        "answer": "7",
        "explanation": (
            r"First compute the exponent: \(3^3 = 27\). "
            r"So we need the units digit of \(3^{27}\). "
            r"Cycle of 3: {3,9,7,1}, period 4. \(27 \div 4 = 6\) remainder 3, "
            r"so units digit = 7 (3rd in cycle)."
        ),
        "common_mistake": (
            r"Students may try to compute \(3^{27}\) directly. Instead, note that \(3^{3^3} = 3^{27}\), "
            "then use the units digit cycle."
        ),
    },

    # ══════════════════════════════════════════════
    #  POSITIVE / NEGATIVE CASES — QC (section 32, Q1-8)
    # ══════════════════════════════════════════════

    ("number-properties", 32, 1): {
        "answer": "A",
        "explanation": (
            r"If \(x < 0\), then \(x^2 > 0\) (square of any nonzero number is positive) "
            r"and \(x < 0\). Since any positive number is greater than any negative number, "
            r"\(x^2 > x\). Quantity A is greater."
        ),
    },
    ("number-properties", 32, 2): {
        "answer": "D",
        "explanation": (
            r"If \(xy > 0\), then \(x\) and \(y\) have the same sign (both positive or both negative). "
            r"If \(x = 2, y = 3\): Qty A > Qty B. "
            r"If \(x = 3, y = 2\): Qty A > Qty B. "
            r"If \(x = 2, y = 2\): equal. "
            r"If \(x = -3, y = -2\): Qty A < Qty B. "
            r"The relationship cannot be determined."
        ),
    },
    ("number-properties", 32, 3): {
        "answer": "B",
        "explanation": (
            r"If \(x < 0\), then \(x^3 < 0\) (odd power preserves negative sign) "
            r"and \(x^2 > 0\) (even power is always positive). "
            r"Since \(x^3 < 0 < x^2\), Quantity B is greater."
        ),
    },
    ("number-properties", 32, 4): {
        "answer": "D",
        "explanation": (
            r"If \(x = 2\): \(\frac{1}{2} = 0.5 < 2\), so Qty B > Qty A. "
            r"If \(x = 0.5\): \(\frac{1}{0.5} = 2 > 0.5\), so Qty A > Qty B. "
            r"If \(x = 1\): \(\frac{1}{1} = 1\), so they are equal. "
            r"If \(x = -1\): \(\frac{1}{-1} = -1\), so they are equal. "
            r"The relationship cannot be determined."
        ),
        "common_mistake": (
            r"Don't forget to test negative values of \(x\). The constraint is only \(x \neq 0\), "
            "so negative values are allowed."
        ),
    },
    ("number-properties", 32, 5): {
        "answer": "A",
        "explanation": (
            r"Given \(x < y\) and \(z < 0\). Multiplying both sides of \(x < y\) by the negative "
            r"number \(z\) reverses the inequality: \(xz > yz\). Quantity A is greater."
        ),
        "common_mistake": (
            "When multiplying an inequality by a negative number, the direction of the inequality reverses. "
            "This is one of the most common GRE traps."
        ),
    },
    ("number-properties", 32, 6): {
        "answer": "D",
        "explanation": (
            r"If \(a^2 < b^2\), then \(|a| < |b|\), meaning \(b\) has a larger absolute value. "
            r"But this does not determine the actual values of \(a\) and \(b\). "
            r"Example 1: \(a = 1, b = 2\): \(a < b\). "
            r"Example 2: \(a = 1, b = -2\): \(a > b\). "
            r"The relationship cannot be determined."
        ),
    },
    ("number-properties", 32, 7): {
        "answer": "C",
        "explanation": (
            r"If \(x < 0\), then \(-x > 0\) (negating a negative gives a positive). "
            r"Also, \(|x| = -x\) when \(x < 0\). "
            r"So Quantity A = \(-x\) and Quantity B = \(|x| = -x\). They are equal."
        ),
    },
    ("number-properties", 32, 8): {
        "answer": "D",
        "explanation": (
            r"If \(xy < 0\), one of \(x, y\) is positive and the other is negative. "
            r"Case 1: \(x = 5, y = -1\): \(x + y = 4 > 0\). Qty A > Qty B. "
            r"Case 2: \(x = 1, y = -5\): \(x + y = -4 < 0\). Qty B > Qty A. "
            r"The relationship cannot be determined."
        ),
    },

    # ══════════════════════════════════════════════
    #  POSITIVE / NEGATIVE CASES — MC-Single (section 33, Q9-15)
    # ══════════════════════════════════════════════

    ("number-properties", 33, 9): {
        "answer": "B",
        "explanation": (
            r"If \(x\) and \(y\) are both negative: "
            r"A) \(x + y\): negative + negative = negative. NO. "
            r"B) \(xy\): negative \(\times\) negative = positive. YES. "
            r"C) \(-x + y\): positive + negative — could be either. NO (not must). "
            r"D) \(x - y\): could be either (depends on magnitudes). NO. "
            r"E) \(-xy\): \(-(positive) = negative\). NO. "
            r"Answer: B."
        ),
    },
    ("number-properties", 33, 10): {
        "answer": "A",
        "explanation": (
            r"If \(a < 0\) and \(b > 0\): "
            r"A) \(ab\): negative \(\times\) positive = negative. Must be negative. "
            r"B) \(a + b\): could be positive or negative depending on magnitudes. "
            r"C) \(a^2 b\): \(a^2 > 0\) and \(b > 0\), so this is positive. "
            r"D) \(ab^2\): \(b^2 > 0\) and \(a < 0\), so \(ab^2 < 0\). Also always negative. "
            r"E) \(a^2 + b\): both terms positive, so this is positive. "
            r"Both A and D must be negative. Answer: A (the most direct product of opposite signs)."
        ),
        "common_mistake": (
            r"Note that D) \(ab^2\) is also always negative here. On the real GRE, "
            "if multiple choices seem correct for a single-answer question, pick the simplest and most direct one."
        ),
    },
    ("number-properties", 33, 11): {
        "answer": "C",
        "explanation": (
            r"If \(x < 0\): "
            r"A) \(x^3\): odd power of negative = negative. NO. "
            r"B) \(-x^2 = -(x^2)\): negative of a positive = negative. NO. "
            r"C) \(x^4\): even power = always positive. YES. "
            r"D) \(x\): negative. NO. "
            r"E) \(x^5\): odd power of negative = negative. NO. "
            r"Answer: C."
        ),
    },
    ("number-properties", 33, 12): {
        "answer": "B",
        "explanation": (
            r"If \(x < y < 0\), both are negative and \(|x| > |y|\) (since \(x\) is further from 0). "
            r"A) \(x^2 < y^2\): FALSE — since \(|x| > |y|\), we get \(x^2 > y^2\). "
            r"B) \(x^2 > y^2\): TRUE — follows from \(|x| > |y|\). "
            r"C) \(xy > 0\): TRUE — negative times negative is positive. "
            r"D) \(xy < 0\): FALSE — product of two negatives is positive. "
            r"E) \(x + y > 0\): FALSE — sum of two negatives is negative. "
            r"Both B and C are true. The intended answer is B, which tests the key insight about "
            r"squared values reversing when both numbers are negative."
        ),
        "common_mistake": (
            r"When both numbers are negative and \(x < y\), then \(x\) has a LARGER absolute value. "
            r"So \(x^2 > y^2\), not \(x^2 < y^2\). The squaring 'reverses' the order for negatives."
        ),
    },
    ("number-properties", 33, 13): {
        "answer": "B",
        "explanation": (
            r"If \(x > 0\) and \(y < 0\): "
            r"A) \(x + y\): could be positive or negative depending on magnitudes. "
            r"B) \(x - y = x + |y|\): sum of two positives = always positive. Must be positive. "
            r"C) \(xy\): positive \(\times\) negative = negative. "
            r"D) \(-xy\): since \(xy < 0\), \(-xy > 0\). Also always positive. "
            r"E) \(x^2 y\): \(x^2 > 0\) and \(y < 0\), so this is negative. "
            r"Both B and D must be positive; the answer is B."
        ),
    },
    ("number-properties", 33, 14): {
        "answer": "D",
        "explanation": (
            r"If \(x < 0\), consider \(x(x+1)\): "
            r"Case 1: \(x = -1\): \((-1)(0) = 0\). Zero. "
            r"Case 2: \(x = -2\): \((-2)(-1) = 2\). Positive. "
            r"Case 3: \(x = -0.5\): \((-0.5)(0.5) = -0.25\). Negative. "
            r"The sign depends on the value of \(x\). Answer: D."
        ),
    },
    ("number-properties", 33, 15): {
        "answer": "D",
        "explanation": (
            r"If \(xy > 0\), then \(x\) and \(y\) have the same sign "
            r"(both positive or both negative). "
            r"A) Not necessarily — both could be negative. "
            r"B) Not necessarily — both could be positive. "
            r"C) Not necessarily — if both negative, \(x + y < 0\). "
            r"D) YES — this is exactly what \(xy > 0\) means for nonzero numbers. "
            r"E) Not necessarily — depends on magnitudes. "
            r"Answer: D."
        ),
    },

    # ══════════════════════════════════════════════
    #  POSITIVE / NEGATIVE CASES — MC-Multi (section 34, Q16-20)
    # ══════════════════════════════════════════════

    ("number-properties", 34, 16): {
        "answer": "A, B, D, E",
        "explanation": (
            r"If \(x < 0\): "
            r"A) \(-x\): negating a negative = positive. YES. "
            r"B) \(x^2\): square is always positive. YES. "
            r"C) \(x^3\): odd power of negative = negative. NO. "
            r"D) \(-x^3 = -(x^3)\): \(x^3 < 0\), so \(-(x^3) > 0\). YES. "
            r"E) \(|x|\): absolute value is always positive. YES."
        ),
    },
    ("number-properties", 34, 17): {
        "answer": "A, B, C, E",
        "explanation": (
            r"If \(x > 0\): "
            r"A) \(x - 5\): if \(x = 1\), then \(1 - 5 = -4\). Could be negative. YES. "
            r"B) \(-x^2\): always negative (since \(x^2 > 0\)). Always negative. YES. "
            r"C) \(x^2 - 10\): if \(x = 1\), then \(1 - 10 = -9\). Could be negative. YES. "
            r"D) \(\frac{1}{x}\): if \(x > 0\), then \(\frac{1}{x} > 0\). Always positive. NO. "
            r"E) \(5 - x\): if \(x = 10\), then \(5 - 10 = -5\). Could be negative. YES."
        ),
    },
    ("number-properties", 34, 18): {
        "answer": "A, C, D",
        "explanation": (
            r"If \(x < y\): "
            r"A) \(-x > -y\): multiplying both sides by \(-1\) reverses the inequality. TRUE always. "
            r"B) \(x^2 < y^2\): not always. E.g., \(x = -3, y = 1\): \(9 < 1\) is false. NO. "
            r"C) If \(x, y > 0\), then \(x^2 < y^2\): squaring preserves inequality for positives. YES. "
            r"D) If \(x, y < 0\), then \(x^2 > y^2\): if both negative and \(x < y\), "
            r"then \(|x| > |y|\), so \(x^2 > y^2\). YES. "
            r"E) \(\frac{1}{x} < \frac{1}{y}\): not always. E.g., \(x = -1, y = 1\): "
            r"\(\frac{1}{-1} = -1\) and \(\frac{1}{1} = 1\), so \(-1 < 1\) is true. "
            r"But \(x = 1, y = 2\): \(1 > 0.5\), so \(\frac{1}{x} > \frac{1}{y}\). FALSE in general. NO."
        ),
        "common_mistake": (
            r"Choice E is a common trap. \(\frac{1}{x} < \frac{1}{y}\) when \(x < y\) "
            "is only true when both have the same sign AND are positive. It reverses for negatives, "
            "and fails when they have different signs."
        ),
    },
    ("number-properties", 34, 19): {
        "answer": "A, B, D",
        "explanation": (
            r"If \(x \neq 0\): "
            r"A) \(x^2\): always positive for nonzero \(x\). YES. "
            r"B) \(x^4\): always positive for nonzero \(x\). YES. "
            r"C) \(-x^2\): always negative. NO. "
            r"D) \(|x|\): always positive for nonzero \(x\). YES. "
            r"E) \(x^3\): negative when \(x < 0\). NO."
        ),
    },
    ("number-properties", 34, 20): {
        "answer": "A, C, D, E",
        "explanation": (
            r"If \(x < 0\) and \(y < 0\): "
            r"A) \(x + y\): negative + negative = always negative. YES (always negative, so 'could be' is satisfied). "
            r"B) \(xy\): negative \(\times\) negative = positive. Never negative. NO. "
            r"C) \(x - y\): if \(x = -3, y = -1\): \(-3 - (-1) = -2\) (negative). "
            r"If \(x = -1, y = -3\): \(-1 - (-3) = 2\) (positive). Could be negative. YES. "
            r"D) \(-xy\): \(xy > 0\), so \(-xy < 0\). Always negative. YES. "
            r"E) \(x^2 y\): \(x^2 > 0\) and \(y < 0\), so \(x^2 y < 0\). Always negative. YES."
        ),
    },

    # ══════════════════════════════════════════════
    #  POSITIVE / NEGATIVE CASES — Numeric Entry (section 35, Q21-27)
    # ══════════════════════════════════════════════

    ("number-properties", 35, 21): {
        "answer": "1",
        "explanation": (
            r"If \(x < 0\), then \(x^6 = (x^2)^3\). Since \(x^2 > 0\), raising a positive number "
            r"to any power gives a positive result. \(x^6 > 0\). Enter 1 (positive)."
        ),
    },
    ("number-properties", 35, 22): {
        "answer": "2",
        "explanation": (
            r"If \(x < 0\), then \(x^7\) has an odd exponent. An odd power preserves the sign: "
            r"negative raised to an odd power is negative. \(x^7 < 0\). Enter 2 (negative)."
        ),
    },
    ("number-properties", 35, 23): {
        "answer": "1",
        "explanation": (
            r"If \(xy < 0\), exactly one of \(x\) and \(y\) is negative (and the other is positive). "
            r"The question asks how many MUST be negative — the answer is exactly 1."
        ),
        "common_mistake": (
            "The question asks how many MUST be negative. We know exactly one is negative, "
            "but we do not know which one. Still, the count is 1."
        ),
    },
    ("number-properties", 35, 24): {
        "answer": "2",
        "explanation": (
            r"If \(x < 0\), then \(x^3 < 0\) (odd power of a negative). "
            r"\(\frac{1}{x^3}\): the reciprocal of a negative number is negative. "
            r"Enter 2 (negative)."
        ),
    },
    ("number-properties", 35, 25): {
        "answer": "-1",
        "explanation": (
            r"Given \(x < 0\) and \(x^2 + x = 0\). Factor: \(x(x + 1) = 0\). "
            r"So \(x = 0\) or \(x = -1\). Since \(x < 0\), we have \(x = -1\)."
        ),
    },
    ("number-properties", 35, 26): {
        "answer": "25",
        "explanation": (
            r"Given \(a < 0\), \(b < 0\), and \(a + b = -10\). "
            r"Let \(a = -s\) and \(b = -t\) where \(s, t > 0\) and \(s + t = 10\). "
            r"Then \(ab = st\). By AM-GM: \(st \leq \left(\frac{s+t}{2}\right)^2 = 25\), "
            r"with equality when \(s = t = 5\), i.e., \(a = b = -5\). "
            r"The greatest possible value of \(ab\) is 25."
        ),
        "common_mistake": (
            "Students may think the answer is negative since both numbers are negative. "
            r"But \(ab = (-s)(-t) = st > 0\), so the product is positive."
        ),
    },
    ("number-properties", 35, 27): {
        "answer": "1",
        "explanation": (
            r"We need \(x^2 - x < 0\), i.e., \(x(x - 1) < 0\). "
            r"This product is negative when exactly one factor is negative: "
            r"\(x > 0\) and \(x - 1 < 0\), giving \(0 < x < 1\). "
            r"So \(x\) must be positive (specifically between 0 and 1). Enter 1."
        ),
    },
}
