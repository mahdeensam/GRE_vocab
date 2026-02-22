# Number Properties Part 2: LCM/GCF, Remainders & Modular Arithmetic, Even/Odd (Parity)
# Section indices 12-23 within the "number-properties" topic
# Key format: ("number-properties", section_index, question_id)

SECTIONS = [
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SUB-TOPIC: LCM / GCF  (indices 12-15)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # --- Section index 12: LCM / GCF  Quantitative Comparison (Q1-8) ---
    {
        "type": "LCM / GCF \u2014 Quantitative Comparison",
        "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
        "questions": [
            {
                "id": 1,
                "stem": r"If \(a = 2^4 \cdot 3^2\) and \(b = 2^3 \cdot 3^4\)",
                "qtyA": r"\(\gcd(a, b)\)",
                "qtyB": r"\(2^3 \cdot 3^2\)",
            },
            {
                "id": 2,
                "stem": r"If \(a = 24\) and \(b = 36\)",
                "qtyA": r"\(\text{lcm}(a, b)\)",
                "qtyB": r"\(72\)",
            },
            {
                "id": 3,
                "stem": r"If \(a\) and \(b\) are positive integers such that \(\gcd(a, b) = 1\)",
                "qtyA": r"\(\text{lcm}(a, b)\)",
                "qtyB": r"\(ab\)",
            },
            {
                "id": 4,
                "stem": r"If \(a = 2^5 \cdot 3^2\) and \(b = 2^3 \cdot 3^4\)",
                "qtyA": r"\(\text{lcm}(a, b)\)",
                "qtyB": r"\(2^5 \cdot 3^4\)",
            },
            {
                "id": 5,
                "stem": r"If \(\gcd(a, b) = 6\) and \(a = 30\)",
                "qtyA": r"\(b\)",
                "qtyB": r"\(36\)",
            },
            {
                "id": 6,
                "stem": r"If \(a = 2^2 \cdot 5^3\) and \(b = 2^3 \cdot 5^2\)",
                "qtyA": r"\(\gcd(a, b)\)",
                "qtyB": r"\(100\)",
            },
            {
                "id": 7,
                "stem": r"If \(a\) and \(b\) are consecutive integers",
                "qtyA": r"\(\gcd(a, b)\)",
                "qtyB": r"\(1\)",
            },
            {
                "id": 8,
                "stem": r"If \(a = 18\) and \(b = 24\)",
                "qtyA": r"\(\gcd(a, b) \cdot \text{lcm}(a, b)\)",
                "qtyB": r"\(ab\)",
            },
        ],
    },

    # --- Section index 13: LCM / GCF  Multiple Choice  Single Answer (Q9-15) ---
    {
        "type": "LCM / GCF \u2014 Multiple Choice \u2014 Single Answer",
        "instructions": "Select <b>one</b> answer choice.",
        "questions": [
            {
                "id": 9,
                "stem": r"What is the greatest common divisor of 84 and 126?",
                "choices": [
                    "A) 14",
                    "B) 21",
                    "C) 28",
                    "D) 42",
                    "E) 63",
                ],
            },
            {
                "id": 10,
                "stem": r"What is the least common multiple of 18 and 30?",
                "choices": [
                    "A) 60",
                    "B) 90",
                    "C) 120",
                    "D) 180",
                    "E) 360",
                ],
            },
            {
                "id": 11,
                "stem": r"If \(a = 2^3 \cdot 3^2 \cdot 5\) and \(b = 2^2 \cdot 3^3\), what is \(\gcd(a, b)\)?",
                "choices": [
                    r"A) \(2^2 \cdot 3^2\)",
                    r"B) \(2^3 \cdot 3^2\)",
                    r"C) \(2^2 \cdot 3^3\)",
                    r"D) \(2^3 \cdot 3^3\)",
                    r"E) \(2 \cdot 3^2\)",
                ],
            },
            {
                "id": 12,
                "stem": r"If \(a\) and \(b\) are relatively prime and \(a = 12\), \(b = 35\), what is \(\text{lcm}(a, b)\)?",
                "choices": [
                    "A) 60",
                    "B) 120",
                    "C) 210",
                    "D) 420",
                    "E) 840",
                ],
            },
            {
                "id": 13,
                "stem": r"Two flashing lights blink every 12 seconds and 18 seconds respectively. If they blink together at time 0, after how many seconds will they blink together again?",
                "choices": [
                    "A) 18",
                    "B) 24",
                    "C) 30",
                    "D) 36",
                    "E) 72",
                ],
            },
            {
                "id": 14,
                "stem": r"If the least common multiple of two integers is 60 and their greatest common divisor is 5, what is the product of the two integers?",
                "choices": [
                    "A) 60",
                    "B) 120",
                    "C) 240",
                    "D) 300",
                    "E) 600",
                ],
            },
            {
                "id": 15,
                "stem": r"If \(a = 2^4 \cdot 3^2\) and \(b = 2^3 \cdot 3\), how many positive divisors does \(\gcd(a, b)\) have?",
                "choices": [
                    "A) 4",
                    "B) 6",
                    "C) 8",
                    "D) 9",
                    "E) 12",
                ],
            },
        ],
    },

    # --- Section index 14: LCM / GCF  Multiple Choice  Select One or More (Q16-18) ---
    {
        "type": "LCM / GCF \u2014 Multiple Choice \u2014 Select One or More",
        "instructions": "Select <b>one or more</b> answer choices.",
        "questions": [
            {
                "id": 16,
                "stem": r"If \(\gcd(a, b) = 4\), which must be true?",
                "choices": [
                    r"A) Both \(a\) and \(b\) are divisible by 4",
                    r"B) Both \(a\) and \(b\) are divisible by 2",
                    r"C) At least one of \(a\) or \(b\) is divisible by 8",
                    r"D) \(\text{lcm}(a, b)\) is divisible by 4",
                    r"E) \(a\) and \(b\) are both even",
                ],
            },
            {
                "id": 17,
                "stem": r"Which pairs of integers are relatively prime?",
                "choices": [
                    "A) 14 and 25",
                    "B) 21 and 28",
                    "C) 35 and 64",
                    "D) 18 and 49",
                    "E) 27 and 45",
                ],
            },
            {
                "id": 18,
                "stem": r"If \(a = 2^{\alpha} \cdot 3^{\beta}\) and \(b = 2^{\gamma} \cdot 3^{\delta}\), which expressions correctly represent \(\text{lcm}(a, b)\)?",
                "choices": [
                    r"A) \(2^{\max(\alpha,\,\gamma)} \cdot 3^{\max(\beta,\,\delta)}\)",
                    r"B) \(2^{\min(\alpha,\,\gamma)} \cdot 3^{\min(\beta,\,\delta)}\)",
                    r"C) Product of highest powers of common primes",
                    r"D) Product of lowest powers of common primes",
                    r"E) Always equals \(ab\)",
                ],
            },
        ],
    },

    # --- Section index 15: LCM / GCF  Numeric Entry (Q19-27) ---
    {
        "type": "LCM / GCF \u2014 Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"Enter the least common multiple of 84 and 90.",
            },
            {
                "id": 20,
                "stem": r"Enter the greatest common divisor of 540 and 360.",
            },
            {
                "id": 21,
                "stem": r"If \(\gcd(a, b) = 12\) and \(\text{lcm}(a, b) = 180\), enter the value of \(ab\).",
            },
            {
                "id": 22,
                "stem": r"Three bells ring every 8, 12, and 18 minutes. If they ring together at 9:00 AM, at what minute after 9:00 AM will they next ring together?",
            },
            {
                "id": 23,
                "stem": r"If \(a = 2^4 \cdot 3^3 \cdot 5\) and \(b = 2^2 \cdot 3^5\), enter the value of \(\text{lcm}(a, b)\).",
            },
            {
                "id": 24,
                "stem": r"If two positive integers have \(\gcd = 7\) and \(\text{lcm} = 84\), enter the smaller possible value of one of the integers.",
            },
            {
                "id": 25,
                "stem": r"If \(n\) is the smallest positive integer divisible by 36 and 90, enter \(n\).",
            },
            {
                "id": 26,
                "stem": r"If \(\gcd(a, b) = 6\) and \(a = 18\), enter the smallest possible value of \(b\).",
            },
            {
                "id": 27,
                "stem": r"If two positive integers have \(\gcd = 15\) and \(\text{lcm} = 315\), and one of the integers is 45, enter the other integer.",
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SUB-TOPIC: REMAINDERS & MODULAR ARITHMETIC  (indices 16-19)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # --- Section index 16: Remainders  Quantitative Comparison (Q1-8) ---
    {
        "type": "Remainders & Modular Arithmetic \u2014 Quantitative Comparison",
        "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
        "questions": [
            {
                "id": 1,
                "stem": r"If an integer \(n\) leaves a remainder of 3 when divided by 5",
                "qtyA": r"Remainder when \(2n\) is divided by 5",
                "qtyB": r"\(1\)",
            },
            {
                "id": 2,
                "stem": r"If \(n\) leaves a remainder of 4 when divided by 6",
                "qtyA": r"Remainder when \(n + 2\) is divided by 6",
                "qtyB": r"\(0\)",
            },
            {
                "id": 3,
                "stem": r"If \(n\) leaves a remainder of 1 when divided by 4",
                "qtyA": r"Remainder when \(n^2\) is divided by 4",
                "qtyB": r"\(1\)",
            },
            {
                "id": 4,
                "stem": "",
                "qtyA": r"Remainder when \(17\) is divided by 4",
                "qtyB": r"Remainder when \(-17\) is divided by 4",
            },
            {
                "id": 5,
                "stem": r"If \(n = 7k + 3\)",
                "qtyA": r"Remainder when \(n\) is divided by 7",
                "qtyB": r"\(3\)",
            },
            {
                "id": 6,
                "stem": r"If \(n\) leaves remainder 2 when divided by 5",
                "qtyA": r"Remainder when \(n^2\) is divided by 5",
                "qtyB": r"\(4\)",
            },
            {
                "id": 7,
                "stem": r"If \(n\) leaves remainder 1 when divided by 3",
                "qtyA": r"Remainder when \(n^3\) is divided by 3",
                "qtyB": r"\(1\)",
            },
            {
                "id": 8,
                "stem": "",
                "qtyA": r"Remainder when \(2^{10}\) is divided by 3",
                "qtyB": r"\(1\)",
            },
        ],
    },

    # --- Section index 17: Remainders  Multiple Choice  Single Answer (Q9-16) ---
    {
        "type": "Remainders & Modular Arithmetic \u2014 Multiple Choice \u2014 Single Answer",
        "instructions": "Select <b>one</b> answer choice.",
        "questions": [
            {
                "id": 9,
                "stem": r"When 53 is divided by 7, what is the remainder?",
                "choices": [
                    "A) 2",
                    "B) 3",
                    "C) 4",
                    "D) 5",
                    "E) 6",
                ],
            },
            {
                "id": 10,
                "stem": r"If \(n\) leaves a remainder of 3 when divided by 8, what is the remainder when \(n + 13\) is divided by 8?",
                "choices": [
                    "A) 0",
                    "B) 3",
                    "C) 4",
                    "D) 5",
                    "E) 6",
                ],
            },
            {
                "id": 11,
                "stem": r"If \(n = 5k + 2\), what is the remainder when \(3n\) is divided by 5?",
                "choices": [
                    "A) 0",
                    "B) 1",
                    "C) 2",
                    "D) 3",
                    "E) 4",
                ],
            },
            {
                "id": 12,
                "stem": r"What is the remainder when \(7^4\) is divided by 6?",
                "choices": [
                    "A) 1",
                    "B) 2",
                    "C) 3",
                    "D) 4",
                    "E) 5",
                ],
            },
            {
                "id": 13,
                "stem": r"When a positive integer \(n\) is divided by 9, the remainder is 4. What is the remainder when \(2n\) is divided by 9?",
                "choices": [
                    "A) 1",
                    "B) 2",
                    "C) 4",
                    "D) 7",
                    "E) 8",
                ],
            },
            {
                "id": 14,
                "stem": r"If \(n\) leaves a remainder of 2 when divided by 5 and a remainder of 1 when divided by 3, what is the smallest positive value of \(n\)?",
                "choices": [
                    "A) 7",
                    "B) 8",
                    "C) 11",
                    "D) 17",
                    "E) 22",
                ],
            },
            {
                "id": 15,
                "stem": r"What is the remainder when \(3^{100}\) is divided by 4?",
                "choices": [
                    "A) 0",
                    "B) 1",
                    "C) 2",
                    "D) 3",
                    "E) Cannot be determined",
                ],
            },
            {
                "id": 16,
                "stem": r"If \(n\) leaves remainder 5 when divided by 12, what is the remainder when \(n^2\) is divided by 12?",
                "choices": [
                    "A) 1",
                    "B) 5",
                    "C) 7",
                    "D) 9",
                    "E) 11",
                ],
            },
        ],
    },

    # --- Section index 18: Remainders  Multiple Choice  Select One or More (Q17-20) ---
    {
        "type": "Remainders & Modular Arithmetic \u2014 Multiple Choice \u2014 Select One or More",
        "instructions": "Select <b>one or more</b> answer choices.",
        "questions": [
            {
                "id": 17,
                "stem": r"If \(n\) leaves remainder 2 when divided by 7, which of the following leave remainder 4 when divided by 7?",
                "choices": [
                    r"A) \(2n\)",
                    r"B) \(n + 2\)",
                    r"C) \(n^2\)",
                    r"D) \(3n\)",
                    r"E) \(n + 9\)",
                ],
            },
            {
                "id": 18,
                "stem": r"Which of the following always leave remainder 1 when divided by 3?",
                "choices": [
                    r"A) \(3^n\)",
                    r"B) \(4^n\)",
                    r"C) \(7^n\)",
                    r"D) \(10^n\)",
                    r"E) \(n^3 - n\)",
                ],
            },
            {
                "id": 19,
                "stem": r"If \(n\) leaves remainder 1 when divided by 5, which must be true?",
                "choices": [
                    r"A) \(n^2\) leaves remainder 1 when divided by 5",
                    r"B) \(n^3\) leaves remainder 1 when divided by 5",
                    r"C) \(n + 4\) leaves remainder 0 when divided by 5",
                    r"D) \(2n\) leaves remainder 2 when divided by 5",
                    r"E) \(n - 1\) leaves remainder 0 when divided by 5",
                ],
            },
            {
                "id": 20,
                "stem": r"Which integers have remainder 2 when divided by 5?",
                "choices": [
                    "A) 12",
                    "B) 17",
                    "C) 22",
                    "D) 27",
                    "E) 30",
                ],
            },
        ],
    },

    # --- Section index 19: Remainders  Numeric Entry (Q21-27) ---
    {
        "type": "Remainders & Modular Arithmetic \u2014 Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 21,
                "stem": r"What is the remainder when 1234 is divided by 9?",
            },
            {
                "id": 22,
                "stem": r"If \(n\) leaves remainder 4 when divided by 7, what is the remainder when \(n^2\) is divided by 7?",
            },
            {
                "id": 23,
                "stem": r"What is the remainder when \(5^{20}\) is divided by 4?",
            },
            {
                "id": 24,
                "stem": r"If \(n\) leaves remainder 3 when divided by 11, what is the remainder when \(4n + 5\) is divided by 11?",
            },
            {
                "id": 25,
                "stem": r"What is the remainder when \(2^{15}\) is divided by 7?",
            },
            {
                "id": 26,
                "stem": r"When \(n\) is divided by 6, the remainder is 5. What is the remainder when \(n^3\) is divided by 6?",
            },
            {
                "id": 27,
                "stem": r"A positive integer \(n\) leaves remainder 3 when divided by 8 and remainder 1 when divided by 3. Enter the smallest possible value of \(n\).",
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SUB-TOPIC: EVEN / ODD (PARITY)  (indices 20-23)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # --- Section index 20: Even / Odd  Quantitative Comparison (Q1-8) ---
    {
        "type": "Even / Odd (Parity) \u2014 Quantitative Comparison",
        "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
        "questions": [
            {
                "id": 1,
                "stem": r"If \(n\) is an even integer",
                "qtyA": r"\(n^2\)",
                "qtyB": r"An even integer",
            },
            {
                "id": 2,
                "stem": r"If \(n\) is an odd integer",
                "qtyA": r"\(n^3\)",
                "qtyB": r"An odd integer",
            },
            {
                "id": 3,
                "stem": r"If \(n\) is an integer",
                "qtyA": r"\(n(n+1)\)",
                "qtyB": r"An even integer",
            },
            {
                "id": 4,
                "stem": r"If \(a\) and \(b\) are odd integers",
                "qtyA": r"\(a + b\)",
                "qtyB": r"An odd integer",
            },
            {
                "id": 5,
                "stem": r"If \(n\) is an odd integer",
                "qtyA": r"\(n^2 - 1\)",
                "qtyB": r"An even integer",
            },
            {
                "id": 6,
                "stem": r"If \(x\) and \(y\) are consecutive integers",
                "qtyA": r"\(xy\)",
                "qtyB": r"An even integer",
            },
            {
                "id": 7,
                "stem": r"If \(n\) is an even integer",
                "qtyA": r"\(3n + 5\)",
                "qtyB": r"An even integer",
            },
            {
                "id": 8,
                "stem": r"If \(n\) is an integer",
                "qtyA": r"\(n^2 + n\)",
                "qtyB": r"An even integer",
            },
        ],
    },

    # --- Section index 21: Even / Odd  Multiple Choice  Single Answer (Q9-15) ---
    {
        "type": "Even / Odd (Parity) \u2014 Multiple Choice \u2014 Single Answer",
        "instructions": "Select <b>one</b> answer choice.",
        "questions": [
            {
                "id": 9,
                "stem": r"If \(n\) is odd, which of the following must be even?",
                "choices": [
                    r"A) \(n + 1\)",
                    r"B) \(n + 2\)",
                    r"C) \(n^2\)",
                    r"D) \(2n + 1\)",
                    r"E) \(n^3\)",
                ],
            },
            {
                "id": 10,
                "stem": r"If \(a\) is even and \(b\) is odd, which of the following must be odd?",
                "choices": [
                    r"A) \(a + b\)",
                    r"B) \(a - b\)",
                    r"C) \(ab\)",
                    r"D) \(a^2 + b\)",
                    r"E) \(a + b^2\)",
                ],
            },
            {
                "id": 11,
                "stem": r"If \(n\) is an integer, which of the following is always even?",
                "choices": [
                    r"A) \(n^2 + 1\)",
                    r"B) \(n^2 + n\)",
                    r"C) \(n^2 + n + 1\)",
                    r"D) \(2n + 1\)",
                    r"E) \(n^3\)",
                ],
            },
            {
                "id": 12,
                "stem": r"If \(n\) is even, which must be true?",
                "choices": [
                    r"A) \(n/2\) is even",
                    r"B) \(n^2\) is divisible by 4",
                    r"C) \(n + 1\) is even",
                    r"D) \(n^3\) is odd",
                    r"E) \(3n + 1\) is even",
                ],
            },
            {
                "id": 13,
                "stem": r"If \(n\) is odd, which expression must be divisible by 8?",
                "choices": [
                    r"A) \(n^2 - 1\)",
                    r"B) \(n^2 + 1\)",
                    r"C) \(n^3 - n\)",
                    r"D) \(n(n + 2)\)",
                    r"E) \(n^4 - 1\)",
                ],
            },
            {
                "id": 14,
                "stem": r"If \(a\), \(b\), and \(c\) are consecutive integers, which must be even?",
                "choices": [
                    r"A) \(a + b + c\)",
                    r"B) \(abc\)",
                    r"C) \(a^2 + b^2 + c^2\)",
                    r"D) \(ab + bc + ca\)",
                    r"E) None of the above",
                ],
            },
            {
                "id": 15,
                "stem": r"If \(n\) is odd, what is the parity of \(n^2 + 3n + 2\)?",
                "choices": [
                    "A) Always even",
                    "B) Always odd",
                    "C) Depends on value of \\(n\\)",
                    "D) Always divisible by 4",
                    "E) Cannot be determined",
                ],
            },
        ],
    },

    # --- Section index 22: Even / Odd  Multiple Choice  Select One or More (Q16-20) ---
    {
        "type": "Even / Odd (Parity) \u2014 Multiple Choice \u2014 Select One or More",
        "instructions": "Select <b>one or more</b> answer choices.",
        "questions": [
            {
                "id": 16,
                "stem": r"Which expressions are always even for integer \(n\)?",
                "choices": [
                    r"A) \(n(n+1)\)",
                    r"B) \(n^2 - n\)",
                    r"C) \(n^2 + n\)",
                    r"D) \(2n + 2\)",
                    r"E) \(n(n+2)\)",
                ],
            },
            {
                "id": 17,
                "stem": r"If \(a\) and \(b\) are odd integers, which must be even?",
                "choices": [
                    r"A) \(a + b\)",
                    r"B) \(a - b\)",
                    r"C) \(ab\)",
                    r"D) \(a^2 - b^2\)",
                    r"E) \(a^2 + b^2\)",
                ],
            },
            {
                "id": 18,
                "stem": r"If \(n\) is an integer, which could be odd?",
                "choices": [
                    r"A) \(n^2\)",
                    r"B) \(n^2 + 1\)",
                    r"C) \(n^2 - n\)",
                    r"D) \(n^3\)",
                    r"E) \(2n^2 + n\)",
                ],
            },
            {
                "id": 19,
                "stem": r"If \(n\) is even, which must be divisible by 4?",
                "choices": [
                    r"A) \(n^2\)",
                    r"B) \(2n\)",
                    r"C) \(n(n+2)\)",
                    r"D) \(n^3\)",
                    r"E) \(4n + 2\)",
                ],
            },
            {
                "id": 20,
                "stem": r"If \(a\) is even and \(b\) is odd, which could be even?",
                "choices": [
                    r"A) \(a + b\)",
                    r"B) \(a - b\)",
                    r"C) \(ab\)",
                    r"D) \(a^2 + b^2\)",
                    r"E) \(2a + b\)",
                ],
            },
        ],
    },

    # --- Section index 23: Even / Odd  Numeric Entry (Q21-27) ---
    {
        "type": "Even / Odd (Parity) \u2014 Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 21,
                "stem": r"If \(n\) is odd, what is the remainder when \(n^2\) is divided by 4?",
            },
            {
                "id": 22,
                "stem": r"If \(n\) is even, what is the smallest possible value of \(n^2\) greater than 10?",
            },
            {
                "id": 23,
                "stem": r"If \(a\) and \(b\) are consecutive integers, what is the remainder when \(ab\) is divided by 2?",
            },
            {
                "id": 24,
                "stem": r"If \(n\) is odd, what is the remainder when \(n^2 - 1\) is divided by 8?",
            },
            {
                "id": 25,
                "stem": r"If \(n\) is even and greater than 2, what is the least possible value of \(n^2 - 4\)?",
            },
            {
                "id": 26,
                "stem": r"If \(a\) and \(b\) are odd integers and \(a + b = 20\), what is the least possible positive value of \(ab\)?",
            },
            {
                "id": 27,
                "stem": r"If \(n\) is an integer such that \(n^4 - n^2\) is odd, enter 1 if such an integer exists, enter 2 if no such integer exists.",
            },
        ],
    },
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANSWERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANSWERS = {

    # ================================================================
    # LCM / GCF  Quantitative Comparison (section 12, Q1-8)
    # ================================================================

    ("number-properties", 12, 1): {
        "answer": "C",
        "explanation": r"We have \(a = 2^4 \cdot 3^2\) and \(b = 2^3 \cdot 3^4\). The GCD takes the minimum exponent of each prime: \(\gcd(a,b) = 2^{\min(4,3)} \cdot 3^{\min(2,4)} = 2^3 \cdot 3^2\). Quantity A \(= 2^3 \cdot 3^2\) and Quantity B \(= 2^3 \cdot 3^2\). They are equal.",
    },
    ("number-properties", 12, 2): {
        "answer": "C",
        "explanation": r"\(24 = 2^3 \cdot 3\) and \(36 = 2^2 \cdot 3^2\). \(\text{lcm}(24,36) = 2^{\max(3,2)} \cdot 3^{\max(1,2)} = 2^3 \cdot 3^2 = 8 \cdot 9 = 72\). Quantity A = 72 = Quantity B. They are equal.",
    },
    ("number-properties", 12, 3): {
        "answer": "C",
        "explanation": r"When \(\gcd(a,b) = 1\) (the integers are coprime), the identity \(\text{lcm}(a,b) = \frac{ab}{\gcd(a,b)} = \frac{ab}{1} = ab\) gives us \(\text{lcm}(a,b) = ab\). The two quantities are equal.",
        "common_mistake": r"Students may think the LCM could be less than \(ab\) even when the numbers are coprime. The LCM equals \(ab\) if and only if \(\gcd(a,b)=1\).",
    },
    ("number-properties", 12, 4): {
        "answer": "C",
        "explanation": r"\(\text{lcm}(a,b) = 2^{\max(5,3)} \cdot 3^{\max(2,4)} = 2^5 \cdot 3^4\). This equals Quantity B exactly. The two quantities are equal.",
    },
    ("number-properties", 12, 5): {
        "answer": "D",
        "explanation": r"We know \(\gcd(a,b) = 6\) and \(a = 30\). Since \(\gcd(30, b) = 6\), we need \(b\) to be a multiple of 6 such that \(\gcd(30, b) = 6\). For example, \(b = 6\) gives \(\gcd(30,6) = 6\) and \(b < 36\); but \(b = 42\) gives \(\gcd(30,42) = 6\) and \(b > 36\). Since \(b\) could be less than or greater than 36, the relationship cannot be determined.",
    },
    ("number-properties", 12, 6): {
        "answer": "C",
        "explanation": r"\(a = 2^2 \cdot 5^3 = 500\) and \(b = 2^3 \cdot 5^2 = 200\). \(\gcd(a,b) = 2^{\min(2,3)} \cdot 5^{\min(3,2)} = 2^2 \cdot 5^2 = 4 \cdot 25 = 100\). Quantity A = 100 = Quantity B. The two quantities are equal.",
    },
    ("number-properties", 12, 7): {
        "answer": "C",
        "explanation": r"Consecutive integers always have \(\gcd = 1\). If \(a\) and \(b\) are consecutive, they share no common factor greater than 1. So \(\gcd(a,b) = 1\). Quantity A = 1 = Quantity B. They are equal.",
        "common_mistake": r"Some students think consecutive integers might share a factor of 2 if one is even and one is odd. But sharing a factor means both are divisible by it; consecutive integers can never both be divisible by the same integer greater than 1.",
    },
    ("number-properties", 12, 8): {
        "answer": "C",
        "explanation": r"The fundamental identity states \(\gcd(a,b) \cdot \text{lcm}(a,b) = ab\) for any positive integers \(a\) and \(b\). With \(a = 18\) and \(b = 24\): Quantity A = \(\gcd(18,24) \cdot \text{lcm}(18,24) = 6 \cdot 72 = 432 = 18 \cdot 24 = ab\) = Quantity B. They are equal.",
    },

    # ================================================================
    # LCM / GCF  Multiple Choice  Single Answer (section 13, Q9-15)
    # ================================================================

    ("number-properties", 13, 9): {
        "answer": "D",
        "explanation": r"\(84 = 2^2 \cdot 3 \cdot 7\) and \(126 = 2 \cdot 3^2 \cdot 7\). \(\gcd = 2^1 \cdot 3^1 \cdot 7^1 = 42\). Answer: D) 42.",
    },
    ("number-properties", 13, 10): {
        "answer": "B",
        "explanation": r"\(18 = 2 \cdot 3^2\) and \(30 = 2 \cdot 3 \cdot 5\). \(\text{lcm} = 2^1 \cdot 3^2 \cdot 5^1 = 2 \cdot 9 \cdot 5 = 90\). Answer: B) 90.",
        "common_mistake": r"A common error is to multiply 18 and 30 directly to get 540 and then pick 360 or 180. Remember that \(\text{lcm}\) uses the maximum exponent of each prime, not the product.",
    },
    ("number-properties", 13, 11): {
        "answer": "A",
        "explanation": r"\(a = 2^3 \cdot 3^2 \cdot 5\) and \(b = 2^2 \cdot 3^3\). \(\gcd = 2^{\min(3,2)} \cdot 3^{\min(2,3)} = 2^2 \cdot 3^2 = 4 \cdot 9 = 36\). Answer: A) \(2^2 \cdot 3^2\).",
    },
    ("number-properties", 13, 12): {
        "answer": "D",
        "explanation": r"Since \(a = 12\) and \(b = 35\) are relatively prime (\(\gcd(12,35) = 1\)), \(\text{lcm}(12,35) = 12 \times 35 = 420\). Answer: D) 420.",
    },
    ("number-properties", 13, 13): {
        "answer": "D",
        "explanation": r"The lights blink together when the time is a common multiple of 12 and 18. \(12 = 2^2 \cdot 3\) and \(18 = 2 \cdot 3^2\). \(\text{lcm}(12,18) = 2^2 \cdot 3^2 = 36\). They blink together again after 36 seconds. Answer: D) 36.",
    },
    ("number-properties", 13, 14): {
        "answer": "D",
        "explanation": r"Using the identity \(ab = \gcd(a,b) \cdot \text{lcm}(a,b)\), we get \(ab = 5 \times 60 = 300\). Answer: D) 300.",
        "common_mistake": r"Students sometimes confuse the identity and compute \(\text{lcm} / \gcd = 12\), or try to find the individual integers. The product identity \(ab = \gcd \cdot \text{lcm}\) gives the answer directly.",
    },
    ("number-properties", 13, 15): {
        "answer": "C",
        "explanation": r"\(\gcd(a,b) = 2^{\min(4,3)} \cdot 3^{\min(2,1)} = 2^3 \cdot 3^1 = 24\). The number of positive divisors of \(24 = 2^3 \cdot 3^1\) is \((3+1)(1+1) = 8\). Answer: C) 8.",
    },

    # ================================================================
    # LCM / GCF  Multiple Choice  Select One or More (section 14, Q16-18)
    # ================================================================

    ("number-properties", 14, 16): {
        "answer": ["A", "B", "D", "E"],
        "explanation": r"If \(\gcd(a,b) = 4\), then 4 divides both \(a\) and \(b\), so (A) is true. Since 4 is divisible by 2, both are divisible by 2, so (B) is true. (C) is not necessarily true: e.g., \(a = 4, b = 4\) gives \(\gcd = 4\) but neither is divisible by 8. (D) Since \(\text{lcm}(a,b)\) is a multiple of both \(a\) and \(b\), and 4 divides \(a\), then 4 divides \(\text{lcm}(a,b)\), so (D) is true. (E) Since both are divisible by 4 (which is even), both are even, so (E) is true.",
    },
    ("number-properties", 14, 17): {
        "answer": ["A", "C", "D"],
        "explanation": r"(A) \(\gcd(14,25)\): \(14 = 2 \cdot 7\), \(25 = 5^2\). No common primes, so \(\gcd = 1\). Relatively prime. (B) \(\gcd(21,28)\): both divisible by 7, so not relatively prime. (C) \(\gcd(35,64)\): \(35 = 5 \cdot 7\), \(64 = 2^6\). No common primes, so \(\gcd = 1\). Relatively prime. (D) \(\gcd(18,49)\): \(18 = 2 \cdot 3^2\), \(49 = 7^2\). No common primes, so \(\gcd = 1\). Relatively prime. (E) \(\gcd(27,45)\): both divisible by 9, so not relatively prime.",
        "common_mistake": r"Students may overlook that 35 and 64 share no common prime factors (5 and 7 vs. only 2). Always do the full prime factorization.",
    },
    ("number-properties", 14, 18): {
        "answer": ["A", "C"],
        "explanation": r"The LCM takes the maximum exponent of each prime. (A) \(2^{\max(\alpha,\gamma)} \cdot 3^{\max(\beta,\delta)}\) is the correct formula. (B) uses min exponents, which gives the GCD, not LCM. (C) 'Product of highest powers of common primes' is a correct verbal description of LCM. (D) describes the GCD. (E) \(\text{lcm}(a,b) = ab\) only when \(\gcd(a,b) = 1\), not always.",
    },

    # ================================================================
    # LCM / GCF  Numeric Entry (section 15, Q19-27)
    # ================================================================

    ("number-properties", 15, 19): {
        "answer": "1260",
        "explanation": r"\(84 = 2^2 \cdot 3 \cdot 7\) and \(90 = 2 \cdot 3^2 \cdot 5\). \(\text{lcm} = 2^2 \cdot 3^2 \cdot 5 \cdot 7 = 4 \cdot 9 \cdot 5 \cdot 7 = 1260\).",
    },
    ("number-properties", 15, 20): {
        "answer": "180",
        "explanation": r"\(540 = 2^2 \cdot 3^3 \cdot 5\) and \(360 = 2^3 \cdot 3^2 \cdot 5\). \(\gcd = 2^2 \cdot 3^2 \cdot 5 = 4 \cdot 9 \cdot 5 = 180\).",
    },
    ("number-properties", 15, 21): {
        "answer": "2160",
        "explanation": r"By the identity \(ab = \gcd(a,b) \cdot \text{lcm}(a,b)\), we get \(ab = 12 \times 180 = 2160\).",
        "common_mistake": r"Some students try to find the individual values of \(a\) and \(b\) first. This is unnecessary -- the product identity gives the answer directly.",
    },
    ("number-properties", 15, 22): {
        "answer": "72",
        "explanation": r"\(8 = 2^3\), \(12 = 2^2 \cdot 3\), \(18 = 2 \cdot 3^2\). \(\text{lcm}(8,12,18) = 2^3 \cdot 3^2 = 8 \cdot 9 = 72\). They next ring together 72 minutes after 9:00 AM.",
    },
    ("number-properties", 15, 23): {
        "answer": "19440",
        "explanation": r"\(a = 2^4 \cdot 3^3 \cdot 5\) and \(b = 2^2 \cdot 3^5\). \(\text{lcm} = 2^{\max(4,2)} \cdot 3^{\max(3,5)} \cdot 5^{\max(1,0)} = 2^4 \cdot 3^5 \cdot 5 = 16 \cdot 243 \cdot 5 = 19440\).",
    },
    ("number-properties", 15, 24): {
        "answer": "7",
        "explanation": r"Let the two integers be \(a\) and \(b\) with \(\gcd(a,b) = 7\) and \(\text{lcm}(a,b) = 84\). Write \(a = 7m\) and \(b = 7n\) where \(\gcd(m,n) = 1\). Then \(\text{lcm}(a,b) = 7mn = 84\), so \(mn = 12\). Coprime pairs \((m,n)\) with product 12: \((1,12), (3,4), (4,3), (12,1)\). The corresponding integers are \((7,84)\) and \((21,28)\). The smallest possible value is 7.",
    },
    ("number-properties", 15, 25): {
        "answer": "180",
        "explanation": r"The smallest positive integer divisible by both 36 and 90 is \(\text{lcm}(36,90)\). \(36 = 2^2 \cdot 3^2\) and \(90 = 2 \cdot 3^2 \cdot 5\). \(\text{lcm} = 2^2 \cdot 3^2 \cdot 5 = 180\).",
    },
    ("number-properties", 15, 26): {
        "answer": "6",
        "explanation": r"We need \(\gcd(18, b) = 6\), so \(b\) must be a multiple of 6. Also, \(\gcd(18, b)\) must be exactly 6 (not 18 or any other common factor). The smallest multiple of 6 is 6 itself. Check: \(\gcd(18, 6) = 6\). So the smallest possible value of \(b\) is 6.",
        "common_mistake": r"Some students might try \(b = 12\): \(\gcd(18,12) = 6\), which also works but is not the smallest. The smallest multiple of 6 that gives \(\gcd = 6\) with 18 is simply 6.",
    },
    ("number-properties", 15, 27): {
        "answer": "105",
        "explanation": r"Using the identity \(ab = \gcd \cdot \text{lcm}\): \(45 \cdot b = 15 \times 315 = 4725\). So \(b = 4725 / 45 = 105\). Verify: \(\gcd(45, 105)\). \(45 = 3^2 \cdot 5\), \(105 = 3 \cdot 5 \cdot 7\). \(\gcd = 3 \cdot 5 = 15\). \(\text{lcm} = 3^2 \cdot 5 \cdot 7 = 315\). Both check out. The other integer is 105.",
    },

    # ================================================================
    # Remainders & Modular Arithmetic  QC (section 16, Q1-8)
    # ================================================================

    ("number-properties", 16, 1): {
        "answer": "C",
        "explanation": r"If \(n \equiv 3 \pmod{5}\), then \(2n \equiv 2 \times 3 = 6 \equiv 1 \pmod{5}\). The remainder when \(2n\) is divided by 5 is 1. Quantity A = 1 = Quantity B. They are equal.",
    },
    ("number-properties", 16, 2): {
        "answer": "C",
        "explanation": r"If \(n \equiv 4 \pmod{6}\), then \(n + 2 \equiv 4 + 2 = 6 \equiv 0 \pmod{6}\). The remainder is 0. Quantity A = 0 = Quantity B. They are equal.",
    },
    ("number-properties", 16, 3): {
        "answer": "C",
        "explanation": r"If \(n \equiv 1 \pmod{4}\), then \(n^2 \equiv 1^2 = 1 \pmod{4}\). The remainder when \(n^2\) is divided by 4 is 1. Quantity A = 1 = Quantity B. They are equal.",
        "common_mistake": r"Students may try plugging in specific values. While that works (e.g., \(n = 5\): \(25 \div 4 = 6\) remainder 1), it is more efficient to use modular arithmetic directly: \(1^2 \equiv 1\).",
    },
    ("number-properties", 16, 4): {
        "answer": "B",
        "explanation": r"Quantity A: \(17 \div 4 = 4\) remainder \(1\). Quantity B: For \(-17 \div 4\), we use the convention that remainders are non-negative. \(-17 = 4 \times (-5) + 3\), so the remainder is 3. Quantity A = 1, Quantity B = 3. Quantity B is greater.",
    },
    ("number-properties", 16, 5): {
        "answer": "C",
        "explanation": r"If \(n = 7k + 3\), then dividing \(n\) by 7 gives quotient \(k\) and remainder 3. Quantity A = 3 = Quantity B. They are equal.",
    },
    ("number-properties", 16, 6): {
        "answer": "C",
        "explanation": r"If \(n \equiv 2 \pmod{5}\), then \(n^2 \equiv 2^2 = 4 \pmod{5}\). Quantity A = 4 = Quantity B. They are equal.",
    },
    ("number-properties", 16, 7): {
        "answer": "C",
        "explanation": r"If \(n \equiv 1 \pmod{3}\), then \(n^3 \equiv 1^3 = 1 \pmod{3}\). Quantity A = 1 = Quantity B. They are equal.",
    },
    ("number-properties", 16, 8): {
        "answer": "C",
        "explanation": r"\(2^1 \equiv 2 \pmod{3}\), \(2^2 \equiv 1 \pmod{3}\). The pattern cycles with period 2: odd powers give remainder 2, even powers give remainder 1. Since 10 is even, \(2^{10} \equiv 1 \pmod{3}\). Quantity A = 1 = Quantity B. They are equal.",
        "common_mistake": r"Students may try to compute \(2^{10} = 1024\) and divide by 3. While this works, recognizing the cyclic pattern (2, 1, 2, 1, ...) is much faster.",
    },

    # ================================================================
    # Remainders  Multiple Choice  Single Answer (section 17, Q9-16)
    # ================================================================

    ("number-properties", 17, 9): {
        "answer": "C",
        "explanation": r"\(53 = 7 \times 7 + 4\). Since \(7 \times 7 = 49\) and \(53 - 49 = 4\), the remainder is 4. Answer: C) 4.",
    },
    ("number-properties", 17, 10): {
        "answer": "A",
        "explanation": r"If \(n \equiv 3 \pmod{8}\), then \(n + 13 \equiv 3 + 13 = 16 \equiv 0 \pmod{8}\). The remainder is 0. Answer: A) 0.",
    },
    ("number-properties", 17, 11): {
        "answer": "B",
        "explanation": r"If \(n = 5k + 2\), then \(n \equiv 2 \pmod{5}\). So \(3n \equiv 3 \times 2 = 6 \equiv 1 \pmod{5}\). The remainder is 1. Answer: B) 1.",
    },
    ("number-properties", 17, 12): {
        "answer": "A",
        "explanation": r"\(7 \equiv 1 \pmod{6}\), so \(7^4 \equiv 1^4 = 1 \pmod{6}\). The remainder is 1. Answer: A) 1.",
        "common_mistake": r"Students sometimes try to compute \(7^4 = 2401\) and divide by 6. While correct (\(2401 = 400 \times 6 + 1\)), noticing that \(7 \equiv 1 \pmod 6\) makes this trivial.",
    },
    ("number-properties", 17, 13): {
        "answer": "E",
        "explanation": r"If \(n \equiv 4 \pmod{9}\), then \(2n \equiv 2 \times 4 = 8 \pmod{9}\). The remainder is 8. Answer: E) 8.",
    },
    ("number-properties", 17, 14): {
        "answer": "A",
        "explanation": r"We need \(n \equiv 2 \pmod{5}\) and \(n \equiv 1 \pmod{3}\). Testing: \(n = 2\): \(2 \div 3\) gives remainder 2, not 1. \(n = 7\): \(7 \div 5\) gives remainder 2 and \(7 \div 3\) gives remainder 1. Both conditions satisfied. Answer: A) 7.",
    },
    ("number-properties", 17, 15): {
        "answer": "B",
        "explanation": r"\(3^1 \equiv 3 \pmod{4}\), \(3^2 \equiv 1 \pmod{4}\). The pattern cycles with period 2: odd powers give 3, even powers give 1. Since 100 is even, \(3^{100} \equiv 1 \pmod{4}\). Answer: B) 1.",
    },
    ("number-properties", 17, 16): {
        "answer": "A",
        "explanation": r"If \(n \equiv 5 \pmod{12}\), then \(n^2 \equiv 5^2 = 25 \equiv 1 \pmod{12}\) (since \(25 = 2 \times 12 + 1\)). The remainder is 1. Answer: A) 1.",
    },

    # ================================================================
    # Remainders  Multiple Choice  Select One or More (section 18, Q17-20)
    # ================================================================

    ("number-properties", 18, 17): {
        "answer": ["A", "B", "C", "E"],
        "explanation": r"With \(n \equiv 2 \pmod{7}\): (A) \(2n \equiv 4 \pmod{7}\). Yes. (B) \(n + 2 \equiv 4 \pmod{7}\). Yes. (C) \(n^2 \equiv 4 \pmod{7}\). Yes. (D) \(3n \equiv 6 \pmod{7}\). No (remainder 6, not 4). (E) \(n + 9 \equiv 2 + 9 = 11 \equiv 4 \pmod{7}\). Yes.",
        "common_mistake": r"For (E), students may forget to reduce 11 mod 7. Since \(11 - 7 = 4\), the remainder is 4.",
    },
    ("number-properties", 18, 18): {
        "answer": ["B", "C", "D"],
        "explanation": r"We need expressions that always leave remainder 1 when divided by 3 (for all positive integers \(n\)). (A) \(3^n \equiv 0 \pmod{3}\). No (remainder 0). (B) \(4^n \equiv 1^n = 1 \pmod{3}\) since \(4 \equiv 1 \pmod 3\). Yes. (C) \(7^n \equiv 1^n = 1 \pmod{3}\) since \(7 \equiv 1 \pmod 3\). Yes. (D) \(10^n \equiv 1^n = 1 \pmod{3}\) since \(10 \equiv 1 \pmod 3\). Yes. (E) \(n^3 - n = n(n-1)(n+1)\) is the product of three consecutive integers, which is always divisible by 3, so remainder 0. No.",
    },
    ("number-properties", 18, 19): {
        "answer": ["A", "B", "C", "D", "E"],
        "explanation": r"With \(n \equiv 1 \pmod{5}\): (A) \(n^2 \equiv 1 \pmod{5}\). True. (B) \(n^3 \equiv 1 \pmod{5}\). True. (C) \(n + 4 \equiv 1 + 4 = 5 \equiv 0 \pmod{5}\). True. (D) \(2n \equiv 2 \pmod{5}\). True. (E) \(n - 1 \equiv 0 \pmod{5}\). True. All five statements must hold.",
    },
    ("number-properties", 18, 20): {
        "answer": ["A", "B", "C", "D"],
        "explanation": r"An integer has remainder 2 when divided by 5 if it is of the form \(5k + 2\). (A) \(12 = 5 \times 2 + 2\). Remainder 2. Yes. (B) \(17 = 5 \times 3 + 2\). Yes. (C) \(22 = 5 \times 4 + 2\). Yes. (D) \(27 = 5 \times 5 + 2\). Yes. (E) \(30 = 5 \times 6 + 0\). Remainder 0. No.",
    },

    # ================================================================
    # Remainders  Numeric Entry (section 19, Q21-27)
    # ================================================================

    ("number-properties", 19, 21): {
        "answer": "1",
        "explanation": r"A number's remainder when divided by 9 equals the remainder of its digit sum divided by 9. Digit sum of 1234: \(1+2+3+4 = 10\). \(10 \div 9 = 1\) remainder 1. The remainder is 1.",
    },
    ("number-properties", 19, 22): {
        "answer": "2",
        "explanation": r"If \(n \equiv 4 \pmod{7}\), then \(n^2 \equiv 4^2 = 16 \equiv 2 \pmod{7}\) (since \(16 = 2 \times 7 + 2\)). The remainder is 2.",
    },
    ("number-properties", 19, 23): {
        "answer": "1",
        "explanation": r"\(5 \equiv 1 \pmod{4}\), so \(5^{20} \equiv 1^{20} = 1 \pmod{4}\). The remainder is 1.",
        "common_mistake": r"Students might try to compute large powers of 5. Instead, notice \(5 = 4 + 1\), so any power of 5 leaves remainder 1 when divided by 4.",
    },
    ("number-properties", 19, 24): {
        "answer": "6",
        "explanation": r"If \(n \equiv 3 \pmod{11}\), then \(4n + 5 \equiv 4(3) + 5 = 17 \equiv 6 \pmod{11}\) (since \(17 - 11 = 6\)). The remainder is 6.",
    },
    ("number-properties", 19, 25): {
        "answer": "1",
        "explanation": r"Powers of 2 mod 7 cycle: \(2^1 \equiv 2\), \(2^2 \equiv 4\), \(2^3 \equiv 1 \pmod{7}\). The cycle length is 3. Since \(15 = 3 \times 5\), we get \(2^{15} = (2^3)^5 \equiv 1^5 = 1 \pmod{7}\). The remainder is 1.",
    },
    ("number-properties", 19, 26): {
        "answer": "5",
        "explanation": r"If \(n \equiv 5 \pmod{6}\), then \(n^3 \equiv 5^3 = 125 \pmod{6}\). \(125 = 20 \times 6 + 5\), so \(n^3 \equiv 5 \pmod{6}\). The remainder is 5.",
    },
    ("number-properties", 19, 27): {
        "answer": "19",
        "explanation": r"We need \(n \equiv 3 \pmod{8}\) and \(n \equiv 1 \pmod{3}\). Values with \(n \equiv 3 \pmod 8\): 3, 11, 19, 27, ... Check mod 3: \(3 \equiv 0\) (no), \(11 \equiv 2\) (no), \(19 \equiv 1\) (yes). The smallest value is 19.",
        "common_mistake": r"Students may try only the first few values. Be systematic: list multiples of 8 plus 3, then check the mod 3 condition for each.",
    },

    # ================================================================
    # Even / Odd (Parity)  QC (section 20, Q1-8)
    # ================================================================

    ("number-properties", 20, 1): {
        "answer": "C",
        "explanation": r"If \(n\) is even, then \(n^2 = (\text{even})^2\) is always even. Quantity A is always an even integer, which matches Quantity B ('an even integer'). The two quantities are equal.",
    },
    ("number-properties", 20, 2): {
        "answer": "C",
        "explanation": r"If \(n\) is odd, \(n^3 = \text{odd} \times \text{odd} \times \text{odd} = \text{odd}\). Quantity A is always odd, matching Quantity B ('an odd integer'). The two quantities are equal.",
    },
    ("number-properties", 20, 3): {
        "answer": "C",
        "explanation": r"\(n(n+1)\) is the product of two consecutive integers, so one is always even. Thus \(n(n+1)\) is always even. Quantity A is always an even integer, matching Quantity B ('an even integer'). The two quantities are equal.",
    },
    ("number-properties", 20, 4): {
        "answer": "A",
        "explanation": r"If \(a\) and \(b\) are both odd, then \(a + b\) is even (odd + odd = even). Quantity A is always an even integer, but Quantity B claims 'an odd integer.' Since the sum of two odd integers is always even, never odd, Quantity A's parity (even) contradicts Quantity B (odd). Quantity A is greater.",
        "common_mistake": r"Students may assume odd + odd could sometimes be odd. It never is: the sum of two odd integers is always even.",
    },
    ("number-properties", 20, 5): {
        "answer": "C",
        "explanation": r"If \(n\) is odd, \(n^2\) is odd, so \(n^2 - 1 = \text{odd} - 1 = \text{even}\). Quantity A is always even, matching Quantity B ('an even integer'). The two quantities are equal.",
    },
    ("number-properties", 20, 6): {
        "answer": "C",
        "explanation": r"If \(x\) and \(y\) are consecutive integers, one is even and one is odd, so \(xy\) is always even. Quantity A is always an even integer, matching Quantity B ('an even integer'). The two quantities are equal.",
    },
    ("number-properties", 20, 7): {
        "answer": "A",
        "explanation": r"If \(n\) is even, then \(3n\) is even, and \(3n + 5 = \text{even} + \text{odd} = \text{odd}\). Quantity A is always odd, but Quantity B claims 'an even integer.' Since \(3n + 5\) is always odd, never even, Quantity A's parity contradicts Quantity B. Quantity A is greater.",
    },
    ("number-properties", 20, 8): {
        "answer": "C",
        "explanation": r"\(n^2 + n = n(n+1)\), which is the product of consecutive integers and is always even. Quantity A is always an even integer, matching Quantity B ('an even integer'). The two quantities are equal.",
    },

    # ================================================================
    # Even / Odd  MC Single Answer (section 21, Q9-15)
    # ================================================================

    ("number-properties", 21, 9): {
        "answer": "A",
        "explanation": r"If \(n\) is odd: (A) \(n+1\) = odd + 1 = even. Must be even. (B) \(n+2\) = odd + 2 = odd. (C) \(n^2\) = odd. (D) \(2n+1\) = even + 1 = odd. (E) \(n^3\) = odd. Answer: A.",
    },
    ("number-properties", 21, 10): {
        "answer": "A",
        "explanation": r"With \(a\) even and \(b\) odd: (A) \(a + b\) = even + odd = odd. Must be odd. (B) \(a - b\) = even - odd = odd. Also odd. (C) \(ab\) = even \(\times\) odd = even. Not odd. (D) \(a^2 + b\) = even + odd = odd. (E) \(a + b^2\) = even + odd = odd. Choices A, B, D, and E are all always odd, but A is the most straightforward answer. Answer: A.",
    },
    ("number-properties", 21, 11): {
        "answer": "B",
        "explanation": r"\(n^2 + n = n(n+1)\). Since \(n\) and \(n+1\) are consecutive integers, one is always even, so their product is always even. (A) \(n^2 + 1\): if \(n\) is odd, \(n^2 + 1\) = odd + 1 = even; if \(n\) is even, \(n^2 + 1\) = even + 1 = odd. Not always even. (C) \(n^2 + n + 1\): since \(n^2 + n\) is always even, \(n^2 + n + 1\) is always odd. (D) \(2n + 1\) is always odd. (E) \(n^3\): odd if \(n\) is odd. Answer: B.",
    },
    ("number-properties", 21, 12): {
        "answer": "B",
        "explanation": r"If \(n\) is even, write \(n = 2k\). (A) \(n/2 = k\), which could be odd or even. Not necessarily true. (B) \(n^2 = (2k)^2 = 4k^2\), which is always divisible by 4. Must be true. (C) \(n + 1\) = even + 1 = odd. Not even. (D) \(n^3 = (2k)^3 = 8k^3\), which is even, not odd. (E) \(3n + 1\) = even + 1 = odd, not even. Answer: B.",
        "common_mistake": r"For (A), students may think \(n/2\) is always even. But if \(n = 2\), then \(n/2 = 1\), which is odd.",
    },
    ("number-properties", 21, 13): {
        "answer": "A",
        "explanation": r"If \(n\) is odd, write \(n = 2k+1\). Then \(n^2 - 1 = (2k+1)^2 - 1 = 4k^2 + 4k + 1 - 1 = 4k^2 + 4k = 4k(k+1)\). Since \(k\) and \(k+1\) are consecutive, one is even, so \(k(k+1)\) is divisible by 2. Thus \(4k(k+1)\) is divisible by 8. Answer: A) \(n^2 - 1\).",
    },
    ("number-properties", 21, 14): {
        "answer": "B",
        "explanation": r"If \(a, b, c\) are consecutive integers, one of them is divisible by 2 (at least), so the product \(abc\) is always even. In fact, among three consecutive integers, at least one is even. (A) \(a + b + c = 3b\), which could be odd (e.g., \(b = 1\): sum = 3). (C) Sum of squares: try 1, 2, 3: \(1 + 4 + 9 = 14\) (even), try 2, 3, 4: \(4 + 9 + 16 = 29\) (odd). Not always even. (D) \(ab + bc + ca\): try 1, 2, 3: \(2 + 6 + 3 = 11\) (odd). Not always even. Answer: B) \(abc\).",
    },
    ("number-properties", 21, 15): {
        "answer": "A",
        "explanation": r"If \(n\) is odd, \(n^2\) is odd, \(3n\) is odd, so \(n^2 + 3n = \text{odd} + \text{odd} = \text{even}\). Then \(n^2 + 3n + 2 = \text{even} + 2 = \text{even}\). Alternatively, factor: \(n^2 + 3n + 2 = (n+1)(n+2)\). If \(n\) is odd, \(n+1\) is even, so the product is even. Answer: A) Always even.",
    },

    # ================================================================
    # Even / Odd  MC Select One or More (section 22, Q16-20)
    # ================================================================

    ("number-properties", 22, 16): {
        "answer": ["A", "B", "C", "D"],
        "explanation": r"(A) \(n(n+1)\): product of consecutive integers, always even. Yes. (B) \(n^2 - n = n(n-1)\): product of consecutive integers, always even. Yes. (C) \(n^2 + n = n(n+1)\): same as (A), always even. Yes. (D) \(2n + 2 = 2(n+1)\): always divisible by 2, so always even. Yes. (E) \(n(n+2)\): if \(n = 1\), \(1 \times 3 = 3\) (odd). Not always even. No.",
        "common_mistake": r"For (E), note that \(n\) and \(n+2\) have the same parity (both even or both odd). If both are odd, the product is odd. So \(n(n+2)\) is not always even.",
    },
    ("number-properties", 22, 17): {
        "answer": ["A", "B", "D", "E"],
        "explanation": r"With \(a\) and \(b\) both odd: (A) \(a + b\): odd + odd = even. Yes. (B) \(a - b\): odd - odd = even. Yes. (C) \(ab\): odd \(\times\) odd = odd. No. (D) \(a^2 - b^2 = (a-b)(a+b)\): both factors are even, so the product is even (divisible by 4). Yes. (E) \(a^2 + b^2\): odd + odd = even. Yes.",
    },
    ("number-properties", 22, 18): {
        "answer": ["A", "B", "D", "E"],
        "explanation": r"We need expressions that could be odd for some integer \(n\). (A) \(n^2\): if \(n\) is odd, \(n^2\) is odd. Yes. (B) \(n^2 + 1\): if \(n\) is even, \(n^2 + 1\) is odd. Yes. (C) \(n^2 - n = n(n-1)\): product of consecutive integers, always even. Cannot be odd. No. (D) \(n^3\): if \(n\) is odd, \(n^3\) is odd. Yes. (E) \(2n^2 + n = n(2n + 1)\). If \(n\) is odd, \(2n + 1\) is odd, so \(n(2n+1) = \text{odd} \times \text{odd} = \text{odd}\). Yes.",
    },
    ("number-properties", 22, 19): {
        "answer": ["A", "B", "C", "D"],
        "explanation": r"If \(n\) is even, write \(n = 2k\). (A) \(n^2 = 4k^2\), divisible by 4. Yes. (B) \(2n = 4k\), divisible by 4. Yes. (C) \(n(n+2) = 2k(2k+2) = 4k(k+1)\), divisible by 4. Yes. (D) \(n^3 = 8k^3\), divisible by 8 (and hence by 4). Yes. (E) \(4n + 2 = 8k + 2 = 2(4k+1)\). Since \(4k+1\) is odd, this is not divisible by 4. No.",
    },
    ("number-properties", 22, 20): {
        "answer": ["C"],
        "explanation": r"With \(a\) even and \(b\) odd: (A) \(a + b\) = even + odd = odd. Always odd. (B) \(a - b\) = even - odd = odd. Always odd. (C) \(ab\) = even \(\times\) odd = even. Always even. Could be even. Yes. (D) \(a^2 + b^2\) = even + odd = odd. Always odd. (E) \(2a + b\) = even + odd = odd. Always odd. Only (C) could be even (it is always even).",
    },

    # ================================================================
    # Even / Odd  Numeric Entry (section 23, Q21-27)
    # ================================================================

    ("number-properties", 23, 21): {
        "answer": "1",
        "explanation": r"If \(n\) is odd, write \(n = 2k + 1\). Then \(n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1\). So \(n^2 \div 4\) leaves remainder 1.",
    },
    ("number-properties", 23, 22): {
        "answer": "16",
        "explanation": r"If \(n\) is even, the possible values of \(n^2\) are \(0, 4, 16, 36, \ldots\). We need the smallest \(n^2 > 10\). \(n = 2\): \(n^2 = 4 < 10\). \(n = 4\): \(n^2 = 16 > 10\). The answer is 16.",
        "common_mistake": r"Students might try \(n = 3\), but 3 is odd. The question specifies \(n\) is even. The smallest even integer whose square exceeds 10 is \(n = 4\).",
    },
    ("number-properties", 23, 23): {
        "answer": "0",
        "explanation": r"If \(a\) and \(b\) are consecutive integers, one is even and one is odd. Their product is always even, so \(ab \div 2\) leaves remainder 0.",
    },
    ("number-properties", 23, 24): {
        "answer": "0",
        "explanation": r"If \(n\) is odd, write \(n = 2k+1\). Then \(n^2 - 1 = (2k+1)^2 - 1 = 4k^2 + 4k = 4k(k+1)\). Since \(k(k+1)\) is the product of consecutive integers, it is always even: \(k(k+1) = 2m\). So \(n^2 - 1 = 8m\), and the remainder when divided by 8 is 0.",
    },
    ("number-properties", 23, 25): {
        "answer": "12",
        "explanation": r"If \(n\) is even and greater than 2, the smallest such \(n\) is 4. Then \(n^2 - 4 = 16 - 4 = 12\). For \(n = 6\): \(36 - 4 = 32\), which is larger. So the least possible value is 12.",
    },
    ("number-properties", 23, 26): {
        "answer": "19",
        "explanation": r"We need odd integers \(a + b = 20\) with \(ab\) minimized and positive. Since \(a\) and \(b\) are odd and sum to 20, possible pairs: \((1,19), (3,17), (5,15), (7,13), (9,11)\). Products: \(19, 51, 75, 91, 99\). The least positive value of \(ab\) is 19 (when \(a = 1, b = 19\)).",
        "common_mistake": r"Students might forget to check all odd pairs or might start from the middle. The minimum product of two numbers with a fixed sum occurs when the numbers are as far apart as possible.",
    },
    ("number-properties", 23, 27): {
        "answer": "2",
        "explanation": r"\(n^4 - n^2 = n^2(n^2 - 1) = n^2(n-1)(n+1)\). This is the product of \(n^2\), \(n-1\), and \(n+1\). Among any three consecutive integers \(n-1, n, n+1\), at least one is even, making the product even. Additionally, \(n^2\) times an even number is even. More directly: if \(n\) is even, \(n^2\) is even, so the product is even; if \(n\) is odd, \(n-1\) is even, so the product is even. The expression is always even, never odd. No such integer exists. Enter 2.",
    },
}
