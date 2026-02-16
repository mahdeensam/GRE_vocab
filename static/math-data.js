// GRE Quant Complete — Study Data
// Extracted from GRE Quant Complete.pdf (54 pages)

const MATH_DATA = [
  // ============================================================
  // CHAPTER 1: ARITHMETIC
  // ============================================================
  {
    id: "arithmetic",
    title: "Arithmetic",
    emoji: "\ud83d\udcd8",
    color: "#6c63ff",
    sections: [
      // --- 1.1 Integers ---
      {
        id: "integers",
        title: "Integers (Positive, Negative)",
        concepts: [
          "Integers are whole numbers: ... \u22123, \u22122, \u22121, 0, 1, 2, 3 ...",
          "Zero is an integer but is neither positive nor negative.",
          "Adding two positives \u2192 positive. Adding two negatives \u2192 negative.",
          "Negative \u00d7 Negative = Positive. Positive \u00d7 Negative = Negative.",
          "Any integer \u00d7 0 = 0.",
          "Odd + Odd = Even; Even + Even = Even; Odd + Even = Odd.",
          "Odd \u00d7 Odd = Odd; Even \u00d7 anything = Even.",
          "\u201cNon-negative\u201d includes zero; \u201cpositive\u201d does not."
        ],
        formulas: [],
        tips: [
          "Zero is even, and it\u2019s neither positive nor negative \u2014 GRE exploits this constantly.",
          "(\u22121)\u207f: even exponent \u2192 positive, odd exponent \u2192 negative.",
          "x\u00b2 \u2265 0 is always true, but x\u00b2 > 0 fails when x = 0."
        ],
        questions: [
          {
            q: "If x is a negative integer and y is a positive integer, which must be negative? A) x + y  B) x \u00d7 y  C) x\u00b2  D) y \u2212 x",
            a: "B) x \u00d7 y \u2014 negative times positive is always negative. The others can be positive."
          },
          {
            q: "What is the sum of all integers from \u22124 to 4, inclusive?",
            a: "0. Each negative pairs with its positive counterpart: (\u22124+4) + (\u22123+3) + (\u22122+2) + (\u22121+1) + 0 = 0."
          },
          {
            q: "Quantitative Comparison: Column A: (\u22121)\u2075\u2070  |  Column B: (\u22121)\u2075\u00b9",
            a: "Column A is greater. (\u22121)\u2075\u2070 = 1 (even exp), (\u22121)\u2075\u00b9 = \u22121 (odd exp). 1 > \u22121."
          },
          {
            q: "If n\u00b2 has 15 positive factors, how many positive factors does n have?",
            a: "Either 6 or 8 depending on n\u2019s prime structure. If n = p\u00b9q\u00b2 \u2192 6 factors. If n = p\u2077 \u2192 8 factors."
          }
        ]
      },
      // --- 1.2 Factors & Multiples ---
      {
        id: "factors-multiples",
        title: "Factors & Multiples",
        concepts: [
          "Factor: divides evenly into another number. Factors of 12 \u2192 1, 2, 3, 4, 6, 12.",
          "Multiple: result of multiplying by any integer. Multiples of 5 \u2192 5, 10, 15, 20 ...",
          "If a is a factor of b, then b is a multiple of a.",
          "Finding factors: check 1 to \u221an, pair each with its complement.",
          "1 is a factor of every integer. Every number is a factor of itself.",
          "0 is a multiple of every integer, but 0 is NOT a factor of any number.",
          "If a | b and b | c, then a | c (transitivity).",
          "If a | b and a | c, then a | (b + c) and a | (b \u2212 c)."
        ],
        formulas: [
          "Number of factors: if n = p\u1d43 \u00d7 q\u1d47 \u00d7 r\u1d9c, then total factors = (a+1)(b+1)(c+1)",
          "Example: 60 = 2\u00b2 \u00d7 3\u00b9 \u00d7 5\u00b9 \u2192 (2+1)(1+1)(1+1) = 12 factors"
        ],
        tips: [
          "Consecutive integers n and n+1 always have GCF = 1.",
          "A number has exactly 3 factors only if it\u2019s the square of a prime (p\u00b2).",
          "The product of n consecutive integers is always divisible by n!."
        ],
        questions: [
          {
            q: "How many positive factors does 240 have?",
            a: "240 = 2\u2074 \u00d7 3 \u00d7 5 \u2192 (4+1)(1+1)(1+1) = 20 factors."
          },
          {
            q: "If the GCF of two numbers is 6 and their LCM is 180, and one number is 36, what is the other?",
            a: "GCF \u00d7 LCM = a \u00d7 b \u2192 6 \u00d7 180 = 36 \u00d7 b \u2192 b = 30."
          },
          {
            q: "QC: n has exactly 3 positive factors. Column A: n  |  Column B: 10",
            a: "Cannot be determined (D). n must be p\u00b2: could be 4, 9 (< 10) or 25, 49 (> 10)."
          }
        ]
      },
      // --- 1.3 Prime Numbers ---
      {
        id: "primes",
        title: "Prime Numbers",
        concepts: [
          "A prime has exactly two factors: 1 and itself.",
          "2 is the only even prime and the smallest prime.",
          "1 is NOT prime. 0 and negatives are NOT prime.",
          "(2, 3) is the only pair of consecutive integers that are both prime.",
          "To test if n is prime: check divisibility by primes up to \u221an.",
          "If p is prime and p | (a\u00d7b), then p | a OR p | b.",
          "Sum of two primes is even EXCEPT when one is 2.",
          "Product of two distinct primes has exactly 4 factors."
        ],
        formulas: [
          "Prime factorization: every integer > 1 = unique product of primes.",
          "Example: 360 = 2\u00b3 \u00d7 3\u00b2 \u00d7 5"
        ],
        tips: [
          "91 = 7 \u00d7 13 (NOT prime!) \u2014 most common GRE trap.",
          "51 = 3 \u00d7 17, 57 = 3 \u00d7 19, 87 = 3 \u00d7 29 \u2014 all NOT prime.",
          "First 10 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29."
        ],
        questions: [
          {
            q: "How many prime numbers are between 40 and 60?",
            a: "5 primes: 41, 43, 47, 53, 59."
          },
          {
            q: "If p and q are distinct primes, how many positive factors does p\u00b2 \u00d7 q\u00b3 have?",
            a: "(2+1)(3+1) = 12 factors."
          },
          {
            q: "QC: p is prime > 2. Col A: remainder when p \u00f7 2. Col B: remainder when p\u00b2 \u00f7 2.",
            a: "Equal (C). All primes > 2 are odd. Odd \u00f7 2 = rem 1. Odd\u00b2 is still odd \u00f7 2 = rem 1."
          }
        ]
      },
      // --- 1.4 Divisibility Rules ---
      {
        id: "divisibility",
        title: "Divisibility Rules",
        concepts: [
          "By 2: last digit even. By 3: digit sum \u00f7 3. By 4: last two digits \u00f7 4.",
          "By 5: ends in 0 or 5. By 6: divisible by both 2 and 3.",
          "By 8: last three digits \u00f7 8. By 9: digit sum \u00f7 9. By 10: ends in 0.",
          "By 11: alternating sum of digits \u00f7 11.",
          "By 12: divisible by both 3 and 4. By 15: divisible by both 3 and 5.",
          "Composite divisor rule: break into co-prime components (e.g., 12 = 3 \u00d7 4, not 2 \u00d7 6).",
          "n consecutive integers always contain exactly one multiple of n."
        ],
        formulas: [
          "Remainder of (a + b) \u00f7 n = [(rem of a) + (rem of b)] mod n",
          "Remainder of (a \u00d7 b) \u00f7 n = [(rem of a) \u00d7 (rem of b)] mod n"
        ],
        tips: [
          "For digit-sum remainder: dividing by 9, the digit sum IS the remainder.",
          "Divisible by 2 AND by 6 does NOT guarantee divisible by 12 (e.g., 6).",
          "The product of n consecutive integers is always divisible by n!."
        ],
        questions: [
          {
            q: "Is 4,572 divisible by 6?",
            a: "Yes. Even (last digit 2) \u2713, digit sum 4+5+7+2 = 18 (\u00f73) \u2713."
          },
          {
            q: "What is the remainder when 2\u2074\u2070 is divided by 3?",
            a: "1. Pattern: 2\u00b9\u21922, 2\u00b2\u21921, 2\u00b3\u21922, 2\u2074\u21921 (cycle of 2). Even powers give remainder 1."
          },
          {
            q: "If 3n + 2 is divisible by 7, what is the remainder when n \u00f7 7?",
            a: "4. 3n \u2261 5 (mod 7). Testing: 3\u00d74 = 12 \u2261 5 (mod 7) \u2713."
          }
        ]
      },
      // --- 1.5 LCM & GCF ---
      {
        id: "lcm-gcf",
        title: "LCM & GCF",
        concepts: [
          "GCF: largest number dividing both. Take LOWEST power of SHARED primes.",
          "LCM: smallest common multiple. Take HIGHEST power of ALL primes.",
          "GCF(a,b) \u2264 min(a,b). LCM(a,b) \u2265 max(a,b).",
          "If GCF(a,b) = 1 (co-prime), then LCM = a \u00d7 b.",
          "GCF of consecutive integers is always 1.",
          "\u201cSync up / coincide\u201d \u2192 use LCM. \u201cEqual groups / largest tile\u201d \u2192 use GCF."
        ],
        formulas: [
          "Golden Identity: GCF(a,b) \u00d7 LCM(a,b) = a \u00d7 b (works for two numbers only!)",
          "LCM shortcut: LCM(a,b) = (a \u00d7 b) \u00f7 GCF(a,b)"
        ],
        tips: [
          "The golden identity only works for exactly two numbers.",
          "For three+ numbers: find LCM of first two, then LCM with the third.",
          "GCF(a,b) always divides LCM(a,b)."
        ],
        questions: [
          {
            q: "Two runners lap every 12 and 18 minutes. When do they first meet at start?",
            a: "LCM(12, 18) = 36 minutes."
          },
          {
            q: "72 apples and 90 oranges. Max identical gift bags using all fruit?",
            a: "GCF(72, 90) = 18 bags. Each: 4 apples + 5 oranges."
          },
          {
            q: "GCF of two numbers is 8, LCM is 96. One number is 32. Find the other.",
            a: "8 \u00d7 96 = 32 \u00d7 b \u2192 b = 24. Verify: GCF(32,24) = 8 \u2713, LCM(32,24) = 96 \u2713."
          }
        ]
      },
      // --- 1.6 Remainders ---
      {
        id: "remainders",
        title: "Remainders",
        concepts: [
          "Division formula: a = b\u00d7q + r, where 0 \u2264 r < b.",
          "Remainder arithmetic: work with remainders only for +, \u2212, \u00d7.",
          "For powers: find the cycle of remainders, then use exponent mod cycle length.",
          "Remainder when \u00f7 10 = last digit. Remainder when \u00f7 100 = last two digits.",
          "Negative remainders: add divisor to make positive. e.g., \u221223 \u00f7 5: rem = 2 (not \u22123).",
          "If a and b give same remainder when \u00f7 n, then (a \u2212 b) is divisible by n."
        ],
        formulas: [
          "rem(a+b) = rem(rem(a) + rem(b))",
          "rem(a\u00d7b) = rem(rem(a) \u00d7 rem(b))",
          "rem(a\u2212b) = rem(rem(a) \u2212 rem(b)), add n if negative"
        ],
        tips: [
          "Same remainder for multiple divisors? Subtract remainder, find LCM.",
          "n \u00f7 6 gives rem 4 \u2192 n = 6q+4 \u2192 n is always even.",
          "1! + 2! + ... + 100! mod 12: only 1!+2!+3! matter (= 9), since n! divisible by 12 for n \u2265 4."
        ],
        questions: [
          {
            q: "What is the remainder when 2\u2075\u2070 is divided by 7?",
            a: "4. Cycle: 2\u00b9\u21922, 2\u00b2\u21924, 2\u00b3\u21921 (length 3). 50 \u00f7 3 = 16 r2 \u2192 same as 2\u00b2 \u2192 rem 4."
          },
          {
            q: "n \u00f7 5 gives rem 3, n \u00f7 7 gives rem 4. Remainder when n \u00f7 35?",
            a: "18. List values with rem 3 when \u00f75: 3, 8, 13, 18... Check 18 \u00f7 7 = 2 rem 4 \u2713."
          },
          {
            q: "n gives remainder 1 when divided by 2, 3, 4, 5, and 6. Smallest n > 1?",
            a: "61. n \u2212 1 = LCM(2,3,4,5,6) = 60. So n = 61."
          }
        ]
      },
      // --- 1.7 Units Digit Patterns ---
      {
        id: "units-digits",
        title: "Units Digit Patterns",
        concepts: [
          "Units digit = last digit = remainder when \u00f7 10.",
          "Never changes (cycle 1): 0, 1, 5, 6.",
          "Alternating (cycle 2): 4 \u2192 4,6,4,6... and 9 \u2192 9,1,9,1...",
          "Four-step cycle: 2 \u2192 2,4,8,6 | 3 \u2192 3,9,7,1 | 7 \u2192 7,9,3,1 | 8 \u2192 8,4,2,6",
          "Method: find units digit of base, look up cycle, exponent mod cycle length.",
          "If remainder = 0, use the LAST position in the cycle.",
          "n\u00b2 can only end in: 0, 1, 4, 5, 6, or 9 (never 2, 3, 7, or 8)."
        ],
        formulas: [],
        tips: [
          "Addition/multiplication: only the units digits of inputs matter.",
          "Product of 5 consecutive integers always ends in 0.",
          "If n ends in 0, 1, 5, or 6 \u2192 n\u00b2 ends in the same digit."
        ],
        questions: [
          {
            q: "What is the units digit of 7\u2077\u2077\u2077\u2077?",
            a: "7. Cycle for 7: 7,9,3,1 (length 4). 7777 \u00f7 4 = 1944 r1 \u2192 1st position = 7."
          },
          {
            q: "Units digit of 17\u00b2\u2079 + 13\u00b3\u00b9?",
            a: "4. 17\u00b2\u2079: base 7, 29\u00f74=7r1 \u2192 7. 13\u00b3\u00b9: base 3, 31\u00f74=7r3 \u2192 7. 7+7=14 \u2192 units 4."
          },
          {
            q: "QC: Col A: units digit of 4\u2079\u2079 | Col B: units digit of 9\u2079\u2079",
            a: "B is greater. 4\u2079\u2079: odd power \u2192 4. 9\u2079\u2079: odd power \u2192 9. 4 < 9."
          }
        ]
      },
      // --- 1.8 Fractions & Decimals ---
      {
        id: "fractions-decimals",
        title: "Fractions & Decimals",
        concepts: [
          "Proper: num < denom (< 1). Improper: num \u2265 denom (\u2265 1).",
          "Simplify: divide both by GCF. 18/24 \u2192 GCF=6 \u2192 3/4.",
          "Fraction \u2192 decimal: divide. 3/8 = 0.375.",
          "Decimal \u2192 fraction: put over power of 10, simplify.",
          "Repeating: 0.aaa... = a/9. 0.ababab... = ab/99.",
          "A fraction terminates iff denominator (in lowest terms) has only factors 2 and 5.",
          "Cross-multiply to compare: a/b vs c/d \u2192 compare a\u00d7d vs b\u00d7c."
        ],
        formulas: [
          "Common equivalents: 1/2=0.5, 1/3=0.33\u0305, 1/4=0.25, 1/5=0.2, 1/6=0.16\u0305, 1/8=0.125",
          "Mixed \u2192 improper: 2\u00be = (2\u00d74+3)/4 = 11/4"
        ],
        tips: [
          "5/12 repeats (12 has factor 3). 7/40 terminates (40 = 2\u00b3\u00d75).",
          "Between any two fractions, there are infinitely many fractions.",
          "Multiplying by a proper fraction makes the number smaller."
        ],
        questions: [
          {
            q: "Which is greater: 7/11 or 5/8?",
            a: "Cross-multiply: 7\u00d78 = 56 vs 11\u00d75 = 55. 56 > 55 \u2192 7/11 > 5/8."
          },
          {
            q: "What fraction equals 0.363636...?",
            a: "36/99 = 4/11."
          },
          {
            q: "Does 7/250 terminate?",
            a: "Yes. 250 = 2 \u00d7 5\u00b3 \u2192 only 2s and 5s \u2192 terminates."
          }
        ]
      },
      // --- 1.9 Ratios & Proportions ---
      {
        id: "ratios",
        title: "Ratios & Proportions",
        concepts: [
          "Ratio a:b means for every a of one, there are b of the other.",
          "Part-to-whole: if a:b, then a\u2019s share = a/(a+b).",
          "Direct variation: y = kx. When one doubles, the other doubles.",
          "Inverse variation: xy = k. When one doubles, the other halves.",
          "To combine ratios: find common term. a:b = 2:3 and b:c = 3:5 \u2192 a:b:c = 2:3:5."
        ],
        formulas: [
          "Proportion: a/b = c/d \u2192 ad = bc (cross-multiply)",
          "Actual values: if ratio is a:b and total is T, then parts are aT/(a+b) and bT/(a+b)"
        ],
        tips: [
          "Ratios don\u2019t give actual values \u2014 only relative amounts.",
          "When combining ratios, make the shared term equal first."
        ],
        questions: [
          {
            q: "The ratio of boys to girls is 3:5. If there are 40 students total, how many boys?",
            a: "Boys = 3/(3+5) \u00d7 40 = 3/8 \u00d7 40 = 15."
          },
          {
            q: "If y varies inversely with x, and y=6 when x=4, find y when x=8.",
            a: "xy = k \u2192 6\u00d74 = 24. When x=8: y = 24/8 = 3."
          }
        ]
      },
      // --- 1.10 Percentages ---
      {
        id: "percentages",
        title: "Percentages",
        concepts: [
          "Percent = per hundred. 25% = 25/100 = 0.25.",
          "Percent increase = (new \u2212 old)/old \u00d7 100.",
          "Percent decrease = (old \u2212 new)/old \u00d7 100.",
          "Successive changes: multiply factors. 20% increase then 10% decrease = 1.2 \u00d7 0.9 = 1.08 (8% net increase).",
          "Profit = Selling Price \u2212 Cost Price. Profit% = (Profit/CP) \u00d7 100."
        ],
        formulas: [
          "x% of y = y% of x (always equal!)",
          "Successive: (1 + r\u2081)(1 + r\u2082) \u2212 1 = net change",
          "If increased by x% then decreased by x%: net loss of x\u00b2/100 %"
        ],
        tips: [
          "A 50% increase followed by a 50% decrease is NOT zero \u2014 it\u2019s a 25% net decrease.",
          "Percent change is always relative to the ORIGINAL value.",
          "20% of 50 = 50% of 20 = 10 (use this trick to simplify)."
        ],
        questions: [
          {
            q: "A price increases 20% then decreases 20%. Net change?",
            a: "1.20 \u00d7 0.80 = 0.96 \u2192 4% net decrease."
          },
          {
            q: "If 60% of x equals 40% of 90, find x.",
            a: "0.6x = 0.4 \u00d7 90 = 36 \u2192 x = 60."
          },
          {
            q: "A shirt\u2019s price drops from $80 to $60. What percent decrease?",
            a: "(80\u221260)/80 \u00d7 100 = 25%."
          }
        ]
      },
      // --- 1.11 Word Problems ---
      {
        id: "word-problems",
        title: "Word Problems (Rate, Work, Mixtures)",
        concepts: [
          "Distance = Speed \u00d7 Time. Work = Rate \u00d7 Time.",
          "Combined work: 1/A + 1/B = 1/T (A and B are individual times).",
          "Average speed \u2260 average of speeds. Use: total distance / total time.",
          "Mixtures: total value = sum of individual values.",
          "Average = Sum / Count. Missing value = Average \u00d7 Count \u2212 known sum."
        ],
        formulas: [
          "Combined work rate: 1/T = 1/A + 1/B \u2192 T = AB/(A+B)",
          "Average speed for equal distances: 2v\u2081v\u2082/(v\u2081+v\u2082)",
          "Weighted average: (w\u2081x\u2081 + w\u2082x\u2082)/(w\u2081 + w\u2082)"
        ],
        tips: [
          "If A does a job in 6 hours, A\u2019s rate is 1/6 per hour.",
          "Average speed with equal distances: use harmonic mean, not arithmetic mean.",
          "In mixture problems, set up: (amount\u2081)(conc\u2081) + (amount\u2082)(conc\u2082) = total."
        ],
        questions: [
          {
            q: "A can finish in 6 hours, B in 4 hours. How long together?",
            a: "1/6 + 1/4 = 2/12 + 3/12 = 5/12. Time = 12/5 = 2.4 hours."
          },
          {
            q: "Drive 60 mph for 120 miles, then 40 mph for 120 miles. Average speed?",
            a: "Total dist = 240. Total time = 2 + 3 = 5 hrs. Average = 240/5 = 48 mph."
          },
          {
            q: "Mix 10L of 30% solution with 20L of 60% solution. Final concentration?",
            a: "(10\u00d70.3 + 20\u00d70.6)/(10+20) = (3+12)/30 = 15/30 = 50%."
          }
        ]
      }
    ]
  },

  // ============================================================
  // CHAPTER 2: ALGEBRA
  // ============================================================
  {
    id: "algebra",
    title: "Algebra",
    emoji: "\ud83d\udcd7",
    color: "#0d9488",
    sections: [
      {
        id: "linear-equations",
        title: "Linear Equations (1 & 2 Variables)",
        concepts: [
          "Standard form: ax + b = 0 \u2192 x = \u2212b/a.",
          "Two variables: solve by substitution or elimination.",
          "System with unique solution: lines intersect at one point.",
          "No solution: parallel lines (same slope, different intercept).",
          "Infinite solutions: same line (proportional coefficients)."
        ],
        formulas: [
          "Substitution: solve one equation for a variable, plug into the other.",
          "Elimination: multiply equations so one variable cancels when added."
        ],
        tips: [
          "If a/d = b/e = c/f, the system has infinite solutions.",
          "If a/d = b/e \u2260 c/f, no solution.",
          "GRE often asks \u201cwhat is 3x + 2y?\u201d without needing individual x, y values."
        ],
        questions: [
          {
            q: "If 3x + 2y = 12 and x \u2212 y = 1, find x and y.",
            a: "From eq2: x = y + 1. Sub: 3(y+1) + 2y = 12 \u2192 5y = 9 \u2192 y = 9/5, x = 14/5."
          },
          {
            q: "If 2x + 3y = 17 and 4x + 6y = 34, how many solutions?",
            a: "Infinite. Second equation = 2 \u00d7 first. They\u2019re the same line."
          }
        ]
      },
      {
        id: "quadratics",
        title: "Quadratic Equations",
        concepts: [
          "Standard form: ax\u00b2 + bx + c = 0.",
          "Factoring: find two numbers that multiply to ac and add to b.",
          "Special products: (a+b)\u00b2 = a\u00b2+2ab+b\u00b2, (a\u2212b)\u00b2 = a\u00b2\u22122ab+b\u00b2.",
          "Difference of squares: a\u00b2 \u2212 b\u00b2 = (a+b)(a\u2212b).",
          "Sum/product of roots: x\u2081+x\u2082 = \u2212b/a, x\u2081\u00d7x\u2082 = c/a."
        ],
        formulas: [
          "Quadratic formula: x = (\u2212b \u00b1 \u221a(b\u00b2\u22124ac)) / 2a",
          "Discriminant = b\u00b2\u22124ac: positive \u2192 2 real roots, 0 \u2192 1 root, negative \u2192 no real roots"
        ],
        tips: [
          "x\u00b2 = 16 has TWO solutions: x = 4 AND x = \u22124.",
          "\u221ax always means the POSITIVE root on the GRE.",
          "If x\u00b2 \u2212 5x + 6 = 0 \u2192 (x\u22122)(x\u22123) = 0 \u2192 x = 2 or 3."
        ],
        questions: [
          {
            q: "Solve: x\u00b2 \u2212 7x + 12 = 0",
            a: "(x\u22123)(x\u22124) = 0 \u2192 x = 3 or x = 4."
          },
          {
            q: "If x\u00b2 + x = 6, what are the possible values of x?",
            a: "x\u00b2 + x \u2212 6 = 0 \u2192 (x+3)(x\u22122) = 0 \u2192 x = \u22123 or 2."
          },
          {
            q: "If x\u00b2 = x, what are all possible values of x?",
            a: "x\u00b2 \u2212 x = 0 \u2192 x(x\u22121) = 0 \u2192 x = 0 or 1. Don\u2019t divide both sides by x!"
          }
        ]
      },
      {
        id: "inequalities",
        title: "Inequalities",
        concepts: [
          "Add/subtract: inequality direction preserved.",
          "Multiply/divide by positive: direction preserved.",
          "Multiply/divide by negative: direction REVERSES.",
          "Compound: \u22123 < x < 5 means both \u22123 < x and x < 5.",
          "|x| < a \u2192 \u2212a < x < a. |x| > a \u2192 x < \u2212a or x > a."
        ],
        formulas: [
          "Triangle inequality: |a + b| \u2264 |a| + |b|",
          "|x \u2212 a| < b means a \u2212 b < x < a + b"
        ],
        tips: [
          "NEVER multiply/divide an inequality by a variable unless you know its sign!",
          "x\u00b2 > 4 \u2192 x > 2 OR x < \u22122 (not just x > 2).",
          "If \u22121 < x < 0, then x\u00b3 < x\u00b2 < x < 1."
        ],
        questions: [
          {
            q: "If \u22123x + 7 > 1, what is the range of x?",
            a: "\u22123x > \u22126 \u2192 x < 2 (flip when dividing by negative)."
          },
          {
            q: "Solve: |2x \u2212 5| \u2264 3",
            a: "\u22123 \u2264 2x\u22125 \u2264 3 \u2192 2 \u2264 2x \u2264 8 \u2192 1 \u2264 x \u2264 4."
          }
        ]
      },
      {
        id: "exponents-radicals",
        title: "Exponents & Radicals",
        concepts: [
          "a\u207a \u00d7 a\u1d47 = a\u207a\u207a\u1d47. a\u207a / a\u1d47 = a\u207a\u207b\u1d47.",
          "(a\u207a)\u1d47 = a\u207a\u1d47. (ab)\u207a = a\u207aa\u1d47.",
          "a\u2070 = 1 (for a \u2260 0). a\u207b\u207f = 1/a\u207f.",
          "a^(1/n) = nth root of a. a^(m/n) = (nth root of a)^m.",
          "\u221a(ab) = \u221aa \u00d7 \u221ab. \u221a(a/b) = \u221aa / \u221ab.",
          "Cannot add/subtract unlike radicals: \u221a2 + \u221a3 \u2260 \u221a5."
        ],
        formulas: [
          "Rationalizing: a/\u221ab = a\u221ab/b",
          "Negative exponents: 2\u207b\u00b3 = 1/2\u00b3 = 1/8"
        ],
        tips: [
          "0\u2070 is undefined on the GRE.",
          "Compare bases: 2\u00b3\u2070 vs 3\u00b2\u2070 \u2192 rewrite as 8\u00b9\u2070 vs 9\u00b9\u2070 \u2192 9\u00b9\u2070 is bigger.",
          "Fractional exponents: 27^(2/3) = (cube root of 27)\u00b2 = 3\u00b2 = 9."
        ],
        questions: [
          {
            q: "Simplify: (2\u00b3)\u2074 \u00d7 2\u207b\u2075",
            a: "2\u00b9\u00b2 \u00d7 2\u207b\u2075 = 2\u2077 = 128."
          },
          {
            q: "QC: Col A: 2\u2074\u2070 | Col B: 3\u00b3\u2070",
            a: "Cannot be determined? Actually: 2\u2074\u2070 = (2\u2074)\u00b9\u2070 = 16\u00b9\u2070. 3\u00b3\u2070 = (3\u00b3)\u00b9\u2070 = 27\u00b9\u2070. 27 > 16 \u2192 B is greater."
          },
          {
            q: "Simplify: \u221a50 + \u221a18",
            a: "5\u221a2 + 3\u221a2 = 8\u221a2."
          }
        ]
      },
      {
        id: "functions",
        title: "Functions",
        concepts: [
          "f(x) = rule that assigns each input exactly one output.",
          "Domain: all valid inputs. Range: all possible outputs.",
          "f(a) means substitute x = a into the rule.",
          "Composite: (f \u2218 g)(x) = f(g(x)) \u2014 apply g first, then f.",
          "GRE often uses symbols (\u25c6, \u25b3, @) as custom function definitions."
        ],
        formulas: [],
        tips: [
          "Read custom function definitions carefully \u2014 they define new operations.",
          "f(x+1) \u2260 f(x) + f(1) in general.",
          "If f(x) = x\u00b2, then f(\u22123) = 9, not \u22129."
        ],
        questions: [
          {
            q: "If f(x) = 2x\u00b2 \u2212 3x + 1, find f(\u22121).",
            a: "2(\u22121)\u00b2 \u2212 3(\u22121) + 1 = 2 + 3 + 1 = 6."
          },
          {
            q: "If a \u25c6 b = a\u00b2 + 2b, what is 3 \u25c6 (2 \u25c6 1)?",
            a: "First: 2 \u25c6 1 = 4 + 2 = 6. Then: 3 \u25c6 6 = 9 + 12 = 21."
          }
        ]
      },
      {
        id: "sequences",
        title: "Sequences",
        concepts: [
          "Arithmetic sequence: constant difference d. a\u2099 = a\u2081 + (n\u22121)d.",
          "Sum of arithmetic: S = n(a\u2081 + a\u2099)/2.",
          "Geometric sequence: constant ratio r. a\u2099 = a\u2081 \u00d7 r\u207f\u207b\u00b9.",
          "Sum of geometric: S = a\u2081(1 \u2212 r\u207f)/(1 \u2212 r) for r \u2260 1.",
          "Sum of first n positive integers: n(n+1)/2.",
          "Sum of first n squares: n(n+1)(2n+1)/6."
        ],
        formulas: [
          "Arithmetic: a\u2099 = a\u2081 + (n\u22121)d, Sum = n/2 \u00d7 (first + last)",
          "Geometric: a\u2099 = a\u2081r\u207f\u207b\u00b9, Sum = a\u2081(1\u2212r\u207f)/(1\u2212r)"
        ],
        tips: [
          "Average of arithmetic sequence = average of first and last terms.",
          "If |r| < 1, infinite geometric sum = a\u2081/(1\u2212r).",
          "1+2+3+...+100 = 100\u00d7101/2 = 5050."
        ],
        questions: [
          {
            q: "Find the 20th term: 5, 8, 11, 14, ...",
            a: "d = 3. a\u2082\u2080 = 5 + 19(3) = 62."
          },
          {
            q: "Sum of all even integers from 2 to 100?",
            a: "n = 50 terms. Sum = 50(2+100)/2 = 2550."
          },
          {
            q: "Geometric: 3, 6, 12, 24. What is the 8th term?",
            a: "r = 2. a\u2088 = 3 \u00d7 2\u2077 = 3 \u00d7 128 = 384."
          }
        ]
      }
    ]
  },

  // ============================================================
  // CHAPTER 3: GEOMETRY
  // ============================================================
  {
    id: "geometry",
    title: "Geometry",
    emoji: "\ud83d\udcd9",
    color: "#d97706",
    sections: [
      {
        id: "lines-angles",
        title: "Lines & Angles",
        concepts: [
          "Straight line = 180\u00b0. Full rotation = 360\u00b0.",
          "Vertical angles are equal. Linear pair sums to 180\u00b0.",
          "Parallel lines + transversal: alternate interior angles equal, corresponding angles equal, co-interior angles sum to 180\u00b0.",
          "Perpendicular lines form 90\u00b0 angles.",
          "Exterior angle of a triangle = sum of the two non-adjacent interior angles."
        ],
        formulas: [
          "Sum of interior angles of n-gon: (n\u22122) \u00d7 180\u00b0",
          "Each interior angle of regular n-gon: (n\u22122) \u00d7 180\u00b0 / n"
        ],
        tips: [
          "Diagrams on the GRE are NOT drawn to scale (unless stated).",
          "With parallel lines, look for Z-angles (alternate), F-angles (corresponding), C-angles (co-interior)."
        ],
        questions: [
          {
            q: "Two angles are supplementary. One is 40\u00b0 more than the other. Find both.",
            a: "x + (x+40) = 180 \u2192 2x = 140 \u2192 x = 70. Angles: 70\u00b0 and 110\u00b0."
          },
          {
            q: "Sum of interior angles of a hexagon?",
            a: "(6\u22122) \u00d7 180 = 720\u00b0."
          }
        ]
      },
      {
        id: "triangles",
        title: "Triangles",
        concepts: [
          "Angle sum = 180\u00b0.",
          "Pythagorean theorem: a\u00b2 + b\u00b2 = c\u00b2 (right triangles).",
          "Common Pythagorean triples: 3-4-5, 5-12-13, 8-15-17, 7-24-25.",
          "30-60-90: sides = x, x\u221a3, 2x.",
          "45-45-90: sides = x, x, x\u221a2.",
          "Triangle inequality: sum of any two sides > third side.",
          "Similar triangles: corresponding sides proportional, angles equal.",
          "Area = \u00bd \u00d7 base \u00d7 height."
        ],
        formulas: [
          "Area = \u00bd bh. Equilateral area = (s\u00b2\u221a3)/4.",
          "30-60-90: 1 : \u221a3 : 2. 45-45-90: 1 : 1 : \u221a2."
        ],
        tips: [
          "The longest side is opposite the largest angle.",
          "In a right triangle, the hypotenuse is always the longest side.",
          "6-8-10, 9-12-15, 10-24-26 are all multiples of basic triples."
        ],
        questions: [
          {
            q: "A right triangle has legs 6 and 8. Find the hypotenuse.",
            a: "6\u00b2 + 8\u00b2 = 36 + 64 = 100. \u221a100 = 10. (3-4-5 triple \u00d72.)"
          },
          {
            q: "In a 30-60-90 triangle, the short leg is 5. Find the hypotenuse.",
            a: "Hypotenuse = 2 \u00d7 short leg = 10."
          },
          {
            q: "Can a triangle have sides 3, 5, 9?",
            a: "No. 3 + 5 = 8 < 9. Violates triangle inequality."
          }
        ]
      },
      {
        id: "quadrilaterals",
        title: "Quadrilaterals & Polygons",
        concepts: [
          "Rectangle: A = l \u00d7 w, P = 2(l + w). All angles 90\u00b0.",
          "Square: A = s\u00b2, P = 4s. Diagonal = s\u221a2.",
          "Parallelogram: opposite sides equal and parallel. A = b \u00d7 h.",
          "Trapezoid: A = \u00bd(b\u2081 + b\u2082) \u00d7 h.",
          "Rhombus: all sides equal. A = \u00bd \u00d7 d\u2081 \u00d7 d\u2082.",
          "Sum of interior angles of quadrilateral = 360\u00b0."
        ],
        formulas: [
          "Rectangle diagonal = \u221a(l\u00b2 + w\u00b2)",
          "Regular polygon: interior angle = (n\u22122)\u00d7180/n"
        ],
        tips: [
          "Every square is a rectangle, but not every rectangle is a square.",
          "Parallelogram diagonals bisect each other.",
          "For max area with fixed perimeter, use a square (or circle)."
        ],
        questions: [
          {
            q: "A rectangle has diagonal 13 and width 5. Find the area.",
            a: "Length = \u221a(13\u00b2 \u2212 5\u00b2) = \u221a(169\u221225) = \u221a144 = 12. Area = 5 \u00d7 12 = 60."
          },
          {
            q: "Each interior angle of a regular polygon is 140\u00b0. How many sides?",
            a: "(n\u22122)\u00d7180/n = 140 \u2192 180n\u2212360 = 140n \u2192 40n = 360 \u2192 n = 9."
          }
        ]
      },
      {
        id: "circles",
        title: "Circles",
        concepts: [
          "Circumference = 2\u03c0r = \u03c0d.",
          "Area = \u03c0r\u00b2.",
          "Arc length = (central angle / 360) \u00d7 2\u03c0r.",
          "Sector area = (central angle / 360) \u00d7 \u03c0r\u00b2.",
          "Central angle = arc measure.",
          "Inscribed angle = \u00bd \u00d7 intercepted arc.",
          "Inscribed angle in semicircle = 90\u00b0."
        ],
        formulas: [
          "C = 2\u03c0r = \u03c0d",
          "A = \u03c0r\u00b2",
          "Arc = (\u03b8/360) \u00d7 2\u03c0r, Sector = (\u03b8/360) \u00d7 \u03c0r\u00b2"
        ],
        tips: [
          "Diameter is the longest chord in a circle.",
          "Tangent line is perpendicular to the radius at the point of tangency.",
          "Two tangent segments from the same external point are equal."
        ],
        questions: [
          {
            q: "A circle has area 49\u03c0. What is its circumference?",
            a: "\u03c0r\u00b2 = 49\u03c0 \u2192 r = 7. C = 2\u03c0(7) = 14\u03c0."
          },
          {
            q: "A 60\u00b0 arc in a circle with radius 12. Find arc length.",
            a: "(60/360) \u00d7 2\u03c0(12) = (1/6)(24\u03c0) = 4\u03c0."
          }
        ]
      },
      {
        id: "3d-geometry",
        title: "3D Geometry",
        concepts: [
          "Rectangular box: V = lwh, SA = 2(lw + lh + wh).",
          "Cube: V = s\u00b3, SA = 6s\u00b2. Space diagonal = s\u221a3.",
          "Cylinder: V = \u03c0r\u00b2h, SA = 2\u03c0r\u00b2 + 2\u03c0rh.",
          "Sphere: V = (4/3)\u03c0r\u00b3, SA = 4\u03c0r\u00b2.",
          "Cone: V = (1/3)\u03c0r\u00b2h."
        ],
        formulas: [
          "Box diagonal = \u221a(l\u00b2 + w\u00b2 + h\u00b2)",
          "Cylinder: V = \u03c0r\u00b2h",
          "Sphere: V = \u2074\u2044\u2083 \u03c0r\u00b3"
        ],
        tips: [
          "Doubling the radius of a cylinder quadruples the volume.",
          "Doubling all dimensions of a box multiplies volume by 8.",
          "Surface area scales as square; volume scales as cube."
        ],
        questions: [
          {
            q: "A cylinder has radius 3 and height 10. Find its volume.",
            a: "V = \u03c0(3)\u00b2(10) = 90\u03c0."
          },
          {
            q: "A cube has volume 64. What is its surface area?",
            a: "s\u00b3 = 64 \u2192 s = 4. SA = 6(4)\u00b2 = 96."
          }
        ]
      },
      {
        id: "coordinate-geometry",
        title: "Coordinate Geometry",
        concepts: [
          "Distance: d = \u221a((x\u2082\u2212x\u2081)\u00b2 + (y\u2082\u2212y\u2081)\u00b2).",
          "Midpoint: ((x\u2081+x\u2082)/2, (y\u2081+y\u2082)/2).",
          "Slope: m = (y\u2082\u2212y\u2081)/(x\u2082\u2212x\u2081).",
          "Parallel lines: same slope. Perpendicular lines: slopes multiply to \u22121.",
          "Slope-intercept: y = mx + b. Point-slope: y \u2212 y\u2081 = m(x \u2212 x\u2081).",
          "x-intercept: set y = 0. y-intercept: set x = 0."
        ],
        formulas: [
          "Distance = \u221a((x\u2082\u2212x\u2081)\u00b2 + (y\u2082\u2212y\u2081)\u00b2)",
          "Slope = rise/run = (y\u2082\u2212y\u2081)/(x\u2082\u2212x\u2081)",
          "Midpoint = ((x\u2081+x\u2082)/2, (y\u2081+y\u2082)/2)"
        ],
        tips: [
          "Horizontal lines: slope = 0. Vertical lines: slope = undefined.",
          "Perpendicular slopes: m\u2081 \u00d7 m\u2082 = \u22121.",
          "Area of triangle with vertices: \u00bd|x\u2081(y\u2082\u2212y\u2083) + x\u2082(y\u2083\u2212y\u2081) + x\u2083(y\u2081\u2212y\u2082)|."
        ],
        questions: [
          {
            q: "Distance between (2, 3) and (6, 6)?",
            a: "\u221a((6\u22122)\u00b2 + (6\u22123)\u00b2) = \u221a(16+9) = \u221a25 = 5."
          },
          {
            q: "A line passes through (1, 4) and (3, 10). Find its equation.",
            a: "m = (10\u22124)/(3\u22121) = 3. y \u2212 4 = 3(x\u22121) \u2192 y = 3x + 1."
          },
          {
            q: "Line L has slope 2/3. What\u2019s the slope of a line perpendicular to L?",
            a: "\u22123/2 (negative reciprocal)."
          }
        ]
      }
    ]
  },

  // ============================================================
  // CHAPTER 4: DATA ANALYSIS
  // ============================================================
  {
    id: "data-analysis",
    title: "Data Analysis",
    emoji: "\ud83d\udcd5",
    color: "#dc2626",
    sections: [
      {
        id: "statistics",
        title: "Mean, Median, Mode, Range",
        concepts: [
          "Mean = sum / count.",
          "Median = middle value (or average of two middle) when sorted.",
          "Mode = most frequent value. Can be none or multiple.",
          "Range = max \u2212 min.",
          "Adding a constant to all values: mean & median shift, range unchanged.",
          "Multiplying all values by k: mean, median, range, SD all multiply by |k|."
        ],
        formulas: [
          "Mean = \u03a3x / n",
          "Weighted mean = \u03a3(w\u1d62x\u1d62) / \u03a3w\u1d62"
        ],
        tips: [
          "Mean is pulled toward outliers; median is resistant to outliers.",
          "In a set of consecutive integers, mean = median.",
          "Evenly spaced set: mean = (first + last) / 2."
        ],
        questions: [
          {
            q: "Scores: 72, 85, 91, 64, 88. Find mean and median.",
            a: "Mean = 400/5 = 80. Sorted: 64,72,85,88,91. Median = 85."
          },
          {
            q: "Five numbers have mean 20. Four are 15, 18, 22, 25. Find the fifth.",
            a: "Sum = 100. Known sum = 80. Fifth = 20."
          },
          {
            q: "Adding 10 to every value in a set. What happens to mean and SD?",
            a: "Mean increases by 10. Standard deviation stays the same."
          }
        ]
      },
      {
        id: "standard-deviation",
        title: "Standard Deviation",
        concepts: [
          "Measures spread/dispersion from the mean.",
          "Low SD = data clustered near mean. High SD = data spread out.",
          "SD = 0 only if all values are identical.",
          "Adding a constant to all values: SD unchanged.",
          "Multiplying all values by k: SD multiplied by |k|.",
          "GRE tests conceptual understanding, not computation of SD."
        ],
        formulas: [
          "SD = \u221a(average of squared deviations from mean)",
          "Variance = SD\u00b2"
        ],
        tips: [
          "Set {1,1,1,1} has SD = 0. Set {1,2,3,4} has higher SD than {2,2,3,3}.",
          "If asked to compare SDs, look at how spread out the values are.",
          "SD is always \u2265 0. It equals 0 only when all values are the same."
        ],
        questions: [
          {
            q: "Which set has greater SD: {10,10,10,10,10} or {8,9,10,11,12}?",
            a: "Second set. First has SD = 0 (all identical). Second is spread around 10."
          },
          {
            q: "Set S = {3,5,7,9,11}. If 4 is added to each element, the new SD is:",
            a: "Same as original. Adding a constant doesn\u2019t change spread."
          }
        ]
      },
      {
        id: "probability",
        title: "Probability",
        concepts: [
          "P(event) = favorable outcomes / total outcomes. Always 0 \u2264 P \u2264 1.",
          "P(not A) = 1 \u2212 P(A).",
          "Independent events: P(A and B) = P(A) \u00d7 P(B).",
          "Mutually exclusive: P(A or B) = P(A) + P(B).",
          "General: P(A or B) = P(A) + P(B) \u2212 P(A and B).",
          "Conditional: P(A|B) = P(A and B) / P(B)."
        ],
        formulas: [
          "Permutations: nPr = n! / (n\u2212r)!",
          "Combinations: nCr = n! / (r!(n\u2212r)!)",
          "With replacement: n\u02b3 outcomes for r picks from n items"
        ],
        tips: [
          "\u201cAt least one\u201d \u2192 use complement: 1 \u2212 P(none).",
          "Order matters \u2192 permutation. Order doesn\u2019t \u2192 combination.",
          "Probability of A AND B (independent): multiply. A OR B (exclusive): add."
        ],
        questions: [
          {
            q: "Two dice rolled. P(sum = 7)?",
            a: "6 favorable out of 36: (1,6)(2,5)(3,4)(4,3)(5,2)(6,1). P = 6/36 = 1/6."
          },
          {
            q: "From 10 people, choose a committee of 3. How many ways?",
            a: "C(10,3) = 10!/(3!\u00d77!) = 120."
          },
          {
            q: "P(rain Monday) = 0.3, P(rain Tuesday) = 0.4. If independent, P(rain both)?",
            a: "0.3 \u00d7 0.4 = 0.12."
          },
          {
            q: "P(at least one head in 3 coin flips)?",
            a: "1 \u2212 P(no heads) = 1 \u2212 (1/2)\u00b3 = 1 \u2212 1/8 = 7/8."
          }
        ]
      },
      {
        id: "data-interpretation",
        title: "Data Interpretation",
        concepts: [
          "Read axis labels, titles, and units carefully.",
          "Bar graphs: compare heights. Stacked bars: read segments.",
          "Pie charts: each slice = percentage of total. All slices sum to 100%.",
          "Line graphs: track trends over time. Slope = rate of change.",
          "Scatterplots: look for correlation (positive, negative, or none).",
          "Tables: cross-reference rows and columns."
        ],
        formulas: [],
        tips: [
          "Always check what the axes represent (count? percent? dollars?).",
          "Estimate when exact values aren\u2019t readable from the graph.",
          "\u201cApproximately\u201d in the question means you can round.",
          "Percent of total from a pie chart: (slice/360) \u00d7 100."
        ],
        questions: [
          {
            q: "A pie chart shows 25% Tech, 30% Finance, 20% Health, rest Other. What angle for Other?",
            a: "Other = 100% \u2212 75% = 25%. Angle = 0.25 \u00d7 360 = 90\u00b0."
          },
          {
            q: "Bar graph shows 2020: 150 sales, 2021: 195 sales. Percent increase?",
            a: "(195\u2212150)/150 \u00d7 100 = 30%."
          }
        ]
      }
    ]
  },

  // ============================================================
  // CHAPTER 5: QUANTITATIVE COMPARISON STRATEGIES
  // ============================================================
  {
    id: "qc-strategy",
    title: "QC Strategies",
    emoji: "\ud83d\udcca",
    color: "#7c3aed",
    sections: [
      {
        id: "qc-number-properties",
        title: "Number Properties for QC",
        concepts: [
          "Test special cases: 0, 1, \u22121, fractions between 0 and 1, large numbers.",
          "Positive fractions (0 < x < 1): x\u00b2 < x and 1/x > x.",
          "Negative numbers: squaring makes positive, cubing stays negative.",
          "Even/odd: test both to check if relationship holds.",
          "Zero: always test x = 0 as it breaks many assumptions."
        ],
        formulas: [],
        tips: [
          "If you find ONE case where A > B and ONE case where B > A \u2192 answer is D.",
          "Don\u2019t assume variables are positive integers unless stated.",
          "x\u00b2 > x is NOT always true (fails for 0 < x < 1)."
        ],
        questions: [
          {
            q: "x > 0. Col A: x\u00b2 | Col B: x",
            a: "Cannot be determined (D). If x=2: 4>2 (A). If x=0.5: 0.25<0.5 (B)."
          },
          {
            q: "x \u2260 0. Col A: x | Col B: 1/x",
            a: "Cannot be determined (D). x=2: 2>0.5 (A). x=0.5: 0.5<2 (B)."
          }
        ]
      },
      {
        id: "qc-estimation",
        title: "Estimation & Comparison Techniques",
        concepts: [
          "Simplify both columns before comparing.",
          "Add/subtract the same value from both columns.",
          "Multiply/divide both by the same POSITIVE value.",
          "Square both columns (only when both are positive).",
          "Compare to a benchmark (e.g., compare both to 1, or to 100)."
        ],
        formulas: [],
        tips: [
          "You can add, subtract, multiply (positive), or divide (positive) both columns.",
          "NEVER multiply/divide both columns by a negative or unknown-sign value.",
          "If both columns are positive, you can square both to remove square roots."
        ],
        questions: [
          {
            q: "Col A: \u221a150 | Col B: 12",
            a: "Square both: 150 vs 144. 150 > 144 \u2192 A is greater."
          },
          {
            q: "Col A: 3/7 + 5/11 | Col B: 1",
            a: "3/7 < 1/2 and 5/11 < 1/2. So sum < 1. B is greater."
          }
        ]
      },
      {
        id: "qc-plugging",
        title: "Plugging Numbers & Testing Cases",
        concepts: [
          "Always test at least 2\u20133 different types of numbers.",
          "Must-test list: 0, 1, \u22121, a fraction (like 1/2), a large positive, a negative.",
          "If the answer is the same for all tests \u2192 likely A, B, or C.",
          "If the answer differs for any test \u2192 answer is D.",
          "After plugging, try to prove algebraically if possible."
        ],
        formulas: [],
        tips: [
          "The GRE designs QC problems so that obvious guesses are wrong.",
          "Always read constraints: \u201cx > 0\u201d eliminates negatives and zero.",
          "When plugging, try numbers that make the expressions equal first."
        ],
        questions: [
          {
            q: "x is an integer. Col A: (\u22121)\u02e3 | Col B: (\u22121)\u02e3\u207a\u00b9",
            a: "Cannot be determined (D). If x=1: \u22121 vs 1 (B). If x=2: 1 vs \u22121 (A)."
          },
          {
            q: "xy > 0. Col A: x + y | Col B: 0",
            a: "Cannot be determined (D). Both positive: A>0 (A). Both negative: A<0 (B)."
          }
        ]
      },
      {
        id: "high-frequency",
        title: "High-Frequency GRE Topics",
        concepts: [
          "Percentages & ratios: successive percent change, weighted averages.",
          "Algebra: equations, inequalities, absolute value.",
          "Word problems: rates, work, mixtures, speed-distance-time.",
          "Number properties: remainders, divisibility, factors, primes.",
          "Probability & statistics: mean, median, SD, basic probability.",
          "Coordinate geometry: slope, distance, midpoint, equation of line."
        ],
        formulas: [
          "Successive %: (1+r\u2081)(1+r\u2082)\u22121",
          "Combined work: 1/T = 1/A + 1/B",
          "Average speed (equal distances): 2v\u2081v\u2082/(v\u2081+v\u2082)"
        ],
        tips: [
          "Know common fraction-decimal conversions cold.",
          "Memorize Pythagorean triples: 3-4-5, 5-12-13, 8-15-17.",
          "For percent problems, use the multiplier method (1.2 for 20% increase).",
          "In QC, the answer is D more often than students expect.",
          "Read every word in the problem \u2014 \u201cpositive\u201d vs \u201cnon-negative\u201d matters."
        ],
        questions: [
          {
            q: "A store marks up by 40% then offers 25% discount. Net change from original?",
            a: "1.40 \u00d7 0.75 = 1.05 \u2192 5% net increase."
          },
          {
            q: "Two pipes fill a tank in 6 and 9 hours. How long together?",
            a: "1/6 + 1/9 = 3/18 + 2/18 = 5/18. Time = 18/5 = 3.6 hours."
          },
          {
            q: "Remainder when 3\u00b2\u2070\u2070 \u00f7 4?",
            a: "3\u00b9\u21923, 3\u00b2\u21921, 3\u00b3\u21923, 3\u2074\u21921 (cycle 2). 200 is even \u2192 rem 1."
          }
        ]
      }
    ]
  }
];
