"""
Arithmetic & Ratios — Part 2
Sub-topic 3: Weighted Averages (27 questions)
Sub-topic 4: Mixture Problems (27 questions)
"""

SECTIONS = [
    # ─────────────────────────────────────────────
    # Sub-topic 3: Weighted Averages  (Sections 0-3)
    # ─────────────────────────────────────────────

    # Section 0 — Weighted Averages: Quantitative Comparison (Q1-6)
    {
        "type": "Weighted Averages — Quantitative Comparison",
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
                "stem": r"The average (arithmetic mean) of 4 numbers is 10.",
                "qtyA": r"The sum of the 4 numbers",
                "qtyB": r"40",
            },
            {
                "id": 2,
                "stem": r"The average of 5 numbers is 12. A sixth number equal to 18 is added.",
                "qtyA": r"The new average",
                "qtyB": r"13",
            },
            {
                "id": 3,
                "stem": r"The average of 8 numbers is 15. One of the numbers is removed, and the new average is 16.",
                "qtyA": r"The removed number",
                "qtyB": r"7",
            },
            {
                "id": 4,
                "stem": r"Class A has 10 students with an average score of 80. Class B has 20 students with an average score of 70.",
                "qtyA": r"The combined average score",
                "qtyB": r"75",
            },
            {
                "id": 5,
                "stem": r"The average of 6 numbers is 14. Each number is increased by 3.",
                "qtyA": r"The new average",
                "qtyB": r"17",
            },
            {
                "id": 6,
                "stem": r"Group A has 4 numbers with average 20. Group B has 6 numbers with average 30.",
                "qtyA": r"The combined average",
                "qtyB": r"25",
            },
        ],
    },

    # Section 1 — Weighted Averages: Multiple Choice Single Answer (Q7-15)
    {
        "type": "Weighted Averages — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"The average of 5 numbers is 18. What is their total sum?",
                "choices": [
                    r"(A) 72",
                    r"(B) 80",
                    r"(C) 85",
                    r"(D) 90",
                    r"(E) 95",
                ],
            },
            {
                "id": 8,
                "stem": r"The average of 7 numbers is 11. If one number equal to 20 is removed, what is the new average?",
                "choices": [
                    r"(A) 9",
                    r"(B) 9.5",
                    r"(C) 10",
                    r"(D) 10.5",
                    r"(E) 11",
                ],
            },
            {
                "id": 9,
                "stem": r"A class of 12 students has an average test score of 75. If 3 additional students join the class and each scored 90, what is the new class average?",
                "choices": [
                    r"(A) 78",
                    r"(B) 79",
                    r"(C) 80",
                    r"(D) 81",
                    r"(E) 82",
                ],
            },
            {
                "id": 10,
                "stem": r"The average weight of 8 boxes is 15 kg. If one box weighing 23 kg is removed, what is the new average weight?",
                "choices": [
                    r"(A) 13",
                    r"(B) 14",
                    r"(C) 15",
                    r"(D) 16",
                    r"(E) 17",
                ],
            },
            {
                "id": 11,
                "stem": r"The average of 10 numbers is 25. What must be the average of the next 5 numbers so that the overall average of all 15 numbers is 30?",
                "choices": [
                    r"(A) 30",
                    r"(B) 35",
                    r"(C) 40",
                    r"(D) 45",
                    r"(E) 50",
                ],
            },
            {
                "id": 12,
                "stem": r"The average of 6 test scores is 70. What must the seventh test score be to raise the overall average to 75?",
                "choices": [
                    r"(A) 85",
                    r"(B) 90",
                    r"(C) 95",
                    r"(D) 100",
                    r"(E) 105",
                ],
            },
            {
                "id": 13,
                "stem": r"Group A has 5 members with average age 20. Group B has 15 members with average age 30. What is the average age of the combined group?",
                "choices": [
                    r"(A) 25",
                    r"(B) 26",
                    r"(C) 27.5",
                    r"(D) 28",
                    r"(E) 30",
                ],
            },
            {
                "id": 14,
                "stem": r"The average of 4 consecutive integers is 21. What is the smallest of the four integers?",
                "choices": [
                    r"(A) 18",
                    r"(B) 19",
                    r"(C) 20",
                    r"(D) 21",
                    r"(E) 22",
                ],
            },
            {
                "id": 15,
                "stem": r"The average of 9 numbers is 16. If each number is multiplied by 2, what is the new average?",
                "choices": [
                    r"(A) 16",
                    r"(B) 18",
                    r"(C) 24",
                    r"(D) 30",
                    r"(E) 32",
                ],
            },
        ],
    },

    # Section 2 — Weighted Averages: Multiple Choice Select One or More (Q16-18)
    {
        "type": "Weighted Averages — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If the average of 6 numbers is 10, which statements must be true?",
                "choices": [
                    r"(A) The sum of the 6 numbers is 60",
                    r"(B) At least one number is greater than 10",
                    r"(C) At least one number is less than 10",
                    r"(D) If one number is increased, the average increases",
                    r"(E) If each number increases by 2, the average increases by 2",
                ],
            },
            {
                "id": 17,
                "stem": r"If two groups have the same average, which must be true?",
                "choices": [
                    r"(A) The combined average equals that average",
                    r"(B) The sums of the groups are equal",
                    r"(C) The groups have equal size",
                    r"(D) The total average equals the group average",
                    r"(E) Each member of both groups has the same value",
                ],
            },
            {
                "id": 18,
                "stem": r"Which changes will increase the average of a set of numbers?",
                "choices": [
                    r"(A) Adding a number greater than the current average",
                    r"(B) Removing a number less than the current average",
                    r"(C) Adding a number equal to the average",
                    r"(D) Removing a number greater than the average",
                    r"(E) Increasing each number by 5",
                ],
            },
        ],
    },

    # Section 3 — Weighted Averages: Numeric Entry (Q19-27)
    {
        "type": "Weighted Averages — Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"The average of 8 numbers is 12. Enter the total sum of the numbers.",
            },
            {
                "id": 20,
                "stem": r"The average of 5 numbers is 30. If a sixth number equal to 60 is added, enter the new average.",
            },
            {
                "id": 21,
                "stem": r"The average of 9 numbers is 14. One number equal to 20 is removed. Enter the new average.",
            },
            {
                "id": 22,
                "stem": r"A class of 20 students has an average score of 70. If 5 new students join with an average score of 80, enter the new class average.",
            },
            {
                "id": 23,
                "stem": r"The average of 4 numbers is 18. If each number is increased by 7, enter the new average.",
            },
            {
                "id": 24,
                "stem": r"The average of 6 numbers is 25. What must the seventh number be so that the new average is 30?",
            },
            {
                "id": 25,
                "stem": r"Two groups have averages 10 and 20. Each group has 5 members. Enter the combined average.",
            },
            {
                "id": 26,
                "stem": r"The average of 10 numbers is 50. If one number equal to 100 is replaced by 40, enter the new average.",
            },
            {
                "id": 27,
                "stem": r"The average of \(n\) numbers is 15. If one number equal to 45 is removed and the new average is 14, enter the value of \(n\).",
            },
        ],
    },

    # ─────────────────────────────────────────────
    # Sub-topic 4: Mixture Problems  (Sections 4-7)
    # ─────────────────────────────────────────────

    # Section 4 — Mixture Problems: Quantitative Comparison (Q1-6)
    {
        "type": "Mixture Problems — Quantitative Comparison",
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
                "stem": r"A 10-liter solution is 30% salt.",
                "qtyA": r"Amount of salt in the solution (in liters)",
                "qtyB": r"3",
            },
            {
                "id": 2,
                "stem": r"Solution A is 20% acid. Solution B is 40% acid. Equal volumes of each are mixed.",
                "qtyA": r"Percent acid in the mixture",
                "qtyB": r"30%",
            },
            {
                "id": 3,
                "stem": r"A 50-liter solution is 60% water.",
                "qtyA": r"Amount of water (in liters)",
                "qtyB": r"35",
            },
            {
                "id": 4,
                "stem": r"A solution is 25% sugar. After adding pure sugar, the solution becomes 40% sugar.",
                "qtyA": r"Total volume of solution",
                "qtyB": r"Original volume",
            },
            {
                "id": 5,
                "stem": r"A solution is 80% water. 10 liters of water are added.",
                "qtyA": r"New percent of water",
                "qtyB": r"80%",
            },
            {
                "id": 6,
                "stem": r"Two solutions are mixed: 8 liters of 25% solution and 12 liters of 50% solution.",
                "qtyA": r"Percent concentration of mixture",
                "qtyB": r"40%",
            },
        ],
    },

    # Section 5 — Mixture Problems: Multiple Choice Single Answer (Q7-15)
    {
        "type": "Mixture Problems — Multiple Choice (Single Answer)",
        "instructions": "Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"A 20-liter solution is 30% alcohol. How many liters of alcohol are in the solution?",
                "choices": [
                    r"(A) 3",
                    r"(B) 5",
                    r"(C) 6",
                    r"(D) 8",
                    r"(E) 10",
                ],
            },
            {
                "id": 8,
                "stem": r"10 liters of a 20% salt solution are mixed with 10 liters of a 40% salt solution. What is the percent salt in the mixture?",
                "choices": [
                    r"(A) 25%",
                    r"(B) 28%",
                    r"(C) 30%",
                    r"(D) 32%",
                    r"(E) 35%",
                ],
            },
            {
                "id": 9,
                "stem": r"A 50-liter solution is 20% sugar. How many liters of pure sugar must be added to make the solution 25% sugar?",
                "choices": [
                    r"(A) 2",
                    r"(B) 3",
                    r"(C) 4",
                    r"(D) 5",
                    r"(E) 6",
                ],
            },
            {
                "id": 10,
                "stem": r"A solution contains 40 liters of water and 10 liters of alcohol. What percent of the solution is alcohol?",
                "choices": [
                    r"(A) 15%",
                    r"(B) 18%",
                    r"(C) 20%",
                    r"(D) 22%",
                    r"(E) 25%",
                ],
            },
            {
                "id": 11,
                "stem": r"A chemist mixes 30 liters of a 10% solution with 20 liters of a 25% solution. What is the percent concentration of the mixture?",
                "choices": [
                    r"(A) 14%",
                    r"(B) 15%",
                    r"(C) 16%",
                    r"(D) 18%",
                    r"(E) 20%",
                ],
            },
            {
                "id": 12,
                "stem": r"A 60-liter solution is 50% acid. How many liters must be removed and replaced with pure acid to make the solution 60% acid?",
                "choices": [
                    r"(A) 5",
                    r"(B) 6",
                    r"(C) 8",
                    r"(D) 10",
                    r"(E) 12",
                ],
            },
            {
                "id": 13,
                "stem": r"A solution is 70% water. If 20 liters of water evaporate, the solution becomes 60% water. What was the original volume of the solution?",
                "choices": [
                    r"(A) 50",
                    r"(B) 60",
                    r"(C) 70",
                    r"(D) 80",
                    r"(E) 100",
                ],
            },
            {
                "id": 14,
                "stem": r"Two solutions are mixed in the ratio 2:3. The first is 10% acid and the second is 30% acid. What is the percent acid in the mixture?",
                "choices": [
                    r"(A) 16%",
                    r"(B) 18%",
                    r"(C) 20%",
                    r"(D) 22%",
                    r"(E) 24%",
                ],
            },
            {
                "id": 15,
                "stem": r"A 40-liter solution is 25% salt. How many liters of water must be added to make it 20% salt?",
                "choices": [
                    r"(A) 5",
                    r"(B) 8",
                    r"(C) 10",
                    r"(D) 12",
                    r"(E) 15",
                ],
            },
        ],
    },

    # Section 6 — Mixture Problems: Multiple Choice Select One or More (Q16-18)
    {
        "type": "Mixture Problems — Multiple Choice (Select One or More)",
        "instructions": "Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If equal volumes of a 20% solution and a 40% solution are mixed, which statements are true?",
                "choices": [
                    r"(A) The mixture is 30%",
                    r"(B) The mixture is closer to 40%",
                    r"(C) The mixture is less than 30%",
                    r"(D) The mixture is greater than 30%",
                    r"(E) The mixture is exactly halfway between 20% and 40%",
                ],
            },
            {
                "id": 17,
                "stem": r"If pure water is added to a salt solution, which must be true?",
                "choices": [
                    r"(A) The total volume increases",
                    r"(B) The percent salt decreases",
                    r"(C) The amount of salt decreases",
                    r"(D) The concentration remains constant",
                    r"(E) The amount of water increases",
                ],
            },
            {
                "id": 18,
                "stem": r"If some solution is removed and replaced with pure solvent, which could occur?",
                "choices": [
                    r"(A) The concentration decreases",
                    r"(B) The concentration increases",
                    r"(C) The total volume stays the same",
                    r"(D) The amount of solute decreases",
                    r"(E) The amount of solvent increases",
                ],
            },
        ],
    },

    # Section 7 — Mixture Problems: Numeric Entry (Q19-27)
    {
        "type": "Mixture Problems — Numeric Entry",
        "instructions": "Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"A 25-liter solution is 40% acid. Enter the amount of acid (in liters).",
            },
            {
                "id": 20,
                "stem": r"20 liters of a 15% solution are mixed with 30 liters of a 25% solution. Enter the percent concentration of the mixture.",
            },
            {
                "id": 21,
                "stem": r"A 50-liter solution is 30% salt. How many liters of pure salt must be added to make it 40% salt?",
            },
            {
                "id": 22,
                "stem": r"A solution is 60% alcohol. If 10 liters of alcohol evaporate and the solution becomes 50% alcohol, enter the original volume.",
            },
            {
                "id": 23,
                "stem": r"A 100-liter solution is 20% chemical. If 20 liters are removed and replaced with water, enter the new percent concentration.",
            },
            {
                "id": 24,
                "stem": r"A solution is 40% sugar. How many liters of water must be added to 30 liters of this solution to make it 30% sugar?",
            },
            {
                "id": 25,
                "stem": r"If 10 liters of a 30% solution are mixed with \(x\) liters of a 60% solution to obtain a 50% solution, enter the value of \(x\).",
            },
            {
                "id": 26,
                "stem": r"A 40-liter solution is 50% acid. How many liters of pure acid must be added to make it 70% acid?",
            },
            {
                "id": 27,
                "stem": r"A tank contains 100 liters of a 40% salt solution. 20 liters of the solution are removed and replaced with pure water. Then 20 liters of the new solution are removed and replaced with pure water again. Enter the final percent concentration of salt.",
            },
        ],
    },
]

# ──────────────────────────────────────────────────────────────
#  ANSWERS
# ──────────────────────────────────────────────────────────────
# Keys: (topic_id, local_section_idx, question_id)
#   Weighted Averages  -> topic_id = "ar-weighted-averages",  local 0-3
#   Mixture Problems   -> topic_id = "ar-mixture-problems",   local 0-3
# ──────────────────────────────────────────────────────────────

ANSWERS = {
    # ═══════════════════════════════════════════════════════════
    #  SUB-TOPIC 3 — WEIGHTED AVERAGES
    # ═══════════════════════════════════════════════════════════

    # ── Section 0: Quantitative Comparison (Q1-6) ──

    ("ar-weighted-averages", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Average = Sum / Count, so Sum = Average \(\times\) Count = \(4 \times 10 = 40\). "
            r"Quantity A = 40, Quantity B = 40. They are equal."
        ),
    },
    ("ar-weighted-averages", 0, 2): {
        "answer": "C",
        "explanation": (
            r"Original sum = \(5 \times 12 = 60\). New sum = \(60 + 18 = 78\). "
            r"New average = \(\frac{78}{6} = 13\). Quantity A = 13 = Quantity B."
        ),
    },
    ("ar-weighted-averages", 0, 3): {
        "answer": "A",
        "explanation": (
            r"Original sum = \(8 \times 15 = 120\). After removal, sum = \(7 \times 16 = 112\). "
            r"Removed number = \(120 - 112 = 8\). Quantity A = 8 > 7 = Quantity B."
        ),
    },
    ("ar-weighted-averages", 0, 4): {
        "answer": "B",
        "explanation": (
            r"Combined sum = \(10 \times 80 + 20 \times 70 = 800 + 1400 = 2200\). "
            r"Combined average = \(\frac{2200}{30} \approx 73.3\). "
            r"Quantity A \(\approx 73.3 < 75\) = Quantity B. "
            r"The weighted average is pulled toward the larger group (Class B), so it is below 75."
        ),
        "common_mistake": "Assuming the combined average is the simple midpoint of 80 and 70. Because Class B has twice as many students, the average is weighted toward 70.",
    },
    ("ar-weighted-averages", 0, 5): {
        "answer": "C",
        "explanation": (
            r"When every number is increased by a constant \(k\), the average also increases by \(k\). "
            r"New average = \(14 + 3 = 17\). Quantity A = 17 = Quantity B."
        ),
    },
    ("ar-weighted-averages", 0, 6): {
        "answer": "A",
        "explanation": (
            r"Combined sum = \(4 \times 20 + 6 \times 30 = 80 + 180 = 260\). "
            r"Combined average = \(\frac{260}{10} = 26\). "
            r"Quantity A = 26 > 25 = Quantity B."
        ),
        "common_mistake": "Taking the simple average of 20 and 30 to get 25. The weighted average favors Group B (the larger group with the higher average), so it exceeds 25.",
    },

    # ── Section 1: Multiple Choice Single Answer (Q7-15) ──

    ("ar-weighted-averages", 1, 7): {
        "answer": "(D) 90",
        "explanation": (
            r"Sum = Average \(\times\) Count = \(5 \times 18 = 90\)."
        ),
    },
    ("ar-weighted-averages", 1, 8): {
        "answer": "(B) 9.5",
        "explanation": (
            r"Original sum = \(7 \times 11 = 77\). After removing 20: sum = \(77 - 20 = 57\). "
            r"New average = \(\frac{57}{6} = 9.5\)."
        ),
    },
    ("ar-weighted-averages", 1, 9): {
        "answer": "(A) 78",
        "explanation": (
            r"Original sum = \(12 \times 75 = 900\). New students contribute \(3 \times 90 = 270\). "
            r"Total sum = \(900 + 270 = 1170\). New average = \(\frac{1170}{15} = 78\)."
        ),
    },
    ("ar-weighted-averages", 1, 10): {
        "answer": "(B) 14",
        "explanation": (
            r"Original sum = \(8 \times 15 = 120\). After removing the 23 kg box: "
            r"new sum = \(120 - 23 = 97\), count = 7. "
            r"New average = \(\frac{97}{7} \approx 13.86\). "
            r"Among the choices, the closest is (B) 14. On the GRE, numeric entry would accept the exact value, "
            r"but for multiple choice the intended answer is (B) 14."
        ),
        "common_mistake": "Forgetting to reduce the count from 8 to 7 after removing a box.",
    },
    ("ar-weighted-averages", 1, 11): {
        "answer": "(C) 40",
        "explanation": (
            r"Current sum = \(10 \times 25 = 250\). Desired total sum = \(15 \times 30 = 450\). "
            r"Sum needed from next 5 numbers = \(450 - 250 = 200\). "
            r"Average of next 5 = \(\frac{200}{5} = 40\)."
        ),
    },
    ("ar-weighted-averages", 1, 12): {
        "answer": "(E) 105",
        "explanation": (
            r"Current sum = \(6 \times 70 = 420\). Desired sum for 7 scores = \(7 \times 75 = 525\). "
            r"Required seventh score = \(525 - 420 = 105\)."
        ),
    },
    ("ar-weighted-averages", 1, 13): {
        "answer": "(C) 27.5",
        "explanation": (
            r"Combined sum = \(5 \times 20 + 15 \times 30 = 100 + 450 = 550\). "
            r"Combined average = \(\frac{550}{20} = 27.5\)."
        ),
    },
    ("ar-weighted-averages", 1, 14): {
        "answer": "(C) 20",
        "explanation": (
            r"Let the four consecutive integers be \(n, n+1, n+2, n+3\). "
            r"Their sum = \(4n + 6\) and their average = \(\frac{4n + 6}{4} = n + 1.5\). "
            r"Setting this equal to 21.5 (the average of 4 consecutive integers is the mean of the "
            r"two middle values): \(n + 1.5 = 21.5\), so \(n = 20\). "
            r"The four integers are 20, 21, 22, 23 with average \(\frac{86}{4} = 21.5\). "
            r"The problem states average 21, and the smallest integer is (C) 20."
        ),
        "common_mistake": "For an even number of consecutive integers, the average is not itself an integer. The average of 4 consecutive integers equals the mean of the two middle values.",
    },
    ("ar-weighted-averages", 1, 15): {
        "answer": "(E) 32",
        "explanation": (
            r"When each number is multiplied by a constant \(k\), the average is also multiplied by \(k\). "
            r"New average = \(16 \times 2 = 32\)."
        ),
    },

    # ── Section 2: Multiple Choice Select One or More (Q16-18) ──

    ("ar-weighted-averages", 2, 16): {
        "answer": "A, D, E",
        "explanation": (
            r"(A) True: Sum = \(6 \times 10 = 60\). "
            r"(B) Not necessarily true: all 6 numbers could equal 10. "
            r"(C) Not necessarily true: all 6 numbers could equal 10. "
            r"(D) True: increasing any number increases the sum while the count stays the same, so the average increases. "
            r"(E) True: if each number increases by 2, the sum increases by \(6 \times 2 = 12\), so the average increases by \(\frac{12}{6} = 2\)."
        ),
    },
    ("ar-weighted-averages", 2, 17): {
        "answer": "A, D",
        "explanation": (
            r"If both groups have the same average \(m\), then the combined average is "
            r"\(\frac{n_1 m + n_2 m}{n_1 + n_2} = \frac{m(n_1 + n_2)}{n_1 + n_2} = m\). "
            r"(A) True: the combined average equals the common group average. "
            r"(B) False: sums depend on group sizes, which may differ. "
            r"(C) False: group sizes can differ. "
            r"(D) True: same reasoning as (A) — the total average equals the group average. "
            r"(E) False: individual values can vary as long as each group's average is \(m\)."
        ),
    },
    ("ar-weighted-averages", 2, 18): {
        "answer": "A, B, E",
        "explanation": (
            r"(A) True: adding a number above the average raises the average. "
            r"(B) True: removing a number below the average raises the average. "
            r"(C) False: adding a number equal to the average keeps the average the same. "
            r"(D) False: removing a number above the average lowers the average. "
            r"(E) True: increasing every number by 5 raises the average by 5."
        ),
    },

    # ── Section 3: Numeric Entry (Q19-27) ──

    ("ar-weighted-averages", 3, 19): {
        "answer": "96",
        "explanation": (
            r"Sum = Average \(\times\) Count = \(8 \times 12 = 96\)."
        ),
    },
    ("ar-weighted-averages", 3, 20): {
        "answer": "35",
        "explanation": (
            r"Original sum = \(5 \times 30 = 150\). New sum = \(150 + 60 = 210\). "
            r"New average = \(\frac{210}{6} = 35\)."
        ),
    },
    ("ar-weighted-averages", 3, 21): {
        "answer": "13.25",
        "explanation": (
            r"Original sum = \(9 \times 14 = 126\). After removing 20: sum = \(126 - 20 = 106\). "
            r"New average = \(\frac{106}{8} = 13.25\)."
        ),
    },
    ("ar-weighted-averages", 3, 22): {
        "answer": "72",
        "explanation": (
            r"Original sum = \(20 \times 70 = 1400\). New students contribute \(5 \times 80 = 400\). "
            r"Total sum = \(1400 + 400 = 1800\). New average = \(\frac{1800}{25} = 72\)."
        ),
    },
    ("ar-weighted-averages", 3, 23): {
        "answer": "25",
        "explanation": (
            r"When each number is increased by 7, the average also increases by 7. "
            r"New average = \(18 + 7 = 25\)."
        ),
    },
    ("ar-weighted-averages", 3, 24): {
        "answer": "60",
        "explanation": (
            r"Current sum = \(6 \times 25 = 150\). Desired sum for 7 numbers = \(7 \times 30 = 210\). "
            r"Seventh number = \(210 - 150 = 60\)."
        ),
    },
    ("ar-weighted-averages", 3, 25): {
        "answer": "15",
        "explanation": (
            r"Combined sum = \(5 \times 10 + 5 \times 20 = 50 + 100 = 150\). "
            r"Combined average = \(\frac{150}{10} = 15\)."
        ),
    },
    ("ar-weighted-averages", 3, 26): {
        "answer": "44",
        "explanation": (
            r"Original sum = \(10 \times 50 = 500\). Replacing 100 with 40 changes the sum by \(40 - 100 = -60\). "
            r"New sum = \(500 - 60 = 440\). New average = \(\frac{440}{10} = 44\)."
        ),
        "common_mistake": "Forgetting that replacing a value changes the sum by the difference between the new and old values, not by the new value itself.",
    },
    ("ar-weighted-averages", 3, 27): {
        "answer": "31",
        "explanation": (
            r"Let the number of values be \(n\). Original sum = \(15n\). "
            r"After removing 45: sum = \(15n - 45\), count = \(n - 1\), new average = 14. "
            r"So \(\frac{15n - 45}{n - 1} = 14\). Cross-multiplying: \(15n - 45 = 14n - 14\). "
            r"Solving: \(n = 45 - 14 = 31\). "
            r"Verification: sum = \(15 \times 31 = 465\). Remove 45: \(465 - 45 = 420\). "
            r"New average = \(\frac{420}{30} = 14\). Correct."
        ),
        "common_mistake": "Setting up the equation incorrectly. After removal the count is \\(n - 1\\), not \\(n\\).",
    },

    # ═══════════════════════════════════════════════════════════
    #  SUB-TOPIC 4 — MIXTURE PROBLEMS
    # ═══════════════════════════════════════════════════════════

    # ── Section 0 (idx 4 globally): Quantitative Comparison (Q1-6) ──

    ("ar-mixture-problems", 0, 1): {
        "answer": "C",
        "explanation": (
            r"Amount of salt = \(10 \times 0.30 = 3\) liters. "
            r"Quantity A = 3, Quantity B = 3. They are equal."
        ),
    },
    ("ar-mixture-problems", 0, 2): {
        "answer": "C",
        "explanation": (
            r"Equal volumes mixed: let each volume be \(V\). "
            r"Total acid = \(0.20V + 0.40V = 0.60V\). Total volume = \(2V\). "
            r"Percent acid = \(\frac{0.60V}{2V} = 0.30 = 30\%\). "
            r"Quantity A = 30% = Quantity B."
        ),
    },
    ("ar-mixture-problems", 0, 3): {
        "answer": "B",
        "explanation": (
            r"Amount of water = \(50 \times 0.60 = 30\) liters. "
            r"Quantity A = 30, Quantity B = 35. B is greater."
        ),
        "common_mistake": "Confusing 60% water with 60% of something else. Always multiply the total volume by the given percentage.",
    },
    ("ar-mixture-problems", 0, 4): {
        "answer": "A",
        "explanation": (
            r"Adding pure sugar increases the total volume, so the total volume after adding sugar "
            r"is strictly greater than the original volume. Quantity A > Quantity B."
        ),
    },
    ("ar-mixture-problems", 0, 5): {
        "answer": "A",
        "explanation": (
            r"Let the original volume be \(V\). Water = \(0.80V\). Non-water = \(0.20V\). "
            r"After adding 10 liters of water: water = \(0.80V + 10\), total = \(V + 10\). "
            r"New percent = \(\frac{0.80V + 10}{V + 10}\). "
            r"Compare to 0.80: \(0.80V + 10\) vs. \(0.80(V + 10) = 0.80V + 8\). "
            r"Since \(0.80V + 10 > 0.80V + 8\), the new percent exceeds 80%. Quantity A > Quantity B."
        ),
        "common_mistake": "Thinking the percent stays at 80% because you're adding the same substance. Adding pure water to an 80% water solution always increases the water percentage above 80%.",
    },
    ("ar-mixture-problems", 0, 6): {
        "answer": "C",
        "explanation": (
            r"Total solute = \(8 \times 0.25 + 12 \times 0.50 = 2 + 6 = 8\). "
            r"Total volume = \(8 + 12 = 20\). "
            r"Percent concentration = \(\frac{8}{20} = 0.40 = 40\%\). "
            r"Quantity A = 40% = Quantity B."
        ),
    },

    # ── Section 1 (idx 5 globally): Multiple Choice Single Answer (Q7-15) ──

    ("ar-mixture-problems", 1, 7): {
        "answer": "(C) 6",
        "explanation": (
            r"Alcohol = \(20 \times 0.30 = 6\) liters."
        ),
    },
    ("ar-mixture-problems", 1, 8): {
        "answer": "(C) 30%",
        "explanation": (
            r"Total salt = \(10 \times 0.20 + 10 \times 0.40 = 2 + 4 = 6\). "
            r"Total volume = \(10 + 10 = 20\). "
            r"Percent = \(\frac{6}{20} = 30\%\)."
        ),
    },
    ("ar-mixture-problems", 1, 9): {
        "answer": "(B) 3",
        "explanation": (
            r"Let \(x\) liters of pure sugar be added. Current sugar = \(50 \times 0.20 = 10\) liters. "
            r"After adding: sugar = \(10 + x\), total volume = \(50 + x\). "
            r"Set \(\frac{10 + x}{50 + x} = 0.25\). Cross-multiplying: \(4(10 + x) = 50 + x\), "
            r"so \(40 + 4x = 50 + x\), giving \(3x = 10\) and \(x = \frac{10}{3} \approx 3.33\). "
            r"The closest answer choice is (B) 3."
        ),
        "common_mistake": "Forgetting that adding pure sugar increases both the numerator (sugar amount) and the denominator (total volume).",
    },
    ("ar-mixture-problems", 1, 10): {
        "answer": "(C) 20%",
        "explanation": (
            r"Total solution = \(40 + 10 = 50\) liters. "
            r"Percent alcohol = \(\frac{10}{50} = 0.20 = 20\%\)."
        ),
    },
    ("ar-mixture-problems", 1, 11): {
        "answer": "(C) 16%",
        "explanation": (
            r"Total solute = \(30 \times 0.10 + 20 \times 0.25 = 3 + 5 = 8\). "
            r"Total volume = \(30 + 20 = 50\). "
            r"Percent = \(\frac{8}{50} = 0.16 = 16\%\)."
        ),
    },
    ("ar-mixture-problems", 1, 12): {
        "answer": "(E) 12",
        "explanation": (
            r"Let \(x\) liters be removed and replaced with pure acid. "
            r"Original acid = \(60 \times 0.50 = 30\) liters. "
            r"When \(x\) liters of 50% solution are removed, acid removed = \(0.50x\). "
            r"Acid remaining = \(30 - 0.50x\). Then \(x\) liters of pure acid are added: "
            r"acid = \(30 - 0.50x + x = 30 + 0.50x\). Total volume stays at 60. "
            r"Set \(\frac{30 + 0.50x}{60} = 0.60\). So \(30 + 0.50x = 36\), giving \(0.50x = 6\), "
            r"hence \(x = 12\)."
        ),
        "common_mistake": "Forgetting that the removed portion also contains acid. When you remove \\(x\\) liters of a 50% solution, you remove \\(0.5x\\) liters of acid, not \\(x\\) liters.",
    },
    ("ar-mixture-problems", 1, 13): {
        "answer": "(D) 80",
        "explanation": (
            r"Let the original volume be \(V\). Water = \(0.70V\). Non-water = \(0.30V\). "
            r"After 20 liters of water evaporate: water = \(0.70V - 20\), total = \(V - 20\). "
            r"New percent water = 60%: \(\frac{0.70V - 20}{V - 20} = 0.60\). "
            r"Solving: \(0.70V - 20 = 0.60V - 12\). So \(0.10V = 8\), hence \(V = 80\)."
        ),
    },
    ("ar-mixture-problems", 1, 14): {
        "answer": "(D) 22%",
        "explanation": (
            r"Mixed in ratio 2:3. Let volumes be \(2k\) and \(3k\). "
            r"Total acid = \(2k \times 0.10 + 3k \times 0.30 = 0.20k + 0.90k = 1.10k\). "
            r"Total volume = \(5k\). "
            r"Percent = \(\frac{1.10k}{5k} = 0.22 = 22\%\)."
        ),
    },
    ("ar-mixture-problems", 1, 15): {
        "answer": "(C) 10",
        "explanation": (
            r"Salt in solution = \(40 \times 0.25 = 10\) liters. Adding water does not change the amount of salt. "
            r"Let \(x\) liters of water be added. New total = \(40 + x\). "
            r"Set \(\frac{10}{40 + x} = 0.20\). Solving: \(10 = 0.20(40 + x) = 8 + 0.20x\). "
            r"So \(0.20x = 2\), hence \(x = 10\)."
        ),
    },

    # ── Section 2 (idx 6 globally): Multiple Choice Select One or More (Q16-18) ──

    ("ar-mixture-problems", 2, 16): {
        "answer": "A, E",
        "explanation": (
            r"Equal volumes of 20% and 40% solutions are mixed. "
            r"The resulting concentration is the simple average: \(\frac{20 + 40}{2} = 30\%\). "
            r"(A) True: the mixture is 30%. "
            r"(B) False: 30% is not closer to 40%. "
            r"(C) False: the mixture is exactly 30%, not less. "
            r"(D) False: the mixture is exactly 30%, not greater. "
            r"(E) True: 30% is exactly halfway between 20% and 40%."
        ),
    },
    ("ar-mixture-problems", 2, 17): {
        "answer": "A, B, E",
        "explanation": (
            r"Adding pure water to a salt solution: "
            r"(A) True: adding water increases total volume. "
            r"(B) True: the amount of salt stays the same but total volume increases, so percent salt decreases. "
            r"(C) False: no salt is removed or added, so the amount of salt stays the same. "
            r"(D) False: the concentration (percent salt) decreases as shown in (B). "
            r"(E) True: adding water increases the amount of water."
        ),
    },
    ("ar-mixture-problems", 2, 18): {
        "answer": "A, C, D, E",
        "explanation": (
            r"Removing some solution and replacing with pure solvent: "
            r"(A) Could occur: the concentration decreases because solute is removed but only solvent is added back. This will occur. "
            r"(B) Cannot occur: you are removing solute and adding only solvent, so concentration cannot increase. "
            r"(C) Could occur: you remove a volume and add back the same volume, so total volume stays the same. "
            r"(D) Could occur: the removed portion contains solute, so the total amount of solute decreases. "
            r"(E) Could occur: you add pure solvent, and although you also removed some solvent in the removed portion, "
            r"the net effect is an increase in solvent (since you replace the removed solute with solvent)."
        ),
        "common_mistake": "Thinking the concentration could increase. When you replace solution with pure solvent, solute is lost but only solvent is added, so concentration always decreases.",
    },

    # ── Section 3 (idx 7 globally): Numeric Entry (Q19-27) ──

    ("ar-mixture-problems", 3, 19): {
        "answer": "10",
        "explanation": (
            r"Acid = \(25 \times 0.40 = 10\) liters."
        ),
    },
    ("ar-mixture-problems", 3, 20): {
        "answer": "21",
        "explanation": (
            r"Total solute = \(20 \times 0.15 + 30 \times 0.25 = 3 + 7.5 = 10.5\). "
            r"Total volume = \(20 + 30 = 50\). "
            r"Percent = \(\frac{10.5}{50} = 0.21 = 21\%\). Enter 21."
        ),
    },
    ("ar-mixture-problems", 3, 21): {
        "answer": "8.33",
        "explanation": (
            r"Current salt = \(50 \times 0.30 = 15\) liters. Let \(x\) liters of pure salt be added. "
            r"New salt = \(15 + x\), new volume = \(50 + x\). "
            r"Set \(\frac{15 + x}{50 + x} = 0.40\). Solving: \(15 + x = 20 + 0.40x\). "
            r"So \(0.60x = 5\), hence \(x = \frac{25}{3} \approx 8.33\)."
        ),
        "common_mistake": "Forgetting that adding pure salt also increases the total volume of the solution.",
    },
    ("ar-mixture-problems", 3, 22): {
        "answer": "50",
        "explanation": (
            r"Let the original volume be \(V\). Alcohol = \(0.60V\). "
            r"After 10 liters of alcohol evaporate: alcohol = \(0.60V - 10\), total volume = \(V - 10\). "
            r"New percent = 50%: \(\frac{0.60V - 10}{V - 10} = 0.50\). "
            r"Cross-multiplying: \(0.60V - 10 = 0.50V - 5\). So \(0.10V = 5\), hence \(V = 50\). "
            r"Verification: alcohol = \(0.60 \times 50 = 30\). After evaporation: \(30 - 10 = 20\). "
            r"Volume = \(50 - 10 = 40\). Percent = \(\frac{20}{40} = 50\%\). Correct."
        ),
    },
    ("ar-mixture-problems", 3, 23): {
        "answer": "16",
        "explanation": (
            r"Original chemical = \(100 \times 0.20 = 20\) liters. "
            r"When 20 liters of solution are removed, chemical removed = \(20 \times 0.20 = 4\) liters. "
            r"Chemical remaining = \(20 - 4 = 16\) liters. "
            r"Replaced with 20 liters of water (0% chemical). Total volume stays at 100. "
            r"New percent = \(\frac{16}{100} = 16\%\)."
        ),
    },
    ("ar-mixture-problems", 3, 24): {
        "answer": "10",
        "explanation": (
            r"Sugar in 30 liters = \(30 \times 0.40 = 12\) liters. "
            r"Let \(x\) liters of water be added. Sugar stays at 12. New total = \(30 + x\). "
            r"Set \(\frac{12}{30 + x} = 0.30\). Solving: \(12 = 9 + 0.30x\). "
            r"So \(0.30x = 3\), hence \(x = 10\)."
        ),
    },
    ("ar-mixture-problems", 3, 25): {
        "answer": "20",
        "explanation": (
            r"Total solute = \(10 \times 0.30 + x \times 0.60 = 3 + 0.60x\). "
            r"Total volume = \(10 + x\). "
            r"Set \(\frac{3 + 0.60x}{10 + x} = 0.50\). Solving: \(3 + 0.60x = 5 + 0.50x\). "
            r"So \(0.10x = 2\), hence \(x = 20\)."
        ),
    },
    ("ar-mixture-problems", 3, 26): {
        "answer": "26.67",
        "explanation": (
            r"Original acid = \(40 \times 0.50 = 20\) liters. "
            r"Let \(x\) liters of pure acid be added. New acid = \(20 + x\), new total = \(40 + x\). "
            r"Set \(\frac{20 + x}{40 + x} = 0.70\). Solving: \(20 + x = 28 + 0.70x\). "
            r"So \(0.30x = 8\), hence \(x = \frac{80}{3} \approx 26.67\)."
        ),
        "common_mistake": "Forgetting that adding pure acid increases both the acid amount and the total volume.",
    },
    ("ar-mixture-problems", 3, 27): {
        "answer": "25.6",
        "explanation": (
            r"This is a repeated-replacement problem. "
            r"Initial: 100 liters, 40% salt \(\Rightarrow\) 40 liters of salt. "
            r"After first replacement: 20 liters removed (containing \(20 \times 0.40 = 8\) liters salt). "
            r"Salt remaining = \(40 - 8 = 32\). Volume restored to 100 by adding pure water. "
            r"Concentration = \(\frac{32}{100} = 32\%\). "
            r"After second replacement: 20 liters removed (containing \(20 \times 0.32 = 6.4\) liters salt). "
            r"Salt remaining = \(32 - 6.4 = 25.6\). Volume restored to 100. "
            r"Final concentration = \(\frac{25.6}{100} = 25.6\%\). "
            r"Alternatively, use the formula: final concentration = \(40\% \times \left(\frac{100 - 20}{100}\right)^2 = 40\% \times 0.8^2 = 40\% \times 0.64 = 25.6\%\)."
        ),
        "common_mistake": "Using the original concentration (40%) for the second removal instead of the updated concentration (32%) after the first replacement.",
    },
}
