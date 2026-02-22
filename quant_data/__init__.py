import json

TOPICS = [
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 1 – LINEAR EQUATIONS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "linear-equations",
        "title": "Linear Equations",
        "icon": "1",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(6x - 5 = 19\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(4\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(3x + 7 = 2x + 15\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(8\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(x\) is a real number and \(2x = 2\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(1\)",
                    },
                    {
                        "id": 4,
                        "stem": r"If \(x\) is a real number and \(5x + 8 = 3x + 14\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 5,
                        "stem": r"If \(0 < x < 1\) and \(2x + 1 = 3\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(1\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(ax + 4 = ax - 6\) and \(a \neq 0\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 7,
                        "stem": r"If \(3x + k = 3x + 7\)",
                        "qtyA": r"Number of solutions when \(k = 7\)",
                        "qtyB": r"Number of solutions when \(k \neq 7\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \((k - 3)x = 0\)",
                        "qtyA": r"Number of solutions when \(k = 3\)",
                        "qtyB": r"Number of solutions when \(k \neq 3\)",
                    },
                    {
                        "id": 9,
                        "stem": r"A system of two linear equations in \(x\) and \(y\) has exactly one solution.",
                        "qtyA": "Slopes of the two lines",
                        "qtyB": "Equal",
                    },
                    {
                        "id": 10,
                        "stem": r"If \(\dfrac{x}{y} = \dfrac{3}{5}\) and \(x + y = 40\)",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(15\)",
                    },
                    {
                        "id": 11,
                        "stem": "",
                        "qtyA": r"Number of real solutions to \(\dfrac{x-2}{x-2} = 1\)",
                        "qtyB": "Infinitely many",
                    },
                    {
                        "id": 12,
                        "stem": r"\[f(x) = \begin{cases} 3x & x \le 2 \\ x + 4 & x > 2 \end{cases}\]",
                        "qtyA": r"\(f(2)\)",
                        "qtyB": r"\(f(3)\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 13,
                        "stem": r"Solve: \(\dfrac{3x}{4} - 2 = \dfrac{x}{2}\)",
                        "choices": ["A) &minus;16", "B) &minus;8", "C) 0", "D) 8", "E) 16"],
                    },
                    {
                        "id": 14,
                        "stem": r"Solve: \(7(2x - 1) = 3(3x + 4)\)",
                        "choices": ["A) &minus;19", "B) &minus;5", "C) 1", "D) 5", "E) 19"],
                    },
                    {
                        "id": 15,
                        "stem": r"For what value of \(k\) does \((k - 2)x = 10\) have no solution?",
                        "choices": ["A) 0", "B) 2", "C) 5", "D) 10", "E) It never has &ldquo;no solution&rdquo;"],
                    },
                    {
                        "id": 16,
                        "stem": r"For what value of \(k\) does \(3x + k = 3x + 7\) have infinitely many solutions?",
                        "choices": ["A) &minus;7", "B) 0", "C) 7", "D) 3", "E) No such value"],
                    },
                    {
                        "id": 17,
                        "stem": r"If \(4x + k = 4x + 9\) for all \(x\), then \(k =\)",
                        "choices": ["A) &minus;9", "B) 0", "C) 4", "D) 9", "E) Cannot be determined"],
                    },
                    {
                        "id": 18,
                        "stem": r"The system \[2x + 3y = 6, \quad 4x + 6y = 12\] has:",
                        "choices": ["A) One solution", "B) No solution", "C) Infinitely many solutions", "D) Exactly two solutions", "E) Cannot be determined"],
                    },
                    {
                        "id": 19,
                        "stem": r"For what value of \(k\) does the system have infinitely many solutions? \[x + ky = 4, \quad 2x + 6y = 8\]",
                        "choices": ["A) 0", "B) 2", "C) 3", "D) 6", "E) No such value"],
                    },
                    {
                        "id": 20,
                        "stem": "Two numbers are in the ratio 4:7. Their difference is 9. The larger number is:",
                        "choices": ["A) 12", "B) 15", "C) 18", "D) 21", "E) 28"],
                    },
                    {
                        "id": 21,
                        "stem": "The sum of three consecutive integers is 72. The smallest integer is:",
                        "choices": ["A) 22", "B) 23", "C) 24", "D) 25", "E) 26"],
                    },
                    {
                        "id": 22,
                        "stem": "A number increased by 30% equals 78. The original number is:",
                        "choices": ["A) 54", "B) 60", "C) 65", "D) 70", "E) 72"],
                    },
                    {
                        "id": 23,
                        "stem": "4 apples and 3 oranges cost $18. 2 apples and 1 orange cost $7. The cost of one apple is:",
                        "choices": ["A) $1", "B) $2", "C) $3", "D) $4", "E) $5"],
                    },
                    {
                        "id": 24,
                        "stem": r"How many real solutions does \(|2x + 1| = 2x + 1\) have?",
                        "choices": ["A) 0", "B) 1", "C) 2", "D) Infinitely many", "E) Cannot be determined"],
                    },
                    {
                        "id": 25,
                        "stem": r"Solve \(|3x - 1| < 5\). Which interval is the solution set?",
                        "choices": [
                            r"A) \((-2, 2)\)",
                            r"B) \(\left(-\frac{4}{3}, 2\right)\)",
                            r"C) \(\left(-\frac{4}{3}, \frac{4}{3}\right)\)",
                            r"D) \(\left(-2, \frac{4}{3}\right)\)",
                            r"E) \(\left(-2, \frac{8}{3}\right)\)",
                        ],
                    },
                    {
                        "id": 26,
                        "stem": r"Solve: \(\dfrac{1}{x - 3} = \dfrac{1}{5}\)",
                        "choices": ["A) &minus;2", "B) 2", "C) 5", "D) 8", "E) No solution"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 27,
                        "stem": r"If \(x > 0\), which statements must be true?",
                        "choices": [
                            r"A) \(x + 1 > 1\)",
                            r"B) \(x - 1 > 0\)",
                            r"C) \(\frac{1}{x} > 0\)",
                            r"D) \(x^2 > x\)",
                            r"E) \(|x| = x\)",
                        ],
                    },
                    {
                        "id": 28,
                        "stem": r"Which values of \(x\) satisfy \(|4x - 8| = 12\)?",
                        "choices": ["A) &minus;1", "B) 1", "C) 2", "D) 5", "E) 8"],
                    },
                    {
                        "id": 29,
                        "stem": r"Which ordered pairs \((x, y)\) satisfy both equations? \[x + y = 6, \quad x - y = 2\]",
                        "choices": ["A) (4, 2)", "B) (2, 4)", "C) (3, 3)", "D) (6, 0)", "E) (0, 6)"],
                    },
                    {
                        "id": 30,
                        "stem": r"For which values of \(k\) does \((k - 2)x = 10\) have exactly one solution?",
                        "choices": [r"A) \(k = 2\)", r"B) \(k = 0\)", r"C) \(k = 5\)", r"D) All real \(k \neq 2\)", r"E) All real \(k\)"],
                    },
                    {
                        "id": 31,
                        "stem": r"For which values of \(k\) does \(5x + k = 5x - 3\) have no solution?",
                        "choices": [r"A) \(k = -3\)", r"B) \(k = 3\)", r"C) \(k \neq -3\)", "D) All real \\(k\\)", "E) None"],
                    },
                    {
                        "id": 32,
                        "stem": r"\[f(x) = \begin{cases} 2x + 1 & x < 3 \\ 7 - x & x \ge 3 \end{cases}\] Which are true?",
                        "choices": [
                            r"A) \(f(2) = 5\)",
                            r"B) \(f(3) = 4\)",
                            r"C) \(f(4) = 3\)",
                            r"D) \(f(0) = 1\)",
                            r"E) \(f(10) = -3\)",
                        ],
                    },
                    {
                        "id": 33,
                        "stem": r"A line passes through \((1, 4)\) and \((5, 12)\). Which are true?",
                        "choices": [
                            "A) Slope is 2",
                            r"B) Slope is \(\frac{8}{4}\)",
                            r"C) Equation could be \(y = 2x + 2\)",
                            r"D) Equation could be \(y = 2x + 4\)",
                            "E) y-intercept is 2",
                        ],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 34,
                        "stem": r"Solve: \(6x - 5 = 19\). Enter \(x\).",
                    },
                    {
                        "id": 35,
                        "stem": r"Solve: \(5(2x - 1) = 3(x + 4)\). Enter \(x\).",
                    },
                    {
                        "id": 36,
                        "stem": r"Solve the system: \[3x + y = 13, \quad x - y = 1\] Enter \(x\).",
                    },
                    {
                        "id": 37,
                        "stem": r"The ratio of \(x\) to \(y\) is 3:5 and \(x + y = 40\). Enter \(y\).",
                    },
                    {
                        "id": 38,
                        "stem": r"Solve: \(4x - 5 > 11\). Enter the smallest integer \(x\) that satisfies.",
                    },
                    {
                        "id": 39,
                        "stem": r"Solve: \(|3x - 6| = 9\). Enter the larger solution.",
                    },
                    {
                        "id": 40,
                        "stem": r"Solve: \(|2x - 1| \le 5\). Enter the greatest integer \(x\) that satisfies.",
                    },
                    {
                        "id": 41,
                        "stem": "A number increased by 25% and then decreased by 25% becomes 90. Enter the original number.",
                    },
                    {
                        "id": 42,
                        "stem": r"A line has slope 3 and passes through \((2, 7)\). Enter the y-intercept.",
                    },
                    {
                        "id": 43,
                        "stem": r"How many real solutions does \(\dfrac{x-2}{x-2} = 1\) have? Enter the number.",
                    },
                    {
                        "id": 44,
                        "stem": r"If \((k - 3)x = 0\) has infinitely many solutions, enter \(k\).",
                    },
                    {
                        "id": 45,
                        "stem": r"If \(ax + b = 0\) has solution \(x = 3\) and \(a \neq 0\), enter \(-\dfrac{b}{a}\).",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 2 – SYSTEMS OF LINEAR EQUATIONS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "systems-of-linear-equations",
        "title": "Systems of Linear Equations",
        "icon": "2",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"The system: \[x + y = 10\]\[x - y = 2\]",
                        "qtyA": r"The value of \(x\)",
                        "qtyB": r"\(6\)",
                    },
                    {
                        "id": 2,
                        "stem": r"The system: \[2x + 3y = 6\]\[4x + 6y = 12\]",
                        "qtyA": "Number of solutions",
                        "qtyB": r"\(1\)",
                    },
                    {
                        "id": 3,
                        "stem": r"The system: \[2x + 3y = 6\]\[4x + 6y = 10\]",
                        "qtyA": "Number of solutions",
                        "qtyB": r"\(0\)",
                    },
                    {
                        "id": 4,
                        "stem": "If a system of two linear equations in two variables has exactly one solution,",
                        "qtyA": "The slopes of the two lines",
                        "qtyB": "Equal",
                    },
                    {
                        "id": 5,
                        "stem": r"The system \[x + ky = 4\]\[2x + 6y = 8\] has infinitely many solutions.",
                        "qtyA": r"\(k\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If the system \[3x + ky = 7\]\[6x + 2ky = 14\] has infinitely many solutions,",
                        "qtyA": "Number of solutions",
                        "qtyB": r"\(1\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 7,
                        "stem": r"Solve the system: \[2x + 3y = 13\]\[x - y = 1\]",
                        "choices": ["A) (4, 3)", "B) (3, 4)", "C) (5, 2)", "D) (2, 5)", "E) (1, 6)"],
                    },
                    {
                        "id": 8,
                        "stem": r"The system \[3x + 2y = 5\]\[6x + 4y = k\] has no solution when \(k\) equals:",
                        "choices": ["A) 5", "B) 8", "C) 10", "D) 12", "E) 15"],
                    },
                    {
                        "id": 9,
                        "stem": "Two numbers are in the ratio 4:7. Their sum is 33. What is the larger number?",
                        "choices": ["A) 12", "B) 18", "C) 21", "D) 24", "E) 28"],
                    },
                    {
                        "id": 10,
                        "stem": "A theater sold 120 tickets for a performance. Adult tickets cost $10 each and child tickets cost $6 each. The total revenue was $960. How many adult tickets were sold?",
                        "choices": ["A) 40", "B) 60", "C) 80", "D) 90", "E) 100"],
                    },
                    {
                        "id": 11,
                        "stem": r"The system \[ax + by = 5\]\[2ax + 2by = 10\] where \(a\) and \(b\) are nonzero constants, has:",
                        "choices": ["A) Exactly one solution", "B) No solution", "C) Infinitely many solutions", "D) Exactly two solutions", "E) Cannot be determined"],
                    },
                    {
                        "id": 12,
                        "stem": r"Solve the system: \[x + y + z = 12\]\[x + y = 7\]\[y + z = 9\] The value of \(y\) is:",
                        "choices": ["A) 2", "B) 3", "C) 4", "D) 5", "E) 6"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 13,
                        "stem": "Which of the following systems have infinitely many solutions?",
                        "choices": [
                            r"A) \(2x+3y=6,\; 4x+6y=12\)",
                            r"B) \(2x+3y=6,\; 4x+6y=10\)",
                            r"C) \(x+y=5,\; 2x+2y=10\)",
                            r"D) \(x+y=5,\; 2x+2y=9\)",
                        ],
                    },
                    {
                        "id": 14,
                        "stem": r"For which values of \(k\) does the system \[(k-1)x + y = 3\]\[2x + (k-3)y = 4\] have no solution?",
                        "choices": [r"A) \(k = 1\)", r"B) \(k = 3\)", r"C) \(k = 2\)", r"D) \(k = 4\)", r"E) No real value of \(k\)"],
                    },
                    {
                        "id": 15,
                        "stem": r"Which ordered pairs satisfy both equations? \[x + y = 6\]\[x - y = 2\]",
                        "choices": ["A) (4, 2)", "B) (2, 4)", "C) (3, 3)", "D) (6, 0)", "E) (0, 6)"],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 16,
                        "stem": r"Solve: \[x + y = 10\]\[x - y = 2\] Enter the value of \(y\).",
                    },
                    {
                        "id": 17,
                        "stem": r"Solve: \[3x + y = 13\]\[x - y = 1\] Enter the value of \(x\).",
                    },
                    {
                        "id": 18,
                        "stem": r"The ratio of \(x\) to \(y\) is 2:3 and \(x + y = 25\). Enter the value of \(x\).",
                    },
                    {
                        "id": 19,
                        "stem": "Two workers together complete a job in 4 hours. One worker alone completes it in 6 hours. Enter the number of hours it would take the second worker working alone.",
                    },
                    {
                        "id": 20,
                        "stem": r"If the system \[kx + y = 2\]\[2x + 4y = 6\] has exactly one solution, enter any value of \(k\) that satisfies this condition.",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 3 – INEQUALITIES
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "inequalities",
        "title": "Inequalities",
        "icon": "3",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(4x - 5 > 11\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(4\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(x < 0\),",
                        "qtyA": r"\(x^2\)",
                        "qtyB": r"\(x\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(0 < x < 1\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(x^2\)",
                    },
                    {
                        "id": 4,
                        "stem": r"If \(x > y\),",
                        "qtyA": r"\(-x\)",
                        "qtyB": r"\(-y\)",
                    },
                    {
                        "id": 5,
                        "stem": r"If \(xy > 0\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(0\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(|x - 3| < 2\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(5\)",
                    },
                    {
                        "id": 7,
                        "stem": r"If \(x > 1\),",
                        "qtyA": r"\(\dfrac{1}{x}\)",
                        "qtyB": r"\(1\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \(x < y\) and both are negative,",
                        "qtyA": r"\(x^2\)",
                        "qtyB": r"\(y^2\)",
                    },
                    {
                        "id": 9,
                        "stem": r"If \(2 < x < 5\),",
                        "qtyA": r"\(3x - 1\)",
                        "qtyB": r"\(5\)",
                    },
                    {
                        "id": 10,
                        "stem": r"If \(x^2 < 4\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(2\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 11,
                        "stem": r"Solve: \[-3x + 7 \le 1\]",
                        "choices": [r"A) \(x \ge 2\)", r"B) \(x \le 2\)", r"C) \(x \ge -2\)", r"D) \(x \le -2\)", r"E) \(x = 2\)"],
                    },
                    {
                        "id": 12,
                        "stem": r"Solve: \[-2 < 3x + 1 \le 7\]",
                        "choices": [r"A) \(-1 < x \le 2\)", r"B) \(-1 \le x < 2\)", r"C) \(-1 < x < 2\)", r"D) \(-1 \le x \le 2\)", r"E) \(x > -1\)"],
                    },
                    {
                        "id": 13,
                        "stem": r"Solve: \[|2x - 5| \le 3\]",
                        "choices": [r"A) \(1 \le x \le 4\)", r"B) \(1 < x < 4\)", r"C) \(x \le 1\) or \(x \ge 4\)", r"D) \(x < 1\) or \(x > 4\)", r"E) \(2 \le x \le 5\)"],
                    },
                    {
                        "id": 14,
                        "stem": r"Solve: \[x^2 - 5x + 6 > 0\]",
                        "choices": [r"A) \(x < 2\) or \(x > 3\)", r"B) \(2 < x < 3\)", r"C) \(x > 3\)", r"D) \(x < 2\)", "E) All real numbers"],
                    },
                    {
                        "id": 15,
                        "stem": r"Solve: \[\frac{x - 2}{x + 1} \le 0\]",
                        "choices": [r"A) \(-1 < x \le 2\)", r"B) \(x < -1\) or \(x \ge 2\)", r"C) \(-1 \le x < 2\)", r"D) \(x = -1\) or \(x = 2\)", r"E) \(x \le -1\)"],
                    },
                    {
                        "id": 16,
                        "stem": r"For which values of \(k\) does \(kx > 4\) hold for all \(x > 2\)?",
                        "choices": [r"A) \(k > 2\)", r"B) \(k = 2\)", r"C) \(k \ge 2\)", r"D) \(k > 0\)", r"E) No such \(k\)"],
                    },
                    {
                        "id": 17,
                        "stem": r"Solve: \[\sqrt{x} < x\]",
                        "choices": [r"A) \(0 < x < 1\)", r"B) \(x > 1\)", r"C) \(x > 0\)", r"D) \(x \ge 1\)", r"E) All real \(x\)"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 18,
                        "stem": r"Which are true for all real numbers \(x\)?",
                        "choices": [
                            r"A) \(x^2 \ge 0\)",
                            r"B) \(|x| \ge x\)",
                            r"C) \(x^3 \ge x\)",
                            r"D) \(-x \le |x|\)",
                            r"E) \(x^2 \ge x\)",
                        ],
                    },
                    {
                        "id": 19,
                        "stem": r"For which values of \(x\) is \(\dfrac{x-3}{x-1} > 0\) true?",
                        "choices": [r"A) \(x > 3\)", r"B) \(x < 1\)", r"C) \(1 < x < 3\)", r"D) \(x = 1\)", r"E) \(x = 3\)"],
                    },
                    {
                        "id": 20,
                        "stem": r"Solve: \[|x - 2| > |x + 1|\]",
                        "choices": [r"A) \(x > \frac{1}{2}\)", r"B) \(x < \frac{1}{2}\)", r"C) \(x > 2\)", r"D) \(x < -1\)", "E) All real numbers"],
                    },
                    {
                        "id": 21,
                        "stem": r"Which ordered pairs satisfy both? \[x + y > 5\]\[x - y < 1\]",
                        "choices": ["A) (4, 2)", "B) (3, 3)", "C) (5, 1)", "D) (2, 4)", "E) (6, 0)"],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 22,
                        "stem": r"Solve: \[5 - 2x > 9\] Enter the greatest integer solution.",
                    },
                    {
                        "id": 23,
                        "stem": r"Solve: \[|3x - 6| > 9\] Enter the smallest integer solution.",
                    },
                    {
                        "id": 24,
                        "stem": r"Solve: \[\frac{2}{x - 3} < 0\] Enter any integer solution.",
                    },
                    {
                        "id": 25,
                        "stem": r"Solve: \[x^2 - 4x < 0\] Enter the greatest integer solution.",
                    },
                    {
                        "id": 26,
                        "stem": r"If \(2 < x < 5\), enter the minimum possible value of \(3x - 1\).",
                    },
                    {
                        "id": 27,
                        "stem": r"If \(x + y = 10\) and \(x > y\), enter the least possible integer value of \(x\).",
                    },
                    {
                        "id": 28,
                        "stem": r"If \(x > y\) and \(xy < 0\), enter 1 if \(x > 0\), enter 2 if \(x < 0\), enter 3 if it cannot be determined.",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 4 – QUADRATICS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "quadratics",
        "title": "Quadratics",
        "icon": "4",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(x^2 - 9 = 0\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(x^2 = 16\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(4\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(x^2 - 4x + 4 = 0\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(2\)",
                    },
                    {
                        "id": 4,
                        "stem": r"If \(x^2 - 5x + 6 = 0\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(2\)",
                    },
                    {
                        "id": 5,
                        "stem": r"If \(x^2 + kx + 9 = 0\) has exactly one real solution,",
                        "qtyA": r"\(k^2\)",
                        "qtyB": r"\(36\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(x^2 - 2x - 3 = 0\),",
                        "qtyA": "Larger root",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 7,
                        "stem": r"If \(x\) is a real number such that \(x^2 < 4\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(2\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \(x^2 > 9\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(3\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 9,
                        "stem": r"Solve: \[x^2 - 5x + 6 = 0\]",
                        "choices": ["A) 2 and 3", "B) &minus;2 and &minus;3", "C) 1 and 6", "D) 3 and 6", "E) &minus;1 and &minus;6"],
                    },
                    {
                        "id": 10,
                        "stem": r"Solve: \[2x^2 - 8x = 0\]",
                        "choices": ["A) 0 and 4", "B) 0 and &minus;4", "C) 4 only", "D) 2 and 4", "E) &minus;2 and &minus;4"],
                    },
                    {
                        "id": 11,
                        "stem": r"The equation \[x^2 - 4x + 5 = 0\] has:",
                        "choices": ["A) Two distinct real roots", "B) One real root", "C) No real roots", "D) Two equal real roots", "E) Exactly one positive root"],
                    },
                    {
                        "id": 12,
                        "stem": r"For what value of \(k\) does \[x^2 + kx + 4 = 0\] have exactly one real solution?",
                        "choices": [r"A) &minus;4", r"B) &minus;8", r"C) \(\pm 4\)", r"D) \(\pm 8\)", "E) 4"],
                    },
                    {
                        "id": 13,
                        "stem": r"If \(x^2 - 7x + 10 = 0\), the sum of the roots is:",
                        "choices": ["A) 3", "B) 5", "C) 7", "D) 10", "E) 17"],
                    },
                    {
                        "id": 14,
                        "stem": r"If \(x^2 + 2x - 8 = 0\), the product of the roots is:",
                        "choices": ["A) &minus;8", "B) 8", "C) &minus;2", "D) 2", "E) 6"],
                    },
                    {
                        "id": 15,
                        "stem": r"The function \(f(x) = x^2 - 6x + 5\) has its minimum value at:",
                        "choices": [r"A) \(x = 3\)", r"B) \(x = -3\)", r"C) \(x = 6\)", r"D) \(x = 5\)", r"E) \(x = 0\)"],
                    },
                    {
                        "id": 16,
                        "stem": r"Rewrite \(x^2 - 4x + 7\) in the form \((x - a)^2 + b\). What is \(a\)?",
                        "choices": ["A) 2", "B) &minus;2", "C) 4", "D) &minus;4", "E) 1"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 17,
                        "stem": "Which equations have two distinct real solutions?",
                        "choices": [
                            r"A) \(x^2 - 9 = 0\)",
                            r"B) \(x^2 + 4x + 4 = 0\)",
                            r"C) \(x^2 + 1 = 0\)",
                            r"D) \(x^2 - 2x - 3 = 0\)",
                            r"E) \(x^2 - 4x + 4 = 0\)",
                        ],
                    },
                    {
                        "id": 18,
                        "stem": r"If \(x^2 - kx + 9 = 0\) has real solutions, which must be true?",
                        "choices": [
                            r"A) \(k^2 \ge 36\)",
                            r"B) \(k \ge 6\)",
                            r"C) \(k \le -6\)",
                            r"D) \(|k| \ge 6\)",
                            r"E) \(k^2 > 36\)",
                        ],
                    },
                    {
                        "id": 19,
                        "stem": "Which of the following could be the roots of a quadratic equation with integer coefficients?",
                        "choices": [
                            r"A) 2 and 3",
                            r"B) \(\sqrt{2}\) and \(-\sqrt{2}\)",
                            r"C) \(\frac{1}{2}\) and 4",
                            r"D) 5 and &minus;5",
                            r"E) 3 and \(\frac{1}{3}\)",
                        ],
                    },
                ],
            },
            {
                "type": "Quadratic Inequalities",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 20,
                        "stem": r"Solve: \[x^2 - 4x < 0\]",
                        "choices": [r"A) \(0 < x < 4\)", r"B) \(x < 0\) or \(x > 4\)", r"C) \(0 \le x \le 4\)", r"D) \(x > 4\)", "E) All real numbers"],
                    },
                    {
                        "id": 21,
                        "stem": r"Solve: \[x^2 - 5x + 6 > 0\]",
                        "choices": [r"A) \(x < 2\) or \(x > 3\)", r"B) \(2 < x < 3\)", r"C) \(x > 3\)", r"D) \(x < 2\)", "E) All real numbers"],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 22,
                        "stem": r"Solve: \[x^2 - 7x + 12 = 0\] Enter the larger root.",
                    },
                    {
                        "id": 23,
                        "stem": r"If the discriminant of \(x^2 + 4x + k = 0\) is zero, enter the value of \(k\).",
                    },
                    {
                        "id": 24,
                        "stem": r"If the roots of \(x^2 - 6x + 5 = 0\) are \(r\) and \(s\), enter \(r + s\).",
                    },
                    {
                        "id": 25,
                        "stem": r"If \(x^2 - kx + 4 = 0\) has no real solutions, enter any value of \(k\) that satisfies this.",
                    },
                    {
                        "id": 26,
                        "stem": r"The parabola \(y = x^2 - 8x + 10\) has a minimum value of what?",
                    },
                    {
                        "id": 27,
                        "stem": r"If \(x\) and \(y\) are real numbers such that \[x + y = 6\]\[xy = 8\] Enter the larger value of \(x\).",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 5 – EXPONENTS & RADICALS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "exponents-radicals",
        "title": "Exponents & Radicals",
        "icon": "5",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(x > 1\),",
                        "qtyA": r"\(x^3\)",
                        "qtyB": r"\(x^2\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(0 < x < 1\),",
                        "qtyA": r"\(x^2\)",
                        "qtyB": r"\(x\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(x < 0\),",
                        "qtyA": r"\(x^2\)",
                        "qtyB": r"\(x^3\)",
                    },
                    {
                        "id": 4,
                        "stem": "",
                        "qtyA": r"\(2^5 \cdot 2^{-3}\)",
                        "qtyB": r"\(4\)",
                    },
                    {
                        "id": 5,
                        "stem": "",
                        "qtyA": r"\(\sqrt{49}\)",
                        "qtyB": r"\(-7\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(a > b > 0\),",
                        "qtyA": r"\(a^2\)",
                        "qtyB": r"\(b^2\)",
                    },
                    {
                        "id": 7,
                        "stem": r"If \(x \neq 0\),",
                        "qtyA": r"\(x^{-1}\)",
                        "qtyB": r"\(\dfrac{1}{x}\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \(x^2 = 9\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 9,
                        "stem": r"If \(2^x = 8\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 10,
                        "stem": "",
                        "qtyA": r"\(3^4\)",
                        "qtyB": r"\(4^3\)",
                    },
                    # v2.0 advanced QC
                    {
                        "id": 11,
                        "stem": r"If \(x > 1\),",
                        "qtyA": r"\(x^5\)",
                        "qtyB": r"\(x^4\)",
                    },
                    {
                        "id": 12,
                        "stem": r"If \(0 < x < 1\),",
                        "qtyA": r"\(x^3\)",
                        "qtyB": r"\(x^4\)",
                    },
                    {
                        "id": 13,
                        "stem": r"If \(x < 0\),",
                        "qtyA": r"\(x^4\)",
                        "qtyB": r"\(x^3\)",
                    },
                    {
                        "id": 14,
                        "stem": "",
                        "qtyA": r"\(2^{10}\)",
                        "qtyB": r"\(3^6\)",
                    },
                    {
                        "id": 15,
                        "stem": r"If \(x^2 = 9\),",
                        "qtyA": r"\(\sqrt{x^2}\)",
                        "qtyB": r"\(x\)",
                    },
                    {
                        "id": 16,
                        "stem": r"If \(a > 0\), \(a \neq 1\), and \(a^x = a^y\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(y\)",
                    },
                    {
                        "id": 17,
                        "stem": r"If \(0 < x < 1\),",
                        "qtyA": r"\(\sqrt{x}\)",
                        "qtyB": r"\(x^{3/2}\)",
                    },
                    {
                        "id": 18,
                        "stem": r"If \(x > 0\),",
                        "qtyA": r"\(5^x\)",
                        "qtyB": r"\(x^5\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 19,
                        "stem": r"Simplify: \[\frac{5^3 \cdot 5^{-1}}{5^2}\]",
                        "choices": ["A) 1", "B) 5", "C) 25", "D) 125", "E) 625"],
                    },
                    {
                        "id": 20,
                        "stem": r"Simplify: \[(3^2)^4\]",
                        "choices": [r"A) \(3^6\)", r"B) \(3^8\)", r"C) \(9^4\)", r"D) \(12^2\)", "E) 81"],
                    },
                    {
                        "id": 21,
                        "stem": r"Solve: \[4^x = 16\]",
                        "choices": ["A) 1", "B) 2", "C) 3", "D) 4", "E) 8"],
                    },
                    {
                        "id": 22,
                        "stem": r"Solve: \[9^x = 3^4\]",
                        "choices": ["A) 1", "B) 2", "C) 3", "D) 4", "E) 8"],
                    },
                    {
                        "id": 23,
                        "stem": r"Simplify: \[\sqrt{50}\]",
                        "choices": [r"A) \(5\sqrt{2}\)", r"B) \(10\sqrt{5}\)", r"C) \(25\sqrt{2}\)", r"D) \(2\sqrt{25}\)", r"E) \(50^{1/2}\)"],
                    },
                    {
                        "id": 24,
                        "stem": r"Rationalize the denominator: \[\frac{5}{\sqrt{3}}\]",
                        "choices": [r"A) \(\frac{5\sqrt{3}}{3}\)", r"B) \(\frac{5}{3\sqrt{3}}\)", r"C) \(\frac{5\sqrt{3}}{9}\)", r"D) \(\frac{15}{\sqrt{3}}\)", r"E) \(\frac{3}{5\sqrt{3}}\)"],
                    },
                    {
                        "id": 25,
                        "stem": r"Simplify: \[27^{2/3}\]",
                        "choices": ["A) 3", "B) 6", "C) 9", "D) 18", "E) 27"],
                    },
                    {
                        "id": 26,
                        "stem": r"Simplify: \[\left(\frac{2}{3}\right)^{-2}\]",
                        "choices": [r"A) \(\frac{4}{9}\)", r"B) \(\frac{9}{4}\)", r"C) \(-\frac{4}{9}\)", r"D) \(-\frac{9}{4}\)", r"E) \(\frac{2}{3}\)"],
                    },
                    # v2.0 advanced MC
                    {
                        "id": 27,
                        "stem": r"Simplify: \[\frac{3^5 \cdot 9^{-1}}{3^2}\]",
                        "choices": [r"A) \(3^2\)", "B) 3", "C) 1", r"D) \(3^3\)", r"E) \(3^4\)"],
                    },
                    {
                        "id": 28,
                        "stem": r"Solve: \[8^x = 4^{x+1}\]",
                        "choices": ["A) 0", "B) 1", "C) 2", "D) &minus;1", "E) No solution"],
                    },
                    {
                        "id": 29,
                        "stem": r"Solve: \[x^x = 16\]",
                        "choices": ["A) 2", "B) 4", "C) &minus;2", "D) 8", "E) No real solution"],
                    },
                    {
                        "id": 30,
                        "stem": r"Simplify: \[\sqrt{9 + 4\sqrt{5}}\]",
                        "choices": [r"A) \(3 + \sqrt{5}\)", r"B) \(2 + \sqrt{5}\)", r"C) \(\sqrt{5} + 1\)", r"D) \(3 + 2\sqrt{5}\)", "E) Cannot be simplified"],
                    },
                    {
                        "id": 31,
                        "stem": r"Rationalize: \[\frac{1}{\sqrt{2} - 1}\]",
                        "choices": [r"A) \(\sqrt{2} - 1\)", r"B) \(\sqrt{2} + 1\)", r"C) \(1 - \sqrt{2}\)", r"D) \(2 - \sqrt{2}\)", r"E) \(2 + \sqrt{2}\)"],
                    },
                    {
                        "id": 32,
                        "stem": r"Solve: \[\sqrt{x - 1} > 3\]",
                        "choices": [r"A) \(x > 10\)", r"B) \(x > 9\)", r"C) \(x \ge 10\)", r"D) \(x > 1\)", r"E) \(1 < x < 10\)"],
                    },
                    {
                        "id": 33,
                        "stem": r"Solve: \[\sqrt{x^2} = x\]",
                        "choices": [r"A) All real \(x\)", r"B) \(x \ge 0\)", r"C) \(x \le 0\)", r"D) \(x > 0\)", "E) No solution"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 34,
                        "stem": r"Which are equal to \(2^6\)?",
                        "choices": [r"A) \(4^3\)", r"B) \(8^2\)", r"C) \(16^1\)", r"D) \(2^3 \cdot 2^3\)", r"E) \(64^1\)"],
                    },
                    {
                        "id": 35,
                        "stem": r"If \(x > 0\), which must be true?",
                        "choices": [
                            r"A) \(\sqrt{x^2} = x\)",
                            r"B) \(x^{1/2} \cdot x^{1/2} = x\)",
                            r"C) \(x^{-1} = \frac{1}{x}\)",
                            r"D) \(x^2 > x\)",
                            r"E) \(\sqrt{x} > x\)",
                        ],
                    },
                    {
                        "id": 36,
                        "stem": "Which equations have real solutions?",
                        "choices": [
                            r"A) \(x^2 = -9\)",
                            r"B) \(x^2 = 9\)",
                            r"C) \(\sqrt{x} = -3\)",
                            r"D) \(\sqrt{x^2} = 5\)",
                            r"E) \(x^{1/2} = 4\)",
                        ],
                    },
                    # v2.0
                    {
                        "id": 37,
                        "stem": r"Which are equal to \(4^5\)?",
                        "choices": [r"A) \(2^{10}\)", r"B) \(8^5\)", r"C) \(16^2\)", r"D) \(32^2\)", r"E) \(2^5 \cdot 2^5\)"],
                    },
                    {
                        "id": 38,
                        "stem": "Which equations have real solutions?",
                        "choices": [
                            r"A) \(x^2 = -4\)",
                            r"B) \(x^3 = -8\)",
                            r"C) \(\sqrt{x} = -3\)",
                            r"D) \(x^{2/3} = 4\)",
                            r"E) \(x^{1/2} = 5\)",
                        ],
                    },
                    {
                        "id": 39,
                        "stem": r"Which are true for all positive \(a\)?",
                        "choices": [
                            r"A) \(a^{m+n} = a^m + a^n\)",
                            r"B) \((a^m)^n = a^{mn}\)",
                            r"C) \(a^{-m} = \frac{1}{a^m}\)",
                            r"D) \(a^{1/2} = \sqrt{a}\)",
                            r"E) \(a^0 = 0\)",
                        ],
                    },
                ],
            },
            {
                "type": "Exponential Growth / Modeling",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 40,
                        "stem": "A population doubles every 5 years. If the initial population is 1,000, what will it be after 15 years?",
                        "choices": ["A) 3,000", "B) 4,000", "C) 6,000", "D) 8,000", "E) 16,000"],
                    },
                    {
                        "id": 41,
                        "stem": "An investment grows by 10% annually. After 2 years, the value is:",
                        "choices": [r"A) \(P(1.10)^2\)", r"B) \(P(2.10)\)", r"C) \(P(1.20)\)", r"D) \(P(1.21)\)", r"E) \(P(2.20)\)"],
                    },
                ],
            },
            {
                "type": "Radical Equations",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 42,
                        "stem": r"Solve: \[\sqrt{x + 5} = 3\]",
                        "choices": ["A) 4", "B) &minus;4", "C) 9", "D) &minus;9", "E) 14"],
                    },
                    {
                        "id": 43,
                        "stem": r"Solve: \[\sqrt{x} = x - 2\]",
                        "choices": ["A) 0", "B) 2", "C) 4", "D) 6", "E) 8"],
                    },
                    {
                        "id": 44,
                        "stem": r"Solve: \[\sqrt{2x - 1} = \sqrt{x + 3}\]",
                        "choices": ["A) &minus;4", "B) &minus;2", "C) 2", "D) 4", "E) 6"],
                    },
                    # v2.0
                    {
                        "id": 45,
                        "stem": r"Solve: \[\sqrt{x + 4} = x\]",
                        "choices": ["A) 0", "B) 2", "C) 4", "D) 5", "E) No real solution"],
                    },
                    {
                        "id": 46,
                        "stem": r"Solve: \[\sqrt{2x + 3} = x - 1\]",
                        "choices": ["A) 2", "B) 3", "C) 4", "D) 5", "E) No real solution"],
                    },
                ],
            },
            {
                "type": "Exponential Inequalities",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 47,
                        "stem": r"Solve: \[2^x > 8\]",
                        "choices": [r"A) \(x > 3\)", r"B) \(x < 3\)", r"C) \(x \ge 3\)", r"D) \(x \le 3\)", r"E) All real \(x\)"],
                    },
                    {
                        "id": 48,
                        "stem": r"If \(0 < x < 1\), which is greatest?",
                        "choices": [r"A) \(x\)", r"B) \(x^2\)", r"C) \(\sqrt{x}\)", r"D) \(x^3\)", "E) Cannot determine"],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 49,
                        "stem": r"Simplify: \[\frac{3^4}{3^2}\]",
                    },
                    {
                        "id": 50,
                        "stem": r"If \(5^x = 125\), enter \(x\).",
                    },
                    {
                        "id": 51,
                        "stem": r"Simplify: \(\sqrt{72}\)",
                    },
                    {
                        "id": 52,
                        "stem": r"If \(x^{3/2} = 8\), enter \(x\).",
                    },
                    {
                        "id": 53,
                        "stem": r"If \(a^x = a^y\) and \(a > 0\), \(a \neq 1\), enter 1 if \(x = y\) must be true, enter 2 if it need not be true.",
                    },
                    # v2.0
                    {
                        "id": 54,
                        "stem": r"Simplify: \[\frac{5^4}{25}\]",
                    },
                    {
                        "id": 55,
                        "stem": r"If \(x^{3/2} = 27\), enter \(x\).",
                    },
                    {
                        "id": 56,
                        "stem": r"Simplify: \(\sqrt{50} + \sqrt{8}\)",
                    },
                    {
                        "id": 57,
                        "stem": r"Solve: \[3^{x+1} = 27\]",
                    },
                    {
                        "id": 58,
                        "stem": r"If \(a > 0\), \(a \neq 1\), and \[a^{x^2 - 4} = a^5\] Enter the positive value of \(x\).",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 6 – ABSOLUTE VALUE
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "absolute-value",
        "title": "Absolute Value",
        "icon": "6",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(|x| = 5\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(5\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(x < 0\),",
                        "qtyA": r"\(|x|\)",
                        "qtyB": r"\(-x\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(|x - 3| < 2\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(5\)",
                    },
                    {
                        "id": 4,
                        "stem": r"If \(|x| > 3\),",
                        "qtyA": r"\(x^2\)",
                        "qtyB": r"\(9\)",
                    },
                    {
                        "id": 5,
                        "stem": r"If \(|x - 2| = 4\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(6\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(|x| < 1\),",
                        "qtyA": r"\(x^2\)",
                        "qtyB": r"\(x\)",
                    },
                    {
                        "id": 7,
                        "stem": r"If \(|x| = |y|\),",
                        "qtyA": r"\(x\)",
                        "qtyB": r"\(y\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \(\bigl||x| - 3\bigr| = 0\),",
                        "qtyA": r"\(|x|\)",
                        "qtyB": r"\(3\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 9,
                        "stem": r"Solve: \[|2x - 5| = 7\]",
                        "choices": ["A) 6 only", "B) &minus;1 only", "C) &minus;1 and 6", "D) 1 and 6", "E) No solution"],
                    },
                    {
                        "id": 10,
                        "stem": r"Solve: \[|x + 3| = |x - 1|\]",
                        "choices": ["A) &minus;1", "B) 0", "C) 1", "D) 2", "E) 3"],
                    },
                    {
                        "id": 11,
                        "stem": r"Solve: \[|3x - 2| \le 4\]",
                        "choices": [r"A) \(-\frac{2}{3} \le x \le 2\)", r"B) \(-\frac{2}{3} < x < 2\)", r"C) \(x \le -\frac{2}{3}\) or \(x \ge 2\)", r"D) \(x < -\frac{2}{3}\) or \(x > 2\)", "E) All real numbers"],
                    },
                    {
                        "id": 12,
                        "stem": r"Solve: \[|x - 4| > 3\]",
                        "choices": [r"A) \(1 < x < 7\)", r"B) \(x < 1\) or \(x > 7\)", r"C) \(x \le 1\) or \(x \ge 7\)", r"D) \(1 \le x \le 7\)", "E) All real numbers"],
                    },
                    {
                        "id": 13,
                        "stem": r"For what value of \(k\) does \(|x - k| = 0\) have exactly one solution?",
                        "choices": [r"A) Any real \(k\)", r"B) \(k = 0\)", r"C) \(k > 0\)", r"D) \(k < 0\)", r"E) No real \(k\)"],
                    },
                    {
                        "id": 14,
                        "stem": r"Solve: \[|x^2 - 4| = 0\]",
                        "choices": ["A) &minus;2 and 2", "B) 2 only", "C) &minus;2 only", "D) 0 only", "E) No solution"],
                    },
                    {
                        "id": 15,
                        "stem": r"Solve: \[\bigl||x| - 2\bigr| < 1\]",
                        "choices": [
                            r"A) \(1 < |x| < 3\)",
                            r"B) \(|x| < 1\)",
                            r"C) \(|x| > 3\)",
                            r"D) \(-3 < x < -1\) or \(1 < x < 3\)",
                            "E) All real numbers",
                        ],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 16,
                        "stem": "Which equations have exactly two real solutions?",
                        "choices": [
                            r"A) \(|x| = 3\)",
                            r"B) \(|x - 2| = 0\)",
                            r"C) \(|x^2 - 1| = 0\)",
                            r"D) \(|x| = -2\)",
                            r"E) \(|x - 1| = 4\)",
                        ],
                    },
                    {
                        "id": 17,
                        "stem": "Which inequalities describe values within 5 units of 3?",
                        "choices": [
                            r"A) \(|x - 3| < 5\)",
                            r"B) \(|x - 3| \le 5\)",
                            r"C) \(-5 < x - 3 < 5\)",
                            r"D) \(-2 < x < 8\)",
                            r"E) \(x < -2\) or \(x > 8\)",
                        ],
                    },
                    {
                        "id": 18,
                        "stem": "Which are always true?",
                        "choices": [
                            r"A) \(|ab| = |a||b|\)",
                            r"B) \(|a + b| = |a| + |b|\)",
                            r"C) \(|-a| = |a|\)",
                            r"D) \(|a|^2 = a^2\)",
                            r"E) \(|a| = a\)",
                        ],
                    },
                ],
            },
            {
                "type": "Systems Involving Absolute Value",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 19,
                        "stem": r"Solve the system: \[|x| = 3\]\[x + y = 5\] What is the value of \(y\)?",
                        "choices": ["A) 2 only", "B) 8 only", "C) 2 and 8", "D) &minus;2 and 8", "E) Cannot determine"],
                    },
                    {
                        "id": 20,
                        "stem": r"Solve: \[|x - 1| = 2\]\[|y - 2| = 3\] How many ordered pairs \((x, y)\) satisfy both?",
                        "choices": ["A) 1", "B) 2", "C) 3", "D) 4", "E) Infinitely many"],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 21,
                        "stem": r"Solve: \[|4x - 8| = 12\] Enter the larger solution.",
                    },
                    {
                        "id": 22,
                        "stem": r"Solve: \[|3x - 6| > 9\] Enter the smallest integer solution.",
                    },
                    {
                        "id": 23,
                        "stem": r"Solve: \[|x| + 2 = 7\] Enter the sum of the solutions.",
                    },
                    {
                        "id": 24,
                        "stem": r"Solve: \[|x^2 - 9| = 0\] Enter the positive solution.",
                    },
                    {
                        "id": 25,
                        "stem": r"If \(|x - 3| + |x + 1| = 4\), enter the value of \(x\).",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 7 – ALGEBRAIC EXPRESSIONS & SIMPLIFICATION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "algebraic-expressions",
        "title": "Algebraic Expressions & Simplification",
        "icon": "7",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(x = 3\),",
                        "qtyA": r"\(2x^2 - 5x + 1\)",
                        "qtyB": r"\(4\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(x > 0\),",
                        "qtyA": r"\(x(x + 1)\)",
                        "qtyB": r"\(x^2 + x\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(x \neq 0\),",
                        "qtyA": r"\(\dfrac{x^2}{x}\)",
                        "qtyB": r"\(x\)",
                    },
                    {
                        "id": 4,
                        "stem": r"If \(x \neq 2\),",
                        "qtyA": r"\(\dfrac{x^2 - 4}{x - 2}\)",
                        "qtyB": r"\(x + 2\)",
                    },
                    {
                        "id": 5,
                        "stem": r"If \(a > b\),",
                        "qtyA": r"\(a^2 - b^2\)",
                        "qtyB": r"\((a - b)^2\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(x = -1\),",
                        "qtyA": r"\(x^3 - x\)",
                        "qtyB": r"\(0\)",
                    },
                    {
                        "id": 7,
                        "stem": "",
                        "qtyA": r"\((x + 3)^2\)",
                        "qtyB": r"\(x^2 + 9\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \(x > 1\),",
                        "qtyA": r"\(\dfrac{x^2 - 1}{x - 1}\)",
                        "qtyB": r"\(x + 1\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 9,
                        "stem": r"Simplify: \[3(2x - 5) - 4(x + 1)\]",
                        "choices": [r"A) \(2x - 19\)", r"B) \(2x - 11\)", r"C) \(6x - 9\)", r"D) \(2x - 9\)", r"E) \(10x - 11\)"],
                    },
                    {
                        "id": 10,
                        "stem": r"Factor completely: \[x^2 - 9\]",
                        "choices": [r"A) \((x - 3)^2\)", r"B) \((x + 3)^2\)", r"C) \((x - 3)(x + 3)\)", r"D) \((x - 9)(x + 1)\)", "E) Prime"],
                    },
                    {
                        "id": 11,
                        "stem": r"Simplify: \[\frac{x^2 - 16}{x - 4} \quad (x \neq 4)\]",
                        "choices": [r"A) \(x - 4\)", r"B) \(x + 4\)", r"C) \(x^2 - 4\)", "D) 4", r"E) \(x\)"],
                    },
                    {
                        "id": 12,
                        "stem": r"Simplify: \[\frac{\frac{2}{x}}{\frac{3}{x}} \quad (x \neq 0)\]",
                        "choices": [r"A) \(\frac{2}{3}\)", r"B) \(\frac{3}{2}\)", r"C) \(\frac{2x}{3}\)", r"D) \(\frac{3x}{2}\)", r"E) \(x\)"],
                    },
                    {
                        "id": 13,
                        "stem": r"Expand: \[(x - 2)(x + 5)\]",
                        "choices": [r"A) \(x^2 + 3x - 10\)", r"B) \(x^2 - 3x - 10\)", r"C) \(x^2 + 10x - 10\)", r"D) \(x^2 + 3x + 10\)", r"E) \(x^2 - 10\)"],
                    },
                    {
                        "id": 14,
                        "stem": r"Factor: \[ax + ay + bx + by\]",
                        "choices": [r"A) \((a + b)(x + y)\)", r"B) \((a - b)(x + y)\)", r"C) \((a + b)(x - y)\)", r"D) \(ab(x + y)\)", "E) Cannot factor"],
                    },
                    {
                        "id": 15,
                        "stem": r"Simplify: \[(x + 1)^2 - x^2\]",
                        "choices": [r"A) \(2x + 1\)", "B) 1", r"C) \(x + 1\)", r"D) \(2x\)", r"E) \(x^2 + 1\)"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 16,
                        "stem": r"Which expressions are equivalent to \(x^2 - 4x + 4\)?",
                        "choices": [
                            r"A) \((x - 2)^2\)",
                            r"B) \((x + 2)^2\)",
                            r"C) \(x(x - 4) + 4\)",
                            r"D) \((x - 1)(x - 4)\)",
                            r"E) \(x^2 - 4(x - 1)\)",
                        ],
                    },
                    {
                        "id": 17,
                        "stem": r"Which expressions are equal to \(\dfrac{x^2 - 9}{x - 3}\) for all \(x \neq 3\)?",
                        "choices": [
                            r"A) \(x + 3\)",
                            r"B) \(x - 3\)",
                            r"C) \(\frac{(x-3)(x+3)}{x-3}\)",
                            r"D) \(x^2 - 3\)",
                            "E) 6",
                        ],
                    },
                    {
                        "id": 18,
                        "stem": "Which are always true?",
                        "choices": [
                            r"A) \((a + b)^2 = a^2 + b^2\)",
                            r"B) \((a - b)^2 = a^2 - 2ab + b^2\)",
                            r"C) \(a(b + c) = ab + ac\)",
                            r"D) \(a^2 - b^2 = (a - b)(a + b)\)",
                            r"E) \(\frac{a}{b+c} = \frac{a}{b} + \frac{a}{c}\)",
                        ],
                    },
                ],
            },
            {
                "type": "Advanced Rational Expressions",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 19,
                        "stem": r"Simplify: \[\frac{x^2 - 1}{x^2 - x} \quad (x \neq 0, 1)\]",
                        "choices": [r"A) \(\frac{x+1}{x}\)", r"B) \(\frac{x-1}{x}\)", r"C) \(\frac{x+1}{x-1}\)", r"D) \(x + 1\)", "E) 1"],
                    },
                    {
                        "id": 20,
                        "stem": r"Factor completely: \[x^3 - 8\]",
                        "choices": [
                            r"A) \((x-2)(x^2+2x+4)\)",
                            r"B) \((x-2)(x^2-2x+4)\)",
                            r"C) \((x-8)(x^2+8x+64)\)",
                            r"D) \((x-2)^3\)",
                            "E) Prime",
                        ],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 21,
                        "stem": r"Simplify: \[\frac{6x^2}{3x} \quad (x \neq 0)\]",
                    },
                    {
                        "id": 22,
                        "stem": r"Evaluate: \[x^2 - 3x + 2\] when \(x = 4\).",
                    },
                    {
                        "id": 23,
                        "stem": r"Simplify: \[\frac{x^2 - 25}{x + 5} \quad (x \neq -5)\]",
                    },
                    {
                        "id": 24,
                        "stem": r"Expand: \[(2x - 3)^2\]",
                    },
                    {
                        "id": 25,
                        "stem": r"Simplify: \[\frac{x^2 - y^2}{x - y} \quad (x \neq y)\]",
                    },
                    {
                        "id": 26,
                        "stem": r"Simplify: \[\frac{x^2 - 4x}{x} \quad (x \neq 0)\]",
                    },
                    {
                        "id": 27,
                        "stem": r"If \(a + b = 5\) and \(ab = 6\), enter the value of \(a^2 + b^2\).",
                    },
                ],
            },
        ],
    },

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TOPIC 8 – FUNCTIONS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {
        "id": "functions",
        "title": "Functions",
        "icon": "8",
        "sections": [
            {
                "type": "Quantitative Comparison",
                "instructions": "For each question, select:<br><b>A.</b> Quantity A is greater &nbsp; <b>B.</b> Quantity B is greater &nbsp; <b>C.</b> The two quantities are equal &nbsp; <b>D.</b> The relationship cannot be determined",
                "questions": [
                    {
                        "id": 1,
                        "stem": r"If \(f(x) = 3x + 2\),",
                        "qtyA": r"\(f(4)\)",
                        "qtyB": r"\(14\)",
                    },
                    {
                        "id": 2,
                        "stem": r"If \(f(x) = x^2 - 1\),",
                        "qtyA": r"\(f(2)\)",
                        "qtyB": r"\(f(-2)\)",
                    },
                    {
                        "id": 3,
                        "stem": r"If \(f(x) = x^2\) and \(x \neq 0\),",
                        "qtyA": r"\(f(x)\)",
                        "qtyB": r"\(f(-x)\)",
                    },
                    {
                        "id": 4,
                        "stem": r"If \(f(x) = 2x + 1\) and \(g(x) = x - 3\),",
                        "qtyA": r"\(f(g(4))\)",
                        "qtyB": r"\(3\)",
                    },
                    {
                        "id": 5,
                        "stem": r"If \(f(x) = |x|\),",
                        "qtyA": r"\(f(-5)\)",
                        "qtyB": r"\(-5\)",
                    },
                    {
                        "id": 6,
                        "stem": r"If \(f(x) = x^3\),",
                        "qtyA": r"\(f(2)\)",
                        "qtyB": r"\(2f(1)\)",
                    },
                    {
                        "id": 7,
                        "stem": r"If \(f(x) = \dfrac{1}{x}\), \(x \neq 0\),",
                        "qtyA": r"\(f(f(2))\)",
                        "qtyB": r"\(2\)",
                    },
                    {
                        "id": 8,
                        "stem": r"If \(f(x) = x + k\) and \(f(3) = 10\),",
                        "qtyA": r"\(k\)",
                        "qtyB": r"\(7\)",
                    },
                ],
            },
            {
                "type": "Multiple Choice — Single Answer",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 9,
                        "stem": r"If \(f(x) = 4x - 3\), what is \(f(5)\)?",
                        "choices": ["A) 17", "B) 20", "C) 23", "D) 25", "E) 27"],
                    },
                    {
                        "id": 10,
                        "stem": r"If \(f(x) = x^2 + 2x\), what is \(f(-3)\)?",
                        "choices": ["A) 3", "B) &minus;3", "C) 9", "D) 15", "E) 21"],
                    },
                    {
                        "id": 11,
                        "stem": r"If \(f(x) = 2x + 1\) and \(g(x) = x^2\), what is \(f(g(3))\)?",
                        "choices": ["A) 6", "B) 10", "C) 19", "D) 37", "E) 81"],
                    },
                    {
                        "id": 12,
                        "stem": r"If \(f(x) = x - 4\), what is \(f^{-1}(x)\)?",
                        "choices": [r"A) \(x + 4\)", r"B) \(x - 4\)", r"C) \(-x + 4\)", r"D) \(4 - x\)", r"E) \(\frac{x}{4}\)"],
                    },
                    {
                        "id": 13,
                        "stem": r"If \(f(x) = 3x^2 - 1\), for what value of \(x\) does \(f(x) = 11\)?",
                        "choices": ["A) 2", "B) &minus;2", "C) 2 and &minus;2", "D) 1", "E) &minus;1"],
                    },
                    {
                        "id": 14,
                        "stem": r"If \(f(x) = \dfrac{x-1}{x+2}\), what is the domain?",
                        "choices": ["A) All real numbers", r"B) \(x \neq -2\)", r"C) \(x \neq 1\)", r"D) \(x > -2\)", r"E) \(x < -2\)"],
                    },
                    {
                        "id": 15,
                        "stem": r"\[f(x) = \begin{cases} 2x & x < 3 \\ x + 4 & x \ge 3 \end{cases}\] What is \(f(3)\)?",
                        "choices": ["A) 6", "B) 7", "C) 10", "D) 12", "E) Cannot be determined"],
                    },
                ],
            },
            {
                "type": "Multiple Choice — Select One or More",
                "instructions": "Select <b>all</b> answer choices that apply.",
                "questions": [
                    {
                        "id": 16,
                        "stem": r"If \(f(x) = x^2 - 4\), which values satisfy \(f(x) = 0\)?",
                        "choices": ["A) &minus;2", "B) &minus;1", "C) 0", "D) 2", "E) 4"],
                    },
                    {
                        "id": 17,
                        "stem": r"If \(f(x) = 2x + 3\) and \(g(x) = 3x - 1\), which are true?",
                        "choices": [
                            r"A) \(f(g(x)) = 6x + 1\)",
                            r"B) \(g(f(x)) = 6x + 8\)",
                            r"C) \(f(g(x)) = 6x + 5\)",
                            r"D) \(g(f(x)) = 6x + 8\)",
                            r"E) \(f(g(1)) = 7\)",
                        ],
                    },
                    {
                        "id": 18,
                        "stem": r"If \(f(x) = x^2\), which are always true?",
                        "choices": [
                            r"A) \(f(-x) = f(x)\)",
                            r"B) \(f(x+y) = f(x) + f(y)\)",
                            r"C) \(f(x) \ge 0\)",
                            r"D) \(f(x) = 0\) only when \(x = 0\)",
                            r"E) \(f(\sqrt{x}) = x\)",
                        ],
                    },
                ],
            },
            {
                "type": "Function Composition & Structure",
                "instructions": "Select <b>one</b> answer choice.",
                "questions": [
                    {
                        "id": 19,
                        "stem": r"If \(f(x) = 3x - 2\) and \(g(x) = 2x + 5\), find \(g(f(x))\).",
                        "choices": [r"A) \(6x - 4 + 5\)", r"B) \(6x + 1\)", r"C) \(6x + 3\)", r"D) \(5x + 3\)", r"E) \(3x + 5\)"],
                    },
                    {
                        "id": 20,
                        "stem": r"If \(f(x) = x^2\), what is \(f(f(2))\)?",
                        "choices": ["A) 4", "B) 8", "C) 16", "D) 32", "E) 64"],
                    },
                ],
            },
            {
                "type": "Numeric Entry",
                "instructions": "Enter your answer (no choices given).",
                "questions": [
                    {
                        "id": 21,
                        "stem": r"If \(f(x) = 5x - 2\), enter \(f(3)\).",
                    },
                    {
                        "id": 22,
                        "stem": r"If \(f(x) = x^2 - 3x\), enter \(f(4)\).",
                    },
                    {
                        "id": 23,
                        "stem": r"If \(f(x) = x + k\) and \(f(2) = 9\), enter \(k\).",
                    },
                    {
                        "id": 24,
                        "stem": r"If \(f(x) = \dfrac{2}{x}\), enter \(f(f(4))\).",
                    },
                    {
                        "id": 25,
                        "stem": r"If \(f(x) = x^2 - 6x + 5\), enter the value of \(x\) where the function has its minimum.",
                    },
                    {
                        "id": 26,
                        "stem": r"If \(f(x) = ax + b\) and \(f(2) = 7\), \(f(5) = 16\), enter \(a\).",
                    },
                    {
                        "id": 27,
                        "stem": r"If \(f(x + y) = f(x) + f(y)\) for all real numbers \(x, y\), and \(f(1) = 3\), enter \(f(4)\).",
                    },
                ],
            },
        ],
    },
]
# ─────────────────────────────────────────────
# Import Number Properties topic
# ─────────────────────────────────────────────
try:
    from .np_part1 import SECTIONS as _NP1, ANSWERS as _NPA1
except ImportError:
    _NP1, _NPA1 = [], {}
try:
    from .np_part2 import SECTIONS as _NP2, ANSWERS as _NPA2
except ImportError:
    _NP2, _NPA2 = [], {}
try:
    from .np_part3 import SECTIONS as _NP3, ANSWERS as _NPA3
except ImportError:
    _NP3, _NPA3 = [], {}

# ── Split Number Properties into 9 individual topics ──
_NP_ALL_SECTIONS = _NP1 + _NP2 + _NP3
_NP_RAW_ANSWERS = {**_NPA1, **_NPA2, **_NPA3}

_NP_SUBTOPICS = [
    {"id": "np-divisibility",            "title": "Divisibility",                    "icon": "÷",  "start": 0},
    {"id": "np-prime-factorization",     "title": "Prime Factorization",             "icon": "P",  "start": 4},
    {"id": "np-prime-factorization-v2",  "title": "Prime Factorization v2.0",        "icon": "P²", "start": 8},
    {"id": "np-lcm-gcf",                "title": "LCM / GCF",                       "icon": "LC", "start": 12},
    {"id": "np-remainders",             "title": "Remainders & Modular Arithmetic",  "icon": "%",  "start": 16},
    {"id": "np-even-odd",               "title": "Even / Odd (Parity)",              "icon": "±",  "start": 20},
    {"id": "np-consecutive",            "title": "Consecutive Integers",             "icon": "N",  "start": 24},
    {"id": "np-units-digit",            "title": "Units Digit Patterns",             "icon": "#",  "start": 28},
    {"id": "np-positive-negative",      "title": "Positive / Negative Cases",        "icon": "∓",  "start": 32},
]

_NP_REMAPPED = {}
for _npt in _NP_SUBTOPICS:
    _start = _npt["start"]
    _secs = _NP_ALL_SECTIONS[_start:_start + 4]
    if _secs:
        TOPICS.append({
            "id": _npt["id"],
            "title": _npt["title"],
            "icon": _npt["icon"],
            "sections": _secs,
        })
        for _li in range(len(_secs)):
            for _q in _secs[_li]["questions"]:
                _old = ("number-properties", _start + _li, _q["id"])
                if _old in _NP_RAW_ANSWERS:
                    _NP_REMAPPED[(_npt["id"], _li, _q["id"])] = _NP_RAW_ANSWERS[_old]

# ─────────────────────────────────────────────
# Arithmetic & Ratios — split into 6 topics
# ─────────────────────────────────────────────
try:
    from .ar_part1 import SECTIONS as _AR1, ANSWERS as _ARA1
except ImportError:
    _AR1, _ARA1 = [], {}
try:
    from .ar_part2 import SECTIONS as _AR2, ANSWERS as _ARA2
except ImportError:
    _AR2, _ARA2 = [], {}
try:
    from .ar_part3 import SECTIONS as _AR3, ANSWERS as _ARA3
except ImportError:
    _AR3, _ARA3 = [], {}

_AR_ALL_SECTIONS = _AR1 + _AR2 + _AR3
_AR_ALL_ANSWERS = {**_ARA1, **_ARA2, **_ARA3}

_AR_SUBTOPICS = [
    {"id": "ar-percent-change",     "title": "Percent Change",       "icon": "%",  "start": 0},
    {"id": "ar-ratio-proportion",   "title": "Ratio & Proportion",   "icon": "R",  "start": 4},
    {"id": "ar-weighted-averages",  "title": "Weighted Averages",    "icon": "W",  "start": 8},
    {"id": "ar-mixture-problems",   "title": "Mixture Problems",     "icon": "M",  "start": 12},
    {"id": "ar-rate-problems",      "title": "Rate Problems",        "icon": "v",  "start": 16},
    {"id": "ar-compound-interest",  "title": "Compound Interest",    "icon": "$",  "start": 20},
]

for _art in _AR_SUBTOPICS:
    _start = _art["start"]
    _secs = _AR_ALL_SECTIONS[_start:_start + 4]
    if _secs:
        TOPICS.append({
            "id": _art["id"],
            "title": _art["title"],
            "icon": _art["icon"],
            "sections": _secs,
        })

# ─────────────────────────────────────────────
# Geometry — split into 6 topics
# ─────────────────────────────────────────────
try:
    from .geo_part1 import SECTIONS as _GEO1, ANSWERS as _GEOA1
except ImportError:
    _GEO1, _GEOA1 = [], {}
try:
    from .geo_part2 import SECTIONS as _GEO2, ANSWERS as _GEOA2
except ImportError:
    _GEO2, _GEOA2 = [], {}
try:
    from .geo_part3 import SECTIONS as _GEO3, ANSWERS as _GEOA3
except ImportError:
    _GEO3, _GEOA3 = [], {}

_GEO_ALL_SECTIONS = _GEO1 + _GEO2 + _GEO3
_GEO_ALL_ANSWERS = {**_GEOA1, **_GEOA2, **_GEOA3}

_GEO_SUBTOPICS = [
    {"id": "geo-triangles",        "title": "Triangles",            "icon": "△",  "start": 0},
    {"id": "geo-circles",          "title": "Circles",              "icon": "○",  "start": 4},
    {"id": "geo-polygons",         "title": "Polygons",             "icon": "⬡",  "start": 8},
    {"id": "geo-coordinate",       "title": "Coordinate Geometry",  "icon": "xy", "start": 12},
    {"id": "geo-slopes-distance",  "title": "Slopes & Distance",    "icon": "m",  "start": 16},
    {"id": "geo-3d-solids",        "title": "3D Solids",            "icon": "3D", "start": 20},
]

for _gt in _GEO_SUBTOPICS:
    _start = _gt["start"]
    _secs = _GEO_ALL_SECTIONS[_start:_start + 4]
    if _secs:
        TOPICS.append({
            "id": _gt["id"],
            "title": _gt["title"],
            "icon": _gt["icon"],
            "sections": _secs,
        })

# ─────────────────────────────────────────────
# Data Interpretation — split into 6 topics
# ─────────────────────────────────────────────
try:
    from .di_part1 import SECTIONS as _DI1, ANSWERS as _DIA1
except ImportError:
    _DI1, _DIA1 = [], {}
try:
    from .di_part2 import SECTIONS as _DI2, ANSWERS as _DIA2
except ImportError:
    _DI2, _DIA2 = [], {}

_DI_ALL_SECTIONS = _DI1 + _DI2
_DI_ALL_ANSWERS = {**_DIA1, **_DIA2}

_DI_SUBTOPICS = [
    {"id": "di-bar-charts",    "title": "Bar Charts",         "icon": "▐",  "start": 0},
    {"id": "di-grouped-bar",   "title": "Grouped Bar Charts", "icon": "▐▌", "start": 4},
    {"id": "di-line-graphs",   "title": "Line Graphs",        "icon": "📈", "start": 8},
    {"id": "di-pie-charts",    "title": "Pie Charts",         "icon": "◔",  "start": 12},
    {"id": "di-tables",        "title": "Data Tables",        "icon": "▦",  "start": 16},
    {"id": "di-combined",      "title": "Combined Charts",    "icon": "▐~", "start": 20},
]

for _dt in _DI_SUBTOPICS:
    _start = _dt["start"]
    _secs = _DI_ALL_SECTIONS[_start:_start + 4]
    if _secs:
        TOPICS.append({
            "id": _dt["id"],
            "title": _dt["title"],
            "icon": _dt["icon"],
            "sections": _secs,
        })

# ─────────────────────────────────────────────
# Merge answers / explanations / common mistakes
# ─────────────────────────────────────────────
try:
    from .answers_1_4 import ANSWERS as _A14
except ImportError:
    _A14 = {}
try:
    from .answers_5_8 import ANSWERS as _A58
except ImportError:
    _A58 = {}

_ALL_ANSWERS = {**_A14, **_A58, **_NP_REMAPPED, **_AR_ALL_ANSWERS, **_GEO_ALL_ANSWERS, **_DI_ALL_ANSWERS}

for _topic in TOPICS:
    for _si, _section in enumerate(_topic["sections"]):
        for _q in _section["questions"]:
            _key = (_topic["id"], _si, _q["id"])
            if _key in _ALL_ANSWERS:
                _q.update(_ALL_ANSWERS[_key])

# ─────────────────────────────────────────────
# Categories — used for sidebar grouping & homepage
# ─────────────────────────────────────────────
CATEGORIES = [
    {"id": "algebra",             "name": "Algebra",              "icon": "x",  "prefix": ""},
    {"id": "number-properties",   "name": "Number Properties",    "icon": "9",  "prefix": "np-"},
    {"id": "arithmetic-ratios",   "name": "Arithmetic & Ratios",  "icon": "\u03c0", "prefix": "ar-"},
    {"id": "geometry",            "name": "Geometry",             "icon": "\u25b3", "prefix": "geo-"},
    {"id": "data-interpretation", "name": "Data Interpretation",  "icon": "\u2590", "prefix": "di-"},
]

_KNOWN_PREFIXES = tuple(c["prefix"] for c in CATEGORIES if c["prefix"])

for _topic in TOPICS:
    _tid = _topic["id"]
    _topic["category"] = "algebra"
    for _c in CATEGORIES:
        if _c["prefix"] and _tid.startswith(_c["prefix"]):
            _topic["category"] = _c["id"]
            break


def _build_topics_json():
    """Serialize TOPICS to a JSON-safe list (used by favorites, flashcards, etc.)."""
    topics_data = []
    for t in TOPICS:
        td = {"id": t["id"], "title": t["title"], "icon": t["icon"], "category": t["category"], "sections": []}
        for si, s in enumerate(t["sections"]):
            sd = {"type": s.get("type", "") or s.get("title", ""), "instructions": s.get("instructions", ""), "questions": []}
            for q in s["questions"]:
                qd = {
                    "id": q["id"],
                    "stem": q.get("stem", ""),
                }
                if "qtyA" in q:
                    qd["qtyA"] = q["qtyA"]
                    qd["qtyB"] = q["qtyB"]
                if "choices" in q:
                    qd["choices"] = q["choices"]
                if "answer" in q:
                    qd["answer"] = q["answer"]
                if "explanation" in q:
                    qd["explanation"] = q["explanation"]
                if "common_mistake" in q:
                    qd["common_mistake"] = q["common_mistake"]
                sd["questions"].append(qd)
            td["sections"].append(sd)
        topics_data.append(td)
    return topics_data


def _build_categories_json():
    """Serialize CATEGORIES to a JSON-safe list."""
    return [{"id": c["id"], "name": c["name"], "icon": c["icon"]} for c in CATEGORIES]
