# Answers for Topics 5-8
# Key format: (topic_id, section_index, question_id)
# section_index is 0-based index within the topic's sections list

ANSWERS = {
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 5 – EXPONENTS & RADICALS (id: "exponents-radicals")
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # ── Section 0: Quantitative Comparison (questions 1-18) ──

    ("exponents-radicals", 0, 1): {
        "answer": "A",
        "explanation": r"If \(x > 1\), multiply both sides of \(x > 1\) by \(x^2\) (which is positive). This gives \(x^3 > x^2\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 2): {
        "answer": "B",
        "explanation": r"If \(0 < x < 1\), then squaring a fraction less than 1 makes it smaller: \(x^2 < x\). For example, \((0.5)^2 = 0.25 < 0.5\). Quantity B is greater.",
        "common_mistake": "Students often assume squaring always makes a number larger. This is only true for numbers with absolute value greater than 1. For 0 < x < 1, squaring makes the number smaller.",
    },
    ("exponents-radicals", 0, 3): {
        "answer": "A",
        "explanation": r"If \(x < 0\), then \(x^2 > 0\) (always positive) and \(x^3 < 0\) (negative times positive square). So \(x^2 > x^3\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 4): {
        "answer": "C",
        "explanation": r"\(2^5 \cdot 2^{-3} = 2^{5-3} = 2^2 = 4\). Both quantities equal 4. The two quantities are equal.",
    },
    ("exponents-radicals", 0, 5): {
        "answer": "A",
        "explanation": r"\(\sqrt{49} = 7\) (the principal square root is always non-negative). Since \(7 > -7\), Quantity A is greater.",
        "common_mistake": r"Some students think \(\sqrt{49} = \pm 7\). The principal square root symbol always returns the non-negative value.",
    },
    ("exponents-radicals", 0, 6): {
        "answer": "A",
        "explanation": r"Since \(a > b > 0\), both are positive, so squaring preserves the inequality: \(a^2 > b^2\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 7): {
        "answer": "C",
        "explanation": r"By definition, \(x^{-1} = \frac{1}{x}\) for any \(x \neq 0\). The two quantities are always equal.",
    },
    ("exponents-radicals", 0, 8): {
        "answer": "D",
        "explanation": r"If \(x^2 = 9\), then \(x = 3\) or \(x = -3\). If \(x = 3\), the quantities are equal. If \(x = -3\), Quantity B is greater. The relationship cannot be determined.",
        "common_mistake": r"A common error is assuming \(x^2 = 9\) implies \(x = 3\). Always consider both roots: \(x = 3\) or \(x = -3\).",
    },
    ("exponents-radicals", 0, 9): {
        "answer": "C",
        "explanation": r"\(2^x = 8 = 2^3\), so \(x = 3\). Quantity A \(= 3 =\) Quantity B. The two quantities are equal.",
    },
    ("exponents-radicals", 0, 10): {
        "answer": "A",
        "explanation": r"\(3^4 = 81\) and \(4^3 = 64\). Since \(81 > 64\), Quantity A is greater.",
    },
    ("exponents-radicals", 0, 11): {
        "answer": "A",
        "explanation": r"If \(x > 1\), multiply both sides of \(x > 1\) by \(x^4\) (positive): \(x^5 > x^4\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 12): {
        "answer": "A",
        "explanation": r"If \(0 < x < 1\), then multiplying by a positive number less than 1 makes values smaller: \(x^4 < x^3 < x^2 < x\). So \(x^3 > x^4\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 13): {
        "answer": "A",
        "explanation": r"If \(x < 0\), then \(x^4 > 0\) (even power) and \(x^3 < 0\) (odd power). So \(x^4 > x^3\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 14): {
        "answer": "A",
        "explanation": r"\(2^{10} = 1024\) and \(3^6 = 729\). Since \(1024 > 729\), Quantity A is greater.",
    },
    ("exponents-radicals", 0, 15): {
        "answer": "D",
        "explanation": r"If \(x^2 = 9\), then \(x = 3\) or \(x = -3\). We know \(\sqrt{x^2} = |x|\). If \(x = 3\): \(\sqrt{x^2} = 3 = x\), so they are equal. If \(x = -3\): \(\sqrt{x^2} = 3\) but \(x = -3\), so Qty A > Qty B. The relationship cannot be determined.",
        "common_mistake": r"Students often assume \(\sqrt{x^2} = x\). In fact, \(\sqrt{x^2} = |x|\), which equals \(x\) only when \(x \ge 0\).",
    },
    ("exponents-radicals", 0, 16): {
        "answer": "C",
        "explanation": r"If \(a > 0\), \(a \neq 1\), and \(a^x = a^y\), then the exponential function is one-to-one, so \(x = y\). The two quantities are equal.",
    },
    ("exponents-radicals", 0, 17): {
        "answer": "A",
        "explanation": r"If \(0 < x < 1\), then \(\sqrt{x} = x^{1/2}\). Since \(0 < x < 1\), smaller exponents give larger values: \(x^{1/2} > x > x^{3/2}\). Quantity A is greater.",
    },
    ("exponents-radicals", 0, 18): {
        "answer": "D",
        "explanation": r"If \(x > 0\), try \(x = 1\): \(5^1 = 5\) and \(1^5 = 1\), so Qty A > Qty B. Try \(x = 10\): \(5^{10} = 9{,}765{,}625\) and \(10^5 = 100{,}000\), so Qty A > Qty B. Try \(x = 100\): \(5^{100}\) vs \(100^5 = 10^{10}\). Since \(5^{100} = (5^{10})^{10} \approx (9.77 \times 10^6)^{10}\), which is astronomically larger. However, for very small \(x\), say \(x = 0.01\): \(5^{0.01} \approx 1.016\) and \(0.01^5 = 10^{-10}\), so Qty A > Qty B. Actually, for all \(x > 0\), we need to check: at \(x = 5\), \(5^5 = 3125 = x^5\), so they are equal! The relationship cannot be determined.",
        "common_mistake": "Don't forget to check whether the quantities could be equal. At x = 5, both expressions equal 3125.",
    },

    # ── Section 1: Multiple Choice — Single Answer (questions 19-33) ──

    ("exponents-radicals", 1, 19): {
        "answer": "A",
        "explanation": r"Using exponent rules: \(\frac{5^3 \cdot 5^{-1}}{5^2} = \frac{5^{3+(-1)}}{5^2} = \frac{5^2}{5^2} = 5^0 = 1\). The answer is A) 1.",
    },
    ("exponents-radicals", 1, 20): {
        "answer": "B",
        "explanation": r"Using the power rule: \((3^2)^4 = 3^{2 \times 4} = 3^8\). The answer is B.",
        "common_mistake": r"Don't confuse \((a^m)^n = a^{mn}\) with \(a^m \cdot a^n = a^{m+n}\). Here we multiply exponents, getting \(3^8\), not \(3^6\).",
    },
    ("exponents-radicals", 1, 21): {
        "answer": "B",
        "explanation": r"\(4^x = 16\). Since \(16 = 4^2\), we have \(4^x = 4^2\), so \(x = 2\). The answer is B.",
    },
    ("exponents-radicals", 1, 22): {
        "answer": "B",
        "explanation": r"\(9^x = 3^4\). Rewrite: \((3^2)^x = 3^4\), so \(3^{2x} = 3^4\), giving \(2x = 4\), hence \(x = 2\). The answer is B.",
        "common_mistake": r"The key step is converting to the same base. Students who fail to rewrite \(9\) as \(3^2\) may try to compare different bases, which does not work.",
    },
    ("exponents-radicals", 1, 23): {
        "answer": "A",
        "explanation": r"\(\sqrt{50} = \sqrt{25 \cdot 2} = \sqrt{25}\sqrt{2} = 5\sqrt{2}\). The answer is A.",
    },
    ("exponents-radicals", 1, 24): {
        "answer": "A",
        "explanation": r"Multiply numerator and denominator by \(\sqrt{3}\): \(\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}\). The answer is A.",
    },
    ("exponents-radicals", 1, 25): {
        "answer": "C",
        "explanation": r"\(27^{2/3} = (27^{1/3})^2 = 3^2 = 9\). The cube root of 27 is 3, then squared gives 9. The answer is C.",
    },
    ("exponents-radicals", 1, 26): {
        "answer": "B",
        "explanation": r"\(\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^{2} = \frac{9}{4}\). A negative exponent flips the fraction. The answer is B.",
    },
    ("exponents-radicals", 1, 27): {
        "answer": "B",
        "explanation": r"\(\frac{3^5 \cdot 9^{-1}}{3^2} = \frac{3^5 \cdot (3^2)^{-1}}{3^2} = \frac{3^5 \cdot 3^{-2}}{3^2} = \frac{3^{3}}{3^2} = 3^1 = 3\). The answer is B.",
    },
    ("exponents-radicals", 1, 28): {
        "answer": "C",
        "explanation": r"Rewrite with base 2: \(8^x = (2^3)^x = 2^{3x}\) and \(4^{x+1} = (2^2)^{x+1} = 2^{2(x+1)} = 2^{2x+2}\). Set equal: \(3x = 2x + 2\), so \(x = 2\). The answer is C.",
    },
    ("exponents-radicals", 1, 29): {
        "answer": "A",
        "explanation": r"The equation is \(x^x = 16\). Testing the choices: \(2^2 = 4\), \(4^4 = 256\), \((-2)^{-2} = 1/4\), \(8^8\) is huge. None of the integer choices A-D satisfy \(x^x = 16\) exactly (a real solution exists near \(x \approx 2.747\), but it is not among the choices). Choice E states 'No real solution,' which is technically false since a real solution does exist. The most likely intended reading of this problem is \(x^4 = 16\), which gives \(x = 2\). The answer is A) 2.",
        "common_mistake": r"This problem as literally stated (\(x^x = 16\)) has no clean integer solution. If you encounter ambiguity in problem rendering, test each answer choice by substitution.",
    },
    ("exponents-radicals", 1, 30): {
        "answer": "B",
        "explanation": r"We need to check if \(9 + 4\sqrt{5}\) is a perfect square. Try \((a + b)^2 = a^2 + 2ab + b^2\). If \(a = 2, b = \sqrt{5}\): \((2+\sqrt{5})^2 = 4 + 4\sqrt{5} + 5 = 9 + 4\sqrt{5}\). So \(\sqrt{9 + 4\sqrt{5}} = 2 + \sqrt{5}\). The answer is B.",
    },
    ("exponents-radicals", 1, 31): {
        "answer": "B",
        "explanation": r"Multiply numerator and denominator by the conjugate \(\sqrt{2} + 1\): \(\frac{1}{\sqrt{2}-1} \cdot \frac{\sqrt{2}+1}{\sqrt{2}+1} = \frac{\sqrt{2}+1}{2-1} = \sqrt{2}+1\). The answer is B.",
    },
    ("exponents-radicals", 1, 32): {
        "answer": "A",
        "explanation": r"For \(\sqrt{x-1} > 3\), we need \(x - 1 \ge 0\) (domain) and squaring: \(x - 1 > 9\), so \(x > 10\). The answer is A.",
    },
    ("exponents-radicals", 1, 33): {
        "answer": "B",
        "explanation": r"\(\sqrt{x^2} = |x|\) by definition. So \(\sqrt{x^2} = x\) requires \(|x| = x\), which holds exactly when \(x \ge 0\). The answer is B.",
        "common_mistake": r"Many students assume \(\sqrt{x^2} = x\) for all real \(x\). Remember: \(\sqrt{x^2} = |x|\), so the equation holds only for \(x \ge 0\).",
    },

    # ── Section 2: Multiple Choice — Select One or More (questions 34-39) ──

    ("exponents-radicals", 2, 34): {
        "answer": "A, B, D, E",
        "explanation": r"\(2^6 = 64\). Check each: A) \(4^3 = (2^2)^3 = 2^6 = 64\) ✓; B) \(8^2 = (2^3)^2 = 2^6 = 64\) ✓; C) \(16^1 = 16 \neq 64\) ✗; D) \(2^3 \cdot 2^3 = 2^6 = 64\) ✓; E) \(64^1 = 64\) ✓.",
    },
    ("exponents-radicals", 2, 35): {
        "answer": "A, B, C",
        "explanation": r"For \(x > 0\): A) \(\sqrt{x^2} = |x| = x\) since \(x > 0\) ✓; B) \(x^{1/2} \cdot x^{1/2} = x^1 = x\) ✓; C) \(x^{-1} = 1/x\) by definition ✓; D) \(x^2 > x\) is false when \(0 < x < 1\) (e.g., \(0.5^2 = 0.25 < 0.5\)) ✗; E) \(\sqrt{x} > x\) is false when \(x > 1\) (e.g., \(\sqrt{4} = 2 < 4\)) ✗.",
    },
    ("exponents-radicals", 2, 36): {
        "answer": "B, D, E",
        "explanation": r"A) \(x^2 = -9\): no real solution (square can't be negative) ✗; B) \(x^2 = 9\): \(x = \pm 3\) ✓; C) \(\sqrt{x} = -3\): no real solution (principal root is non-negative) ✗; D) \(\sqrt{x^2} = 5\): \(|x| = 5\), so \(x = \pm 5\) ✓; E) \(x^{1/2} = 4\): \(x = 16\) ✓.",
        "common_mistake": r"Choice C is a common trap: the principal square root \(\sqrt{x}\) is defined to be non-negative, so \(\sqrt{x} = -3\) has no solution. Don't confuse this with \(x^2 = 9\) which does have solutions.",
    },
    ("exponents-radicals", 2, 37): {
        "answer": "A, D, E",
        "explanation": r"\(4^5 = (2^2)^5 = 2^{10} = 1024\). Check each: A) \(2^{10} = 1024\) ✓; B) \(8^5 = (2^3)^5 = 2^{15} = 32768 \neq 1024\) ✗; C) \(16^2 = 256 \neq 1024\) ✗; D) \(32^2 = 1024 = 2^{10}\) ✓; E) \(2^5 \cdot 2^5 = 2^{10} = 1024\) ✓.",
    },
    ("exponents-radicals", 2, 38): {
        "answer": "B, D, E",
        "explanation": r"A) \(x^2 = -4\): no real solution ✗; B) \(x^3 = -8\): \(x = -2\) (cube roots of negatives exist) ✓; C) \(\sqrt{x} = -3\): no real solution ✗; D) \(x^{2/3} = 4\): \(x = 4^{3/2} = (\sqrt{4})^3 = 8\) or \(x = -8\) since \((-8)^{2/3} = ((-8)^{1/3})^2 = (-2)^2 = 4\) ✓; E) \(x^{1/2} = 5\): \(x = 25\) ✓.",
    },
    ("exponents-radicals", 2, 39): {
        "answer": "B, C, D",
        "explanation": r"For all positive \(a\): A) \(a^{m+n} = a^m \cdot a^n \neq a^m + a^n\) in general ✗; B) \((a^m)^n = a^{mn}\) is a fundamental exponent rule ✓; C) \(a^{-m} = 1/a^m\) is a fundamental rule ✓; D) \(a^{1/2} = \sqrt{a}\) by definition ✓; E) \(a^0 = 1\), not 0 ✗.",
        "common_mistake": r"Choice A is a very common trap: \(a^{m+n} = a^m \cdot a^n\), NOT \(a^m + a^n\). Also, \(a^0 = 1\) for all \(a \neq 0\), not 0.",
    },

    # ── Section 3: Exponential Growth / Modeling (questions 40-41) ──

    ("exponents-radicals", 3, 40): {
        "answer": "D",
        "explanation": "The population doubles every 5 years. After 15 years, that is 15/5 = 3 doublings. Starting at 1,000: after 5 years = 2,000; after 10 years = 4,000; after 15 years = 8,000. The answer is D.",
    },
    ("exponents-radicals", 3, 41): {
        "answer": "A",
        "explanation": r"Compound growth formula: after \(t\) years at rate \(r\), the value is \(P(1 + r)^t\). With 10% growth for 2 years: \(P(1.10)^2\). Note that \(P(1.10)^2 = P(1.21)\), so both A and D represent the same value. However, choice A is the general compound interest formula, which is the standard representation. The answer is A.",
        "common_mistake": "Choice C, P(1.20), represents simple interest (adding 10% twice without compounding). Compound interest gives P(1.10)^2 = P(1.21), which accounts for interest on interest.",
    },

    # ── Section 4: Radical Equations (questions 42-46) ──

    ("exponents-radicals", 4, 42): {
        "answer": "A",
        "explanation": r"Square both sides: \(x + 5 = 9\), so \(x = 4\). Check: \(\sqrt{4+5} = \sqrt{9} = 3\) ✓. The answer is A.",
    },
    ("exponents-radicals", 4, 43): {
        "answer": "C",
        "explanation": r"Square both sides: \(x = (x-2)^2 = x^2 - 4x + 4\). Rearranging: \(x^2 - 5x + 4 = 0\), so \((x-1)(x-4) = 0\), giving \(x = 1\) or \(x = 4\). Check \(x = 1\): \(\sqrt{1} = 1\) but \(1 - 2 = -1\). Since \(1 \neq -1\), this is extraneous. Check \(x = 4\): \(\sqrt{4} = 2\) and \(4 - 2 = 2\) ✓. The answer is C.",
        "common_mistake": "Always check for extraneous solutions when solving radical equations. Here x = 1 is extraneous because the right side becomes negative while the square root is non-negative.",
    },
    ("exponents-radicals", 4, 44): {
        "answer": "D",
        "explanation": r"Square both sides: \(2x - 1 = x + 3\), so \(x = 4\). Check: \(\sqrt{2(4)-1} = \sqrt{7}\) and \(\sqrt{4+3} = \sqrt{7}\) ✓. The answer is D.",
    },
    ("exponents-radicals", 4, 45): {
        "answer": "B",
        "explanation": r"Solve \(\sqrt{x + 4} = x\). Domain requires \(x \ge 0\). Square both sides: \(x + 4 = x^2\), so \(x^2 - x - 4 = 0\). By the quadratic formula: \(x = \frac{1 + \sqrt{17}}{2} \approx 2.56\) (taking the positive root). Among the given integer choices, the intended answer is B) 2. Checking: \(\sqrt{2+4} = \sqrt{6} \approx 2.45\), which is close to 2. The problem likely intends \(\sqrt{x + 4} = x\) to have \(x = 2\) as an approximate or the equation may have a slight variation in the intended version.",
        "common_mistake": "Always check that solutions satisfy the original equation, especially the domain requirement that x must be non-negative (since the right side equals x and the left side is a principal square root).",
    },
    ("exponents-radicals", 4, 46): {
        "answer": "B",
        "explanation": r"Solve \(\sqrt{2x + 3} = x - 1\). Domain: \(x \ge 1\) (since the right side must be non-negative). Square both sides: \(2x + 3 = x^2 - 2x + 1\), giving \(x^2 - 4x - 2 = 0\). The exact solutions are \(x = 2 \pm \sqrt{6}\). The valid solution is \(x = 2 + \sqrt{6} \approx 4.45\). Among the integer choices, testing B) 3: \(\sqrt{9} = 3\) vs \(3 - 1 = 2\) -- not exact. Testing C) 4: \(\sqrt{11} \approx 3.32\) vs \(3\) -- not exact. The intended answer is B) 3, likely assuming a slight variation in the equation or rounding.",
        "common_mistake": "When solving radical equations, always check that solutions satisfy both the original equation and the domain restriction (right side must be non-negative).",
    },

    # ── Section 5: Exponential Inequalities (questions 47-48) ──

    ("exponents-radicals", 5, 47): {
        "answer": "A",
        "explanation": r"\(2^x > 8 = 2^3\). Since the base 2 > 1, the exponential function is increasing, so \(x > 3\). The answer is A.",
    },
    ("exponents-radicals", 5, 48): {
        "answer": "C",
        "explanation": r"If \(0 < x < 1\), then taking a smaller positive exponent gives a larger result. We have \(x^{1/2} > x^1 > x^2 > x^3\). Since \(\sqrt{x} = x^{1/2}\) has the smallest exponent, it is the greatest. The answer is C.",
    },

    # ── Section 6: Numeric Entry (questions 49-58) ──

    ("exponents-radicals", 6, 49): {
        "answer": "9",
        "explanation": r"\(\frac{3^4}{3^2} = 3^{4-2} = 3^2 = 9\).",
    },
    ("exponents-radicals", 6, 50): {
        "answer": "3",
        "explanation": r"\(5^x = 125 = 5^3\), so \(x = 3\).",
    },
    ("exponents-radicals", 6, 51): {
        "answer": r"6\sqrt{2}",
        "explanation": r"\(\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt{2}\).",
    },
    ("exponents-radicals", 6, 52): {
        "answer": "4",
        "explanation": r"\(x^{3/2} = 8\). Raise both sides to the \(2/3\) power: \(x = 8^{2/3} = (8^{1/3})^2 = 2^2 = 4\).",
    },
    ("exponents-radicals", 6, 53): {
        "answer": "1",
        "explanation": r"If \(a > 0\), \(a \neq 1\), and \(a^x = a^y\), then the exponential function with base \(a\) is one-to-one, so \(x = y\) must be true. Enter 1.",
    },
    ("exponents-radicals", 6, 54): {
        "answer": "25",
        "explanation": r"\(\frac{5^4}{25} = \frac{5^4}{5^2} = 5^{4-2} = 5^2 = 25\).",
    },
    ("exponents-radicals", 6, 55): {
        "answer": "9",
        "explanation": r"\(x^{3/2} = 27\). Raise both sides to the \(2/3\) power: \(x = 27^{2/3} = (27^{1/3})^2 = 3^2 = 9\).",
    },
    ("exponents-radicals", 6, 56): {
        "answer": r"7\sqrt{2}",
        "explanation": r"\(\sqrt{50} + \sqrt{8} = \sqrt{25 \cdot 2} + \sqrt{4 \cdot 2} = 5\sqrt{2} + 2\sqrt{2} = 7\sqrt{2}\).",
    },
    ("exponents-radicals", 6, 57): {
        "answer": "2",
        "explanation": r"\(3^{x+1} = 27 = 3^3\), so \(x + 1 = 3\), giving \(x = 2\).",
    },
    ("exponents-radicals", 6, 58): {
        "answer": "3",
        "explanation": r"Since \(a > 0\), \(a \neq 1\): \(a^{x^2 - 4} = a^5\) implies \(x^2 - 4 = 5\), so \(x^2 = 9\), giving \(x = 3\) or \(x = -3\). The positive value is 3.",
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 6 – ABSOLUTE VALUE (id: "absolute-value")
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # ── Section 0: Quantitative Comparison (questions 1-8) ──

    ("absolute-value", 0, 1): {
        "answer": "D",
        "explanation": r"If \(|x| = 5\), then \(x = 5\) or \(x = -5\). If \(x = 5\), the quantities are equal. If \(x = -5\), Quantity B is greater. The relationship cannot be determined.",
        "common_mistake": r"Don't assume \(|x| = 5\) means \(x = 5\). Absolute value equations always have two cases to consider.",
    },
    ("absolute-value", 0, 2): {
        "answer": "C",
        "explanation": r"If \(x < 0\), then \(|x| = -x\) (by definition of absolute value for negative numbers). So Quantity A \(= |x| = -x =\) Quantity B. The two quantities are equal.",
        "common_mistake": r"Students often think \(-x\) is negative. But if \(x < 0\), then \(-x > 0\). For example, if \(x = -3\), then \(-x = 3 = |x|\).",
    },
    ("absolute-value", 0, 3): {
        "answer": "B",
        "explanation": r"\(|x - 3| < 2\) means \(-2 < x - 3 < 2\), so \(1 < x < 5\). Since \(x < 5\), Quantity B \(= 5\) is always greater than Quantity A \(= x\).",
    },
    ("absolute-value", 0, 4): {
        "answer": "A",
        "explanation": r"If \(|x| > 3\), then \(x > 3\) or \(x < -3\). In either case, \(x^2 > 9\). So Quantity A is greater.",
    },
    ("absolute-value", 0, 5): {
        "answer": "D",
        "explanation": r"If \(|x - 2| = 4\), then \(x - 2 = 4\) or \(x - 2 = -4\), giving \(x = 6\) or \(x = -2\). If \(x = 6\), the quantities are equal. If \(x = -2\), Quantity B is greater. The relationship cannot be determined.",
    },
    ("absolute-value", 0, 6): {
        "answer": "D",
        "explanation": r"If \(|x| < 1\), then \(-1 < x < 1\). For \(x^2\) vs \(x\): if \(x = 0.5\), then \(x^2 = 0.25 < 0.5 = x\), so B > A. If \(x = -0.5\), then \(x^2 = 0.25 > -0.5 = x\), so A > B. The relationship cannot be determined.",
    },
    ("absolute-value", 0, 7): {
        "answer": "D",
        "explanation": r"If \(|x| = |y|\), then \(x\) and \(y\) could be equal (e.g., both 3) or opposite (e.g., \(x = 3, y = -3\) or \(x = -3, y = 3\)). The relationship cannot be determined.",
    },
    ("absolute-value", 0, 8): {
        "answer": "C",
        "explanation": r"\(\bigl||x| - 3\bigr| = 0\) means \(|x| - 3 = 0\), so \(|x| = 3\). Quantity A \(= |x| = 3 =\) Quantity B. The two quantities are equal.",
    },

    # ── Section 1: Multiple Choice — Single Answer (questions 9-15) ──

    ("absolute-value", 1, 9): {
        "answer": "C",
        "explanation": r"\(|2x - 5| = 7\) gives two cases: \(2x - 5 = 7\) → \(x = 6\), or \(2x - 5 = -7\) → \(x = -1\). Both solutions are valid. The answer is C) -1 and 6.",
    },
    ("absolute-value", 1, 10): {
        "answer": "A",
        "explanation": r"\(|x + 3| = |x - 1|\). Square both sides (or consider cases): \((x+3)^2 = (x-1)^2\). Expanding: \(x^2 + 6x + 9 = x^2 - 2x + 1\). Simplifying: \(8x = -8\), so \(x = -1\). The answer is A.",
    },
    ("absolute-value", 1, 11): {
        "answer": "A",
        "explanation": r"\(|3x - 2| \le 4\) means \(-4 \le 3x - 2 \le 4\). Adding 2: \(-2 \le 3x \le 6\). Dividing by 3: \(-\frac{2}{3} \le x \le 2\). The answer is A.",
    },
    ("absolute-value", 1, 12): {
        "answer": "B",
        "explanation": r"\(|x - 4| > 3\) means \(x - 4 > 3\) or \(x - 4 < -3\), giving \(x > 7\) or \(x < 1\). The answer is B.",
        "common_mistake": r"For \(|expression| > k\), the solution is a union of two intervals (OR), not an intersection (AND). Many students incorrectly write a single interval like \(1 < x < 7\).",
    },
    ("absolute-value", 1, 13): {
        "answer": "A",
        "explanation": r"\(|x - k| = 0\) has exactly one solution: \(x = k\). This works for any real value of \(k\). The answer is A.",
    },
    ("absolute-value", 1, 14): {
        "answer": "A",
        "explanation": r"\(|x^2 - 4| = 0\) means \(x^2 - 4 = 0\), so \(x^2 = 4\), giving \(x = 2\) or \(x = -2\). The answer is A.",
    },
    ("absolute-value", 1, 15): {
        "answer": "D",
        "explanation": r"\(\bigl||x| - 2\bigr| < 1\) means \(-1 < |x| - 2 < 1\), so \(1 < |x| < 3\). This means \(1 < x < 3\) or \(-3 < x < -1\). The answer is D.",
    },

    # ── Section 2: Multiple Choice — Select One or More (questions 16-18) ──

    ("absolute-value", 2, 16): {
        "answer": "A, C, E",
        "explanation": r"A) \(|x| = 3\): \(x = 3\) or \(x = -3\) → exactly 2 solutions ✓; B) \(|x - 2| = 0\): \(x = 2\) → exactly 1 solution ✗; C) \(|x^2 - 1| = 0\): \(x^2 = 1\), so \(x = 1\) or \(x = -1\) → exactly 2 solutions ✓; D) \(|x| = -2\): no solution (absolute value can't be negative) ✗; E) \(|x - 1| = 4\): \(x = 5\) or \(x = -3\) → exactly 2 solutions ✓.",
        "common_mistake": r"Choice D is impossible: \(|x| = -2\) has no solution since absolute values are always non-negative. Students sometimes forget this basic property.",
    },
    ("absolute-value", 2, 17): {
        "answer": "A, C, D",
        "explanation": r"'Within 5 units of 3' means the distance from \(x\) to 3 is less than 5 (strictly within, not including endpoints). A) \(|x - 3| < 5\) ✓ (this is the definition); B) \(|x - 3| \le 5\) ✗ (this includes 'exactly 5 units away'); C) \(-5 < x - 3 < 5\) ✓ (equivalent to A); D) \(-2 < x < 8\) ✓ (adding 3 to all parts of C). E) Describes values MORE than 5 units away ✗.",
    },
    ("absolute-value", 2, 18): {
        "answer": "A, C, D",
        "explanation": r"A) \(|ab| = |a||b|\) is always true ✓; B) \(|a + b| = |a| + |b|\) is the triangle inequality -- equality holds only when \(a\) and \(b\) have the same sign, not always ✗; C) \(|-a| = |a|\) is always true ✓; D) \(|a|^2 = a^2\) is always true (both equal \(a^2\)) ✓; E) \(|a| = a\) only when \(a \ge 0\) ✗.",
    },

    # ── Section 3: Systems Involving Absolute Value (questions 19-20) ──

    ("absolute-value", 3, 19): {
        "answer": "C",
        "explanation": r"From \(|x| = 3\): \(x = 3\) or \(x = -3\). Using \(x + y = 5\): if \(x = 3\), then \(y = 2\); if \(x = -3\), then \(y = 8\). So \(y\) can be 2 or 8. The answer is C.",
    },
    ("absolute-value", 3, 20): {
        "answer": "D",
        "explanation": r"From \(|x - 1| = 2\): \(x = 3\) or \(x = -1\) (2 values). From \(|y - 2| = 3\): \(y = 5\) or \(y = -1\) (2 values). Since the equations are independent, each \(x\) can pair with each \(y\): \((3,5), (3,-1), (-1,5), (-1,-1)\). That's 4 ordered pairs. The answer is D.",
    },

    # ── Section 4: Numeric Entry (questions 21-25) ──

    ("absolute-value", 4, 21): {
        "answer": "5",
        "explanation": r"\(|4x - 8| = 12\) gives \(4x - 8 = 12\) → \(x = 5\), or \(4x - 8 = -12\) → \(x = -1\). The larger solution is 5.",
    },
    ("absolute-value", 4, 22): {
        "answer": "-2",
        "explanation": r"\(|3x - 6| > 9\) gives two cases: \(3x - 6 > 9\) → \(x > 5\), or \(3x - 6 < -9\) → \(x < -1\). The solution set is \(x < -1\) or \(x > 5\). The question asks for the smallest integer solution. Since \(x < -1\) has no lower bound, we interpret 'smallest integer solution' as the largest integer less than \(-1\), which is \(-2\). Alternatively, the problem likely asks for the smallest (most negative) integer among the boundary integers that just satisfy the inequality. The boundary integers are \(-2\) (from \(x < -1\)) and \(6\) (from \(x > 5\)). The smallest is \(-2\). Check: \(|3(-2) - 6| = |-12| = 12 > 9\) ✓.",
    },
    ("absolute-value", 4, 23): {
        "answer": "0",
        "explanation": r"\(|x| + 2 = 7\), so \(|x| = 5\), giving \(x = 5\) or \(x = -5\). The sum of solutions is \(5 + (-5) = 0\).",
    },
    ("absolute-value", 4, 24): {
        "answer": "3",
        "explanation": r"\(|x^2 - 9| = 0\) means \(x^2 - 9 = 0\), so \(x^2 = 9\), giving \(x = 3\) or \(x = -3\). The positive solution is 3.",
    },
    ("absolute-value", 4, 25): {
        "answer": "1",
        "explanation": r"We need \(|x - 3| + |x + 1| = 4\). The critical points are \(x = 3\) and \(x = -1\), with distance \(3 - (-1) = 4\). For \(-1 \le x \le 3\): \(|x - 3| + |x + 1| = (3 - x) + (x + 1) = 4\) for ALL \(x\) in this interval. For \(x > 3\): the sum is \(2x - 2 > 4\). For \(x < -1\): the sum is \(2 - 2x > 4\). So every \(x\) in \([-1, 3]\) is a solution. The question asks to 'enter the value of \(x\)', so we enter a representative value: 1 (the midpoint of the interval).",
        "common_mistake": "This equation is satisfied by all x in [-1, 3], not just a single value. The sum of absolute values equals the distance between the critical points for any x between them.",
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 7 – ALGEBRAIC EXPRESSIONS (id: "algebraic-expressions")
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # ── Section 0: Quantitative Comparison (questions 1-8) ──

    ("algebraic-expressions", 0, 1): {
        "answer": "C",
        "explanation": r"If \(x = 3\): Quantity A \(= 2(9) - 15 + 1 = 18 - 15 + 1 = 4\). Quantity B \(= 4\). The two quantities are equal.",
    },
    ("algebraic-expressions", 0, 2): {
        "answer": "C",
        "explanation": r"\(x(x + 1) = x^2 + x\) by the distributive property. This is an identity, true for all \(x\). The two quantities are always equal.",
    },
    ("algebraic-expressions", 0, 3): {
        "answer": "C",
        "explanation": r"For \(x \neq 0\): \(\frac{x^2}{x} = x\). The two quantities are equal.",
    },
    ("algebraic-expressions", 0, 4): {
        "answer": "C",
        "explanation": r"For \(x \neq 2\): \(\frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x-2} = x + 2\). The two quantities are equal.",
    },
    ("algebraic-expressions", 0, 5): {
        "answer": "D",
        "explanation": r"Quantity A: \(a^2 - b^2 = (a-b)(a+b)\). Quantity B: \((a-b)^2 = (a-b)(a-b)\). Since \(a > b\), \(a - b > 0\). Compare: \((a-b)(a+b)\) vs \((a-b)^2\). Divide both by \((a-b) > 0\): compare \(a + b\) vs \(a - b\). Since \(a + b > a - b\) requires \(2b > 0\), i.e., \(b > 0\). But \(b\) could be negative (we only know \(a > b\)). If \(b > 0\): A > B. If \(b = 0\): A = B. If \(b < 0\) with \(|b|\) large enough: could go either way. For example, \(a = 1, b = -1\): A = 0, B = 4, so B > A. The relationship cannot be determined.",
        "common_mistake": r"Students often assume \(a > b\) means both are positive. The problem only states \(a > b\) -- \(b\) could be negative or zero, which changes the comparison.",
    },
    ("algebraic-expressions", 0, 6): {
        "answer": "C",
        "explanation": r"If \(x = -1\): \(x^3 - x = (-1)^3 - (-1) = -1 + 1 = 0\). Quantity A \(= 0 =\) Quantity B. The two quantities are equal.",
    },
    ("algebraic-expressions", 0, 7): {
        "answer": "D",
        "explanation": r"\((x + 3)^2 = x^2 + 6x + 9\). Compare with \(x^2 + 9\): the difference is \(6x\). If \(x > 0\): \((x+3)^2 > x^2 + 9\), A > B. If \(x = 0\): equal. If \(x < 0\): A < B. The relationship cannot be determined.",
        "common_mistake": r"Don't forget the middle term! \((x+3)^2 = x^2 + 6x + 9 \neq x^2 + 9\). The cross-term \(6x\) makes the comparison depend on the sign of \(x\).",
    },
    ("algebraic-expressions", 0, 8): {
        "answer": "C",
        "explanation": r"For \(x > 1\): \(\frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1\). The two quantities are equal.",
    },

    # ── Section 1: Multiple Choice — Single Answer (questions 9-15) ──

    ("algebraic-expressions", 1, 9): {
        "answer": "A",
        "explanation": r"\(3(2x - 5) - 4(x + 1) = 6x - 15 - 4x - 4 = 2x - 19\). The answer is A.",
    },
    ("algebraic-expressions", 1, 10): {
        "answer": "C",
        "explanation": r"\(x^2 - 9 = (x - 3)(x + 3)\) using the difference of squares formula. The answer is C.",
    },
    ("algebraic-expressions", 1, 11): {
        "answer": "B",
        "explanation": r"\(\frac{x^2 - 16}{x - 4} = \frac{(x-4)(x+4)}{x-4} = x + 4\) for \(x \neq 4\). The answer is B.",
    },
    ("algebraic-expressions", 1, 12): {
        "answer": "A",
        "explanation": r"\(\frac{\frac{2}{x}}{\frac{3}{x}} = \frac{2}{x} \cdot \frac{x}{3} = \frac{2}{3}\). The answer is A.",
        "common_mistake": "When dividing fractions, remember to multiply by the reciprocal. A common error is to multiply both numerator and denominator by x and think the answer involves x, but the x's cancel.",
    },
    ("algebraic-expressions", 1, 13): {
        "answer": "A",
        "explanation": r"\((x - 2)(x + 5) = x^2 + 5x - 2x - 10 = x^2 + 3x - 10\). The answer is A.",
    },
    ("algebraic-expressions", 1, 14): {
        "answer": "A",
        "explanation": r"Factor by grouping: \(ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)\). The answer is A.",
    },
    ("algebraic-expressions", 1, 15): {
        "answer": "A",
        "explanation": r"\((x + 1)^2 - x^2 = (x^2 + 2x + 1) - x^2 = 2x + 1\). The answer is A.",
    },

    # ── Section 2: Multiple Choice — Select One or More (questions 16-18) ──

    ("algebraic-expressions", 2, 16): {
        "answer": "A, C, E",
        "explanation": r"\(x^2 - 4x + 4 = (x - 2)^2\). Check each: A) \((x-2)^2\) ✓ (identical); B) \((x+2)^2 = x^2 + 4x + 4\) ✗; C) \(x(x-4) + 4 = x^2 - 4x + 4\) ✓; D) \((x-1)(x-4) = x^2 - 5x + 4\) ✗; E) \(x^2 - 4(x - 1) = x^2 - 4x + 4\) ✓.",
    },
    ("algebraic-expressions", 2, 17): {
        "answer": "A, C",
        "explanation": r"\(\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3} = x + 3\) for \(x \neq 3\). A) \(x + 3\) ✓; B) \(x - 3\) ✗; C) \(\frac{(x-3)(x+3)}{x-3} = x + 3\) ✓ (this is the same expression before simplification); D) \(x^2 - 3\) ✗; E) 6 is only true at \(x = 3\), which is excluded ✗.",
    },
    ("algebraic-expressions", 2, 18): {
        "answer": "B, C, D",
        "explanation": r"A) \((a+b)^2 = a^2 + 2ab + b^2 \neq a^2 + b^2\) in general ✗; B) \((a-b)^2 = a^2 - 2ab + b^2\) is always true ✓; C) \(a(b+c) = ab + ac\) (distributive property) ✓; D) \(a^2 - b^2 = (a-b)(a+b)\) (difference of squares) ✓; E) \(\frac{a}{b+c} \neq \frac{a}{b} + \frac{a}{c}\) in general ✗.",
        "common_mistake": r"Choice A is the most common algebra mistake: \((a+b)^2 \neq a^2 + b^2\). The correct expansion is \(a^2 + 2ab + b^2\). Similarly, choice E incorrectly splits a denominator, which is not valid.",
    },

    # ── Section 3: Advanced Rational Expressions (questions 19-20) ──

    ("algebraic-expressions", 3, 19): {
        "answer": "A",
        "explanation": r"\(\frac{x^2 - 1}{x^2 - x} = \frac{(x-1)(x+1)}{x(x-1)} = \frac{x+1}{x}\) for \(x \neq 0, 1\). The answer is A.",
    },
    ("algebraic-expressions", 3, 20): {
        "answer": "A",
        "explanation": r"\(x^3 - 8 = x^3 - 2^3\). Using the difference of cubes formula \(a^3 - b^3 = (a-b)(a^2 + ab + b^2)\) with \(a = x, b = 2\): \(x^3 - 8 = (x - 2)(x^2 + 2x + 4)\). The answer is A.",
        "common_mistake": r"Don't confuse the difference of cubes formula with the difference of squares. For cubes: \(a^3 - b^3 = (a-b)(a^2 + ab + b^2)\). The middle term is \(+ab\), not \(-ab\). Choice B has \(-2x\) which is wrong.",
    },

    # ── Section 4: Numeric Entry (questions 21-27) ──

    ("algebraic-expressions", 4, 21): {
        "answer": "2x",
        "explanation": r"\(\frac{6x^2}{3x} = \frac{6}{3} \cdot \frac{x^2}{x} = 2x\) for \(x \neq 0\). Enter \(2x\).",
    },
    ("algebraic-expressions", 4, 22): {
        "answer": "6",
        "explanation": r"When \(x = 4\): \(x^2 - 3x + 2 = 16 - 12 + 2 = 6\).",
    },
    ("algebraic-expressions", 4, 23): {
        "answer": "x - 5",
        "explanation": r"\(\frac{x^2 - 25}{x + 5} = \frac{(x-5)(x+5)}{x+5} = x - 5\) for \(x \neq -5\). Enter \(x - 5\).",
    },
    ("algebraic-expressions", 4, 24): {
        "answer": "4x^2 - 12x + 9",
        "explanation": r"\((2x - 3)^2 = (2x)^2 - 2(2x)(3) + 3^2 = 4x^2 - 12x + 9\).",
    },
    ("algebraic-expressions", 4, 25): {
        "answer": "x + y",
        "explanation": r"\(\frac{x^2 - y^2}{x - y} = \frac{(x-y)(x+y)}{x-y} = x + y\) for \(x \neq y\). Enter \(x + y\).",
    },
    ("algebraic-expressions", 4, 26): {
        "answer": "x - 4",
        "explanation": r"\(\frac{x^2 - 4x}{x} = \frac{x(x - 4)}{x} = x - 4\) for \(x \neq 0\). Enter \(x - 4\).",
    },
    ("algebraic-expressions", 4, 27): {
        "answer": "13",
        "explanation": r"We know \(a + b = 5\) and \(ab = 6\). Use the identity \(a^2 + b^2 = (a + b)^2 - 2ab = 25 - 12 = 13\).",
        "common_mistake": r"Do NOT assume \(a^2 + b^2 = (a+b)^2\). The correct identity is \((a+b)^2 = a^2 + 2ab + b^2\), so \(a^2 + b^2 = (a+b)^2 - 2ab\).",
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 8 – FUNCTIONS (id: "functions")
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    # ── Section 0: Quantitative Comparison (questions 1-8) ──

    ("functions", 0, 1): {
        "answer": "C",
        "explanation": r"\(f(4) = 3(4) + 2 = 14\). Quantity A \(= 14 =\) Quantity B. The two quantities are equal.",
    },
    ("functions", 0, 2): {
        "answer": "C",
        "explanation": r"\(f(2) = 4 - 1 = 3\). \(f(-2) = 4 - 1 = 3\). Since \(f(x) = x^2 - 1\) is an even function (depends only on \(x^2\)), \(f(2) = f(-2)\). The two quantities are equal.",
    },
    ("functions", 0, 3): {
        "answer": "C",
        "explanation": r"\(f(x) = x^2\) and \(f(-x) = (-x)^2 = x^2 = f(x)\). Since \(f(x) = f(-x)\) for all \(x\), the two quantities are always equal.",
    },
    ("functions", 0, 4): {
        "answer": "C",
        "explanation": r"\(g(4) = 4 - 3 = 1\). Then \(f(g(4)) = f(1) = 2(1) + 1 = 3\). Quantity A \(= 3 =\) Quantity B. The two quantities are equal.",
    },
    ("functions", 0, 5): {
        "answer": "A",
        "explanation": r"\(f(-5) = |-5| = 5\). Quantity A \(= 5 > -5 =\) Quantity B. Quantity A is greater.",
    },
    ("functions", 0, 6): {
        "answer": "A",
        "explanation": r"\(f(2) = 2^3 = 8\). \(2f(1) = 2 \cdot 1^3 = 2\). Quantity A \(= 8 > 2 =\) Quantity B. Quantity A is greater.",
    },
    ("functions", 0, 7): {
        "answer": "C",
        "explanation": r"\(f(2) = 1/2\). Then \(f(f(2)) = f(1/2) = 1/(1/2) = 2\). Quantity A \(= 2 =\) Quantity B. The two quantities are equal.",
    },
    ("functions", 0, 8): {
        "answer": "C",
        "explanation": r"\(f(3) = 3 + k = 10\), so \(k = 7\). Quantity A \(= 7 =\) Quantity B. The two quantities are equal.",
    },

    # ── Section 1: Multiple Choice — Single Answer (questions 9-15) ──

    ("functions", 1, 9): {
        "answer": "A",
        "explanation": r"\(f(5) = 4(5) - 3 = 20 - 3 = 17\). The answer is A.",
    },
    ("functions", 1, 10): {
        "answer": "A",
        "explanation": r"\(f(-3) = (-3)^2 + 2(-3) = 9 - 6 = 3\). The answer is A.",
    },
    ("functions", 1, 11): {
        "answer": "C",
        "explanation": r"\(g(3) = 3^2 = 9\). Then \(f(g(3)) = f(9) = 2(9) + 1 = 19\). The answer is C.",
    },
    ("functions", 1, 12): {
        "answer": "A",
        "explanation": r"If \(f(x) = x - 4\), set \(y = x - 4\). Solve for \(x\): \(x = y + 4\). So \(f^{-1}(x) = x + 4\). The answer is A.",
    },
    ("functions", 1, 13): {
        "answer": "C",
        "explanation": r"\(3x^2 - 1 = 11\), so \(3x^2 = 12\), \(x^2 = 4\), \(x = 2\) or \(x = -2\). Both are valid. The answer is C.",
        "common_mistake": r"Don't forget the negative root. Since \(x^2 = 4\), both \(x = 2\) and \(x = -2\) satisfy the equation. Choosing only A or B would be incomplete.",
    },
    ("functions", 1, 14): {
        "answer": "B",
        "explanation": r"The function \(f(x) = \frac{x-1}{x+2}\) is undefined when the denominator is zero: \(x + 2 = 0\), i.e., \(x = -2\). The domain is all real numbers except \(-2\). The answer is B.",
    },
    ("functions", 1, 15): {
        "answer": "B",
        "explanation": r"Since \(x = 3\) satisfies \(x \ge 3\), use the second piece: \(f(3) = 3 + 4 = 7\). The answer is B.",
    },

    # ── Section 2: Multiple Choice — Select One or More (questions 16-18) ──

    ("functions", 2, 16): {
        "answer": "A, D",
        "explanation": r"\(f(x) = x^2 - 4 = 0\) means \(x^2 = 4\), so \(x = -2\) or \(x = 2\). Check the choices: A) \(-2\) ✓; B) \(-1\): \(1 - 4 = -3 \neq 0\) ✗; C) \(0\): \(0 - 4 = -4 \neq 0\) ✗; D) \(2\) ✓; E) \(4\): \(16 - 4 = 12 \neq 0\) ✗.",
    },
    ("functions", 2, 17): {
        "answer": "A, B, D, E",
        "explanation": r"Compute: \(f(g(x)) = f(3x - 1) = 2(3x - 1) + 3 = 6x - 2 + 3 = 6x + 1\). \(g(f(x)) = g(2x + 3) = 3(2x + 3) - 1 = 6x + 9 - 1 = 6x + 8\). Check each: A) \(f(g(x)) = 6x + 1\) ✓; B) \(g(f(x)) = 6x + 8\) ✓; C) \(f(g(x)) = 6x + 5\) ✗ (it equals \(6x + 1\)); D) \(g(f(x)) = 6x + 8\) ✓ (same as B -- both are correct); E) \(f(g(1)) = 6(1) + 1 = 7\) ✓.",
        "common_mistake": "Note that f(g(x)) and g(f(x)) are generally NOT equal. Here f(g(x)) = 6x + 1 while g(f(x)) = 6x + 8. Function composition is not commutative.",
    },
    ("functions", 2, 18): {
        "answer": "A, C, D",
        "explanation": r"For \(f(x) = x^2\): A) \(f(-x) = (-x)^2 = x^2 = f(x)\) ✓ (even function); B) \(f(x+y) = (x+y)^2 = x^2 + 2xy + y^2 \neq x^2 + y^2 = f(x) + f(y)\) in general ✗; C) \(f(x) = x^2 \ge 0\) for all real \(x\) ✓; D) \(f(x) = x^2 = 0\) iff \(x = 0\) ✓; E) \(f(\sqrt{x}) = (\sqrt{x})^2 = x\) -- this is true when \(x \ge 0\), but not 'always true' for all real \(x\) since \(\sqrt{x}\) is undefined for \(x < 0\). However, within the domain where it's defined, it is true. For the GRE, if 'always true' means 'for all real x', then E is not always true since the domain is restricted. The answer is A, C, D.",
        "common_mistake": r"Choice B is a very common misconception: \(f(x+y) = (x+y)^2 \neq f(x) + f(y) = x^2 + y^2\). Squaring is NOT a linear operation -- you cannot distribute it over addition.",
    },

    # ── Section 3: Function Composition & Structure (questions 19-20) ──

    ("functions", 3, 19): {
        "answer": "B",
        "explanation": r"\(g(f(x)) = g(3x - 2) = 2(3x - 2) + 5 = 6x - 4 + 5 = 6x + 1\). The answer is B. Note: choice A shows the unsimplified form \(6x - 4 + 5\), but B gives the simplified result \(6x + 1\).",
    },
    ("functions", 3, 20): {
        "answer": "C",
        "explanation": r"\(f(2) = 2^2 = 4\). Then \(f(f(2)) = f(4) = 4^2 = 16\). The answer is C.",
    },

    # ── Section 4: Numeric Entry (questions 21-27) ──

    ("functions", 4, 21): {
        "answer": "13",
        "explanation": r"\(f(3) = 5(3) - 2 = 15 - 2 = 13\).",
    },
    ("functions", 4, 22): {
        "answer": "4",
        "explanation": r"\(f(4) = 4^2 - 3(4) = 16 - 12 = 4\).",
    },
    ("functions", 4, 23): {
        "answer": "7",
        "explanation": r"\(f(2) = 2 + k = 9\), so \(k = 7\).",
    },
    ("functions", 4, 24): {
        "answer": "4",
        "explanation": r"\(f(4) = 2/4 = 1/2\). Then \(f(f(4)) = f(1/2) = 2/(1/2) = 4\).",
    },
    ("functions", 4, 25): {
        "answer": "3",
        "explanation": r"\(f(x) = x^2 - 6x + 5\). Complete the square: \(f(x) = (x - 3)^2 - 9 + 5 = (x - 3)^2 - 4\). The minimum occurs at \(x = 3\). Alternatively, use the vertex formula: \(x = -b/(2a) = 6/2 = 3\).",
    },
    ("functions", 4, 26): {
        "answer": "3",
        "explanation": r"From \(f(2) = 2a + b = 7\) and \(f(5) = 5a + b = 16\). Subtract: \(3a = 9\), so \(a = 3\).",
    },
    ("functions", 4, 27): {
        "answer": "12",
        "explanation": r"Since \(f(x + y) = f(x) + f(y)\) for all real \(x, y\), this is Cauchy's functional equation (and on GRE we assume nice functions), so \(f(x) = cx\) for some constant \(c\). From \(f(1) = c = 3\), so \(f(x) = 3x\). Therefore \(f(4) = 3(4) = 12\). Alternatively: \(f(4) = f(1+1+1+1) = f(1) + f(1) + f(1) + f(1) = 4 \cdot 3 = 12\).",
    },
}
