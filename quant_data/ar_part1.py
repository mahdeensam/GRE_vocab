"""
Arithmetic & Ratios — Part 1
Sub-topics: Percent Change, Ratio & Proportion
54 questions total (27 per sub-topic), with full answer explanations.
"""

SECTIONS = [
    # =====================================================================
    # SUB-TOPIC 1: PERCENT CHANGE  (Sections 0-3)
    # =====================================================================

    # --- Section 0: Percent Change — Quantitative Comparison (Q1-6) ------
    {
        "type": "Percent Change — Quantitative Comparison",
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
                "stem": r"A quantity is increased by 20 percent and then decreased by 20 percent.",
                "qtyA": r"The final value",
                "qtyB": r"The original value",
            },
            {
                "id": 2,
                "stem": r"A price increases from 50 to 65.",
                "qtyA": r"The percent increase",
                "qtyB": r"30%",
            },
            {
                "id": 3,
                "stem": r"A number is decreased by 25 percent and the result is 75.",
                "qtyA": r"The original number",
                "qtyB": r"100",
            },
            {
                "id": 4,
                "stem": r"A value increases from 80 to 100.",
                "qtyA": r"The percent increase",
                "qtyB": r"20%",
            },
            {
                "id": 5,
                "stem": r"A quantity is increased by 10 percent and then increased again by 10 percent.",
                "qtyA": r"The final value",
                "qtyB": r"120% of the original value",
            },
            {
                "id": 6,
                "stem": r"A price is decreased by 40 percent and then increased by 40 percent.",
                "qtyA": r"The final price",
                "qtyB": r"The original price",
            },
        ],
    },

    # --- Section 1: Percent Change — Multiple Choice (Single Answer) (Q7-15) ---
    {
        "type": "Percent Change — Multiple Choice (Single Answer)",
        "instructions": r"Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"A number is increased by 25 percent and the result is 250. What was the original number?",
                "choices": [
                    r"(A) 150",
                    r"(B) 180",
                    r"(C) 200",
                    r"(D) 225",
                    r"(E) 240",
                ],
            },
            {
                "id": 8,
                "stem": r"The price of a jacket decreases from $120 to $90. What is the percent decrease?",
                "choices": [
                    r"(A) 20%",
                    r"(B) 25%",
                    r"(C) 30%",
                    r"(D) 33⅓%",
                    r"(E) 40%",
                ],
            },
            {
                "id": 9,
                "stem": r"A salary increases from $40,000 to $46,000. What is the percent increase?",
                "choices": [
                    r"(A) 10%",
                    r"(B) 12%",
                    r"(C) 15%",
                    r"(D) 18%",
                    r"(E) 20%",
                ],
            },
            {
                "id": 10,
                "stem": r"A value is increased by 30 percent and then decreased by 10 percent. What is the net percent change?",
                "choices": [
                    r"(A) 17% increase",
                    r"(B) 20% increase",
                    r"(C) 17% decrease",
                    r"(D) 20% decrease",
                    r"(E) 3% increase",
                ],
            },
            {
                "id": 11,
                "stem": r"After a 20 percent discount, a shirt costs $64. What was the original price?",
                "choices": [
                    r"(A) 70",
                    r"(B) 75",
                    r"(C) 80",
                    r"(D) 85",
                    r"(E) 90",
                ],
            },
            {
                "id": 12,
                "stem": r"A number is decreased by 20 percent and then increased by 25 percent. What is the net percent change?",
                "choices": [
                    r"(A) 0%",
                    r"(B) 5% increase",
                    r"(C) 5% decrease",
                    r"(D) 10% increase",
                    r"(E) 10% decrease",
                ],
            },
            {
                "id": 13,
                "stem": r"The population of a town increases by 5 percent each year for 2 years. If the original population was 10,000, what is the population after 2 years?",
                "choices": [
                    r"(A) 10,500",
                    r"(B) 11,000",
                    r"(C) 11,025",
                    r"(D) 11,050",
                    r"(E) 11,100",
                ],
            },
            {
                "id": 14,
                "stem": r"A price increases by 50 percent and then decreases by 50 percent. If the original price was $100, what is the final price?",
                "choices": [
                    r"(A) 50",
                    r"(B) 75",
                    r"(C) 100",
                    r"(D) 125",
                    r"(E) 150",
                ],
            },
            {
                "id": 15,
                "stem": r"A number is increased by 10 percent and then increased by 20 percent. What is the overall percent increase?",
                "choices": [
                    r"(A) 28%",
                    r"(B) 30%",
                    r"(C) 32%",
                    r"(D) 35%",
                    r"(E) 40%",
                ],
            },
        ],
    },

    # --- Section 2: Percent Change — Multiple Choice (Select One or More) (Q16-18) ---
    {
        "type": "Percent Change — Multiple Choice (Select One or More)",
        "instructions": r"Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If a quantity is increased by 50 percent and then decreased by 50 percent, which statements are true?",
                "choices": [
                    r"(A) The final value equals the original value",
                    r"(B) The final value is less than the original value",
                    r"(C) The final value is greater than the original value",
                    r"(D) The net change is a decrease",
                    r"(E) The net change is zero",
                ],
            },
            {
                "id": 17,
                "stem": r"If a value is increased by \(x\) percent and then decreased by \(x\) percent (where \(x > 0\)), which must be true?",
                "choices": [
                    r"(A) The final value equals the original value",
                    r"(B) The final value is less than the original value",
                    r"(C) The final value is greater than the original value",
                    r"(D) The net change is zero",
                    r"(E) The net change is negative",
                ],
            },
            {
                "id": 18,
                "stem": r"If a number increases from 40 to 50, which statements are true?",
                "choices": [
                    r"(A) The percent increase is 25%",
                    r"(B) The percent increase is 20%",
                    r"(C) The increase is 10",
                    r"(D) The increase is 25% of 40",
                    r"(E) The increase is 20% of 50",
                ],
            },
        ],
    },

    # --- Section 3: Percent Change — Numeric Entry (Q19-27) ---
    {
        "type": "Percent Change — Numeric Entry",
        "instructions": r"Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"A number is increased by 15 percent and the result is 230. Enter the original number.",
            },
            {
                "id": 20,
                "stem": r"A value decreases from 500 to 425. Enter the percent decrease.",
            },
            {
                "id": 21,
                "stem": r"A price increases by 12 percent and then increases by 8 percent. Enter the overall percent increase.",
            },
            {
                "id": 22,
                "stem": r"A quantity is decreased by 30 percent and then increased by 50 percent. If the original value was 200, enter the final value.",
            },
            {
                "id": 23,
                "stem": r"After a 25 percent discount, the sale price of an item is 150. Enter the original price.",
            },
            {
                "id": 24,
                "stem": r"A number is increased by 20 percent and then decreased by 10 percent. If the original number was 500, enter the final number.",
            },
            {
                "id": 25,
                "stem": r"If a value increases from 60 to 75, enter the percent increase.",
            },
            {
                "id": 26,
                "stem": r"If a price decreases by 20 percent and then decreases again by 10 percent, enter the total percent decrease.",
            },
            {
                "id": 27,
                "stem": (
                    r"A quantity is increased by \(p\) percent and then decreased by \(p\) percent, where \(p > 0\). "
                    r"Enter 1 if the final value must equal the original value. "
                    r"Enter 2 if the final value must be less than the original value. "
                    r"Enter 3 if the relationship cannot be determined without knowing \(p\)."
                ),
            },
        ],
    },

    # =====================================================================
    # SUB-TOPIC 2: RATIO & PROPORTION  (Sections 4-7)
    # =====================================================================

    # --- Section 4: Ratio & Proportion — Quantitative Comparison (Q1-6) ---
    {
        "type": "Ratio & Proportion — Quantitative Comparison",
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
                "stem": r"The ratio of \(x\) to \(y\) is 3 to 5.",
                "qtyA": r"\(x\)",
                "qtyB": r"\(y\)",
            },
            {
                "id": 2,
                "stem": r"The ratio of \(a\) to \(b\) is 2 to 3, and \(a + b = 25\).",
                "qtyA": r"\(a\)",
                "qtyB": r"10",
            },
            {
                "id": 3,
                "stem": r"The ratio of boys to girls in a class is 4 to 7.",
                "qtyA": r"The fraction of the class that are boys",
                "qtyB": r"\(\frac{4}{11}\)",
            },
            {
                "id": 4,
                "stem": r"If \(x : y = 5 : 8\),",
                "qtyA": r"\(\frac{x}{y}\)",
                "qtyB": r"\(\frac{8}{5}\)",
            },
            {
                "id": 5,
                "stem": r"Two numbers are in the ratio 3:4. The larger number is 28.",
                "qtyA": r"The smaller number",
                "qtyB": r"21",
            },
            {
                "id": 6,
                "stem": r"If \(a : b = 4 : 5\) and \(b : c = 2 : 3\),",
                "qtyA": r"\(a : c\)",
                "qtyB": r"\(8 : 15\)",
            },
        ],
    },

    # --- Section 5: Ratio & Proportion — Multiple Choice (Single Answer) (Q7-15) ---
    {
        "type": "Ratio & Proportion — Multiple Choice (Single Answer)",
        "instructions": r"Select <b>one</b> answer.",
        "questions": [
            {
                "id": 7,
                "stem": r"The ratio of \(x\) to \(y\) is 7 to 9. If \(x + y = 80\), what is the value of \(x\)?",
                "choices": [
                    r"(A) 30",
                    r"(B) 32",
                    r"(C) 35",
                    r"(D) 40",
                    r"(E) 45",
                ],
            },
            {
                "id": 8,
                "stem": r"A mixture contains red and blue marbles in the ratio 3:5. If there are 40 marbles in total, how many are red?",
                "choices": [
                    r"(A) 12",
                    r"(B) 15",
                    r"(C) 18",
                    r"(D) 20",
                    r"(E) 25",
                ],
            },
            {
                "id": 9,
                "stem": r"If \(a : b = 2 : 3\) and \(b : c = 4 : 5\), what is \(a : c\)?",
                "choices": [
                    r"(A) 2:5",
                    r"(B) 4:5",
                    r"(C) 8:15",
                    r"(D) 2:15",
                    r"(E) 4:15",
                ],
            },
            {
                "id": 10,
                "stem": r"Two numbers are in the ratio 5:7. If the difference between them is 18, what is the larger number?",
                "choices": [
                    r"(A) 30",
                    r"(B) 35",
                    r"(C) 42",
                    r"(D) 45",
                    r"(E) 63",
                ],
            },
            {
                "id": 11,
                "stem": r"If the ratio of men to women in a room is 3:2 and there are 50 people in the room, how many are women?",
                "choices": [
                    r"(A) 15",
                    r"(B) 18",
                    r"(C) 20",
                    r"(D) 25",
                    r"(E) 30",
                ],
            },
            {
                "id": 12,
                "stem": r"If \(x : y = 3 : 4\) and both are increased by 6, the new ratio is 5:6. What is the value of \(x\)?",
                "choices": [
                    r"(A) 6",
                    r"(B) 9",
                    r"(C) 12",
                    r"(D) 15",
                    r"(E) 18",
                ],
            },
            {
                "id": 13,
                "stem": r"If \(a : b = 4 : 7\), and \(a\) is increased by 50% while \(b\) remains unchanged, what is the new ratio?",
                "choices": [
                    r"(A) 4:7",
                    r"(B) 6:7",
                    r"(C) 2:7",
                    r"(D) 7:6",
                    r"(E) 6:11",
                ],
            },
            {
                "id": 14,
                "stem": r"A recipe requires flour and sugar in the ratio 5:2. If 3 more cups of sugar are added, the new ratio becomes 5:3. How many cups of sugar were originally used?",
                "choices": [
                    r"(A) 2",
                    r"(B) 4",
                    r"(C) 6",
                    r"(D) 8",
                    r"(E) 10",
                ],
            },
            {
                "id": 15,
                "stem": r"If two numbers are in the ratio 8:11 and their sum is 190, what is the smaller number?",
                "choices": [
                    r"(A) 70",
                    r"(B) 72",
                    r"(C) 80",
                    r"(D) 88",
                    r"(E) 110",
                ],
            },
        ],
    },

    # --- Section 6: Ratio & Proportion — Multiple Choice (Select One or More) (Q16-18) ---
    {
        "type": "Ratio & Proportion — Multiple Choice (Select One or More)",
        "instructions": r"Select <b>all</b> that apply.",
        "questions": [
            {
                "id": 16,
                "stem": r"If \(x : y = 3 : 5\), which expressions could represent \(x\) and \(y\)?",
                "choices": [
                    r"(A) 6 and 10",
                    r"(B) 9 and 15",
                    r"(C) 12 and 18",
                    r"(D) 15 and 25",
                    r"(E) 18 and 30",
                ],
            },
            {
                "id": 17,
                "stem": r"If \(a : b = 2 : 3\), which statements must be true?",
                "choices": [
                    r"(A) \(\frac{a}{a+b} = \frac{2}{5}\)",
                    r"(B) \(\frac{b}{a+b} = \frac{3}{5}\)",
                    r"(C) \(a = \frac{2}{3}b\)",
                    r"(D) \(b = \frac{3}{2}a\)",
                    r"(E) \(a < b\)",
                ],
            },
            {
                "id": 18,
                "stem": r"If the ratio of boys to girls is 4:5 and 3 boys leave, which could be true?",
                "choices": [
                    r"(A) The ratio becomes 1:1",
                    r"(B) The ratio becomes 3:5",
                    r"(C) The total decreases",
                    r"(D) The number of girls increases",
                    r"(E) The ratio becomes 4:5",
                ],
            },
        ],
    },

    # --- Section 7: Ratio & Proportion — Numeric Entry (Q19-27) ---
    {
        "type": "Ratio & Proportion — Numeric Entry",
        "instructions": r"Enter your answer as a number.",
        "questions": [
            {
                "id": 19,
                "stem": r"If \(x : y = 4 : 9\) and \(x + y = 65\), enter the value of \(y\).",
            },
            {
                "id": 20,
                "stem": r"Two numbers are in the ratio 6:7. If their sum is 91, enter the larger number.",
            },
            {
                "id": 21,
                "stem": r"If \(a : b = 5 : 8\) and \(b : c = 4 : 9\), enter the ratio \(a : c\) in simplest form as \(a : c\).",
            },
            {
                "id": 22,
                "stem": r"If the ratio of red to blue balls is 7:3 and there are 80 balls total, enter the number of red balls.",
            },
            {
                "id": 23,
                "stem": r"If \(x : y = 2 : 5\) and \(x + y + 9 = 30\), enter the value of \(y\).",
            },
            {
                "id": 24,
                "stem": r"If two numbers are in the ratio 9:4 and their difference is 25, enter the larger number.",
            },
            {
                "id": 25,
                "stem": r"If the ratio of students to teachers is 12:1 and there are 260 students, enter the number of teachers.",
            },
            {
                "id": 26,
                "stem": r"If \(a : b = 3 : 7\) and \(a + 5 : b + 5 = 1 : 2\), enter the value of \(a\).",
            },
            {
                "id": 27,
                "stem": r"If \(x : y = 3 : 5\) and \(y : z = 4 : 7\), enter the ratio \(x : z\) in simplest form.",
            },
        ],
    },
]


# =========================================================================
# ANSWERS
# =========================================================================
# Keys: (topic_id, local_section_idx, question_id)
#   Percent Change  → topic_id = "ar-percent-change",  local_section_idx 0-3
#   Ratio & Proportion → topic_id = "ar-ratio-proportion", local_section_idx 0-3
# =========================================================================

ANSWERS = {
    # =================================================================
    # PERCENT CHANGE — Section 0: Quantitative Comparison (Q1-6)
    # =================================================================
    ("ar-percent-change", 0, 1): {
        "answer": "B",
        "explanation": (
            r"Let the original value be \(V\). After a 20% increase: \(V \times 1.20 = 1.20V\). "
            r"After a 20% decrease of that result: \(1.20V \times 0.80 = 0.96V\). "
            r"Since \(0.96V < V\), the final value is less than the original. Quantity B is greater."
        ),
        "common_mistake": (
            "Students often assume that a 20% increase followed by a 20% decrease returns to the original value. "
            "The decrease is applied to a larger base, so the net effect is a loss."
        ),
    },
    ("ar-percent-change", 0, 2): {
        "answer": "C",
        "explanation": (
            r"Percent increase \(= \frac{65 - 50}{50} \times 100 = \frac{15}{50} \times 100 = 30\%\). "
            r"Quantity A \(= 30\%\) and Quantity B \(= 30\%\). The two quantities are equal."
        ),
    },
    ("ar-percent-change", 0, 3): {
        "answer": "C",
        "explanation": (
            r"If the original number is decreased by 25%, the result is 75% of the original. "
            r"So \(0.75 \times \text{original} = 75\), giving \(\text{original} = \frac{75}{0.75} = 100\). "
            r"Quantity A \(= 100\) and Quantity B \(= 100\). The two quantities are equal."
        ),
    },
    ("ar-percent-change", 0, 4): {
        "answer": "A",
        "explanation": (
            r"Percent increase \(= \frac{100 - 80}{80} \times 100 = \frac{20}{80} \times 100 = 25\%\). "
            r"Quantity A \(= 25\%\) which is greater than Quantity B \(= 20\%\)."
        ),
        "common_mistake": (
            "Students sometimes compute the change as 20 and assume 20%, but the base is 80, not 100."
        ),
    },
    ("ar-percent-change", 0, 5): {
        "answer": "A",
        "explanation": (
            r"Let the original be \(V\). After two successive 10% increases: "
            r"\(V \times 1.10 \times 1.10 = 1.21V\). "
            r"Quantity A \(= 1.21V\) and Quantity B \(= 1.20V\). Since \(1.21V > 1.20V\), Quantity A is greater."
        ),
        "common_mistake": (
            "Students add 10% + 10% = 20% and pick C (equal). Successive percent increases compound, "
            "so the result is 21%, not 20%."
        ),
    },
    ("ar-percent-change", 0, 6): {
        "answer": "B",
        "explanation": (
            r"Let the original price be \(P\). After a 40% decrease: \(P \times 0.60 = 0.60P\). "
            r"After a 40% increase: \(0.60P \times 1.40 = 0.84P\). "
            r"Since \(0.84P < P\), the final price is less than the original. Quantity B is greater."
        ),
    },

    # =================================================================
    # PERCENT CHANGE — Section 1: Multiple Choice Single Answer (Q7-15)
    # =================================================================
    ("ar-percent-change", 1, 7): {
        "answer": "(C) 200",
        "explanation": (
            r"Let the original number be \(x\). A 25% increase gives \(1.25x = 250\). "
            r"So \(x = \frac{250}{1.25} = 200\)."
        ),
    },
    ("ar-percent-change", 1, 8): {
        "answer": "(B) 25%",
        "explanation": (
            r"Percent decrease \(= \frac{120 - 90}{120} \times 100 = \frac{30}{120} \times 100 = 25\%\)."
        ),
        "common_mistake": (
            "Some students compute 30/90 = 33.3% by using the new price as the base instead of the original price."
        ),
    },
    ("ar-percent-change", 1, 9): {
        "answer": "(C) 15%",
        "explanation": (
            r"Percent increase \(= \frac{46{,}000 - 40{,}000}{40{,}000} \times 100 = \frac{6{,}000}{40{,}000} \times 100 = 15\%\)."
        ),
    },
    ("ar-percent-change", 1, 10): {
        "answer": "(A) 17% increase",
        "explanation": (
            r"Let the original value be 100. After a 30% increase: \(100 \times 1.30 = 130\). "
            r"After a 10% decrease: \(130 \times 0.90 = 117\). "
            r"Net change \(= 117 - 100 = 17\), which is a 17% increase."
        ),
    },
    ("ar-percent-change", 1, 11): {
        "answer": "(C) 80",
        "explanation": (
            r"After a 20% discount, the shirt costs 80% of the original price. "
            r"So \(0.80 \times \text{original} = 64\), giving \(\text{original} = \frac{64}{0.80} = 80\)."
        ),
    },
    ("ar-percent-change", 1, 12): {
        "answer": "(A) 0%",
        "explanation": (
            r"Let the original be 100. After a 20% decrease: \(100 \times 0.80 = 80\). "
            r"After a 25% increase: \(80 \times 1.25 = 100\). "
            r"The value returns to 100, so the net change is 0%."
        ),
        "common_mistake": (
            "Students may think any increase-decrease pair results in a net loss. "
            "Here the 25% increase on the smaller base exactly offsets the 20% decrease."
        ),
    },
    ("ar-percent-change", 1, 13): {
        "answer": "(C) 11,025",
        "explanation": (
            r"Compounding 5% for 2 years: \(10{,}000 \times 1.05 \times 1.05 = 10{,}000 \times 1.1025 = 11{,}025\)."
        ),
        "common_mistake": (
            "Adding 5% + 5% = 10% gives 11,000 (choice B). The correct approach is to compound: "
            "\\(1.05^2 = 1.1025\\), not \\(1.10\\)."
        ),
    },
    ("ar-percent-change", 1, 14): {
        "answer": "(B) 75",
        "explanation": (
            r"Starting at \$100. After a 50% increase: \(100 \times 1.50 = 150\). "
            r"After a 50% decrease: \(150 \times 0.50 = 75\). The final price is \$75."
        ),
        "common_mistake": (
            "Students often pick (C) 100, assuming the increase and decrease cancel out. "
            "The 50% decrease applies to 150, not 100."
        ),
    },
    ("ar-percent-change", 1, 15): {
        "answer": "(C) 32%",
        "explanation": (
            r"Let the original be 100. After a 10% increase: \(100 \times 1.10 = 110\). "
            r"After a 20% increase: \(110 \times 1.20 = 132\). "
            r"Overall percent increase \(= 132 - 100 = 32\%\)."
        ),
    },

    # =================================================================
    # PERCENT CHANGE — Section 2: Multiple Choice Select One or More (Q16-18)
    # =================================================================
    ("ar-percent-change", 2, 16): {
        "answer": "B, D",
        "explanation": (
            r"Let the original value be \(V\). After a 50% increase: \(1.50V\). "
            r"After a 50% decrease: \(1.50V \times 0.50 = 0.75V\). "
            r"The final value is \(0.75V\), which is less than \(V\) (B is true) and the net change is a decrease (D is true). "
            r"Choices A, C, and E are false."
        ),
    },
    ("ar-percent-change", 2, 17): {
        "answer": "B, E",
        "explanation": (
            r"Let the original value be \(V\). After an \(x\%\) increase: \(V \times \left(1 + \frac{x}{100}\right)\). "
            r"After an \(x\%\) decrease: \(V \times \left(1 + \frac{x}{100}\right)\left(1 - \frac{x}{100}\right) = V \times \left(1 - \frac{x^2}{10{,}000}\right)\). "
            r"Since \(x > 0\), we have \(\frac{x^2}{10{,}000} > 0\), so the final value is less than \(V\) (B is true) "
            r"and the net change is negative (E is true)."
        ),
        "common_mistake": (
            "Many students pick A and D, thinking symmetric percent changes cancel out. "
            "They never do when x > 0."
        ),
    },
    ("ar-percent-change", 2, 18): {
        "answer": "A, C, D, E",
        "explanation": (
            r"The increase is \(50 - 40 = 10\). "
            r"Percent increase \(= \frac{10}{40} \times 100 = 25\%\). So (A) is true and (B) is false. "
            r"(C) The increase is 10 — true. "
            r"(D) 25% of 40 \(= 10\), which equals the increase — true. "
            r"(E) 20% of 50 \(= 10\), which also equals the increase — true."
        ),
    },

    # =================================================================
    # PERCENT CHANGE — Section 3: Numeric Entry (Q19-27)
    # =================================================================
    ("ar-percent-change", 3, 19): {
        "answer": "200",
        "explanation": (
            r"Let the original number be \(x\). A 15% increase gives \(1.15x = 230\). "
            r"So \(x = \frac{230}{1.15} = 200\)."
        ),
    },
    ("ar-percent-change", 3, 20): {
        "answer": "15%",
        "explanation": (
            r"Percent decrease \(= \frac{500 - 425}{500} \times 100 = \frac{75}{500} \times 100 = 15\%\)."
        ),
    },
    ("ar-percent-change", 3, 21): {
        "answer": "20.96%",
        "explanation": (
            r"Successive increases: \(1.12 \times 1.08 = 1.2096\). "
            r"Overall percent increase \(= 1.2096 - 1 = 0.2096 = 20.96\%\)."
        ),
        "common_mistake": (
            "Adding 12% + 8% = 20% ignores the compounding effect. "
            "The extra 0.96% comes from 12% of 8% (i.e., 0.12 × 0.08 = 0.0096)."
        ),
    },
    ("ar-percent-change", 3, 22): {
        "answer": "210",
        "explanation": (
            r"Original value = 200. After a 30% decrease: \(200 \times 0.70 = 140\). "
            r"After a 50% increase: \(140 \times 1.50 = 210\). The final value is 210."
        ),
    },
    ("ar-percent-change", 3, 23): {
        "answer": "200",
        "explanation": (
            r"After a 25% discount, the sale price is 75% of the original. "
            r"So \(0.75 \times \text{original} = 150\), giving \(\text{original} = \frac{150}{0.75} = 200\)."
        ),
    },
    ("ar-percent-change", 3, 24): {
        "answer": "540",
        "explanation": (
            r"Original = 500. After a 20% increase: \(500 \times 1.20 = 600\). "
            r"After a 10% decrease: \(600 \times 0.90 = 540\). The final number is 540."
        ),
    },
    ("ar-percent-change", 3, 25): {
        "answer": "25%",
        "explanation": (
            r"Percent increase \(= \frac{75 - 60}{60} \times 100 = \frac{15}{60} \times 100 = 25\%\)."
        ),
    },
    ("ar-percent-change", 3, 26): {
        "answer": "28%",
        "explanation": (
            r"Let the original price be 100. After a 20% decrease: \(100 \times 0.80 = 80\). "
            r"After another 10% decrease: \(80 \times 0.90 = 72\). "
            r"Total percent decrease \(= \frac{100 - 72}{100} \times 100 = 28\%\)."
        ),
        "common_mistake": (
            "Adding 20% + 10% = 30% is incorrect. Successive decreases compound: "
            "the second decrease applies to an already-reduced value."
        ),
    },
    ("ar-percent-change", 3, 27): {
        "answer": "2",
        "explanation": (
            r"Let the original value be \(V\). After a \(p\%\) increase and then a \(p\%\) decrease: "
            r"\(V \times \left(1 + \frac{p}{100}\right)\left(1 - \frac{p}{100}\right) = V\left(1 - \frac{p^2}{10{,}000}\right)\). "
            r"Since \(p > 0\), the factor \(\left(1 - \frac{p^2}{10{,}000}\right) < 1\), so the final value is always less than the original. "
            r"The answer is 2."
        ),
        "common_mistake": (
            "Students who pick 1 believe the changes cancel. Students who pick 3 think it depends on p. "
            "In fact, for any positive p, the final value is always less than the original."
        ),
    },

    # =================================================================
    # RATIO & PROPORTION — Section 0 (global 4): Quantitative Comparison (Q1-6)
    # =================================================================
    ("ar-ratio-proportion", 0, 1): {
        "answer": "D",
        "explanation": (
            r"We know \(\frac{x}{y} = \frac{3}{5}\), so \(x = \frac{3}{5}y\). "
            r"If \(x\) and \(y\) are both positive, then \(x < y\), so Quantity B is greater. "
            r"But if both are negative (e.g., \(x = -3, y = -5\)), then \(x > y\). "
            r"Since we don't know the signs, the relationship cannot be determined."
        ),
        "common_mistake": (
            "Students assume variables are positive and pick B. "
            "The ratio 3:5 holds for negative values too (e.g., -3 and -5), reversing the comparison."
        ),
    },
    ("ar-ratio-proportion", 0, 2): {
        "answer": "C",
        "explanation": (
            r"\(a : b = 2 : 3\), so let \(a = 2k\) and \(b = 3k\). "
            r"Then \(a + b = 5k = 25\), giving \(k = 5\). "
            r"So \(a = 10\). Quantity A \(= 10 =\) Quantity B. They are equal."
        ),
    },
    ("ar-ratio-proportion", 0, 3): {
        "answer": "C",
        "explanation": (
            r"Boys : Girls \(= 4 : 7\), so total parts \(= 4 + 7 = 11\). "
            r"The fraction that are boys \(= \frac{4}{11}\). "
            r"Quantity A \(= \frac{4}{11} =\) Quantity B. They are equal."
        ),
    },
    ("ar-ratio-proportion", 0, 4): {
        "answer": "B",
        "explanation": (
            r"\(x : y = 5 : 8\), so \(\frac{x}{y} = \frac{5}{8} = 0.625\). "
            r"Quantity B \(= \frac{8}{5} = 1.6\). "
            r"Since \(0.625 < 1.6\), Quantity B is greater."
        ),
    },
    ("ar-ratio-proportion", 0, 5): {
        "answer": "C",
        "explanation": (
            r"The numbers are in the ratio \(3 : 4\). Let them be \(3k\) and \(4k\). "
            r"The larger number is \(4k = 28\), so \(k = 7\). "
            r"The smaller number is \(3k = 21\). Quantity A \(= 21 =\) Quantity B. They are equal."
        ),
    },
    ("ar-ratio-proportion", 0, 6): {
        "answer": "C",
        "explanation": (
            r"\(a : b = 4 : 5\) and \(b : c = 2 : 3\). To combine, make \(b\) the same: "
            r"multiply the first ratio by 2 and the second by 5: "
            r"\(a : b = 8 : 10\) and \(b : c = 10 : 15\). "
            r"So \(a : b : c = 8 : 10 : 15\), giving \(a : c = 8 : 15\). "
            r"Quantity A \(= 8 : 15 =\) Quantity B. They are equal."
        ),
    },

    # =================================================================
    # RATIO & PROPORTION — Section 1 (global 5): MC Single Answer (Q7-15)
    # =================================================================
    ("ar-ratio-proportion", 1, 7): {
        "answer": "(C) 35",
        "explanation": (
            r"\(x : y = 7 : 9\), so let \(x = 7k, y = 9k\). "
            r"\(x + y = 16k = 80\), so \(k = 5\). "
            r"Therefore \(x = 7 \times 5 = 35\)."
        ),
    },
    ("ar-ratio-proportion", 1, 8): {
        "answer": "(B) 15",
        "explanation": (
            r"Red : Blue \(= 3 : 5\), total parts \(= 8\). "
            r"Red marbles \(= \frac{3}{8} \times 40 = 15\)."
        ),
    },
    ("ar-ratio-proportion", 1, 9): {
        "answer": "(C) 8:15",
        "explanation": (
            r"\(a : b = 2 : 3\) and \(b : c = 4 : 5\). "
            r"Make \(b\) common: multiply the first by 4 and the second by 3: "
            r"\(a : b = 8 : 12\) and \(b : c = 12 : 15\). "
            r"So \(a : c = 8 : 15\)."
        ),
    },
    ("ar-ratio-proportion", 1, 10): {
        "answer": "(E) 63",
        "explanation": (
            r"Let the numbers be \(5k\) and \(7k\). "
            r"Difference: \(7k - 5k = 2k = 18\), so \(k = 9\). "
            r"The larger number \(= 7 \times 9 = 63\)."
        ),
    },
    ("ar-ratio-proportion", 1, 11): {
        "answer": "(C) 20",
        "explanation": (
            r"Men : Women \(= 3 : 2\), total parts \(= 5\). "
            r"Women \(= \frac{2}{5} \times 50 = 20\)."
        ),
    },
    ("ar-ratio-proportion", 1, 12): {
        "answer": "(B) 9",
        "explanation": (
            r"Let \(x = 3k\) and \(y = 4k\). After adding 6 to each: "
            r"\(\frac{3k + 6}{4k + 6} = \frac{5}{6}\). "
            r"Cross-multiplying: \(6(3k + 6) = 5(4k + 6)\), so \(18k + 36 = 20k + 30\). "
            r"Solving: \(6 = 2k\), so \(k = 3\). Therefore \(x = 3 \times 3 = 9\)."
        ),
    },
    ("ar-ratio-proportion", 1, 13): {
        "answer": "(B) 6:7",
        "explanation": (
            r"Let \(a = 4k\) and \(b = 7k\). After a 50% increase in \(a\): "
            r"\(a_{\text{new}} = 4k \times 1.5 = 6k\). "
            r"New ratio \(= 6k : 7k = 6 : 7\)."
        ),
    },
    ("ar-ratio-proportion", 1, 14): {
        "answer": "(C) 6",
        "explanation": (
            r"Let flour \(= 5k\) and sugar \(= 2k\). After adding 3 cups of sugar: "
            r"\(\frac{5k}{2k + 3} = \frac{5}{3}\). "
            r"Cross-multiplying: \(15k = 5(2k + 3) = 10k + 15\). "
            r"So \(5k = 15\), giving \(k = 3\). Original sugar \(= 2 \times 3 = 6\) cups."
        ),
    },
    ("ar-ratio-proportion", 1, 15): {
        "answer": "(C) 80",
        "explanation": (
            r"Let the numbers be \(8k\) and \(11k\). "
            r"\(8k + 11k = 19k = 190\), so \(k = 10\). "
            r"The smaller number \(= 8 \times 10 = 80\)."
        ),
    },

    # =================================================================
    # RATIO & PROPORTION — Section 2 (global 6): MC Select One or More (Q16-18)
    # =================================================================
    ("ar-ratio-proportion", 2, 16): {
        "answer": "A, B, D, E",
        "explanation": (
            r"\(x : y = 3 : 5\), so \(\frac{x}{y} = \frac{3}{5}\). "
            r"Check each: (A) \(6/10 = 3/5\) — yes. (B) \(9/15 = 3/5\) — yes. "
            r"(C) \(12/18 = 2/3 \neq 3/5\) — no. (D) \(15/25 = 3/5\) — yes. (E) \(18/30 = 3/5\) — yes."
        ),
    },
    ("ar-ratio-proportion", 2, 17): {
        "answer": "A, B, C, D, E",
        "explanation": (
            r"Given \(a : b = 2 : 3\), let \(a = 2k, b = 3k\) for some positive \(k\) "
            r"(the problem states a ratio, and in GRE context the values are positive). "
            r"(A) \(\frac{a}{a+b} = \frac{2k}{5k} = \frac{2}{5}\) — true. "
            r"(B) \(\frac{b}{a+b} = \frac{3k}{5k} = \frac{3}{5}\) — true. "
            r"(C) \(a = \frac{2}{3}b\): \(2k = \frac{2}{3}(3k) = 2k\) — true. "
            r"(D) \(b = \frac{3}{2}a\): \(3k = \frac{3}{2}(2k) = 3k\) — true. "
            r"(E) \(a < b\): \(2k < 3k\) for positive \(k\) — true."
        ),
        "common_mistake": (
            "If negative values of k are considered, (E) would fail. However, in standard GRE ratio "
            "problems, the multiplier k is assumed positive."
        ),
    },
    ("ar-ratio-proportion", 2, 18): {
        "answer": "B, C",
        "explanation": (
            r"Boys : Girls \(= 4 : 5\). Let boys \(= 4k\), girls \(= 5k\). After 3 boys leave, boys \(= 4k - 3\). "
            r"(A) Ratio becomes 1:1: need \(4k - 3 = 5k\), giving \(k = -3\), which is impossible. False. "
            r"(B) Ratio becomes 3:5: \(\frac{4k-3}{5k} = \frac{3}{5}\), cross-multiply: \(20k - 15 = 15k\), so \(k = 3\). "
            r"Boys \(= 12\), after 3 leave \(= 9\); girls \(= 15\). Ratio \(= 9:15 = 3:5\). True. "
            r"(C) The total decreases: 3 boys leave, so the total drops by 3. True. "
            r"(D) The number of girls increases: no girls are added or removed. False. "
            r"(E) The ratio remains 4:5: \(\frac{4k-3}{5k} = \frac{4}{5}\) gives \(20k - 15 = 20k\), which is impossible. False."
        ),
    },

    # =================================================================
    # RATIO & PROPORTION — Section 3 (global 7): Numeric Entry (Q19-27)
    # =================================================================
    ("ar-ratio-proportion", 3, 19): {
        "answer": "45",
        "explanation": (
            r"\(x : y = 4 : 9\), so let \(x = 4k, y = 9k\). "
            r"\(x + y = 13k = 65\), giving \(k = 5\). "
            r"Therefore \(y = 9 \times 5 = 45\)."
        ),
    },
    ("ar-ratio-proportion", 3, 20): {
        "answer": "49",
        "explanation": (
            r"Let the numbers be \(6k\) and \(7k\). "
            r"\(6k + 7k = 13k = 91\), so \(k = 7\). "
            r"The larger number \(= 7 \times 7 = 49\)."
        ),
    },
    ("ar-ratio-proportion", 3, 21): {
        "answer": "5:18",
        "explanation": (
            r"\(a : b = 5 : 8\) and \(b : c = 4 : 9\). "
            r"Make \(b\) common: multiply the first by 4 and the second by 8 (LCM of 8 and 4 is 8): "
            r"First: \(a : b = 5 \times 1 : 8 \times 1 = 5 : 8\). "
            r"We need \(b\) the same in both ratios. \(b = 8\) in the first, \(b = 4\) in the second. "
            r"Multiply the second ratio by 2: \(b : c = 8 : 18\). "
            r"Now \(a : b : c = 5 : 8 : 18\), so \(a : c = 5 : 18\)."
        ),
    },
    ("ar-ratio-proportion", 3, 22): {
        "answer": "56",
        "explanation": (
            r"Red : Blue \(= 7 : 3\), total parts \(= 10\). "
            r"Red balls \(= \frac{7}{10} \times 80 = 56\)."
        ),
    },
    ("ar-ratio-proportion", 3, 23): {
        "answer": "15",
        "explanation": (
            r"\(x : y = 2 : 5\), so let \(x = 2k, y = 5k\). "
            r"\(x + y + 9 = 30\), so \(7k + 9 = 30\), giving \(7k = 21\), so \(k = 3\). "
            r"Therefore \(y = 5 \times 3 = 15\)."
        ),
    },
    ("ar-ratio-proportion", 3, 24): {
        "answer": "45",
        "explanation": (
            r"Let the numbers be \(9k\) and \(4k\). "
            r"Difference: \(9k - 4k = 5k = 25\), so \(k = 5\). "
            r"The larger number \(= 9 \times 5 = 45\)."
        ),
    },
    ("ar-ratio-proportion", 3, 25): {
        "answer": "65/3",
        "explanation": (
            r"Students : Teachers \(= 12 : 1\). Let teachers \(= k\), then students \(= 12k\). "
            r"\(12k = 260\), so \(k = \frac{260}{12} = \frac{65}{3}\). "
            r"As a decimal this is approximately \(21.67\). "
            r"On the GRE numeric entry, enter \(\frac{65}{3}\) or the decimal equivalent."
        ),
        "common_mistake": (
            "Students may round to 22, but the GRE expects the exact value. "
            "If entering as a fraction, use 65/3."
        ),
    },
    ("ar-ratio-proportion", 3, 26): {
        "answer": "15",
        "explanation": (
            r"Let \(a = 3k, b = 7k\). The condition is \(\frac{a+5}{b+5} = \frac{1}{2}\). "
            r"So \(\frac{3k+5}{7k+5} = \frac{1}{2}\). Cross-multiplying: \(2(3k+5) = 7k+5\). "
            r"\(6k + 10 = 7k + 5\), giving \(k = 5\). "
            r"Therefore \(a = 3 \times 5 = 15\)."
        ),
    },
    ("ar-ratio-proportion", 3, 27): {
        "answer": "12:35",
        "explanation": (
            r"\(x : y = 3 : 5\) and \(y : z = 4 : 7\). "
            r"Make \(y\) common: LCM of 5 and 4 is 20. "
            r"Multiply the first ratio by 4: \(x : y = 12 : 20\). "
            r"Multiply the second ratio by 5: \(y : z = 20 : 35\). "
            r"So \(x : y : z = 12 : 20 : 35\), giving \(x : z = 12 : 35\)."
        ),
    },
}
