"""
Arithmetic & Ratios — Part 3
Sub-topic 5: Rate Problems (Work/Time, Distance/Speed)
Sub-topic 6: Compound Interest
54 questions total (27 per sub-topic), with full answer explanations.
"""

SECTIONS = [
    # ──────────────────────────────────────────────
    # Sub-topic 5: Rate Problems  (Sections 0-3)
    # ──────────────────────────────────────────────

    # Section 0 — Rate Problems: Quantitative Comparison (Q1-6)
    {
        "type": "Rate Problems — Quantitative Comparison",
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
                "stem": r"Machine A completes a job in 4 hours. Machine B completes the same job in 6 hours.",
                "qtyA": r"Time required if both machines work together",
                "qtyB": r"2 hours",
            },
            {
                "id": 2,
                "stem": r"A car travels 60 miles at 30 mph and returns 60 miles at 60 mph.",
                "qtyA": r"The average speed for the entire trip",
                "qtyB": r"45 mph",
            },
            {
                "id": 3,
                "stem": r"Two runners start at the same point and run in opposite directions at speeds of 5 mph and 7 mph.",
                "qtyA": r"The distance between them after 2 hours",
                "qtyB": r"24 miles",
            },
            {
                "id": 4,
                "stem": r"A boat travels downstream at 12 mph and upstream at 8 mph.",
                "qtyA": r"Speed of the boat in still water",
                "qtyB": r"10 mph",
            },
            {
                "id": 5,
                "stem": r"Worker A can complete a job in 10 hours. Worker B can complete the same job in 15 hours.",
                "qtyA": r"Fraction of the job completed in 1 hour working together",
                "qtyB": r"\(\frac{1}{6}\)",
            },
            {
                "id": 6,
                "stem": r"A train travels 100 miles in 2 hours.",
                "qtyA": r"Its speed in miles per hour",
                "qtyB": r"55 mph",
            },
        ],
    },

    # Section 1 — Rate Problems: Multiple Choice – Single Answer (Q7-15)
    {
        "type": "Rate Problems — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"If a car travels 180 miles in 3 hours, what is its average speed?",
                "choices": [
                    r"(A) 50 mph",
                    r"(B) 55 mph",
                    r"(C) 60 mph",
                    r"(D) 65 mph",
                    r"(E) 70 mph",
                ],
            },
            {
                "id": 8,
                "stem": r"Worker A can complete a job in 12 hours. Worker B can complete the same job in 8 hours. How long will it take them working together?",
                "choices": [
                    r"(A) 4 hours",
                    r"(B) 4.8 hours",
                    r"(C) 5 hours",
                    r"(D) 6 hours",
                    r"(E) 6.5 hours",
                ],
            },
            {
                "id": 9,
                "stem": r"A pipe can fill a tank in 6 hours. Another pipe can fill the same tank in 4 hours. How long will it take both pipes working together?",
                "choices": [
                    r"(A) 2 hours",
                    r"(B) 2.4 hours",
                    r"(C) 3 hours",
                    r"(D) 3.5 hours",
                    r"(E) 4 hours",
                ],
            },
            {
                "id": 10,
                "stem": r"Two cars start 300 miles apart and travel toward each other at speeds of 60 mph and 40 mph. How many hours will it take for them to meet?",
                "choices": [
                    r"(A) 2",
                    r"(B) 2.5",
                    r"(C) 3",
                    r"(D) 3.5",
                    r"(E) 4",
                ],
            },
            {
                "id": 11,
                "stem": r"A boat travels 40 miles downstream in 4 hours and the same distance upstream in 5 hours. What is the speed of the current?",
                "choices": [
                    r"(A) 1 mph",
                    r"(B) 2 mph",
                    r"(C) 3 mph",
                    r"(D) 4 mph",
                    r"(E) 5 mph",
                ],
            },
            {
                "id": 12,
                "stem": r"A worker completes half of a job in 3 hours. At that rate, how many hours will it take to complete the entire job?",
                "choices": [
                    r"(A) 4",
                    r"(B) 5",
                    r"(C) 6",
                    r"(D) 7",
                    r"(E) 8",
                ],
            },
            {
                "id": 13,
                "stem": r"A car travels 100 miles at 50 mph and then 100 miles at 25 mph. What is the average speed for the entire trip?",
                "choices": [
                    r"(A) 33⅓ mph",
                    r"(B) 35 mph",
                    r"(C) 37.5 mph",
                    r"(D) 40 mph",
                    r"(E) 45 mph",
                ],
            },
            {
                "id": 14,
                "stem": r"Three workers can complete a job in 5 hours. If one worker leaves, the remaining two workers complete the job in 7.5 hours. How long would it take the single worker alone to complete the job?",
                "choices": [
                    r"(A) 10 hours",
                    r"(B) 12 hours",
                    r"(C) 15 hours",
                    r"(D) 20 hours",
                    r"(E) 30 hours",
                ],
            },
            {
                "id": 15,
                "stem": r"A person walks at 4 mph and runs at 8 mph. If the total trip is 12 miles and takes 2 hours, how many miles were walked?",
                "choices": [
                    r"(A) 2",
                    r"(B) 4",
                    r"(C) 6",
                    r"(D) 8",
                    r"(E) 10",
                ],
            },
        ],
    },

    # Section 2 — Rate Problems: Multiple Choice – Select One or More (Q16-18)
    {
        "type": "Rate Problems — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If two workers can complete a job together in less time than either can alone, which must be true?",
                "choices": [
                    r"(A) Each worker has a positive rate",
                    r"(B) The combined rate equals the sum of individual rates",
                    r"(C) The time working together is the average of their individual times",
                    r"(D) The combined rate is greater than each individual rate",
                    r"(E) The job takes longer working together",
                ],
            },
            {
                "id": 17,
                "stem": r"Which situations involve constant rate?",
                "choices": [
                    r"(A) A car traveling at 60 mph",
                    r"(B) A tank filling at 5 liters per minute",
                    r"(C) A car accelerating",
                    r"(D) A worker completing equal portions per hour",
                    r"(E) A boat changing speed",
                ],
            },
            {
                "id": 18,
                "stem": r"If a car doubles its speed for the same distance, which must be true?",
                "choices": [
                    r"(A) The travel time is cut in half",
                    r"(B) The travel time is doubled",
                    r"(C) The travel time decreases",
                    r"(D) The distance changes",
                    r"(E) The rate increases",
                ],
            },
        ],
    },

    # Section 3 — Rate Problems: Numeric Entry (Q19-27)
    {
        "type": "Rate Problems — Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"A worker can complete a job in 9 hours. Enter the fraction of the job completed in 1 hour.",
            },
            {
                "id": 20,
                "stem": r"Two pipes fill a tank in 6 hours and 9 hours respectively. Enter the number of hours required to fill the tank working together.",
            },
            {
                "id": 21,
                "stem": r"A car travels 150 miles in 2.5 hours. Enter its speed in miles per hour.",
            },
            {
                "id": 22,
                "stem": r"Two cyclists travel toward each other from towns 180 miles apart at 20 mph and 25 mph. Enter the number of hours until they meet.",
            },
            {
                "id": 23,
                "stem": r"A boat's speed in still water is 15 mph and the current is 3 mph. Enter the upstream speed.",
            },
            {
                "id": 24,
                "stem": r"A car travels 60 miles at 30 mph and then 90 miles at 45 mph. Enter the average speed for the entire trip.",
            },
            {
                "id": 25,
                "stem": r"A worker completes 40% of a job in 2 hours. Enter the number of hours needed to complete the entire job.",
            },
            {
                "id": 26,
                "stem": r"Three identical machines can complete a job in 4 hours. Enter the time required for one machine alone.",
            },
            {
                "id": 27,
                "stem": r"Worker A can complete a job in 8 hours and Worker B in 12 hours. They work together for 2 hours, after which Worker B leaves. Enter the number of additional hours Worker A must work alone to finish the job.",
            },
        ],
    },

    # ──────────────────────────────────────────────
    # Sub-topic 6: Compound Interest  (Sections 4-7)
    # ──────────────────────────────────────────────

    # Section 4 — Compound Interest: Quantitative Comparison (Q1-6)
    {
        "type": "Compound Interest — Quantitative Comparison",
        "instructions": (
            "For each question, select:<br>"
            "<b>A.</b> Quantity A is greater &nbsp; "
            "<b>B.</b> Quantity B is greater &nbsp; "
            "<b>C.</b> The two quantities are equal &nbsp; "
            "<b>D.</b> The relationship cannot be determined<br><br>"
            "Assume interest is compounded annually unless otherwise stated."
        ),
        "questions": [
            {
                "id": 1,
                "stem": r"An investment of $1,000 earns 10% annual compound interest for 2 years.",
                "qtyA": r"The total interest earned",
                "qtyB": r"$200",
            },
            {
                "id": 2,
                "stem": r"An investment grows at 5% per year for 3 years.",
                "qtyA": r"The final amount",
                "qtyB": r"\(1.15\) times the original amount",
            },
            {
                "id": 3,
                "stem": r"$2,000 is invested at 4% compound interest for 1 year.",
                "qtyA": r"The amount after 1 year",
                "qtyB": r"$2,080",
            },
            {
                "id": 4,
                "stem": r"An investment earns 8% annually.",
                "qtyA": r"Value after 2 years",
                "qtyB": r"\(1.16\) times the original value",
            },
            {
                "id": 5,
                "stem": r"An investment grows at 10% per year for 2 years.",
                "qtyA": r"Growth if compounded annually",
                "qtyB": r"Growth if simple interest is used",
            },
            {
                "id": 6,
                "stem": r"An investment grows by 20% in the first year and decreases by 20% in the second year.",
                "qtyA": r"Final value",
                "qtyB": r"Original value",
            },
        ],
    },

    # Section 5 — Compound Interest: Multiple Choice – Single Answer (Q7-15)
    {
        "type": "Compound Interest — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"$5,000 is invested at 6% annual compound interest for 2 years. What is the value of the investment after 2 years?",
                "choices": [
                    r"(A) $5,600",
                    r"(B) $5,618",
                    r"(C) $5,636",
                    r"(D) $5,650",
                    r"(E) $5,700",
                ],
            },
            {
                "id": 8,
                "stem": r"An investment doubles in value in 10 years at compound interest. Which expression represents the annual growth factor?",
                "choices": [
                    r"(A) \(1 + \frac{1}{10}\)",
                    r"(B) \(2^{1/10}\)",
                    r"(C) \(10^{1/2}\)",
                    r"(D) \(\frac{2}{10}\)",
                    r"(E) \(2 \times 10\)",
                ],
            },
            {
                "id": 9,
                "stem": r"$1,000 is invested at 5% annual compound interest for 3 years. Which expression represents the amount after 3 years?",
                "choices": [
                    r"(A) \(1000(1.05)(3)\)",
                    r"(B) \(1000(1.05)^3\)",
                    r"(C) \(1000 + 3(0.05)\)",
                    r"(D) \(1000(0.05)^3\)",
                    r"(E) \(1000(1.15)\)",
                ],
            },
            {
                "id": 10,
                "stem": r"An investment of $800 grows to $968 in 2 years at compound interest. What is the annual growth rate?",
                "choices": [
                    r"(A) 8%",
                    r"(B) 9%",
                    r"(C) 10%",
                    r"(D) 11%",
                    r"(E) 12%",
                ],
            },
            {
                "id": 11,
                "stem": r"$10,000 is invested at 5% annual compound interest. Approximately how much is the investment worth after 2 years?",
                "choices": [
                    r"(A) $10,500",
                    r"(B) $10,750",
                    r"(C) $11,000",
                    r"(D) $11,025",
                    r"(E) $11,050",
                ],
            },
            {
                "id": 12,
                "stem": r"An investment grows at 4% annually for 3 years. What is the percent increase over the 3-year period?",
                "choices": [
                    r"(A) 12%",
                    r"(B) 12.48%",
                    r"(C) 12.5%",
                    r"(D) 13%",
                    r"(E) 16%",
                ],
            },
            {
                "id": 13,
                "stem": r"$2,000 earns 10% annual compound interest for 2 years. How much interest is earned in the second year alone?",
                "choices": [
                    r"(A) $200",
                    r"(B) $210",
                    r"(C) $220",
                    r"(D) $240",
                    r"(E) $242",
                ],
            },
            {
                "id": 14,
                "stem": r"An investment grows from $1,000 to $1,210 in 2 years. What is the annual compound interest rate?",
                "choices": [
                    r"(A) 5%",
                    r"(B) 8%",
                    r"(C) 9%",
                    r"(D) 10%",
                    r"(E) 11%",
                ],
            },
            {
                "id": 15,
                "stem": r"An investment increases by 5% annually. After 4 years, the value is closest to what multiple of the original?",
                "choices": [
                    r"(A) 1.15",
                    r"(B) 1.20",
                    r"(C) 1.22",
                    r"(D) 1.25",
                    r"(E) 1.30",
                ],
            },
        ],
    },

    # Section 6 — Compound Interest: Multiple Choice – Select One or More (Q16-18)
    {
        "type": "Compound Interest — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"Which expressions represent compound growth of 8% per year for 3 years?",
                "choices": [
                    r"(A) \(P(1.08)^3\)",
                    r"(B) \(P(1 + 0.08 \cdot 3)\)",
                    r"(C) \(P + 3(0.08P)\)",
                    r"(D) \(P(1.08)(1.08)(1.08)\)",
                    r"(E) \(P(1.24)\)",
                ],
            },
            {
                "id": 17,
                "stem": r"If an investment grows at rate \(r\) per year for \(n\) years, which expressions represent the final amount?",
                "choices": [
                    r"(A) \(P(1+r)^n\)",
                    r"(B) \(P + nr\)",
                    r"(C) \(P(1 + rn)\)",
                    r"(D) \(P(1+r)(1+r)\cdots(1+r)\)",
                    r"(E) \(Pr^n\)",
                ],
            },
            {
                "id": 18,
                "stem": r"If an investment increases 10% in year 1 and 10% in year 2, which must be true?",
                "choices": [
                    r"(A) The total increase is 20%",
                    r"(B) The total increase is greater than 20%",
                    r"(C) The second year's interest is greater than the first year's interest",
                    r"(D) The growth is linear",
                    r"(E) The final value equals \(P(1.10)^2\)",
                ],
            },
        ],
    },

    # Section 7 — Compound Interest: Numeric Entry (Q19-27)
    {
        "type": "Compound Interest — Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"$1,000 is invested at 10% compound interest for 2 years. Enter the final amount.",
            },
            {
                "id": 20,
                "stem": r"$2,000 is invested at 5% compound interest for 3 years. Enter the final amount (rounded to nearest dollar).",
            },
            {
                "id": 21,
                "stem": r"$3,000 grows to $3,630 in 2 years. Enter the annual compound interest rate (as a percent).",
            },
            {
                "id": 22,
                "stem": r"An investment grows at 6% per year for 2 years. Enter the percent increase over the 2-year period.",
            },
            {
                "id": 23,
                "stem": r"$5,000 is invested at 4% compound interest for 3 years. Enter the interest earned in the third year only (rounded to nearest dollar).",
            },
            {
                "id": 24,
                "stem": r"An investment doubles in 8 years. Enter the annual growth factor (rounded to three decimal places).",
            },
            {
                "id": 25,
                "stem": r"$10,000 grows to $12,100 in 2 years. Enter the annual interest rate.",
            },
            {
                "id": 26,
                "stem": r"An investment grows at 3% annually for 5 years. Enter the approximate percent increase over 5 years.",
            },
            {
                "id": 27,
                "stem": r"An investment grows at rate \(r\) per year. After 2 years, its value is \(1.21P\). Enter the value of \(r\).",
            },
        ],
    },
]


# ────────────────────────────────────────────────────────────────
# ANSWERS
# Keys: (topic_id, local_section_idx, question_id)
#   Rate Problems      → topic "ar-rate-problems",       local 0-3
#   Compound Interest  → topic "ar-compound-interest",    local 0-3
# ────────────────────────────────────────────────────────────────

ANSWERS = {
    # =========================================================
    # SUB-TOPIC 5 — Rate Problems
    # =========================================================

    # --- Section 0: Quantitative Comparison (Q1-6) -----------
    ("ar-rate-problems", 0, 1): {
        "answer": "A",
        "explanation": (
            r"Rate of A = \(\frac{1}{4}\) job/hr; rate of B = \(\frac{1}{6}\) job/hr. "
            r"Combined rate = \(\frac{1}{4} + \frac{1}{6} = \frac{5}{12}\) job/hr. "
            r"Time together = \(\frac{12}{5} = 2.4\) hours. "
            r"Quantity A = 2.4 hours > Quantity B = 2 hours, so A is greater."
        ),
    },
    ("ar-rate-problems", 0, 2): {
        "answer": "B",
        "explanation": (
            r"Average speed = Total distance / Total time. "
            r"Time for first leg = \(\frac{60}{30} = 2\) hr; second leg = \(\frac{60}{60} = 1\) hr. "
            r"Average speed = \(\frac{120}{3} = 40\) mph. "
            r"Quantity A = 40 mph < Quantity B = 45 mph, so B is greater."
        ),
        "common_mistake": "Taking the arithmetic mean of the speeds (45 mph) instead of using total distance / total time.",
    },
    ("ar-rate-problems", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Running in opposite directions, the separation rate = 5 + 7 = 12 mph. "
            r"After 2 hours: distance = \(12 \times 2 = 24\) miles. "
            r"Quantity A = 24 = Quantity B. They are equal."
        ),
    },
    ("ar-rate-problems", 0, 4): {
        "answer": "C",
        "explanation": (
            r"Speed in still water = \(\frac{\text{downstream} + \text{upstream}}{2} = \frac{12 + 8}{2} = 10\) mph. "
            r"Quantity A = 10 mph = Quantity B. They are equal."
        ),
    },
    ("ar-rate-problems", 0, 5): {
        "answer": "C",
        "explanation": (
            r"Rate of A = \(\frac{1}{10}\); rate of B = \(\frac{1}{15}\). "
            r"Combined rate = \(\frac{1}{10} + \frac{1}{15} = \frac{3}{30} + \frac{2}{30} = \frac{5}{30} = \frac{1}{6}\). "
            r"Quantity A = \(\frac{1}{6}\) = Quantity B. They are equal."
        ),
    },
    ("ar-rate-problems", 0, 6): {
        "answer": "B",
        "explanation": (
            r"Speed = \(\frac{100}{2} = 50\) mph. "
            r"Quantity A = 50 mph < Quantity B = 55 mph, so B is greater."
        ),
    },

    # --- Section 1: MC Single Answer (Q7-15) -----------------
    ("ar-rate-problems", 1, 7): {
        "answer": "(C) 60 mph",
        "explanation": (
            r"Average speed = \(\frac{\text{distance}}{\text{time}} = \frac{180}{3} = 60\) mph."
        ),
    },
    ("ar-rate-problems", 1, 8): {
        "answer": "(B) 4.8 hours",
        "explanation": (
            r"Rate of A = \(\frac{1}{12}\); rate of B = \(\frac{1}{8}\). "
            r"Combined rate = \(\frac{1}{12} + \frac{1}{8} = \frac{2}{24} + \frac{3}{24} = \frac{5}{24}\). "
            r"Time = \(\frac{24}{5} = 4.8\) hours."
        ),
    },
    ("ar-rate-problems", 1, 9): {
        "answer": "(B) 2.4 hours",
        "explanation": (
            r"Rate of pipe 1 = \(\frac{1}{6}\); rate of pipe 2 = \(\frac{1}{4}\). "
            r"Combined rate = \(\frac{1}{6} + \frac{1}{4} = \frac{2}{12} + \frac{3}{12} = \frac{5}{12}\). "
            r"Time = \(\frac{12}{5} = 2.4\) hours."
        ),
    },
    ("ar-rate-problems", 1, 10): {
        "answer": "(C) 3",
        "explanation": (
            r"They close the gap at a combined rate of \(60 + 40 = 100\) mph. "
            r"Time = \(\frac{300}{100} = 3\) hours."
        ),
    },
    ("ar-rate-problems", 1, 11): {
        "answer": "(A) 1 mph",
        "explanation": (
            r"Downstream speed = \(\frac{40}{4} = 10\) mph; upstream speed = \(\frac{40}{5} = 8\) mph. "
            r"Current speed = \(\frac{10 - 8}{2} = 1\) mph."
        ),
    },
    ("ar-rate-problems", 1, 12): {
        "answer": "(C) 6",
        "explanation": (
            r"Half the job takes 3 hours, so the full job takes \(3 \times 2 = 6\) hours."
        ),
    },
    ("ar-rate-problems", 1, 13): {
        "answer": "(A) 33⅓ mph",
        "explanation": (
            r"Time for first 100 miles = \(\frac{100}{50} = 2\) hr; second 100 miles = \(\frac{100}{25} = 4\) hr. "
            r"Total time = 6 hr; total distance = 200 miles. "
            r"Average speed = \(\frac{200}{6} = 33.\overline{3}\) mph."
        ),
        "common_mistake": "Averaging the two speeds to get 37.5 mph instead of using total distance / total time.",
    },
    ("ar-rate-problems", 1, 14): {
        "answer": "(C) 15 hours",
        "explanation": (
            r"Three workers together: rate = \(\frac{1}{5}\) job/hr. "
            r"Two workers together: rate = \(\frac{1}{7.5} = \frac{2}{15}\) job/hr. "
            r"Rate of the single worker = \(\frac{1}{5} - \frac{2}{15} = \frac{3}{15} - \frac{2}{15} = \frac{1}{15}\) job/hr. "
            r"So the single worker takes 15 hours alone."
        ),
    },
    ("ar-rate-problems", 1, 15): {
        "answer": "(B) 4",
        "explanation": (
            r"Let \(w\) = miles walked, \(12 - w\) = miles run. "
            r"Time equation: \(\frac{w}{4} + \frac{12 - w}{8} = 2\). "
            r"Multiply through by 8: \(2w + 12 - w = 16\), so \(w = 4\). "
            r"Check: \(\frac{4}{4} + \frac{8}{8} = 1 + 1 = 2\) hours and \(4 + 8 = 12\) miles. "
            r"The person walked 4 miles."
        ),
    },

    # --- Section 2: MC Multi Answer (Q16-18) -----------------
    ("ar-rate-problems", 2, 16): {
        "answer": "A, B, D",
        "explanation": (
            r"(A) True — each worker must have a positive rate for combined work to be faster. "
            r"(B) True — combined rate = sum of individual rates is the fundamental work-rate principle. "
            r"(C) False — the combined time is the harmonic mean, not the arithmetic average. "
            r"(D) True — the sum of two positive rates exceeds each individual rate. "
            r"(E) False — working together is always faster, not longer."
        ),
    },
    ("ar-rate-problems", 2, 17): {
        "answer": "A, B, D",
        "explanation": (
            r"(A) A car at a fixed speed of 60 mph is a constant rate. "
            r"(B) A tank filling at 5 liters/min is constant rate. "
            r"(C) Accelerating means the rate is changing — not constant. "
            r"(D) Equal portions per hour is constant rate by definition. "
            r"(E) A boat changing speed is not constant rate."
        ),
    },
    ("ar-rate-problems", 2, 18): {
        "answer": "A, C, E",
        "explanation": (
            r"If speed doubles for the same distance: "
            r"(A) True — \(t = \frac{d}{2v} = \frac{1}{2} \cdot \frac{d}{v}\), so time is halved. "
            r"(B) False — time decreases, not increases. "
            r"(C) True — since time is halved, it decreases. "
            r"(D) False — the distance is stated as the same. "
            r"(E) True — doubling speed means the rate increases."
        ),
        "common_mistake": "Forgetting that halving time automatically means the time decreases — both (A) and (C) are correct.",
    },

    # --- Section 3: Numeric Entry (Q19-27) -------------------
    ("ar-rate-problems", 3, 19): {
        "answer": "1/9",
        "explanation": (
            r"If the full job takes 9 hours, the fraction completed in 1 hour is \(\frac{1}{9}\)."
        ),
    },
    ("ar-rate-problems", 3, 20): {
        "answer": "3.6",
        "explanation": (
            r"Rate of pipe 1 = \(\frac{1}{6}\); rate of pipe 2 = \(\frac{1}{9}\). "
            r"Combined rate = \(\frac{1}{6} + \frac{1}{9} = \frac{3}{18} + \frac{2}{18} = \frac{5}{18}\). "
            r"Time = \(\frac{18}{5} = 3.6\) hours."
        ),
    },
    ("ar-rate-problems", 3, 21): {
        "answer": "60",
        "explanation": (
            r"Speed = \(\frac{150}{2.5} = 60\) mph."
        ),
    },
    ("ar-rate-problems", 3, 22): {
        "answer": "4",
        "explanation": (
            r"Combined closing speed = \(20 + 25 = 45\) mph. "
            r"Time = \(\frac{180}{45} = 4\) hours."
        ),
    },
    ("ar-rate-problems", 3, 23): {
        "answer": "12",
        "explanation": (
            r"Upstream speed = boat speed − current = \(15 - 3 = 12\) mph."
        ),
    },
    ("ar-rate-problems", 3, 24): {
        "answer": "37.5",
        "explanation": (
            r"Time for first leg = \(\frac{60}{30} = 2\) hr; second leg = \(\frac{90}{45} = 2\) hr. "
            r"Total distance = 150 miles; total time = 4 hours. "
            r"Average speed = \(\frac{150}{4} = 37.5\) mph."
        ),
        "common_mistake": "Averaging 30 and 45 to get 37.5 — this happens to give the same answer here only because the two time segments are equal.",
    },
    ("ar-rate-problems", 3, 25): {
        "answer": "5",
        "explanation": (
            r"40% of the job in 2 hours means the rate = 20% per hour. "
            r"Full job = \(\frac{100\%}{20\%/\text{hr}} = 5\) hours."
        ),
    },
    ("ar-rate-problems", 3, 26): {
        "answer": "12",
        "explanation": (
            r"Three machines complete the job in 4 hours, so their combined rate = \(\frac{1}{4}\) job/hr. "
            r"One machine's rate = \(\frac{1}{12}\) job/hr. "
            r"Time for one machine = 12 hours."
        ),
    },
    ("ar-rate-problems", 3, 27): {
        "answer": "14/3",
        "explanation": (
            r"Rate of A = \(\frac{1}{8}\) job/hr; rate of B = \(\frac{1}{12}\) job/hr. "
            r"In 2 hours together they complete \(2\left(\frac{1}{8} + \frac{1}{12}\right) = 2 \cdot \frac{5}{24} = \frac{10}{24} = \frac{5}{12}\). "
            r"Remaining work = \(1 - \frac{5}{12} = \frac{7}{12}\). "
            r"Time for A alone = \(\frac{7/12}{1/8} = \frac{7}{12} \times 8 = \frac{56}{12} = \frac{14}{3}\) hours (approximately 4.67 hours)."
        ),
        "common_mistake": "Forgetting to subtract the work already done in the 2 hours of joint work before calculating A's remaining solo time.",
    },

    # =========================================================
    # SUB-TOPIC 6 — Compound Interest
    # =========================================================

    # --- Section 4 (local 0): Quantitative Comparison (Q1-6) --
    ("ar-compound-interest", 0, 1): {
        "answer": "A",
        "explanation": (
            r"After 2 years: \(1000(1.10)^2 = 1000 \times 1.21 = 1210\). "
            r"Total interest = \(1210 - 1000 = 210\). "
            r"Quantity A = $210 > Quantity B = $200. A is greater."
        ),
        "common_mistake": "Assuming simple interest ($200) instead of compound interest ($210).",
    },
    ("ar-compound-interest", 0, 2): {
        "answer": "A",
        "explanation": (
            r"Final amount with compound interest = \(P(1.05)^3 = P \times 1.157625\). "
            r"Quantity B = \(1.15P\). "
            r"Since \(1.157625P > 1.15P\), Quantity A is greater."
        ),
    },
    ("ar-compound-interest", 0, 3): {
        "answer": "C",
        "explanation": (
            r"After 1 year: \(2000(1.04) = 2080\). "
            r"For a single year, compound and simple interest are identical. "
            r"Quantity A = $2,080 = Quantity B. They are equal."
        ),
    },
    ("ar-compound-interest", 0, 4): {
        "answer": "A",
        "explanation": (
            r"After 2 years: \(P(1.08)^2 = P \times 1.1664\). "
            r"Quantity B = \(1.16P\). "
            r"Since \(1.1664P > 1.16P\), Quantity A is greater."
        ),
        "common_mistake": "Thinking 8% for 2 years is exactly 16%. The compound effect adds an extra 0.64%.",
    },
    ("ar-compound-interest", 0, 5): {
        "answer": "A",
        "explanation": (
            r"Compound growth: \(P(1.10)^2 = 1.21P\); growth = \(0.21P\). "
            r"Simple interest growth: \(P \times 0.10 \times 2 = 0.20P\). "
            r"Quantity A (\(0.21P\)) > Quantity B (\(0.20P\)). A is greater."
        ),
    },
    ("ar-compound-interest", 0, 6): {
        "answer": "B",
        "explanation": (
            r"After year 1: \(P \times 1.20 = 1.20P\). "
            r"After year 2: \(1.20P \times 0.80 = 0.96P\). "
            r"Quantity A = \(0.96P\) < Quantity B = \(P\). B is greater."
        ),
        "common_mistake": "Assuming +20% then −20% returns to the original value. It does not — you lose 4%.",
    },

    # --- Section 5 (local 1): MC Single Answer (Q7-15) -------
    ("ar-compound-interest", 1, 7): {
        "answer": "(B) $5,618",
        "explanation": (
            r"After 2 years: \(5000(1.06)^2 = 5000 \times 1.1236 = 5618\)."
        ),
    },
    ("ar-compound-interest", 1, 8): {
        "answer": r"(B) \(2^{1/10}\)",
        "explanation": (
            r"If the investment doubles in 10 years, then \(P \cdot g^{10} = 2P\), "
            r"so \(g^{10} = 2\) and \(g = 2^{1/10}\)."
        ),
    },
    ("ar-compound-interest", 1, 9): {
        "answer": r"(B) \(1000(1.05)^3\)",
        "explanation": (
            r"The compound interest formula is \(A = P(1 + r)^n\). "
            r"Here: \(A = 1000(1.05)^3\). "
            r"Option (A) multiplies by 3 instead of raising to the power 3. "
            r"Option (E) uses simple interest logic."
        ),
    },
    ("ar-compound-interest", 1, 10): {
        "answer": "(C) 10%",
        "explanation": (
            r"\(800(1 + r)^2 = 968\). "
            r"\((1 + r)^2 = \frac{968}{800} = 1.21\). "
            r"\(1 + r = 1.1\), so \(r = 0.10 = 10\%\)."
        ),
    },
    ("ar-compound-interest", 1, 11): {
        "answer": "(D) $11,025",
        "explanation": (
            r"\(10000(1.05)^2 = 10000 \times 1.1025 = 11025\)."
        ),
    },
    ("ar-compound-interest", 1, 12): {
        "answer": "(B) 12.48%",
        "explanation": (
            r"\((1.04)^3 = 1.124864\). "
            r"Percent increase = \(12.4864\% \approx 12.49\%\). "
            r"The closest answer is 12.48%."
        ),
        "common_mistake": "Multiplying 4% by 3 to get 12%. Compound interest yields slightly more than simple interest over multiple periods.",
    },
    ("ar-compound-interest", 1, 13): {
        "answer": "(C) $220",
        "explanation": (
            r"After year 1: \(2000 \times 1.10 = 2200\). Interest in year 1 = $200. "
            r"After year 2: \(2200 \times 1.10 = 2420\). Interest in year 2 = \(2420 - 2200 = 220\)."
        ),
    },
    ("ar-compound-interest", 1, 14): {
        "answer": "(D) 10%",
        "explanation": (
            r"\(1000(1 + r)^2 = 1210\). "
            r"\((1 + r)^2 = 1.21\). "
            r"\(1 + r = 1.1\), so \(r = 10\%\)."
        ),
    },
    ("ar-compound-interest", 1, 15): {
        "answer": "(C) 1.22",
        "explanation": (
            r"\((1.05)^4 = 1.21550625 \approx 1.22\). "
            r"After 4 years the value is approximately 1.22 times the original."
        ),
    },

    # --- Section 6 (local 2): MC Multi Answer (Q16-18) -------
    ("ar-compound-interest", 2, 16): {
        "answer": "A, D",
        "explanation": (
            r"(A) \(P(1.08)^3\) is the compound interest formula — correct. "
            r"(B) \(P(1 + 0.08 \cdot 3) = P(1.24)\) is simple interest, not compound. "
            r"(C) \(P + 3(0.08P) = P(1.24)\) is also simple interest. "
            r"(D) \(P(1.08)(1.08)(1.08) = P(1.08)^3\) — this is equivalent to (A), so correct. "
            r"(E) \(P(1.24)\) is simple interest for 3 years at 8%."
        ),
    },
    ("ar-compound-interest", 2, 17): {
        "answer": "A, D",
        "explanation": (
            r"(A) \(P(1+r)^n\) is the standard compound interest formula — correct. "
            r"(B) \(P + nr\) is not a valid growth formula. "
            r"(C) \(P(1 + rn)\) is simple interest. "
            r"(D) \(P(1+r)(1+r)\cdots(1+r)\) with \(n\) factors is the expanded form of \((1+r)^n\) — correct. "
            r"(E) \(Pr^n\) omits the base principal and the '1 +' factor."
        ),
    },
    ("ar-compound-interest", 2, 18): {
        "answer": "B, C, E",
        "explanation": (
            r"(A) False — the total increase is \((1.10)^2 - 1 = 0.21 = 21\%\), not 20%. "
            r"(B) True — 21% > 20%. "
            r"(C) True — the second year's interest is 10% of a larger base (1.10P vs P). "
            r"(D) False — compound growth is exponential, not linear. "
            r"(E) True — by definition, \(P(1.10)^2\) is the final value after two years of 10% compounding."
        ),
    },

    # --- Section 7 (local 3): Numeric Entry (Q19-27) ---------
    ("ar-compound-interest", 3, 19): {
        "answer": "1210",
        "explanation": (
            r"\(1000(1.10)^2 = 1000 \times 1.21 = 1210\)."
        ),
    },
    ("ar-compound-interest", 3, 20): {
        "answer": "2315",
        "explanation": (
            r"\(2000(1.05)^3 = 2000 \times 1.157625 = 2315.25 \approx 2315\)."
        ),
    },
    ("ar-compound-interest", 3, 21): {
        "answer": "10",
        "explanation": (
            r"\(3000(1 + r)^2 = 3630\). "
            r"\((1 + r)^2 = 1.21\). "
            r"\(1 + r = 1.1\), so \(r = 0.10 = 10\%\)."
        ),
    },
    ("ar-compound-interest", 3, 22): {
        "answer": "12.36",
        "explanation": (
            r"\((1.06)^2 = 1.1236\). "
            r"Percent increase = \(12.36\%\)."
        ),
    },
    ("ar-compound-interest", 3, 23): {
        "answer": "216",
        "explanation": (
            r"After year 1: \(5000 \times 1.04 = 5200\). "
            r"After year 2: \(5200 \times 1.04 = 5408\). "
            r"After year 3: \(5408 \times 1.04 = 5624.32\). "
            r"Interest in year 3 = \(5624.32 - 5408 = 216.32 \approx 216\)."
        ),
    },
    ("ar-compound-interest", 3, 24): {
        "answer": "1.091",
        "explanation": (
            r"If the investment doubles in 8 years: \(g^8 = 2\). "
            r"\(g = 2^{1/8} \approx 1.0905 \approx 1.091\)."
        ),
    },
    ("ar-compound-interest", 3, 25): {
        "answer": "10",
        "explanation": (
            r"\(10000(1 + r)^2 = 12100\). "
            r"\((1 + r)^2 = 1.21\). "
            r"\(1 + r = 1.1\), so \(r = 0.10 = 10\%\)."
        ),
    },
    ("ar-compound-interest", 3, 26): {
        "answer": "15.93",
        "explanation": (
            r"\((1.03)^5 = 1.159274 \approx 1.1593\). "
            r"Percent increase \(\approx 15.93\%\)."
        ),
    },
    ("ar-compound-interest", 3, 27): {
        "answer": "0.10",
        "explanation": (
            r"\(P(1 + r)^2 = 1.21P\). "
            r"\((1 + r)^2 = 1.21\). "
            r"\(1 + r = 1.1\), so \(r = 0.10\)."
        ),
        "common_mistake": "Dividing 0.21 by 2 to get 0.105. That would be the simple interest rate, not the compound rate.",
    },
}
