// GRE Quant Complete — Study Data
// Comprehensive notes with detailed explanations, examples, and practice

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
          "Integers are whole numbers with no fractional or decimal part: ... \u22123, \u22122, \u22121, 0, 1, 2, 3 ...",
          "Zero is an integer. It is EVEN, but it is neither positive nor negative. This is one of the most tested facts on the GRE.",
          "Positive integers: 1, 2, 3, ... (do NOT include 0). Negative integers: \u22121, \u22122, \u22123, ...",
          "\u201cNon-negative\u201d means \u2265 0 (includes zero). \u201cPositive\u201d means > 0 (excludes zero). The GRE loves testing this distinction.",
          "Sign rules for multiplication/division: Positive \u00d7 Positive = Positive. Negative \u00d7 Negative = Positive. Positive \u00d7 Negative = Negative. Example: (\u22123)(\u22124) = 12, but (\u22123)(4) = \u221212.",
          "Any number multiplied by 0 equals 0. This means if ab = 0, then a = 0 or b = 0 (or both).",
          "Odd/Even addition: Odd + Odd = Even (3+5=8). Even + Even = Even (4+6=10). Odd + Even = Odd (3+4=7). Think of it like this: two \u201cleftovers\u201d combine to make a whole.",
          "Odd/Even multiplication: Odd \u00d7 Odd = Odd (3\u00d75=15). Even \u00d7 anything = Even (2\u00d77=14). If ANY factor is even, the product is even.",
          "The product of n consecutive integers is always divisible by n!. For example, any 3 consecutive integers: one is divisible by 3, at least one by 2, so the product is divisible by 6.",
          "Consecutive integers: n, n+1, n+2, ... They alternate odd/even. Among any two consecutive integers, exactly one is even.",
          "Absolute value |x| = distance from 0 on the number line. Always \u2265 0. Example: |\u22127| = 7, |7| = 7."
        ],
        formulas: [
          "(\u22121)^n: If n is even \u2192 result is +1. If n is odd \u2192 result is \u22121. Example: (\u22121)\u00b9\u2070\u2070 = 1, (\u22121)\u2077\u2077 = \u22121.",
          "Sum of first n positive integers = n(n+1)/2. Example: 1+2+3+...+10 = 10(11)/2 = 55.",
          "Number of integers from a to b inclusive = b \u2212 a + 1. Example: integers from 5 to 20 = 20 \u2212 5 + 1 = 16."
        ],
        tips: [
          "Zero is even, and it\u2019s neither positive nor negative \u2014 the GRE exploits this constantly. If a problem says \u201cpositive integer,\u201d zero is excluded.",
          "x\u00b2 \u2265 0 is always true for all real numbers, but x\u00b2 > 0 fails when x = 0. The GRE will set traps around this.",
          "When a problem says \u201cinteger,\u201d don\u2019t assume positive! Test negative integers and zero.",
          "Squaring a negative number makes it positive: (\u22123)\u00b2 = 9. But cubing preserves the sign: (\u22123)\u00b3 = \u221227.",
          "The sum of an EVEN number of consecutive integers is never divisible by that count. The sum of an ODD number of consecutive integers is always divisible by that count."
        ],
        questions: [
          {
            q: "If x is a negative integer and y is a positive integer, which MUST be negative? A) x + y  B) x \u00d7 y  C) x\u00b2  D) y \u2212 x",
            a: "B) x \u00d7 y. Step by step: A) x + y could be positive (e.g., \u22121 + 5 = 4) or negative. B) Negative \u00d7 positive = always negative \u2713. C) x\u00b2 is always positive. D) y \u2212 x = positive \u2212 negative = positive + positive = always positive. So only B is always negative."
          },
          {
            q: "What is the sum of all integers from \u221250 to 50, inclusive?",
            a: "0. Every negative integer pairs with its positive counterpart: (\u221250+50) + (\u221249+49) + ... + (\u22121+1) + 0 = 0. Alternatively, there are 101 integers with mean 0, so sum = 0."
          },
          {
            q: "Quantitative Comparison \u2014 Column A: (\u22121)\u2075\u2070  |  Column B: (\u22121)\u2075\u00b9",
            a: "Column A is greater. (\u22121)\u2075\u2070 = 1 because 50 is even. (\u22121)\u2075\u00b9 = \u22121 because 51 is odd. Since 1 > \u22121, Column A wins."
          },
          {
            q: "If the sum of 5 consecutive integers is 35, what is the largest of the five?",
            a: "The middle number = 35/5 = 7. The five consecutive integers are 5, 6, 7, 8, 9. The largest is 9. (For odd count of consecutive integers, the mean equals the middle value.)"
          },
          {
            q: "Is the product of three consecutive integers always divisible by 6?",
            a: "Yes! Among any 3 consecutive integers: at least one is even (divisible by 2), and exactly one is divisible by 3. So the product is divisible by 2\u00d73 = 6. Example: 4\u00d75\u00d76 = 120, and 120/6 = 20 \u2713."
          },
          {
            q: "If n is an integer such that n\u00b3 < n, which of the following must be true? A) n < 0  B) n < 1  C) n < \u22121  D) \u22121 < n < 0",
            a: "B) n < 1. When n\u00b3 < n, then n\u00b3 \u2212 n < 0, so n(n\u00b2 \u2212 1) < 0, meaning n(n\u22121)(n+1) < 0. Testing: n = 0 gives 0 (not < 0), so n \u2260 0. For n = \u22122: (\u22122)(3)(\u22121) = 6 > 0, fails. For n = \u22121: 0, fails. Since n is an integer, we need n < \u22121 or 0 < n < 1 (no integers). Wait \u2014 for integers, testing shows n\u00b3 < n fails for all integers. The question likely means real n, where the solution is n < \u22121 or 0 < n < 1."
          }
        ]
      },
      // --- 1.2 Factors & Multiples ---
      {
        id: "factors-multiples",
        title: "Factors & Multiples",
        concepts: [
          "A factor (divisor) of n divides evenly into n with no remainder. Example: Factors of 12 are 1, 2, 3, 4, 6, 12.",
          "A multiple of n is any number you get by multiplying n by an integer. Example: Multiples of 5 are 5, 10, 15, 20, 25, ...",
          "Key relationship: If a is a factor of b, then b is a multiple of a. Example: 4 is a factor of 20, and 20 is a multiple of 4.",
          "How to find all factors of n: Test every integer from 1 up to \u221an. For each factor you find, pair it with n divided by that factor. Example: Factors of 36 \u2192 test 1 to 6. Pairs: (1,36), (2,18), (3,12), (4,9), (6,6). Total: 9 factors.",
          "1 is a factor of every integer. Every positive integer is a factor of itself.",
          "0 is a multiple of every integer (since n\u00d70 = 0), but 0 is NOT a factor of any nonzero number (since you can\u2019t divide by 0).",
          "Transitivity of factors: If a | b and b | c, then a | c. Example: 3 | 12 and 12 | 60, so 3 | 60.",
          "If a | b and a | c, then a | (b + c) and a | (b \u2212 c). Example: 5 | 20 and 5 | 15, so 5 | 35 and 5 | 5.",
          "A perfect square always has an ODD number of factors (because one factor is its own pair: \u221an pairs with itself). Example: 36 has 9 factors.",
          "A non-square always has an EVEN number of factors (factors come in distinct pairs)."
        ],
        formulas: [
          "Counting factors using prime factorization: If n = p\u1d43 \u00d7 q\u1d47 \u00d7 r\u1d9c, then total number of positive factors = (a+1)(b+1)(c+1). Example: 60 = 2\u00b2 \u00d7 3\u00b9 \u00d7 5\u00b9 \u2192 (2+1)(1+1)(1+1) = 12 factors.",
          "Sum of factors: For n = p\u1d43 \u00d7 q\u1d47, sum = (1+p+p\u00b2+...+p\u1d43)(1+q+q\u00b2+...+q\u1d47). Example: 12 = 2\u00b2\u00d73\u00b9 \u2192 (1+2+4)(1+3) = 7\u00d74 = 28.",
          "Number of EVEN factors of n: Total factors minus odd factors. Odd factors come from ignoring all 2s in the factorization.",
          "Product of all factors of n = n^(d(n)/2), where d(n) = number of factors."
        ],
        tips: [
          "Consecutive integers n and n+1 always share NO common factor other than 1 (GCF = 1). This is because any number dividing both would have to divide their difference, which is 1.",
          "A number has exactly 2 factors only if it\u2019s prime. A number has exactly 3 factors only if it\u2019s the square of a prime (p\u00b2). Example: 4 = 2\u00b2 has factors 1, 2, 4.",
          "The product of n consecutive integers is always divisible by n!. Example: 5\u00d76\u00d77\u00d78 (four consecutive) is divisible by 4! = 24.",
          "If the GRE asks \u201chow many factors does n have,\u201d always prime-factorize first. Don\u2019t try to list factors for large numbers.",
          "A number with exactly 4 factors is either p\u00b3 (like 8: 1,2,4,8) or pq where p,q are distinct primes (like 15: 1,3,5,15)."
        ],
        questions: [
          {
            q: "How many positive factors does 240 have?",
            a: "Step 1: Prime factorize. 240 = 2\u2074 \u00d7 3\u00b9 \u00d7 5\u00b9. Step 2: Apply formula. (4+1)(1+1)(1+1) = 5\u00d72\u00d72 = 20 factors."
          },
          {
            q: "If the GCF of two numbers is 6 and their LCM is 180, and one number is 36, what is the other?",
            a: "Use the golden identity: GCF \u00d7 LCM = a \u00d7 b. So 6 \u00d7 180 = 36 \u00d7 b. 1080 = 36b. b = 30. Verify: GCF(36,30) = 6 \u2713, LCM(36,30) = 180 \u2713."
          },
          {
            q: "QC: n has exactly 3 positive factors. Column A: n  |  Column B: 10",
            a: "Answer: D (Cannot be determined). A number with exactly 3 factors must be p\u00b2 (square of a prime). Possibilities: 2\u00b2=4, 3\u00b2=9, 5\u00b2=25, 7\u00b2=49, ... Some are less than 10 (4, 9), others greater (25, 49). So the relationship can\u2019t be determined."
          },
          {
            q: "How many positive factors of 720 are even?",
            a: "720 = 2\u2074 \u00d7 3\u00b2 \u00d7 5\u00b9. Total factors = (4+1)(2+1)(1+1) = 30. Odd factors (ignore all 2s): 3\u00b2 \u00d7 5\u00b9 has (2+1)(1+1) = 6 odd factors. Even factors = 30 \u2212 6 = 24."
          },
          {
            q: "If n is a positive integer with exactly 6 factors, what are the possible forms of n?",
            a: "6 = (5+1) or (2+1)(1+1). So n = p\u2075 (like 32 = 2\u2075) or n = p\u00b2q where p,q are distinct primes (like 12 = 2\u00b2\u00d73, or 18 = 2\u00d73\u00b2). These are the only forms."
          }
        ]
      },
      // --- 1.3 Prime Numbers ---
      {
        id: "primes",
        title: "Prime Numbers",
        concepts: [
          "A prime number has exactly two distinct factors: 1 and itself. Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.",
          "2 is the ONLY even prime number and the smallest prime. Every other even number is divisible by 2, so it can\u2019t be prime.",
          "1 is NOT prime (it has only one factor, not two). 0 and negative numbers are also NOT prime.",
          "The pair (2, 3) is the ONLY pair of consecutive integers that are both prime. After 2, all primes are odd, so consecutive odd numbers differ by 2 (twin primes like 11,13).",
          "Primality test: To check if n is prime, test divisibility by all primes up to \u221an. If none divide n, it\u2019s prime. Example: Is 97 prime? \u221a97 \u2248 9.8. Test primes 2,3,5,7. None divide 97 \u2192 97 is prime.",
          "Fundamental Theorem of Arithmetic: Every integer > 1 has a UNIQUE prime factorization (up to order). Example: 360 = 2\u00b3 \u00d7 3\u00b2 \u00d7 5.",
          "If p is prime and p divides (a\u00d7b), then p must divide a or p must divide b (or both). This is a crucial property unique to primes.",
          "Sum of two primes is even UNLESS one of the primes is 2 (because 2 is the only even prime, and even + odd = odd).",
          "Product of two distinct primes always has exactly 4 factors: 1, p, q, and pq. Example: 15 = 3\u00d75 has factors 1, 3, 5, 15.",
          "There are infinitely many primes (proven by Euclid). They get more spread out but never stop."
        ],
        formulas: [
          "Prime factorization: Break n down by dividing by smallest prime repeatedly. Example: 360 \u00f7 2 = 180 \u00f7 2 = 90 \u00f7 2 = 45 \u00f7 3 = 15 \u00f7 3 = 5. So 360 = 2\u00b3 \u00d7 3\u00b2 \u00d7 5.",
          "Number of prime factors vs. total factors: 12 = 2\u00b2 \u00d7 3 has 2 distinct prime factors but 6 total factors (1,2,3,4,6,12).",
          "For n!, every prime p \u2264 n appears in the factorization. The power of p in n! = \u230an/p\u230b + \u230an/p\u00b2\u230b + \u230an/p\u00b3\u230b + ... (Legendre\u2019s formula)"
        ],
        tips: [
          "TRAP numbers that LOOK prime but aren\u2019t: 91 = 7\u00d713, 51 = 3\u00d717, 57 = 3\u00d719, 87 = 3\u00d729, 119 = 7\u00d717. Memorize these!",
          "First 15 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47. Know these cold.",
          "Quick divisibility check for primality: If a number\u2019s digit sum is divisible by 3, the number is divisible by 3 (so not prime, unless it IS 3). Example: 51 \u2192 5+1=6, divisible by 3.",
          "A prime p > 3 is always of the form 6k\u00b11. This means it\u2019s always one more or one less than a multiple of 6. (Not all 6k\u00b11 are prime, but all primes >3 have this form.)",
          "The number of trailing zeros in n! equals the number of times 10 divides n!, which equals \u230an/5\u230b + \u230an/25\u230b + \u230an/125\u230b + ... (count factors of 5, since factors of 2 are always more plentiful)."
        ],
        questions: [
          {
            q: "How many prime numbers are between 40 and 60?",
            a: "Check each odd number: 41\u2713(prime), 43\u2713, 45=9\u00d75\u2717, 47\u2713, 49=7\u00b2\u2717, 51=3\u00d717\u2717, 53\u2713, 55=5\u00d711\u2717, 57=3\u00d719\u2717, 59\u2713. Answer: 5 primes (41, 43, 47, 53, 59)."
          },
          {
            q: "If p and q are distinct primes, how many positive factors does p\u00b2 \u00d7 q\u00b3 have?",
            a: "Apply the formula: (2+1)(3+1) = 3\u00d74 = 12 factors. These are all numbers of the form p\u1d43q\u1d47 where 0\u2264a\u22642 and 0\u2264b\u22643."
          },
          {
            q: "How many trailing zeros does 100! have?",
            a: "Count factors of 5: \u230a100/5\u230b + \u230a100/25\u230b = 20 + 4 = 24 trailing zeros. (We don\u2019t need \u230a100/125\u230b since 125 > 100.)"
          },
          {
            q: "QC: p is prime > 2. Col A: remainder when p \u00f7 2. Col B: remainder when p\u00b2 \u00f7 2.",
            a: "Equal (C). Every prime > 2 is odd. Odd \u00f7 2 always gives remainder 1. Odd\u00b2 is still odd, so odd\u00b2 \u00f7 2 also gives remainder 1. Both columns equal 1."
          },
          {
            q: "The product of two integers is 546. If both are greater than 1, and one is a prime, what is the prime?",
            a: "546 = 2 \u00d7 273 = 2 \u00d7 3 \u00d7 91 = 2 \u00d7 3 \u00d7 7 \u00d7 13. We need to split into two factors, one prime. The prime factor options are 2, 3, 7, 13. Check: 546/2 = 273, 546/3 = 182, 546/7 = 78, 546/13 = 42. All valid since both factors > 1. Multiple answers possible; a GRE question would add constraints."
          }
        ]
      },
      // --- 1.4 Divisibility Rules ---
      {
        id: "divisibility",
        title: "Divisibility Rules",
        concepts: [
          "Divisible by 2: Last digit is even (0, 2, 4, 6, 8). Example: 4,738 is divisible by 2 because 8 is even.",
          "Divisible by 3: Sum of all digits is divisible by 3. Example: 729 \u2192 7+2+9 = 18, and 18\u00f73 = 6 \u2713.",
          "Divisible by 4: Last TWO digits form a number divisible by 4. Example: 1,532 \u2192 32\u00f74 = 8 \u2713.",
          "Divisible by 5: Last digit is 0 or 5. Example: 9,845 ends in 5 \u2713.",
          "Divisible by 6: Divisible by BOTH 2 AND 3. Example: 234 \u2192 even \u2713, digit sum 2+3+4=9 divisible by 3 \u2713.",
          "Divisible by 8: Last THREE digits form a number divisible by 8. Example: 3,720 \u2192 720\u00f78 = 90 \u2713.",
          "Divisible by 9: Sum of all digits is divisible by 9. Example: 8,127 \u2192 8+1+2+7 = 18, and 18\u00f79 = 2 \u2713.",
          "Divisible by 10: Last digit is 0.",
          "Divisible by 11: Alternating sum of digits is divisible by 11 (or equals 0). Example: 9,163 \u2192 9\u22121+6\u22123 = 11 \u2713.",
          "Divisible by 12: Divisible by BOTH 3 AND 4 (use co-prime components, not 2\u00d76 since they share factor 2).",
          "Composite divisor trick: To test divisibility by a composite number, break it into co-prime factors. For 15, check 3 and 5. For 12, check 3 and 4 (not 2 and 6!).",
          "Among any n consecutive integers, exactly one is divisible by n. Example: In 14,15,16,17,18 \u2014 exactly one is divisible by 5 (that\u2019s 15)."
        ],
        formulas: [
          "Division algorithm: a = bq + r, where q is the quotient and 0 \u2264 r < b. Example: 47 = 5\u00d79 + 2, so 47\u00f75 has quotient 9, remainder 2.",
          "Remainder of (a + b) \u00f7 n = remainder of [(rem of a) + (rem of b)] \u00f7 n. Example: (17+23) \u00f7 5: rem(17)=2, rem(23)=3, 2+3=5, rem(5\u00f75)=0 \u2713.",
          "Remainder of (a \u00d7 b) \u00f7 n = remainder of [(rem of a) \u00d7 (rem of b)] \u00f7 n. Example: (17\u00d723) \u00f7 5: 2\u00d73=6, rem(6\u00f75)=1. Check: 391\u00f75 = 78 rem 1 \u2713.",
          "If a \u2261 b (mod n), then a and b have the same remainder when divided by n, and (a\u2212b) is divisible by n."
        ],
        tips: [
          "For divisibility by 9: the digit sum gives the EXACT remainder when dividing by 9. Example: 47 has digit sum 11, and 11 mod 9 = 2, so 47 mod 9 = 2.",
          "Common trap: Divisible by 2 AND by 6 does NOT guarantee divisible by 12. Example: 6 is divisible by 2 and 6, but not by 12. You must use CO-PRIME factors (3 and 4 for 12).",
          "The product of any n consecutive integers is always divisible by n!. This is because C(n consecutive, n) is always an integer.",
          "If you need to find the remainder of a large power (like 3\u00b2\u2070\u2070 mod 4), find the pattern/cycle of remainders first, then use the exponent mod the cycle length."
        ],
        questions: [
          {
            q: "Is 4,572 divisible by 6?",
            a: "Check both conditions: (1) Even? Last digit is 2, yes \u2713. (2) Digit sum divisible by 3? 4+5+7+2 = 18, and 18\u00f73 = 6 \u2713. Both conditions met, so yes, 4,572 is divisible by 6."
          },
          {
            q: "What is the remainder when 2\u2074\u2070 is divided by 3?",
            a: "Find the cycle: 2\u00b9 mod 3 = 2, 2\u00b2 mod 3 = 1, 2\u00b3 mod 3 = 2, 2\u2074 mod 3 = 1. The cycle is {2, 1} with length 2. Since 40 is even (40 mod 2 = 0), we use the 2nd position in the cycle: remainder = 1."
          },
          {
            q: "If 3n + 2 is divisible by 7, what is the remainder when n is divided by 7?",
            a: "3n + 2 \u2261 0 (mod 7) \u2192 3n \u2261 \u22122 \u2261 5 (mod 7). We need: 3 \u00d7 ? \u2261 5 (mod 7). Test: 3\u00d74 = 12 \u2261 5 (mod 7) \u2713. So n \u2261 4 (mod 7). The remainder is 4."
          },
          {
            q: "A 5-digit number 3a,45b is divisible by 36. Find a and b.",
            a: "36 = 4 \u00d7 9 (co-prime). Divisible by 4: last two digits \u201c5b\u201d must be divisible by 4. Options: 52, 56 \u2192 b = 2 or 6. Divisible by 9: digit sum 3+a+4+5+b = 12+a+b must be divisible by 9. If b=2: 14+a divisible by 9 \u2192 a=4. If b=6: 18+a divisible by 9 \u2192 a=0 or 9. Solutions: (a,b) = (4,2), (0,6), or (9,6)."
          },
          {
            q: "What is the remainder when 1! + 2! + 3! + ... + 100! is divided by 12?",
            a: "For n \u2265 4, n! is divisible by 12 (since 4! = 24 is divisible by 12, and every n! for n\u22654 contains 4! as a factor). So only 1! + 2! + 3! matter. 1 + 2 + 6 = 9. Remainder = 9."
          }
        ]
      },
      // --- 1.5 LCM & GCF ---
      {
        id: "lcm-gcf",
        title: "LCM & GCF",
        concepts: [
          "GCF (Greatest Common Factor), also called GCD: The largest number that divides both numbers evenly. To find it: prime factorize both, take each shared prime raised to its LOWEST power. Example: GCF(48, 36) = GCF(2\u2074\u00d73, 2\u00b2\u00d73\u00b2) = 2\u00b2\u00d73 = 12.",
          "LCM (Least Common Multiple): The smallest positive number that both numbers divide into. To find it: prime factorize both, take each prime raised to its HIGHEST power. Example: LCM(48, 36) = 2\u2074\u00d73\u00b2 = 144.",
          "GCF(a,b) always divides both a and b. LCM(a,b) is always a multiple of both a and b.",
          "GCF(a,b) \u2264 min(a,b) and LCM(a,b) \u2265 max(a,b). In other words, GCF is never bigger than the smaller number, and LCM is never smaller than the larger number.",
          "If GCF(a,b) = 1, the numbers are called co-prime (relatively prime). In this case, LCM(a,b) = a \u00d7 b. Example: GCF(8,15) = 1, so LCM(8,15) = 120.",
          "GCF of consecutive integers is ALWAYS 1. Example: GCF(14, 15) = 1.",
          "Real-world applications: \u201cWhen do two events sync up/coincide?\u201d \u2192 LCM. \u201cLargest equal groups/biggest tile size?\u201d \u2192 GCF.",
          "GCF(a,b) always divides LCM(a,b). In fact, LCM(a,b) / GCF(a,b) is always a positive integer."
        ],
        formulas: [
          "Golden Identity (ONLY for two numbers): GCF(a,b) \u00d7 LCM(a,b) = a \u00d7 b. Example: GCF(12,18) = 6, LCM(12,18) = 36. Check: 6\u00d736 = 216 = 12\u00d718 \u2713.",
          "Shortcut from golden identity: LCM(a,b) = (a \u00d7 b) / GCF(a,b).",
          "For three numbers: Find LCM of the first two, then find LCM of that result with the third. Example: LCM(4,6,10) = LCM(LCM(4,6), 10) = LCM(12, 10) = 60.",
          "GCF of fractions: GCF(numerators) / LCM(denominators). LCM of fractions: LCM(numerators) / GCF(denominators)."
        ],
        tips: [
          "The golden identity GCF \u00d7 LCM = a \u00d7 b only works for exactly TWO numbers. For three or more numbers, it does NOT hold.",
          "To find LCM quickly for small numbers: List multiples of the larger number until one is also a multiple of the smaller. Example: LCM(8,12): Multiples of 12: 12, 24\u2014stop! 24 is also a multiple of 8. LCM = 24.",
          "If a | b (a divides b), then GCF(a,b) = a and LCM(a,b) = b. Example: GCF(5,30) = 5, LCM(5,30) = 30.",
          "Euclidean algorithm for GCF: GCF(a,b) = GCF(b, a mod b). Repeat until remainder is 0. Example: GCF(48,18) = GCF(18,12) = GCF(12,6) = GCF(6,0) = 6."
        ],
        questions: [
          {
            q: "Two runners lap a track every 12 and 18 minutes. When do they first meet at the start together?",
            a: "This is an LCM problem (when do they \u201csync up\u201d?). LCM(12, 18): 12 = 2\u00b2\u00d73, 18 = 2\u00d73\u00b2. LCM = 2\u00b2\u00d73\u00b2 = 36 minutes."
          },
          {
            q: "72 apples and 90 oranges must be split into identical gift bags using ALL fruit. What\u2019s the maximum number of bags?",
            a: "This is a GCF problem (largest equal groups). GCF(72, 90): 72 = 2\u00b3\u00d73\u00b2, 90 = 2\u00d73\u00b2\u00d75. GCF = 2\u00d73\u00b2 = 18 bags. Each bag gets 72/18 = 4 apples and 90/18 = 5 oranges."
          },
          {
            q: "GCF of two numbers is 8, LCM is 96. One number is 32. Find the other.",
            a: "Golden identity: GCF \u00d7 LCM = a \u00d7 b. So 8 \u00d7 96 = 32 \u00d7 b. 768 = 32b. b = 24. Verify: GCF(32,24) = 8 \u2713, LCM(32,24) = 96 \u2713."
          },
          {
            q: "What is the LCM of 12, 15, and 20?",
            a: "Prime factorize: 12 = 2\u00b2\u00d73, 15 = 3\u00d75, 20 = 2\u00b2\u00d75. Take highest power of each prime: 2\u00b2\u00d73\u00d75 = 60. Alternatively: LCM(12,15) = 60, then LCM(60,20) = 60."
          },
          {
            q: "Three bells ring at intervals of 6, 8, and 12 seconds. If they ring together at noon, when do they next ring together?",
            a: "LCM(6, 8, 12): 6 = 2\u00d73, 8 = 2\u00b3, 12 = 2\u00b2\u00d73. LCM = 2\u00b3\u00d73 = 24 seconds. They next ring together 24 seconds after noon."
          }
        ]
      },
      // --- 1.6 Remainders ---
      {
        id: "remainders",
        title: "Remainders",
        concepts: [
          "Division algorithm: For any integers a and b (b > 0), there exist unique integers q (quotient) and r (remainder) such that a = bq + r, where 0 \u2264 r < b. Example: 47 = 5\u00d79 + 2, so 47 divided by 5 gives quotient 9 and remainder 2.",
          "Remainder arithmetic: You can work with just the remainders for addition, subtraction, and multiplication. This is called modular arithmetic. Example: (47 + 28) mod 5 = (2 + 3) mod 5 = 0.",
          "For powers/exponents: Find the cycle of remainders, then use exponent mod cycle length. Example: Powers of 3 mod 5: 3,4,2,1,3,4,2,1... (cycle length 4). So 3\u00b9\u2070\u2070 mod 5: 100 mod 4 = 0 \u2192 use 4th position = 1.",
          "Remainder when dividing by 10 = last digit. Remainder when dividing by 100 = last two digits. This is very useful for units digit problems.",
          "Negative remainders don\u2019t exist in standard form. If you get a negative result, add the divisor. Example: \u221223 mod 5: \u221223 = 5\u00d7(\u22125) + 2, so remainder = 2. Or: \u221223 + 25 = 2.",
          "If a and b give the same remainder when divided by n, then (a \u2212 b) is divisible by n. Conversely, if n | (a\u2212b), then a and b have the same remainder mod n.",
          "Chinese Remainder Theorem concept: If n divides by m gives remainder r, and n divides by k gives remainder s (where GCF(m,k) = 1), there\u2019s a unique remainder when dividing by mk."
        ],
        formulas: [
          "rem(a + b, n) = rem(rem(a,n) + rem(b,n), n). In words: add the individual remainders, then take the remainder of that sum.",
          "rem(a \u00d7 b, n) = rem(rem(a,n) \u00d7 rem(b,n), n). In words: multiply the individual remainders, then take the remainder.",
          "rem(a \u2212 b, n) = rem(rem(a,n) \u2212 rem(b,n) + n, n). The +n ensures we don\u2019t get a negative number.",
          "rem(a^k, n): Find cycle of rem(a,n), rem(a\u00b2,n), rem(a\u00b3,n)... Then use k mod (cycle length) to find position."
        ],
        tips: [
          "When a problem says \u201cn leaves remainder r when divided by d,\u201d translate to: n = dq + r for some integer q. This lets you write n in a useful form.",
          "If n mod 6 = 4, then n is even (since n = 6q + 4, and both 6q and 4 are even). Always check if the remainder tells you something about odd/even.",
          "For factorial remainders: 1! + 2! + ... + 100! mod 12 \u2014 only 1! + 2! + 3! matter, since n! for n\u22654 is divisible by 4! = 24 > 12. So answer = 1+2+6 = 9.",
          "If n gives the same remainder r when divided by several numbers (say 5 and 7), then (n \u2212 r) is divisible by LCM of those numbers. Example: n mod 5 = 3 and n mod 7 = 3 \u2192 (n\u22123) is divisible by 35.",
          "The remainder when dividing by 9 equals the digit sum mod 9. This is the basis for \u201ccasting out nines.\u201d"
        ],
        questions: [
          {
            q: "What is the remainder when 2\u2075\u2070 is divided by 7?",
            a: "Find the cycle of powers of 2 mod 7: 2\u00b9=2, 2\u00b2=4, 2\u00b3=8\u22611, 2\u2074\u22612, 2\u2075\u22614, 2\u2076\u22611... Cycle: {2,4,1} with length 3. Now 50 mod 3 = 2, so the answer is the 2nd position: remainder = 4."
          },
          {
            q: "n \u00f7 5 gives remainder 3, n \u00f7 7 gives remainder 4. What is the remainder when n \u00f7 35?",
            a: "List numbers with remainder 3 when \u00f75: 3, 8, 13, 18, 23, 28, 33... Check each mod 7: 3%7=3\u2717, 8%7=1\u2717, 13%7=6\u2717, 18%7=4\u2713! So n \u2261 18 (mod 35). Remainder = 18."
          },
          {
            q: "n gives remainder 1 when divided by 2, 3, 4, 5, and 6. What is the smallest n > 1?",
            a: "n\u22121 is divisible by 2, 3, 4, 5, and 6. So (n\u22121) is a multiple of LCM(2,3,4,5,6) = 60. The smallest positive multiple is 60, so n = 61."
          },
          {
            q: "What is the remainder when 7\u00b2\u2070\u2070 is divided by 5?",
            a: "Powers of 7 mod 5: 7\u00b9\u22612, 7\u00b2\u22614, 7\u00b3\u22613, 7\u2074\u22611, 7\u2075\u22612... Cycle: {2,4,3,1} with length 4. 200 mod 4 = 0, which means use the 4th position: remainder = 1."
          },
          {
            q: "If the remainder when n is divided by 12 is 7, what is the remainder when n is divided by 6?",
            a: "n = 12q + 7 for some integer q. Rewrite: n = 6(2q + 1) + 1. So n mod 6 = 1. (You can also check: if n=7, 7/6 = 1 rem 1. If n=19, 19/6 = 3 rem 1. Always 1.)"
          }
        ]
      },
      // --- 1.7 Units Digit Patterns ---
      {
        id: "units-digits",
        title: "Units Digit Patterns",
        concepts: [
          "The units digit of a number is its last digit, which equals the remainder when dividing by 10. For any arithmetic, ONLY the units digits of the inputs affect the units digit of the output.",
          "Some digits NEVER change when raised to any power (cycle length 1): 0\u2192always 0, 1\u2192always 1, 5\u2192always 5, 6\u2192always 6. Example: 6\u00b9=6, 6\u00b2=36, 6\u00b3=216 \u2014 always ends in 6.",
          "Two-step cycle: 4 cycles through 4,6,4,6... (odd power\u21924, even power\u21926). 9 cycles through 9,1,9,1... (odd power\u21929, even power\u21921).",
          "Four-step cycles: 2\u21922,4,8,6 | 3\u21923,9,7,1 | 7\u21927,9,3,1 | 8\u21928,4,2,6. These are the most commonly tested on the GRE.",
          "Method for finding units digit of a^n: Step 1: Find the units digit of the base a. Step 2: Look up which cycle it follows. Step 3: Find n mod (cycle length). Step 4: That position in the cycle is your answer. If the mod result is 0, use the LAST position.",
          "Perfect squares can only end in: 0, 1, 4, 5, 6, or 9. They can NEVER end in 2, 3, 7, or 8. This is useful for eliminating answer choices.",
          "For addition/multiplication of units digits: Just work with the last digits. Example: Units digit of 47\u00d763 = units digit of 7\u00d73 = units digit of 21 = 1."
        ],
        formulas: [
          "Complete units digit cycle table: 0\u2192{0}, 1\u2192{1}, 2\u2192{2,4,8,6}, 3\u2192{3,9,7,1}, 4\u2192{4,6}, 5\u2192{5}, 6\u2192{6}, 7\u2192{7,9,3,1}, 8\u2192{8,4,2,6}, 9\u2192{9,1}.",
          "Shortcut for even powers: Any number ending in 1,5,6 stays the same. Numbers ending in 4 become 6. Numbers ending in 9 become 1. Numbers ending in 2,3,7,8 have cycle length 4."
        ],
        tips: [
          "The product of 5 consecutive integers always ends in 0 (because it contains a multiple of 2 and a multiple of 5).",
          "If n ends in 0, 1, 5, or 6, then n^k ends in the same digit for all positive k.",
          "When the GRE asks for units digit of a SUM, find each units digit separately, then add and take the last digit of the sum.",
          "Common trap: The cycle starts at the 1st power, NOT the 0th power. a\u2070 = 1 for all nonzero a."
        ],
        questions: [
          {
            q: "What is the units digit of 7\u2077\u2077\u2077\u2077?",
            a: "Step 1: Base ends in 7. Step 2: Cycle for 7 is {7,9,3,1} with length 4. Step 3: 7777 mod 4 = 1 (since 7776 is divisible by 4). Step 4: Position 1 = 7. Units digit is 7."
          },
          {
            q: "What is the units digit of 17\u00b2\u2079 + 13\u00b3\u00b9?",
            a: "17\u00b2\u2079: Base ends in 7, cycle {7,9,3,1}, length 4. 29 mod 4 = 1. Position 1 \u2192 7. 13\u00b3\u00b9: Base ends in 3, cycle {3,9,7,1}, length 4. 31 mod 4 = 3. Position 3 \u2192 7. Sum: 7 + 7 = 14. Units digit = 4."
          },
          {
            q: "QC: Col A: units digit of 4\u2079\u2079 | Col B: units digit of 9\u2079\u2079",
            a: "4\u2079\u2079: Cycle for 4 is {4,6}. 99 is odd \u2192 position 1 \u2192 4. 9\u2079\u2079: Cycle for 9 is {9,1}. 99 is odd \u2192 position 1 \u2192 9. Since 4 < 9, Column B is greater."
          },
          {
            q: "What is the units digit of 2\u00b9 + 2\u00b2 + 2\u00b3 + ... + 2\u00b2\u2070?",
            a: "Units digits of powers of 2 cycle: 2,4,8,6 (sum = 20, units digit 0). There are 20 terms = 5 complete cycles of 4. Each cycle\u2019s units digits sum to 2+4+8+6 = 20 (units digit 0). So 5 \u00d7 20 = 100. Units digit = 0."
          },
          {
            q: "A perfect square ends in 6. What digit does its square root end in?",
            a: "Which digits squared give units digit 6? 4\u00b2 = 16 (units 6) \u2713. 6\u00b2 = 36 (units 6) \u2713. So the square root ends in either 4 or 6."
          }
        ]
      },
      // --- 1.8 Fractions & Decimals ---
      {
        id: "fractions-decimals",
        title: "Fractions & Decimals",
        concepts: [
          "A fraction a/b represents a parts out of b equal pieces. Proper fraction: a < b (value < 1). Improper: a \u2265 b (value \u2265 1). Example: 3/4 is proper, 7/4 is improper.",
          "Simplifying: Divide both numerator and denominator by their GCF. Example: 18/24 \u2192 GCF = 6 \u2192 3/4. Always simplify to lowest terms.",
          "Converting fraction to decimal: Divide numerator by denominator. Example: 3/8 = 0.375. Or: 1/3 = 0.333... (repeating).",
          "Converting decimal to fraction: Count decimal places, put over that power of 10, simplify. Example: 0.125 = 125/1000 = 1/8.",
          "Repeating decimal patterns: 0.aaa... = a/9 (example: 0.777... = 7/9). 0.ababab... = ab/99 (example: 0.363636... = 36/99 = 4/11). 0.abcabc... = abc/999.",
          "A fraction in lowest terms produces a terminating decimal if and only if the denominator has ONLY factors of 2 and/or 5. Example: 7/40 terminates (40 = 2\u00b3\u00d75), but 5/12 repeats (12 = 2\u00b2\u00d73, has factor 3).",
          "Comparing fractions: Cross-multiply. To compare a/b and c/d, compare a\u00d7d with b\u00d7c. If ad > bc, then a/b > c/d. Example: 7/11 vs 5/8 \u2192 7\u00d78=56 vs 11\u00d75=55. Since 56 > 55, 7/11 > 5/8.",
          "Between any two distinct fractions, there are infinitely many other fractions. One way to find one: average the two fractions.",
          "Multiplying by a proper fraction (0 < f < 1) makes a positive number smaller. Dividing by a proper fraction makes it larger. Example: 10 \u00d7 (1/2) = 5 (smaller), 10 \u00f7 (1/2) = 20 (larger)."
        ],
        formulas: [
          "Must-know fraction-decimal equivalents: 1/2=0.5, 1/3\u22480.333, 1/4=0.25, 1/5=0.2, 1/6\u22480.167, 1/7\u22480.143, 1/8=0.125, 1/9\u22480.111, 1/10=0.1, 1/11\u22480.0909, 1/12\u22480.0833.",
          "Mixed to improper: a b/c = (ac + b)/c. Example: 2\u00be = (2\u00d74+3)/4 = 11/4.",
          "Adding fractions: a/b + c/d = (ad + bc) / bd, then simplify. Or find the LCD first. Example: 2/3 + 3/4 = (8+9)/12 = 17/12.",
          "Dividing fractions: a/b \u00f7 c/d = a/b \u00d7 d/c (flip and multiply). Example: (3/4) \u00f7 (2/5) = (3/4)(5/2) = 15/8."
        ],
        tips: [
          "Quick comparison trick: If two fractions have the same numerator, the one with the SMALLER denominator is larger. Example: 3/5 > 3/7.",
          "To quickly compare fractions to 1/2: If numerator > half of denominator, the fraction > 1/2. Example: 5/9 > 1/2 (because 5 > 9/2 = 4.5).",
          "Common trap: Students forget that dividing by a fraction between 0 and 1 gives a LARGER result. Example: 6 \u00f7 (1/3) = 18, not 2.",
          "Benchmark fractions: Compare unknowns to 0, 1/4, 1/3, 1/2, 2/3, 3/4, 1 to quickly narrow down answers.",
          "Complex fractions: Simplify by multiplying top and bottom by the LCD of all denominators. Example: (1/2 + 1/3)/(1/4) = multiply all by 12 \u2192 (6+4)/3 = 10/3."
        ],
        questions: [
          {
            q: "Which is greater: 7/11 or 5/8?",
            a: "Cross-multiply: 7\u00d78 = 56 and 11\u00d75 = 55. Since 56 > 55, we know 7/11 > 5/8. (Alternatively: 7/11 \u2248 0.636 and 5/8 = 0.625.)"
          },
          {
            q: "What fraction equals 0.363636...?",
            a: "The repeating block is \u201c36\u201d (2 digits). Use the formula: 0.ababab... = ab/99. So 0.363636... = 36/99. Simplify: GCF(36,99) = 9. 36/9 = 4, 99/9 = 11. Answer: 4/11."
          },
          {
            q: "Does 7/250 produce a terminating decimal?",
            a: "Check the denominator in lowest terms: 250 = 2 \u00d7 5\u00b3. Only factors of 2 and 5 \u2192 yes, it terminates. (7/250 = 0.028.)"
          },
          {
            q: "Arrange in order from least to greatest: 3/7, 5/11, 7/15",
            a: "Convert to decimals: 3/7 \u2248 0.4286, 5/11 \u2248 0.4545, 7/15 \u2248 0.4667. Order: 3/7 < 5/11 < 7/15. Or cross-multiply pairs to confirm."
          },
          {
            q: "Simplify: (2/3 + 3/4) \u00f7 (5/6)",
            a: "First: 2/3 + 3/4. LCD = 12. 8/12 + 9/12 = 17/12. Then: (17/12) \u00f7 (5/6) = (17/12) \u00d7 (6/5) = (17\u00d76)/(12\u00d75) = 102/60 = 17/10 = 1.7."
          }
        ]
      },
      // --- 1.9 Ratios & Proportions ---
      {
        id: "ratios",
        title: "Ratios & Proportions",
        concepts: [
          "A ratio a:b compares two quantities. It means \u201cfor every a of one thing, there are b of the other.\u201d A ratio does NOT tell you the actual values, only the relative relationship. Example: Boys:Girls = 3:5 means there could be 3 and 5, or 6 and 10, or 30 and 50, etc.",
          "Part-to-whole: If the ratio of A to B is a:b, then A\u2019s fraction of the total = a/(a+b) and B\u2019s fraction = b/(a+b). Example: Ratio 3:5 \u2192 A is 3/8 of total, B is 5/8 of total.",
          "Three-part ratios: a:b:c means the total is split into a + b + c parts. Example: If ages are in ratio 2:3:5 and the total is 50, the three ages are: 2\u00d750/10=10, 3\u00d750/10=15, 5\u00d750/10=25.",
          "Combining ratios: When two ratios share a common term, equalize that term to combine. Example: A:B = 2:3 and B:C = 4:5. Make B equal: A:B = 8:12 and B:C = 12:15. Combined: A:B:C = 8:12:15.",
          "Direct variation (direct proportion): y = kx, where k is a constant. When x doubles, y doubles. The ratio y/x is always the same. Graph is a straight line through the origin.",
          "Inverse variation (inverse proportion): xy = k, where k is a constant. When x doubles, y halves. The product xy is always the same. Graph is a hyperbola.",
          "Proportions: If a/b = c/d, then ad = bc (cross-multiply). You can also do: a/c = b/d (means-extremes property)."
        ],
        formulas: [
          "Proportion solving: a/b = c/d \u2192 ad = bc. Example: 3/x = 12/20 \u2192 3\u00d720 = 12x \u2192 x = 5.",
          "Actual values from ratio: If ratio is a:b and total is T, then first part = aT/(a+b), second part = bT/(a+b).",
          "Direct variation: y = kx \u2192 k = y/x. If y\u2081/x\u2081 = y\u2082/x\u2082, they\u2019re directly proportional.",
          "Inverse variation: xy = k. If x\u2081y\u2081 = x\u2082y\u2082, they\u2019re inversely proportional.",
          "Joint variation: z = kxy (z varies directly with both x and y). Example: Area of triangle = (1/2)bh."
        ],
        tips: [
          "A ratio doesn\u2019t give actual values \u2014 only relative amounts. If told ratio is 3:5 and nothing else, you can\u2019t determine the actual numbers.",
          "When combining ratios, always make the shared term equal before combining. This is one of the most common GRE ratio tricks.",
          "In proportion problems, check units carefully. If the problem mixes units (hours and minutes, feet and inches), convert first.",
          "Percent is a ratio out of 100. So \u201c40%\u201d is the ratio 40:100 = 2:5.",
          "If a recipe calls for ingredients in a certain ratio, and you change one amount, all others must change by the same factor to maintain the ratio."
        ],
        questions: [
          {
            q: "The ratio of boys to girls in a class is 3:5. If there are 40 students total, how many boys?",
            a: "Total parts = 3 + 5 = 8. Boys = (3/8) \u00d7 40 = 15. Girls = (5/8) \u00d7 40 = 25. Check: 15 + 25 = 40 \u2713, and 15/25 = 3/5 \u2713."
          },
          {
            q: "If y varies inversely with x, and y = 6 when x = 4, find y when x = 8.",
            a: "Inverse variation: xy = k. Find k: 6 \u00d7 4 = 24. When x = 8: 8y = 24 \u2192 y = 3. (As x doubled from 4 to 8, y halved from 6 to 3.)"
          },
          {
            q: "A:B = 2:3 and B:C = 5:7. Find A:B:C.",
            a: "Make B the same in both ratios. B is 3 in the first and 5 in the second. LCM(3,5) = 15. Scale: A:B = 10:15 and B:C = 15:21. Combined: A:B:C = 10:15:21."
          },
          {
            q: "In a mixture, the ratio of water to alcohol is 3:1. If 5 liters of alcohol are added, the ratio becomes 3:2. Find the original amount of water.",
            a: "Let water = 3x, alcohol = x. After adding 5L alcohol: 3x/(x+5) = 3/2. Cross-multiply: 6x = 3x + 15. 3x = 15. x = 5. Original water = 3(5) = 15 liters."
          },
          {
            q: "The speed of a car is directly proportional to the fuel consumption rate. At 60 mph, it uses 8 gallons/hour. How much fuel at 45 mph?",
            a: "Direct proportion: fuel/speed = constant. k = 8/60 = 2/15. At 45 mph: fuel = (2/15) \u00d7 45 = 6 gallons/hour."
          }
        ]
      },
      // --- 1.10 Percentages ---
      {
        id: "percentages",
        title: "Percentages",
        concepts: [
          "Percent means \u201cper hundred.\u201d 25% = 25/100 = 0.25 = 1/4. Always convert to decimals or fractions for calculations.",
          "Three types of percent problems: (1) What is 30% of 200? \u2192 0.30 \u00d7 200 = 60. (2) 60 is what percent of 200? \u2192 60/200 = 0.30 = 30%. (3) 60 is 30% of what? \u2192 60/0.30 = 200.",
          "Percent increase = (New \u2212 Original)/Original \u00d7 100. Example: Price goes from $40 to $50. Increase = (50\u221240)/40 \u00d7 100 = 25%.",
          "Percent decrease = (Original \u2212 New)/Original \u00d7 100. Example: Price drops from $80 to $60. Decrease = (80\u221260)/80 \u00d7 100 = 25%.",
          "Successive percent changes: MULTIPLY the multipliers, don\u2019t add/subtract percentages. Example: 20% increase then 10% decrease = 1.20 \u00d7 0.90 = 1.08 = 8% net increase.",
          "The multiplier method: Increase of x% \u2192 multiply by (1 + x/100). Decrease of x% \u2192 multiply by (1 \u2212 x/100). This is the fastest way to handle percent changes.",
          "Profit & loss: Profit = Selling Price \u2212 Cost Price. Profit % = (Profit/Cost Price) \u00d7 100. Loss % = (Loss/Cost Price) \u00d7 100. NOTE: Always calculated on the COST price.",
          "Markup/discount: A store marks up by 40% then offers 20% discount. Net effect = 1.40 \u00d7 0.80 = 1.12 = 12% markup from cost.",
          "Simple interest: I = Prt (principal \u00d7 rate \u00d7 time). Compound interest: A = P(1 + r/n)^(nt)."
        ],
        formulas: [
          "x% of y = y% of x. This is always true! Example: 8% of 50 = 50% of 8 = 4. Use whichever calculation is easier.",
          "Successive percent changes: Net multiplier = (1 + r\u2081/100)(1 + r\u2082/100). Net percent change = (net multiplier \u2212 1) \u00d7 100.",
          "Increase by x% then decrease by x%: Net result = 1 \u2212 (x/100)\u00b2 = always a NET DECREASE of x\u00b2/100 percent.",
          "To reverse a percent increase: If something increased by x%, the original = new / (1 + x/100). Example: After 25% increase, price is $100. Original = 100/1.25 = $80.",
          "Percent change between a and b: ((b\u2212a)/a) \u00d7 100. The denominator is always the ORIGINAL (starting) value."
        ],
        tips: [
          "The biggest trap: A 50% increase followed by a 50% decrease is NOT zero change! It\u2019s 1.50 \u00d7 0.50 = 0.75 = 25% net DECREASE. Increases and decreases of the same percent do NOT cancel.",
          "Percent change is always relative to the ORIGINAL value, not the new value. Going from 40 to 50 is a 25% increase, but going from 50 to 40 is only a 20% decrease.",
          "Use the \u201cnice number\u201d trick: When a problem says \u201ca certain number,\u201d pick 100 as the starting value. This makes percent calculations trivial.",
          "x% of y = y% of x is incredibly useful. 17% of 50 is hard to compute, but 50% of 17 = 8.5 is easy!",
          "When comparing percent increases, remember: the same absolute change is a bigger percent of a smaller base and a smaller percent of a larger base."
        ],
        questions: [
          {
            q: "A price increases by 20% then decreases by 20%. What is the net percent change?",
            a: "Multiply the multipliers: 1.20 \u00d7 0.80 = 0.96. This is 96% of the original, meaning a 4% net decrease. (Using the shortcut: x\u00b2/100 = 20\u00b2/100 = 4% decrease.)"
          },
          {
            q: "If 60% of x equals 40% of 90, find x.",
            a: "0.60x = 0.40 \u00d7 90. 0.60x = 36. x = 36/0.60 = 60."
          },
          {
            q: "A shirt originally costs $80. After a 25% discount, what\u2019s the sale price? Then 8% tax is added. What\u2019s the final price?",
            a: "Discount: $80 \u00d7 0.75 = $60. Tax: $60 \u00d7 1.08 = $64.80. Note: 80 \u00d7 0.75 \u00d7 1.08 = 80 \u00d7 0.81 = $64.80."
          },
          {
            q: "Population grows by 10% in year 1, 20% in year 2, and 50% in year 3. Starting population: 1000. Final?",
            a: "1000 \u00d7 1.10 \u00d7 1.20 \u00d7 1.50 = 1000 \u00d7 1.98 = 1980. (Don\u2019t add 10+20+50=80%. The correct net increase is 98%.)"
          },
          {
            q: "A merchant buys goods for $200 and wants a 25% profit after offering a 20% discount. What should the marked price be?",
            a: "Desired selling price = $200 \u00d7 1.25 = $250. If marked price is M, then M \u00d7 0.80 = 250. M = 250/0.80 = $312.50."
          },
          {
            q: "In an election, candidate A got 60% of the votes and won by 8,000 votes. How many total votes were cast?",
            a: "A got 60%, B got 40%. Difference = 60% \u2212 40% = 20% of total = 8,000. Total = 8,000/0.20 = 40,000 votes."
          }
        ]
      },
      // --- 1.11 Word Problems ---
      {
        id: "word-problems",
        title: "Word Problems (Rate, Work, Mixtures)",
        concepts: [
          "Distance = Speed \u00d7 Time (d = st). This is the fundamental relationship. Rearranged: Speed = Distance/Time, Time = Distance/Speed.",
          "Work = Rate \u00d7 Time. If a machine does a job in 6 hours, its rate is 1/6 of the job per hour. Rate is always \u201camount per unit time.\u201d",
          "Combined work: If A does a job in a hours and B in b hours, working TOGETHER their combined rate is 1/a + 1/b = (a+b)/(ab). Time together = ab/(a+b). Example: A in 6 hrs, B in 4 hrs \u2192 together in (6\u00d74)/(6+4) = 24/10 = 2.4 hrs.",
          "If someone works at rate r for time t, they complete r\u00d7t of the job. Example: A works at 1/6 per hour for 2 hours \u2192 completes 2/6 = 1/3 of the job.",
          "Average speed \u2260 average of the two speeds! Average speed = Total Distance / Total Time. This is one of the most common traps.",
          "For equal distances at two different speeds: Average speed = 2v\u2081v\u2082/(v\u2081+v\u2082) (harmonic mean). Example: 60 mph one way, 40 mph back. Average = 2(60)(40)/(60+40) = 4800/100 = 48 mph.",
          "Mixture problems: The total value/amount of the mixture = sum of individual values. Set up: (amount\u2081)(concentration\u2081) + (amount\u2082)(concentration\u2082) = (total amount)(final concentration).",
          "Average problems: Average = Sum/Count. Missing value = (Target Average \u00d7 Count) \u2212 Sum of known values.",
          "Relative speed: Objects moving toward each other \u2192 add speeds. Moving in same direction \u2192 subtract speeds. Moving apart \u2192 add speeds."
        ],
        formulas: [
          "Combined work rate: 1/T = 1/A + 1/B, so T = AB/(A+B). For three workers: 1/T = 1/A + 1/B + 1/C.",
          "Average speed (equal distances): 2v\u2081v\u2082/(v\u2081 + v\u2082). This is always LESS than the arithmetic mean.",
          "Weighted average: (w\u2081x\u2081 + w\u2082x\u2082 + ...)/(w\u2081 + w\u2082 + ...). Example: 3 tests at 80 and 2 tests at 90 \u2192 (3\u00d780 + 2\u00d790)/5 = 420/5 = 84.",
          "Meeting/overtaking: If A and B start d apart moving toward each other at speeds v\u2081 and v\u2082, time to meet = d/(v\u2081+v\u2082).",
          "Pipes: Filling pipe rate is positive, draining pipe rate is negative. Combined rate = 1/fill \u2212 1/drain."
        ],
        tips: [
          "If A does a job in 6 hours, A\u2019s rate is 1/6 per hour, NOT 6. Rate = 1/(time to complete whole job).",
          "For work problems where one person leaves partway: Calculate how much each person completes separately, then ensure the fractions sum to 1 (the whole job).",
          "For average speed, NEVER just average the two speeds. You MUST use total distance \u00f7 total time, or the harmonic mean formula for equal distances.",
          "In mixture problems, set up a clear table: Amount | Concentration | Value for each component and the mixture. Value = Amount \u00d7 Concentration.",
          "When a problem says \u201cA is twice as fast as B,\u201d that means A\u2019s rate = 2 \u00d7 B\u2019s rate, which means A takes HALF the time B takes."
        ],
        questions: [
          {
            q: "A can finish a job in 6 hours, B in 4 hours. How long working together?",
            a: "Combined rate: 1/6 + 1/4 = 2/12 + 3/12 = 5/12 of the job per hour. Time = 12/5 = 2.4 hours = 2 hours 24 minutes."
          },
          {
            q: "Drive 120 miles at 60 mph, then 120 miles at 40 mph. What is the average speed for the whole trip?",
            a: "Total distance = 240 miles. Total time = 120/60 + 120/40 = 2 + 3 = 5 hours. Average speed = 240/5 = 48 mph. (NOT 50, which is the average of 60 and 40!)"
          },
          {
            q: "Mix 10L of 30% salt solution with 20L of 60% salt solution. What is the final concentration?",
            a: "Total salt: 10\u00d70.30 + 20\u00d70.60 = 3 + 12 = 15 liters of salt. Total solution: 10 + 20 = 30 liters. Concentration = 15/30 = 50%. (This is a weighted average: closer to 60% because there\u2019s more of that solution.)"
          },
          {
            q: "A can do a job in 12 hours. B can do it in 8 hours. A works alone for 3 hours, then A and B work together. How much longer to finish?",
            a: "A works alone for 3 hours: completes 3/12 = 1/4 of the job. Remaining: 3/4. Together rate: 1/12 + 1/8 = 2/24 + 3/24 = 5/24 per hour. Time for remaining 3/4: (3/4) \u00f7 (5/24) = (3/4)(24/5) = 72/20 = 3.6 hours."
          },
          {
            q: "Two trains 300 miles apart travel toward each other at 70 mph and 80 mph. When do they meet?",
            a: "Relative speed (moving toward each other) = 70 + 80 = 150 mph. Time = Distance/Speed = 300/150 = 2 hours."
          },
          {
            q: "A student needs an average of 85 on 5 tests. The first 4 scores are 78, 92, 83, 88. What score is needed on the 5th test?",
            a: "Required total = 85 \u00d7 5 = 425. Current total = 78 + 92 + 83 + 88 = 341. Needed: 425 \u2212 341 = 84."
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
      // --- 2.1 Linear Equations ---
{
  id: "linear-equations",
  title: "Linear Equations (1 & 2 Variables)",
  concepts: [
    "A linear equation is an equation where the highest power of the variable is 1. Examples: 3x + 5 = 14, 2y \u2212 7 = 9. The graph of a linear equation in two variables is always a straight line.",
    "To solve a single-variable linear equation, isolate the variable by performing inverse operations on both sides. Example: 3x + 5 = 14 \u2192 3x = 14 \u2212 5 \u2192 3x = 9 \u2192 x = 3. Always check by plugging back in: 3(3) + 5 = 14 \u2713.",
    "A linear equation in two variables has the form ax + by = c. For example, 2x + 3y = 12 has infinitely many (x, y) solutions that form a line. A single equation in two variables cannot be solved for unique values unless additional information is given.",
    "The substitution method solves a system by isolating one variable in one equation and plugging it into the other. Example: If x + y = 10 and 2x \u2212 y = 5, from equation 1: y = 10 \u2212 x. Substitute into equation 2: 2x \u2212 (10 \u2212 x) = 5 \u2192 3x \u2212 10 = 5 \u2192 3x = 15 \u2192 x = 5, then y = 10 \u2212 5 = 5.",
    "The elimination method adds or subtracts equations to cancel one variable. Example: 3x + 2y = 16 and x \u2212 2y = 0. Adding them: 4x = 16 \u2192 x = 4. Then 4 \u2212 2y = 0 \u2192 y = 2. Tip: multiply one or both equations by constants to align coefficients before adding.",
    "A system has no solution (inconsistent) when the equations represent parallel lines. This happens when the ratios of coefficients are equal but the constants differ. Example: 2x + 4y = 10 and x + 2y = 8. Multiply the second by 2: 2x + 4y = 16, which contradicts the first equation (10 \u2260 16). No (x, y) satisfies both.",
    "A system has infinitely many solutions (dependent) when both equations describe the same line. Example: x + 2y = 6 and 2x + 4y = 12. The second equation is exactly 2 times the first, so every point on x + 2y = 6 is a solution.",
    "Quick test for systems: given a\u2081x + b\u2081y = c\u2081 and a\u2082x + b\u2082y = c\u2082. If a\u2081/a\u2082 \u2260 b\u2081/b\u2082 \u2192 one unique solution. If a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082 \u2192 no solution. If a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082 \u2192 infinitely many solutions.",
    "Word problems often set up systems. Example: 'The sum of two numbers is 20 and their difference is 4.' Let the numbers be x and y: x + y = 20 and x \u2212 y = 4. Adding: 2x = 24 \u2192 x = 12, y = 8.",
    "When a GRE problem says 'the equation has no solution,' it usually means simplifying both sides leads to a contradiction like 5 = 3. When it says 'infinitely many solutions,' simplifying leads to an identity like 0 = 0."
  ],
  formulas: [
    "Slope-intercept form: y = mx + b, where m = slope and b = y-intercept",
    "Standard form: ax + by = c (useful for elimination method)",
    "Slope between two points: m = (y\u2082 \u2212 y\u2081) / (x\u2082 \u2212 x\u2081)",
    "Point-slope form: y \u2212 y\u2081 = m(x \u2212 x\u2081)"
  ],
  tips: [
    "If a system has two equations and two unknowns, substitution is faster when one variable already has a coefficient of 1 (like x = ... or y = ...). Otherwise, elimination is often quicker.",
    "Always simplify each equation first\u2014distribute, combine like terms\u2014before choosing a method.",
    "On the GRE, if a problem asks for a combination like 2x + 3y rather than individual values, you may be able to find it directly without solving for x and y separately.",
    "Watch for trick questions: if the system gives you 3 equations and 2 unknowns, one equation may be redundant or may create an inconsistency.",
    "When checking your answer in a system, substitute into BOTH original equations, not just one."
  ],
  questions: [
    {
      q: "Solve for x: 5(x \u2212 3) + 2 = 3x + 1",
      a: "Step 1: Distribute: 5x \u2212 15 + 2 = 3x + 1.\nStep 2: Combine like terms on the left: 5x \u2212 13 = 3x + 1.\nStep 3: Subtract 3x from both sides: 2x \u2212 13 = 1.\nStep 4: Add 13 to both sides: 2x = 14.\nStep 5: Divide by 2: x = 7.\nCheck: 5(7 \u2212 3) + 2 = 5(4) + 2 = 22; 3(7) + 1 = 22. \u2713"
    },
    {
      q: "Solve the system: 2x + y = 7 and x \u2212 3y = \u22128",
      a: "Step 1 (Substitution): From eq. 1, y = 7 \u2212 2x.\nStep 2: Substitute into eq. 2: x \u2212 3(7 \u2212 2x) = \u22128.\nStep 3: Distribute: x \u2212 21 + 6x = \u22128 \u2192 7x \u2212 21 = \u22128.\nStep 4: Add 21: 7x = 13 \u2192 x = 13/7.\nStep 5: y = 7 \u2212 2(13/7) = 49/7 \u2212 26/7 = 23/7.\nAnswer: x = 13/7, y = 23/7."
    },
    {
      q: "For what value of k does the system 3x + 6y = 9 and kx + 2y = 3 have infinitely many solutions?",
      a: "Step 1: For infinitely many solutions, the second equation must be a scalar multiple of the first.\nStep 2: Divide eq. 1 by 3: x + 2y = 3.\nStep 3: The second equation is kx + 2y = 3. For these to be identical, we need k = 1.\nStep 4: Check ratios: a\u2081/a\u2082 = 3/k, b\u2081/b\u2082 = 6/2 = 3, c\u2081/c\u2082 = 9/3 = 3. We need 3/k = 3 \u2192 k = 1.\nAnswer: k = 1."
    },
    {
      q: "The sum of two numbers is 50. Twice the larger minus three times the smaller equals 10. Find both numbers.",
      a: "Step 1: Let L = larger, S = smaller. L + S = 50 and 2L \u2212 3S = 10.\nStep 2: From eq. 1: L = 50 \u2212 S.\nStep 3: Substitute: 2(50 \u2212 S) \u2212 3S = 10 \u2192 100 \u2212 2S \u2212 3S = 10.\nStep 4: Simplify: 100 \u2212 5S = 10 \u2192 \u22125S = \u221290 \u2192 S = 18.\nStep 5: L = 50 \u2212 18 = 32.\nAnswer: The numbers are 32 and 18."
    },
    {
      q: "If 3x + 4y = 24 and 6x + 8y = k, for what value of k does the system have no solution?",
      a: "Step 1: Multiply the first equation by 2: 6x + 8y = 48.\nStep 2: The second equation is 6x + 8y = k.\nStep 3: For no solution, the left sides are identical but right sides differ, so k \u2260 48.\nStep 4: Any value of k other than 48 gives no solution. If k = 48, there are infinitely many.\nAnswer: k can be any value except 48 (e.g., k = 10, k = 0, etc.)."
    },
    {
      q: "Solve: (x + 2)/3 \u2212 (x \u2212 1)/4 = 2",
      a: "Step 1: Find LCD of 3 and 4, which is 12.\nStep 2: Multiply every term by 12: 4(x + 2) \u2212 3(x \u2212 1) = 24.\nStep 3: Distribute: 4x + 8 \u2212 3x + 3 = 24.\nStep 4: Combine: x + 11 = 24.\nStep 5: Subtract 11: x = 13.\nCheck: (13 + 2)/3 \u2212 (13 \u2212 1)/4 = 15/3 \u2212 12/4 = 5 \u2212 3 = 2. \u2713"
    }
  ]
},
// --- 2.2 Quadratic Equations ---
{
  id: "quadratic-equations",
  title: "Quadratic Equations",
  concepts: [
    "A quadratic equation has the form ax\u00b2 + bx + c = 0, where a \u2260 0. The highest power of the variable is 2. Examples: x\u00b2 \u2212 5x + 6 = 0, 2x\u00b2 + 3x \u2212 2 = 0. Quadratics can have 0, 1, or 2 real solutions.",
    "Factoring is the fastest way to solve when possible. Look for two numbers that multiply to give a\u00d7c and add to give b. Example: x\u00b2 \u2212 5x + 6 = 0. We need two numbers that multiply to 6 and add to \u22125: those are \u22122 and \u22123. So (x \u2212 2)(x \u2212 3) = 0 \u2192 x = 2 or x = 3.",
    "Special product \u2014 Perfect square trinomial: a\u00b2 + 2ab + b\u00b2 = (a + b)\u00b2 and a\u00b2 \u2212 2ab + b\u00b2 = (a \u2212 b)\u00b2. Example: x\u00b2 + 10x + 25 = (x + 5)\u00b2. Recognize this pattern: the first and last terms are perfect squares, and the middle term is twice the product of their roots.",
    "Special product \u2014 Difference of squares: a\u00b2 \u2212 b\u00b2 = (a + b)(a \u2212 b). Example: x\u00b2 \u2212 49 = (x + 7)(x \u2212 7). This works because the middle terms cancel: (a + b)(a \u2212 b) = a\u00b2 \u2212 ab + ab \u2212 b\u00b2 = a\u00b2 \u2212 b\u00b2. GRE loves testing this with numbers: 51\u00b2 \u2212 49\u00b2 = (51 + 49)(51 \u2212 49) = 100 \u00d7 2 = 200.",
    "The quadratic formula solves any quadratic: x = (\u2212b \u00b1 \u221a(b\u00b2 \u2212 4ac)) / 2a. Example: 2x\u00b2 + 3x \u2212 2 = 0. Here a = 2, b = 3, c = \u22122. Discriminant = 9 \u2212 4(2)(\u22122) = 9 + 16 = 25. x = (\u22123 \u00b1 5)/4, so x = 2/4 = 1/2 or x = \u22128/4 = \u22122.",
    "The discriminant D = b\u00b2 \u2212 4ac tells you the nature of roots without solving. If D > 0: two distinct real roots. If D = 0: one repeated real root (the parabola touches the x-axis). If D < 0: no real roots (the parabola doesn\u2019t cross the x-axis). The GRE frequently tests this concept.",
    "Sum and product of roots: For ax\u00b2 + bx + c = 0, if the roots are r and s, then r + s = \u2212b/a and r \u00d7 s = c/a. Example: x\u00b2 \u2212 7x + 12 = 0 has roots 3 and 4. Sum = 3 + 4 = 7 = \u2212(\u22127)/1. Product = 3 \u00d7 4 = 12 = 12/1. This lets you answer questions about roots without actually finding them.",
    "Completing the square converts ax\u00b2 + bx + c to a(x \u2212 h)\u00b2 + k form. Example: x\u00b2 + 6x + 2 = 0 \u2192 (x\u00b2 + 6x + 9) \u2212 9 + 2 = 0 \u2192 (x + 3)\u00b2 = 7 \u2192 x = \u22123 \u00b1 \u221a7. Take half the x-coefficient (6/2 = 3), square it (9), add and subtract it.",
    "GRE trick: If a problem says x\u00b2 = 9, the answer is x = 3 or x = \u22123 (both!). But if it says x = \u221a9, the answer is only x = 3 (the principal root). Never forget the negative root when you take a square root of both sides of an equation."
  ],
  formulas: [
    "Quadratic formula: x = (\u2212b \u00b1 \u221a(b\u00b2 \u2212 4ac)) / (2a)",
    "Discriminant: D = b\u00b2 \u2212 4ac (D > 0: two real roots, D = 0: one repeated root, D < 0: no real roots)",
    "Sum of roots: r + s = \u2212b/a",
    "Product of roots: r \u00d7 s = c/a"
  ],
  tips: [
    "Always try factoring first\u2014it\u2019s the fastest method. Use the quadratic formula only when factoring is difficult or the roots are irrational.",
    "On the GRE, if a quadratic equation is set equal to zero, check whether the question asks for the positive root, the greater root, or all roots. Read carefully.",
    "The difference of squares identity a\u00b2 \u2212 b\u00b2 = (a + b)(a \u2212 b) is one of the most frequently tested algebra concepts on the GRE. Be ready to use it with numbers, not just variables.",
    "If a question asks 'how many real solutions does the equation have,' compute the discriminant. You do not need to solve the equation.",
    "Remember: sum and product of roots formulas let you find relationships between roots without solving. If a question asks for r\u00b2 + s\u00b2, use (r + s)\u00b2 \u2212 2rs."
  ],
  questions: [
    {
      q: "Solve: x\u00b2 \u2212 x \u2212 12 = 0",
      a: "Step 1: Find two numbers that multiply to \u221212 and add to \u22121.\nStep 2: Those numbers are \u22124 and 3 (since \u22124 \u00d7 3 = \u221212 and \u22124 + 3 = \u22121).\nStep 3: Factor: (x \u2212 4)(x + 3) = 0.\nStep 4: Set each factor to 0: x \u2212 4 = 0 \u2192 x = 4, or x + 3 = 0 \u2192 x = \u22123.\nAnswer: x = 4 or x = \u22123."
    },
    {
      q: "If x\u00b2 + bx + 16 = 0 has exactly one real solution, what are the possible values of b?",
      a: "Step 1: One real solution means the discriminant equals 0.\nStep 2: D = b\u00b2 \u2212 4(1)(16) = b\u00b2 \u2212 64 = 0.\nStep 3: b\u00b2 = 64.\nStep 4: b = 8 or b = \u22128.\nAnswer: b = 8 or b = \u22128."
    },
    {
      q: "Without solving, find the sum and product of the roots of 3x\u00b2 \u2212 12x + 7 = 0.",
      a: "Step 1: Identify a = 3, b = \u221212, c = 7.\nStep 2: Sum of roots = \u2212b/a = \u2212(\u221212)/3 = 12/3 = 4.\nStep 3: Product of roots = c/a = 7/3.\nAnswer: Sum = 4, Product = 7/3."
    },
    {
      q: "Compute 73\u00b2 \u2212 27\u00b2 without a calculator.",
      a: "Step 1: Recognize the difference of squares: a\u00b2 \u2212 b\u00b2 = (a + b)(a \u2212 b).\nStep 2: 73\u00b2 \u2212 27\u00b2 = (73 + 27)(73 \u2212 27).\nStep 3: = (100)(46).\nStep 4: = 4600.\nAnswer: 4600."
    },
    {
      q: "The roots of x\u00b2 \u2212 5x + 3 = 0 are r and s. Find r\u00b2 + s\u00b2.",
      a: "Step 1: We know r + s = 5 and rs = 3 (sum and product of roots).\nStep 2: Use the identity r\u00b2 + s\u00b2 = (r + s)\u00b2 \u2212 2rs.\nStep 3: r\u00b2 + s\u00b2 = 5\u00b2 \u2212 2(3) = 25 \u2212 6 = 19.\nAnswer: 19."
    },
    {
      q: "Solve by completing the square: x\u00b2 \u2212 8x + 5 = 0",
      a: "Step 1: Move constant: x\u00b2 \u2212 8x = \u22125.\nStep 2: Take half the x-coefficient: \u22128/2 = \u22124. Square it: 16.\nStep 3: Add 16 to both sides: x\u00b2 \u2212 8x + 16 = \u22125 + 16 = 11.\nStep 4: Factor left side: (x \u2212 4)\u00b2 = 11.\nStep 5: Take square root: x \u2212 4 = \u00b1\u221a11.\nStep 6: x = 4 \u00b1 \u221a11.\nAnswer: x = 4 + \u221a11 or x = 4 \u2212 \u221a11."
    }
  ]
},
// --- 2.3 Inequalities ---
{
  id: "inequalities",
  title: "Inequalities",
  concepts: [
    "An inequality compares expressions using <, >, \u2264, or \u2265. Solving an inequality is like solving an equation: add, subtract, multiply, or divide both sides by the same value. Example: 2x + 3 > 11 \u2192 2x > 8 \u2192 x > 4.",
    "CRITICAL RULE: When you multiply or divide both sides of an inequality by a negative number, you MUST flip the inequality sign. Example: \u22123x > 12 \u2192 divide by \u22123 \u2192 x < \u22124 (sign flips from > to <). This is the #1 mistake students make on inequality problems.",
    "Compound inequalities combine two inequalities. 'And' means both must be true (intersection). 'Or' means at least one is true (union). Example: \u22121 < 2x + 3 < 9 is an 'and' compound inequality. Solve: subtract 3 from all parts: \u22124 < 2x < 6, then divide by 2: \u22122 < x < 3.",
    "Absolute value inequalities split into two cases. For |expression| < k (where k > 0): \u2212k < expression < k. For |expression| > k: expression > k OR expression < \u2212k. Example: |x \u2212 3| < 5 means \u22125 < x \u2212 3 < 5 \u2192 \u22122 < x < 8.",
    "For |expression| > k: Example: |2x + 1| > 7 means 2x + 1 > 7 or 2x + 1 < \u22127. Case 1: 2x > 6 \u2192 x > 3. Case 2: 2x < \u22128 \u2192 x < \u22124. Answer: x > 3 or x < \u22124.",
    "When multiplying or dividing an inequality by a variable, you must consider whether that variable is positive or negative. If you don\u2019t know the sign, split into cases. Example: if x > 0, then x\u00b2 > 0 is always true. But if x could be negative, x\u00b2 > 0 is true for all x \u2260 0.",
    "Graphing inequalities on a number line: use an open circle for < or > (endpoint not included) and a closed/filled circle for \u2264 or \u2265 (endpoint included). Example: x \u2265 3 has a closed circle at 3 with a ray going right.",
    "The product/quotient sign rule: To determine where an expression like (x \u2212 2)(x + 3) > 0 is positive, find the zeros (x = 2, x = \u22123), then test intervals: x < \u22123 (both negative, product positive), \u22123 < x < 2 (one positive, one negative, product negative), x > 2 (both positive, product positive). Answer: x < \u22123 or x > 2.",
    "GRE Quantitative Comparison tip: When comparing quantities involving variables, you cannot assume a variable is positive unless stated. For example, if x\u00b2 = 4, x could be 2 or \u22122, so x could be greater than or less than 1."
  ],
  formulas: [
    "If |x| < a (a > 0), then \u2212a < x < a",
    "If |x| > a (a > 0), then x > a or x < \u2212a",
    "If |x| = a (a > 0), then x = a or x = \u2212a",
    "Triangle inequality: |a + b| \u2264 |a| + |b|"
  ],
  tips: [
    "Flip the sign when multiplying/dividing by a negative. Write \u2018FLIP\u2019 in your scratch work every time you do this so you don\u2019t forget.",
    "For absolute value inequalities, remember: 'Less thAND' (|x| < a gives an AND compound inequality) vs. 'GreatOR' (|x| > a gives an OR compound inequality).",
    "On the GRE, if an inequality question doesn\u2019t specify integers, the variable can take any real value. If it says 'x is a positive integer,' use that constraint to narrow the answer.",
    "When you see a quadratic inequality like x\u00b2 \u2212 5x + 6 < 0, factor it as (x \u2212 2)(x \u2212 3) < 0 and use the sign-chart method to find the interval where the product is negative: 2 < x < 3.",
    "Never multiply both sides of an inequality by a variable unless you know its sign. If the variable could be negative, split into two cases."
  ],
  questions: [
    {
      q: "Solve: \u22123x + 7 \u2265 1",
      a: "Step 1: Subtract 7 from both sides: \u22123x \u2265 \u22126.\nStep 2: Divide by \u22123 and FLIP the inequality sign: x \u2264 2.\nAnswer: x \u2264 2."
    },
    {
      q: "Solve: |2x \u2212 5| < 9",
      a: "Step 1: This is a 'less than' absolute value, so write the compound inequality: \u22129 < 2x \u2212 5 < 9.\nStep 2: Add 5 to all three parts: \u22124 < 2x < 14.\nStep 3: Divide all parts by 2: \u22122 < x < 7.\nAnswer: \u22122 < x < 7."
    },
    {
      q: "Solve: |3x + 2| \u2265 11",
      a: "Step 1: This is a 'greater than or equal' absolute value, so split into two cases.\nCase 1: 3x + 2 \u2265 11 \u2192 3x \u2265 9 \u2192 x \u2265 3.\nCase 2: 3x + 2 \u2264 \u221211 \u2192 3x \u2264 \u221213 \u2192 x \u2264 \u221213/3.\nAnswer: x \u2265 3 or x \u2264 \u221213/3."
    },
    {
      q: "Solve: (x \u2212 1)(x + 4) > 0",
      a: "Step 1: Find zeros: x = 1 and x = \u22124.\nStep 2: Create a sign chart with intervals: x < \u22124, \u22124 < x < 1, x > 1.\nStep 3: Test x = \u22125: (\u22126)(\u22121) = 6 > 0 \u2713.\nStep 4: Test x = 0: (\u22121)(4) = \u22124 < 0 \u2717.\nStep 5: Test x = 2: (1)(6) = 6 > 0 \u2713.\nAnswer: x < \u22124 or x > 1."
    },
    {
      q: "If \u22123 \u2264 x \u2264 5 and \u22122 \u2264 y \u2264 4, what is the greatest possible value of x \u2212 y?",
      a: "Step 1: To maximize x \u2212 y, we need the largest x and the smallest y.\nStep 2: Largest x = 5, smallest y = \u22122.\nStep 3: Maximum x \u2212 y = 5 \u2212 (\u22122) = 5 + 2 = 7.\nAnswer: 7."
    },
    {
      q: "For how many integer values of x is |x \u2212 3| \u2264 5 satisfied?",
      a: "Step 1: Rewrite as a compound inequality: \u22125 \u2264 x \u2212 3 \u2264 5.\nStep 2: Add 3 to all parts: \u22122 \u2264 x \u2264 8.\nStep 3: List the integers from \u22122 to 8: \u22122, \u22121, 0, 1, 2, 3, 4, 5, 6, 7, 8.\nStep 4: Count them: 11 integers.\nAnswer: 11."
    }
  ]
},
// --- 2.4 Exponents & Radicals ---
{
  id: "exponents-radicals",
  title: "Exponents & Radicals",
  concepts: [
    "An exponent tells you how many times to multiply a base by itself. Example: 2\u2074 = 2 \u00d7 2 \u00d7 2 \u00d7 2 = 16. The base is 2 and the exponent is 4. Any number raised to the power of 1 is itself: x\u00b9 = x.",
    "Product rule: When multiplying same bases, ADD the exponents. a\u207c \u00d7 a\u207f = a^(m+n). Example: 3\u00b2 \u00d7 3\u2074 = 3\u2076 = 729. Common mistake: 3\u00b2 \u00d7 3\u2074 \u2260 9\u2076. The base stays the same!",
    "Quotient rule: When dividing same bases, SUBTRACT the exponents. a\u207c / a\u207f = a^(m\u2212n). Example: 5\u2077 / 5\u00b3 = 5\u2074 = 625.",
    "Power rule: When raising a power to a power, MULTIPLY the exponents. (a\u207c)\u207f = a^(m\u00d7n). Example: (2\u00b3)\u2074 = 2\u00b9\u00b2 = 4096. Also: (ab)\u207f = a\u207f \u00d7 b\u207f and (a/b)\u207f = a\u207f / b\u207f.",
    "Zero exponent: Any nonzero number raised to the 0 power is 1. a\u2070 = 1 (where a \u2260 0). Example: 5\u2070 = 1, (\u22127)\u2070 = 1, (1000)\u2070 = 1. Note: 0\u2070 is undefined/indeterminate.",
    "Negative exponents mean reciprocals. a^(\u2212n) = 1/a\u207f. Example: 2\u207b\u00b3 = 1/2\u00b3 = 1/8. Also: (a/b)^(\u2212n) = (b/a)\u207f. Example: (2/3)\u207b\u00b2 = (3/2)\u00b2 = 9/4.",
    "Fractional exponents are radicals. a^(1/n) = the nth root of a. a^(m/n) = (\u221a[n]{a})\u207c = \u221a[n]{a\u207c}. Example: 8^(1/3) = \u221a[3]{8} = 2. Example: 27^(2/3) = (\u221a[3]{27})\u00b2 = 3\u00b2 = 9.",
    "Simplifying radicals: Factor out perfect squares (or cubes, etc.) from under the radical. \u221a50 = \u221a(25 \u00d7 2) = 5\u221a2. \u221a72 = \u221a(36 \u00d7 2) = 6\u221a2. For cube roots: \u221a[3]{54} = \u221a[3]{27 \u00d7 2} = 3\u221a[3]{2}.",
    "Rationalizing the denominator means removing radicals from the denominator. For single terms: 1/\u221a3 = (1 \u00d7 \u221a3)/(\u221a3 \u00d7 \u221a3) = \u221a3/3. For binomials: multiply by the conjugate. Example: 1/(\u221a5 + \u221a2) \u00d7 (\u221a5 \u2212 \u221a2)/(\u221a5 \u2212 \u221a2) = (\u221a5 \u2212 \u221a2)/(5 \u2212 2) = (\u221a5 \u2212 \u221a2)/3.",
    "You can only add or subtract radicals with the same radicand (number under the radical). Example: 3\u221a5 + 2\u221a5 = 5\u221a5, but 3\u221a5 + 2\u221a3 cannot be simplified further. However, sometimes simplifying first reveals like terms: \u221a12 + \u221a27 = 2\u221a3 + 3\u221a3 = 5\u221a3."
  ],
  formulas: [
    "a\u207c \u00d7 a\u207f = a^(m+n) | a\u207c / a\u207f = a^(m\u2212n) | (a\u207c)\u207f = a^(mn)",
    "a\u2070 = 1 (a \u2260 0) | a^(\u2212n) = 1/a\u207f | a^(m/n) = \u221a[n]{a\u207c}",
    "\u221a(a \u00d7 b) = \u221aa \u00d7 \u221ab | \u221a(a/b) = \u221aa / \u221ab",
    "Rationalize: a/\u221ab = (a\u221ab)/b | a/(\u221ab + \u221ac) = a(\u221ab \u2212 \u221ac)/(b \u2212 c)"
  ],
  tips: [
    "When comparing exponents on the GRE, try to express both numbers with the same base. For example, 8\u00b2 vs 4\u00b3: rewrite as (2\u00b3)\u00b2 = 2\u2076 and (2\u00b2)\u00b3 = 2\u2076, so they are equal.",
    "Remember that (\u22122)\u00b2 = 4 but \u22122\u00b2 = \u22124. Parentheses matter! Without parentheses, only the 2 is squared, and then the negative is applied.",
    "For GRE speed: memorize common powers: 2\u00b9\u2070 = 1024, 3\u2074 = 81, 5\u00b3 = 125, and perfect squares up to 15\u00b2 = 225.",
    "When you see large exponents like 2\u00b3\u2070, don\u2019t calculate\u2014look for patterns, cancel common bases, or use the exponent rules to simplify.",
    "A negative number raised to an even power is positive; raised to an odd power is negative. Example: (\u22122)\u2074 = 16 but (\u22122)\u00b3 = \u22128."
  ],
  questions: [
    {
      q: "Simplify: (3\u00b2 \u00d7 3\u2074) / 3\u00b3",
      a: "Step 1: Apply product rule to numerator: 3\u00b2 \u00d7 3\u2074 = 3^(2+4) = 3\u2076.\nStep 2: Apply quotient rule: 3\u2076 / 3\u00b3 = 3^(6\u22123) = 3\u00b3.\nStep 3: Calculate: 3\u00b3 = 27.\nAnswer: 27."
    },
    {
      q: "Evaluate: 16^(3/4)",
      a: "Step 1: Write 16 as a power of 2: 16 = 2\u2074.\nStep 2: Apply the rule: (2\u2074)^(3/4) = 2^(4 \u00d7 3/4) = 2\u00b3.\nStep 3: Calculate: 2\u00b3 = 8.\nAlternatively: 16^(1/4) = 2 (fourth root of 16), then 2\u00b3 = 8.\nAnswer: 8."
    },
    {
      q: "Simplify: \u221a72 + \u221a32 \u2212 \u221a18",
      a: "Step 1: Simplify each radical.\n\u221a72 = \u221a(36 \u00d7 2) = 6\u221a2.\n\u221a32 = \u221a(16 \u00d7 2) = 4\u221a2.\n\u221a18 = \u221a(9 \u00d7 2) = 3\u221a2.\nStep 2: Combine like terms: 6\u221a2 + 4\u221a2 \u2212 3\u221a2 = (6 + 4 \u2212 3)\u221a2 = 7\u221a2.\nAnswer: 7\u221a2."
    },
    {
      q: "Rationalize the denominator: 6 / (\u221a7 \u2212 \u221a3)",
      a: "Step 1: Multiply by the conjugate: 6(\u221a7 + \u221a3) / ((\u221a7 \u2212 \u221a3)(\u221a7 + \u221a3)).\nStep 2: Denominator uses difference of squares: (\u221a7)\u00b2 \u2212 (\u221a3)\u00b2 = 7 \u2212 3 = 4.\nStep 3: Numerator: 6\u221a7 + 6\u221a3.\nStep 4: Result: (6\u221a7 + 6\u221a3) / 4 = (3\u221a7 + 3\u221a3) / 2.\nAnswer: (3\u221a7 + 3\u221a3)/2 or equivalently 3(\u221a7 + \u221a3)/2."
    },
    {
      q: "If 2^x = 32 and 3^y = 81, what is 2^x \u00d7 3^y?",
      a: "Step 1: Solve for x: 2^x = 32 = 2\u2075, so x = 5.\nStep 2: Solve for y: 3^y = 81 = 3\u2074, so y = 4.\nStep 3: But the question asks for 2^x \u00d7 3^y = 32 \u00d7 81.\nStep 4: 32 \u00d7 81 = 32 \u00d7 80 + 32 \u00d7 1 = 2560 + 32 = 2592.\nAnswer: 2592."
    },
    {
      q: "Which is greater: 2\u00b3\u2070 or 3\u00b2\u2070?",
      a: "Step 1: Rewrite to compare with a common exponent.\n2\u00b3\u2070 = (2\u00b3)\u00b9\u2070 = 8\u00b9\u2070.\n3\u00b2\u2070 = (3\u00b2)\u00b9\u2070 = 9\u00b9\u2070.\nStep 2: Since 9 > 8 and both are raised to the same positive exponent 10, 9\u00b9\u2070 > 8\u00b9\u2070.\nAnswer: 3\u00b2\u2070 is greater."
    }
  ]
},
// --- 2.5 Functions ---
{
  id: "functions",
  title: "Functions",
  concepts: [
    "A function is a rule that assigns exactly one output to each input. Written as f(x), the x is the input and f(x) is the output. Example: If f(x) = 2x + 3, then f(4) = 2(4) + 3 = 11. The notation f(4) means 'substitute 4 for x in the rule.'",
    "The domain of a function is the set of all valid inputs (x-values). Common restrictions: (1) Denominators cannot be 0. (2) Expressions under an even root (\u221a) must be \u2265 0. Example: f(x) = 1/(x \u2212 3) has domain x \u2260 3. g(x) = \u221a(x \u2212 5) has domain x \u2265 5.",
    "The range of a function is the set of all possible outputs (y-values). Example: f(x) = x\u00b2 has range y \u2265 0 because squaring always gives a non-negative result. f(x) = |x| also has range y \u2265 0.",
    "Composite functions apply one function inside another. (f \u2218 g)(x) = f(g(x)) means 'first apply g to x, then apply f to the result.' Example: If f(x) = x\u00b2 and g(x) = x + 3, then f(g(2)) = f(5) = 25. Note: f(g(x)) \u2260 g(f(x)) in general\u2014order matters!",
    "To evaluate f(g(x)) algebraically: substitute the entire expression for g(x) wherever x appears in f. Example: f(x) = 2x + 1, g(x) = x\u00b2. Then f(g(x)) = 2(x\u00b2) + 1 = 2x\u00b2 + 1. And g(f(x)) = (2x + 1)\u00b2 = 4x\u00b2 + 4x + 1.",
    "GRE-style custom symbol/operation problems define a new operator using \u2660, \u25cb, #, @, etc. Example: 'For all numbers x and y, define x \u2660 y = x\u00b2 + 2xy. What is 3 \u2660 4?' Just substitute: 3\u00b2 + 2(3)(4) = 9 + 24 = 33. Treat the symbol like a function and follow the given rule exactly.",
    "Nested custom operations: If x \u2660 y = x\u00b2 \u2212 y, find 2 \u2660 (3 \u2660 1). First compute the inner operation: 3 \u2660 1 = 3\u00b2 \u2212 1 = 8. Then compute the outer: 2 \u2660 8 = 2\u00b2 \u2212 8 = 4 \u2212 8 = \u22124. Always work from the inside out.",
    "Function transformations: f(x) + k shifts up by k. f(x) \u2212 k shifts down. f(x + h) shifts left by h. f(x \u2212 h) shifts right. \u2212f(x) reflects over the x-axis. f(\u2212x) reflects over the y-axis. These are sometimes tested in GRE coordinate geometry problems.",
    "A function is even if f(\u2212x) = f(x) for all x (symmetric about the y-axis). Examples: x\u00b2, |x|, cos(x). A function is odd if f(\u2212x) = \u2212f(x) for all x (symmetric about the origin). Examples: x\u00b3, x. The GRE occasionally tests these properties."
  ],
  formulas: [
    "Composite: (f \u2218 g)(x) = f(g(x))",
    "Domain restriction (fraction): denominator \u2260 0",
    "Domain restriction (radical): expression under even root \u2265 0",
    "Even function: f(\u2212x) = f(x) | Odd function: f(\u2212x) = \u2212f(x)"
  ],
  tips: [
    "For GRE symbol/operation problems, just follow the definition mechanically. Don\u2019t overthink it\u2014plug in the values exactly as the rule states.",
    "When finding the domain, ask: 'What values of x would cause division by zero or a negative under an even root?' Exclude those values.",
    "For composite functions, always work inside-out. First evaluate the inner function, then plug that result into the outer function.",
    "If a problem asks for f(a + h) and f(x) = x\u00b2, replace EVERY x with (a + h): f(a + h) = (a + h)\u00b2 = a\u00b2 + 2ah + h\u00b2. Don\u2019t forget to expand.",
    "Custom operator problems sometimes test commutativity: is a \u2660 b = b \u2660 a? Check by swapping the variables in the definition. If x \u2660 y = x \u2212 y, then 5 \u2660 3 = 2 but 3 \u2660 5 = \u22122. They are NOT equal, so the operation is not commutative."
  ],
  questions: [
    {
      q: "If f(x) = 3x\u00b2 \u2212 2x + 1, find f(\u22122).",
      a: "Step 1: Substitute x = \u22122 into the function.\nStep 2: f(\u22122) = 3(\u22122)\u00b2 \u2212 2(\u22122) + 1.\nStep 3: = 3(4) \u2212 (\u22124) + 1.\nStep 4: = 12 + 4 + 1 = 17.\nAnswer: f(\u22122) = 17."
    },
    {
      q: "If f(x) = x + 2 and g(x) = x\u00b2 \u2212 1, find f(g(3)) and g(f(3)).",
      a: "Part 1 \u2014 f(g(3)):\nStep 1: g(3) = 3\u00b2 \u2212 1 = 9 \u2212 1 = 8.\nStep 2: f(8) = 8 + 2 = 10.\nSo f(g(3)) = 10.\n\nPart 2 \u2014 g(f(3)):\nStep 1: f(3) = 3 + 2 = 5.\nStep 2: g(5) = 5\u00b2 \u2212 1 = 25 \u2212 1 = 24.\nSo g(f(3)) = 24.\n\nNotice: f(g(3)) \u2260 g(f(3)). Order matters!"
    },
    {
      q: "For all positive numbers x and y, define x # y = (x + y) / (x \u2212 y) where x \u2260 y. What is 7 # 3?",
      a: "Step 1: Apply the definition with x = 7 and y = 3.\nStep 2: 7 # 3 = (7 + 3) / (7 \u2212 3) = 10 / 4 = 5/2.\nAnswer: 5/2 or 2.5."
    },
    {
      q: "Define x \u2660 y = x\u00b2 + xy \u2212 y\u00b2. Find (2 \u2660 3) \u2212 (3 \u2660 2).",
      a: "Step 1: Compute 2 \u2660 3 = 2\u00b2 + (2)(3) \u2212 3\u00b2 = 4 + 6 \u2212 9 = 1.\nStep 2: Compute 3 \u2660 2 = 3\u00b2 + (3)(2) \u2212 2\u00b2 = 9 + 6 \u2212 4 = 11.\nStep 3: (2 \u2660 3) \u2212 (3 \u2660 2) = 1 \u2212 11 = \u221210.\nAnswer: \u221210."
    },
    {
      q: "What is the domain of f(x) = \u221a(6 \u2212 2x)?",
      a: "Step 1: The expression under the square root must be \u2265 0.\nStep 2: 6 \u2212 2x \u2265 0.\nStep 3: \u22122x \u2265 \u22126.\nStep 4: Divide by \u22122 and flip the sign: x \u2264 3.\nAnswer: Domain is x \u2264 3 (or equivalently (\u2212\u221e, 3])."
    },
    {
      q: "If f(x) = 2x \u2212 1 and f(g(x)) = 6x + 5, find g(x).",
      a: "Step 1: We know f(g(x)) = 2(g(x)) \u2212 1.\nStep 2: Set this equal to 6x + 5: 2(g(x)) \u2212 1 = 6x + 5.\nStep 3: Add 1 to both sides: 2(g(x)) = 6x + 6.\nStep 4: Divide by 2: g(x) = 3x + 3.\nCheck: f(g(x)) = f(3x + 3) = 2(3x + 3) \u2212 1 = 6x + 6 \u2212 1 = 6x + 5. \u2713\nAnswer: g(x) = 3x + 3."
    }
  ]
},
// --- 2.6 Sequences ---
{
  id: "sequences",
  title: "Sequences",
  concepts: [
    "A sequence is an ordered list of numbers following a pattern. Each number is called a term. The first term is a\u2081, the second is a\u2082, and so on. Example: 2, 5, 8, 11, 14, ... is a sequence where each term is 3 more than the previous.",
    "An arithmetic sequence has a constant difference (d) between consecutive terms. The common difference d = a\u2082 \u2212 a\u2081. Example: 3, 7, 11, 15, 19, ... has d = 4. Each term is formed by adding d to the previous term.",
    "The nth term of an arithmetic sequence is a\u2099 = a\u2081 + (n \u2212 1)d. Example: In the sequence 5, 8, 11, 14, ..., a\u2081 = 5 and d = 3. The 20th term is a\u2082\u2080 = 5 + (20 \u2212 1)(3) = 5 + 57 = 62. Note: the formula uses (n \u2212 1), not n, because the first term has zero additions of d.",
    "The sum of the first n terms of an arithmetic sequence is S\u2099 = n/2 \u00d7 (a\u2081 + a\u2099) or equivalently S\u2099 = n/2 \u00d7 (2a\u2081 + (n \u2212 1)d). Example: Sum of the first 10 terms of 2, 5, 8, ... where a\u2081 = 2, d = 3: S\u2081\u2080 = 10/2 \u00d7 (2 + 29) = 5 \u00d7 31 = 155. (Here a\u2081\u2080 = 2 + 9(3) = 29.)",
    "A geometric sequence has a constant ratio (r) between consecutive terms. The common ratio r = a\u2082/a\u2081. Example: 3, 6, 12, 24, 48, ... has r = 2. Each term is found by multiplying the previous term by r.",
    "The nth term of a geometric sequence is a\u2099 = a\u2081 \u00d7 r^(n\u22121). Example: In the sequence 5, 15, 45, 135, ..., a\u2081 = 5 and r = 3. The 6th term is a\u2086 = 5 \u00d7 3\u2075 = 5 \u00d7 243 = 1215.",
    "The sum of the first n terms of a geometric sequence (r \u2260 1) is S\u2099 = a\u2081(1 \u2212 r\u207f) / (1 \u2212 r). Example: Sum of the first 5 terms of 2, 6, 18, 54, ... where a\u2081 = 2, r = 3: S\u2085 = 2(1 \u2212 3\u2075)/(1 \u2212 3) = 2(1 \u2212 243)/(\u22122) = 2(\u2212242)/(\u22122) = 242.",
    "Common series to memorize: Sum of first n positive integers = n(n + 1)/2. Example: 1 + 2 + 3 + ... + 100 = 100(101)/2 = 5050 (Gauss\u2019s formula). Sum of first n squares = n(n + 1)(2n + 1)/6.",
    "On the GRE, sequence problems often give a recursive rule like 'each term after the first is 3 more than twice the previous term.' If a\u2081 = 1, then a\u2082 = 2(1) + 3 = 5, a\u2083 = 2(5) + 3 = 13, a\u2084 = 2(13) + 3 = 29. Just follow the rule step by step.",
    "GRE tip: If a problem defines a sequence by a formula like a\u2099 = (\u22121)\u207f \u00d7 n, the sequence alternates signs: \u22121, 2, \u22123, 4, \u22125, 6, ... The (\u22121)\u207f part creates the alternating pattern. Odd-indexed terms are negative, even-indexed terms are positive."
  ],
  formulas: [
    "Arithmetic: a\u2099 = a\u2081 + (n \u2212 1)d | S\u2099 = n/2 \u00d7 (a\u2081 + a\u2099) = n/2 \u00d7 (2a\u2081 + (n \u2212 1)d)",
    "Geometric: a\u2099 = a\u2081 \u00d7 r^(n\u22121) | S\u2099 = a\u2081(1 \u2212 r\u207f) / (1 \u2212 r) for r \u2260 1",
    "Sum of 1 + 2 + 3 + ... + n = n(n + 1)/2",
    "Sum of 1\u00b2 + 2\u00b2 + 3\u00b2 + ... + n\u00b2 = n(n + 1)(2n + 1)/6"
  ],
  tips: [
    "To determine if a sequence is arithmetic, check whether the difference between consecutive terms is constant. To check geometric, see if the ratio is constant.",
    "The sum formula S\u2099 = n/2 \u00d7 (first + last) works because you\u2019re really computing the average of the first and last terms, then multiplying by the number of terms.",
    "For GRE problems that ask 'what is the sum of all even integers from 20 to 80,' recognize this as an arithmetic series: a\u2081 = 20, a\u2099 = 80, d = 2. First find n: 80 = 20 + (n\u22121)(2) \u2192 n = 31. Then S = 31/2 \u00d7 (20 + 80) = 31 \u00d7 50 = 1550.",
    "Watch for off-by-one errors: the number of integers from a to b inclusive is b \u2212 a + 1. The number of even integers from 2 to 100 inclusive is (100 \u2212 2)/2 + 1 = 50.",
    "If a geometric series has |r| < 1, the sum of an INFINITE geometric series converges to S = a\u2081/(1 \u2212 r). Example: 1 + 1/2 + 1/4 + 1/8 + ... = 1/(1 \u2212 1/2) = 2. This occasionally appears on the GRE."
  ],
  questions: [
    {
      q: "In an arithmetic sequence, the 3rd term is 14 and the 7th term is 30. Find the first term and the common difference.",
      a: "Step 1: Use a\u2099 = a\u2081 + (n \u2212 1)d.\na\u2083 = a\u2081 + 2d = 14 ... (i)\na\u2087 = a\u2081 + 6d = 30 ... (ii)\nStep 2: Subtract (i) from (ii): 4d = 16 \u2192 d = 4.\nStep 3: Substitute d = 4 into (i): a\u2081 + 8 = 14 \u2192 a\u2081 = 6.\nAnswer: First term = 6, common difference = 4."
    },
    {
      q: "Find the sum of all integers from 1 to 200.",
      a: "Step 1: Use Gauss\u2019s formula: S = n(n + 1)/2.\nStep 2: S = 200(201)/2.\nStep 3: S = 200 \u00d7 201/2 = 100 \u00d7 201 = 20100.\nAnswer: 20,100."
    },
    {
      q: "The first term of a geometric sequence is 4 and the common ratio is 3. What is the sum of the first 6 terms?",
      a: "Step 1: Use S\u2099 = a\u2081(1 \u2212 r\u207f)/(1 \u2212 r) with a\u2081 = 4, r = 3, n = 6.\nStep 2: S\u2086 = 4(1 \u2212 3\u2076)/(1 \u2212 3).\nStep 3: 3\u2076 = 729.\nStep 4: S\u2086 = 4(1 \u2212 729)/(\u22122) = 4(\u2212728)/(\u22122).\nStep 5: S\u2086 = 4 \u00d7 364 = 1456.\nAnswer: 1456."
    },
    {
      q: "What is the sum of all odd integers from 1 to 99?",
      a: "Step 1: Odd integers from 1 to 99 form an arithmetic sequence: 1, 3, 5, ..., 99.\nStep 2: Find n: 99 = 1 + (n \u2212 1)(2) \u2192 98 = 2(n \u2212 1) \u2192 n \u2212 1 = 49 \u2192 n = 50.\nStep 3: Sum = n/2 \u00d7 (first + last) = 50/2 \u00d7 (1 + 99) = 25 \u00d7 100 = 2500.\nAnswer: 2500."
    },
    {
      q: "A sequence is defined by a\u2081 = 2 and a\u2099 = 3a\u2099\u208b\u2081 \u2212 1 for n \u2265 2. Find a\u2084.",
      a: "Step 1: a\u2081 = 2 (given).\nStep 2: a\u2082 = 3(a\u2081) \u2212 1 = 3(2) \u2212 1 = 5.\nStep 3: a\u2083 = 3(a\u2082) \u2212 1 = 3(5) \u2212 1 = 14.\nStep 4: a\u2084 = 3(a\u2083) \u2212 1 = 3(14) \u2212 1 = 41.\nAnswer: a\u2084 = 41."
    },
    {
      q: "An infinite geometric series has first term 12 and sum 18. What is the common ratio?",
      a: "Step 1: Use the infinite sum formula S = a\u2081/(1 \u2212 r).\nStep 2: 18 = 12/(1 \u2212 r).\nStep 3: Multiply both sides by (1 \u2212 r): 18(1 \u2212 r) = 12.\nStep 4: 18 \u2212 18r = 12.\nStep 5: \u221218r = \u22126 \u2192 r = 1/3.\nCheck: 12/(1 \u2212 1/3) = 12/(2/3) = 18. \u2713\nAnswer: r = 1/3."
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
      // --- 3.1 Lines & Angles ---
{
  id: "lines-angles",
  title: "Lines & Angles",
  concepts: [
    "A straight line measures 180\u00b0. If two or more angles sit on a straight line, they must add up to 180\u00b0. Example: if one angle is 110\u00b0, the adjacent angle on the same line is 180\u00b0 \u2212 110\u00b0 = 70\u00b0. These are called supplementary angles.",
    "A full rotation around a point is 360\u00b0. If several angles meet at a single point, all of them together add up to 360\u00b0. Example: four angles meeting at a point measure 90\u00b0, 120\u00b0, 85\u00b0, and x\u00b0. Then x = 360 \u2212 90 \u2212 120 \u2212 85 = 65\u00b0.",
    "Vertical angles are the pairs of opposite angles formed when two lines cross. Vertical angles are always equal. Example: two lines intersect and one angle is 130\u00b0. The angle directly across from it is also 130\u00b0, and the two side angles are each 180\u00b0 \u2212 130\u00b0 = 50\u00b0.",
    "Complementary angles add up to 90\u00b0. Example: if angle A = 35\u00b0, its complement is 90\u00b0 \u2212 35\u00b0 = 55\u00b0. Supplementary angles add up to 180\u00b0. Example: if angle B = 72\u00b0, its supplement is 180\u00b0 \u2212 72\u00b0 = 108\u00b0. Remember: 'C' in complementary comes before 'S' in supplementary, just as 90 comes before 180.",
    "When a transversal crosses two parallel lines, it creates 8 angles. Corresponding angles (same position at each intersection) are equal. Example: the top-right angle at the first intersection equals the top-right angle at the second intersection.",
    "Alternate interior angles are on opposite sides of the transversal, between the parallel lines, and they are equal. Example: if one alternate interior angle is 65\u00b0, the other is also 65\u00b0. Alternate exterior angles (outside the parallel lines, opposite sides) are also equal.",
    "Co-interior angles (also called same-side interior or consecutive interior angles) are on the same side of the transversal, between the parallel lines. They are supplementary\u2014they add up to 180\u00b0. Example: if one co-interior angle is 110\u00b0, the other is 70\u00b0.",
    "The sum of interior angles of any polygon with n sides is (n \u2212 2) \u00d7 180\u00b0. Triangle: (3 \u2212 2) \u00d7 180\u00b0 = 180\u00b0. Quadrilateral: (4 \u2212 2) \u00d7 180\u00b0 = 360\u00b0. Pentagon: (5 \u2212 2) \u00d7 180\u00b0 = 540\u00b0. Hexagon: (6 \u2212 2) \u00d7 180\u00b0 = 720\u00b0.",
    "For a regular polygon (all sides and angles equal), each interior angle = (n \u2212 2) \u00d7 180\u00b0 \u00f7 n. Example: a regular hexagon has each interior angle = (6 \u2212 2) \u00d7 180\u00b0 \u00f7 6 = 720\u00b0 \u00f7 6 = 120\u00b0. Each exterior angle of a regular polygon = 360\u00b0 \u00f7 n. For a hexagon: 360\u00b0 \u00f7 6 = 60\u00b0.",
    "The sum of exterior angles of any convex polygon is always 360\u00b0, no matter how many sides it has. This is a useful shortcut: if a regular polygon has an exterior angle of 40\u00b0, then n = 360\u00b0 \u00f7 40\u00b0 = 9 sides."
  ],
  formulas: [
    "Supplementary angles: A + B = 180\u00b0",
    "Complementary angles: A + B = 90\u00b0",
    "Interior angle sum of n-sided polygon: (n \u2212 2) \u00d7 180\u00b0",
    "Each interior angle of a regular n-gon: (n \u2212 2) \u00d7 180\u00b0 \u00f7 n"
  ],
  tips: [
    "When you see parallel lines cut by a transversal, immediately mark all equal angles. There are really only two distinct angle measures, and they are supplementary (add to 180\u00b0).",
    "Vertical angles are always equal\u2014this is one of the most tested angle facts on the GRE. Spot the X-shape formed by intersecting lines.",
    "If a problem asks for the number of sides given an interior angle, use the exterior angle instead: exterior = 180\u00b0 \u2212 interior, then n = 360\u00b0 \u00f7 exterior. It\u2019s faster.",
    "For any angle problem, write down every equation you can (angles on a line = 180\u00b0, vertical angles equal, etc.). Often one extra equation reveals the answer.",
    "The exterior angle of a triangle equals the sum of the two non-adjacent interior angles. Example: if two interior angles are 50\u00b0 and 60\u00b0, the exterior angle at the third vertex is 110\u00b0."
  ],
  questions: [
    {
      q: "Two lines intersect. One of the angles formed is 3x + 10. The angle adjacent to it is 2x + 20. Find x.",
      a: "Adjacent angles on a straight line are supplementary.\n(3x + 10) + (2x + 20) = 180\n5x + 30 = 180\n5x = 150\nx = 30.\nThe angles are 3(30) + 10 = 100\u00b0 and 2(30) + 20 = 80\u00b0. Check: 100 + 80 = 180 \u2713"
    },
    {
      q: "A transversal crosses two parallel lines. One of the alternate interior angles is (4x \u2212 5)\u00b0 and the other is (3x + 15)\u00b0. Find x and the angle measure.",
      a: "Alternate interior angles are equal when lines are parallel.\n4x \u2212 5 = 3x + 15\n4x \u2212 3x = 15 + 5\nx = 20.\nAngle = 4(20) \u2212 5 = 75\u00b0.\nBoth alternate interior angles measure 75\u00b0."
    },
    {
      q: "What is the sum of the interior angles of an octagon (8 sides)?",
      a: "Use the formula: (n \u2212 2) \u00d7 180\u00b0.\nn = 8, so (8 \u2212 2) \u00d7 180\u00b0 = 6 \u00d7 180\u00b0 = 1080\u00b0.\nThe sum of the interior angles of an octagon is 1080\u00b0."
    },
    {
      q: "Each interior angle of a regular polygon is 144\u00b0. How many sides does it have?",
      a: "Each exterior angle = 180\u00b0 \u2212 144\u00b0 = 36\u00b0.\nNumber of sides = 360\u00b0 \u00f7 36\u00b0 = 10.\nThe polygon has 10 sides (it is a regular decagon)."
    },
    {
      q: "Three angles meet at a point. Two of them are 95\u00b0 and 140\u00b0. What is the third angle?",
      a: "Angles around a point sum to 360\u00b0.\nThird angle = 360\u00b0 \u2212 95\u00b0 \u2212 140\u00b0 = 125\u00b0."
    },
    {
      q: "In a triangle, one exterior angle measures 130\u00b0. The two non-adjacent interior angles are x\u00b0 and (x + 30)\u00b0. Find x.",
      a: "An exterior angle of a triangle equals the sum of the two non-adjacent interior angles.\nx + (x + 30) = 130\n2x + 30 = 130\n2x = 100\nx = 50.\nThe two interior angles are 50\u00b0 and 80\u00b0. The third interior angle = 180\u00b0 \u2212 130\u00b0 = 50\u00b0."
    }
  ]
},
// --- 3.2 Triangles ---
{
  id: "triangles",
  title: "Triangles",
  concepts: [
    "The three interior angles of any triangle always add up to exactly 180\u00b0. Example: if two angles are 45\u00b0 and 65\u00b0, the third is 180\u00b0 \u2212 45\u00b0 \u2212 65\u00b0 = 70\u00b0. This is one of the most fundamental facts in geometry and is used constantly on the GRE.",
    "The Pythagorean Theorem applies only to right triangles: a\u00b2 + b\u00b2 = c\u00b2, where c is the hypotenuse (the longest side, opposite the 90\u00b0 angle) and a, b are the two legs. Example: if the legs are 6 and 8, then c\u00b2 = 36 + 64 = 100, so c = 10.",
    "Common Pythagorean triples to memorize: 3-4-5, 5-12-13, 8-15-17, 7-24-25. Their multiples also work: 3-4-5 scales to 6-8-10, 9-12-15, 12-16-20, and so on. 5-12-13 scales to 10-24-26. Recognizing these saves huge time on the GRE because you skip the calculation entirely.",
    "A 45-45-90 triangle (isosceles right triangle) has sides in the ratio 1 : 1 : \u221a2. If each leg is s, the hypotenuse is s\u221a2. Example: legs = 5, hypotenuse = 5\u221a2. Conversely, if the hypotenuse is 10, each leg = 10 \u00f7 \u221a2 = 10\u221a2 \u00f7 2 = 5\u221a2.",
    "A 30-60-90 triangle has sides in the ratio 1 : \u221a3 : 2. The side opposite 30\u00b0 is the shortest (x), opposite 60\u00b0 is x\u221a3, and the hypotenuse (opposite 90\u00b0) is 2x. Example: if the short side is 4, then the other sides are 4\u221a3 and 8. If the hypotenuse is 12, the short side is 6 and the middle side is 6\u221a3.",
    "Similar triangles have the same shape but possibly different sizes. Their corresponding angles are equal and their corresponding sides are in proportion. Example: triangle ABC ~ triangle DEF with sides 3, 4, 5 and 6, 8, 10. The scale factor is 2. If you know three sides of one triangle and two sides of the other, set up a proportion to find the missing side.",
    "The Triangle Inequality Theorem states: the sum of any two sides must be greater than the third side. For sides a, b, c: a + b > c, a + c > b, and b + c > a. Example: can a triangle have sides 3, 5, 9? Check: 3 + 5 = 8, which is NOT greater than 9, so no\u2014this triangle is impossible.",
    "Area of a triangle = \u00bd \u00d7 base \u00d7 height. The height must be perpendicular to the base. Example: base = 10, height = 6, area = \u00bd \u00d7 10 \u00d7 6 = 30. Any side can serve as the base; just use the corresponding perpendicular height.",
    "An equilateral triangle has all three sides equal and all three angles = 60\u00b0. Its area = (\u221a3 / 4) \u00d7 s\u00b2, where s is the side length. Example: side = 6, area = (\u221a3 / 4) \u00d7 36 = 9\u221a3 \u2248 15.59. Its height = (s\u221a3) / 2.",
    "An isosceles triangle has two equal sides and two equal base angles. The altitude from the apex to the base bisects both the base and the apex angle, creating two congruent right triangles. Example: isosceles triangle with equal sides 10 and base 12. The altitude splits the base into two segments of 6. Height = \u221a(10\u00b2 \u2212 6\u00b2) = \u221a(100 \u2212 36) = \u221a64 = 8."
  ],
  formulas: [
    "Angle sum: A + B + C = 180\u00b0",
    "Pythagorean Theorem: a\u00b2 + b\u00b2 = c\u00b2 (right triangles only)",
    "Area = \u00bd \u00d7 base \u00d7 height",
    "Equilateral triangle area = (\u221a3 / 4) \u00d7 s\u00b2"
  ],
  tips: [
    "Memorize the common Pythagorean triples (3-4-5, 5-12-13, 8-15-17) and their multiples. When you see a right triangle on the GRE, check for a triple before calculating.",
    "For 30-60-90 triangles, the hypotenuse is always exactly twice the shortest side. If you see a right triangle with a hypotenuse that is double one leg, it is a 30-60-90 triangle.",
    "For 45-45-90 triangles, multiply a leg by \u221a2 to get the hypotenuse, or divide the hypotenuse by \u221a2 to get a leg. These appear frequently when a square is cut diagonally.",
    "When checking whether three lengths can form a triangle, you only need to check that the sum of the two shorter sides is greater than the longest side. If that works, the other two inequalities are automatically satisfied.",
    "If two triangles are similar, the ratio of their areas equals the square of the ratio of their corresponding sides. Example: if sides are in ratio 2:3, areas are in ratio 4:9."
  ],
  questions: [
    {
      q: "A right triangle has legs of length 9 and 12. What is the hypotenuse?",
      a: "Use the Pythagorean Theorem: a\u00b2 + b\u00b2 = c\u00b2.\n9\u00b2 + 12\u00b2 = c\u00b2\n81 + 144 = c\u00b2\n225 = c\u00b2\nc = 15.\nShortcut: 9-12-15 is a multiple of the 3-4-5 triple (multiply each by 3). The hypotenuse is 15."
    },
    {
      q: "In a 30-60-90 triangle, the side opposite the 60\u00b0 angle is 5\u221a3. Find the other two sides.",
      a: "In a 30-60-90 triangle, sides are x : x\u221a3 : 2x.\nThe side opposite 60\u00b0 = x\u221a3 = 5\u221a3, so x = 5.\nSide opposite 30\u00b0 (shortest side) = x = 5.\nHypotenuse = 2x = 10.\nThe sides are 5, 5\u221a3, and 10."
    },
    {
      q: "Triangle ABC is similar to triangle DEF. AB = 4, BC = 6, AC = 8. If DE = 10, find EF and DF.",
      a: "Corresponding sides are proportional.\nAB corresponds to DE: scale factor = DE / AB = 10 / 4 = 2.5.\nEF = BC \u00d7 2.5 = 6 \u00d7 2.5 = 15.\nDF = AC \u00d7 2.5 = 8 \u00d7 2.5 = 20.\nThe sides of triangle DEF are 10, 15, and 20."
    },
    {
      q: "Can a triangle have sides of length 7, 10, and 18?",
      a: "Apply the Triangle Inequality: the sum of the two shorter sides must be greater than the longest side.\n7 + 10 = 17.\n17 is NOT greater than 18.\nSo no, these lengths cannot form a triangle."
    },
    {
      q: "A 45-45-90 triangle has a hypotenuse of 8\u221a2. What is the area of the triangle?",
      a: "In a 45-45-90 triangle, hypotenuse = leg \u00d7 \u221a2.\nleg = 8\u221a2 \u00f7 \u221a2 = 8.\nBoth legs are 8.\nArea = \u00bd \u00d7 base \u00d7 height = \u00bd \u00d7 8 \u00d7 8 = 32."
    },
    {
      q: "An equilateral triangle has a perimeter of 24. What is its area?",
      a: "Perimeter = 3s = 24, so s = 8.\nArea of equilateral triangle = (\u221a3 / 4) \u00d7 s\u00b2\n= (\u221a3 / 4) \u00d7 64\n= 16\u221a3\n\u2248 27.71.\nThe area is 16\u221a3."
    }
  ]
},
// --- 3.3 Quadrilaterals & Polygons ---
{
  id: "quads-polygons",
  title: "Quadrilaterals & Polygons",
  concepts: [
    "A rectangle has four right angles (each 90\u00b0). Opposite sides are equal and parallel. Area = length \u00d7 width. Perimeter = 2(length + width). Example: a rectangle with length 8 and width 5 has area = 40 and perimeter = 26. The diagonal of a rectangle = \u221a(l\u00b2 + w\u00b2) by the Pythagorean Theorem.",
    "A square is a special rectangle where all four sides are equal. Area = s\u00b2. Perimeter = 4s. The diagonal of a square = s\u221a2. Example: a square with side 6 has area = 36, perimeter = 24, and diagonal = 6\u221a2 \u2248 8.49. Every square is a rectangle, rhombus, and parallelogram.",
    "A parallelogram has two pairs of parallel sides. Opposite sides are equal, and opposite angles are equal. Consecutive angles are supplementary (add to 180\u00b0). Area = base \u00d7 height (the height is the perpendicular distance between the parallel sides, NOT the slanted side). Example: base = 10, height = 7, area = 70.",
    "A rhombus is a parallelogram with all four sides equal. Its diagonals bisect each other at right angles. Area = \u00bd \u00d7 d\u2081 \u00d7 d\u2082, where d\u2081 and d\u2082 are the diagonals. Example: diagonals of 6 and 10, area = \u00bd \u00d7 6 \u00d7 10 = 30. Also, area = base \u00d7 height works for a rhombus.",
    "A trapezoid (called trapezium in British English) has exactly one pair of parallel sides, called the bases. Area = \u00bd \u00d7 (base\u2081 + base\u2082) \u00d7 height. Example: parallel sides (bases) are 6 and 10, height is 4. Area = \u00bd \u00d7 (6 + 10) \u00d7 4 = \u00bd \u00d7 16 \u00d7 4 = 32.",
    "An isosceles trapezoid has equal non-parallel sides (legs). Its base angles are equal, and its diagonals are equal in length. This is a common shape on the GRE\u2014look for symmetry to simplify calculations.",
    "The sum of interior angles of any quadrilateral is 360\u00b0. This follows from the general polygon formula: (4 \u2212 2) \u00d7 180\u00b0 = 360\u00b0. Example: if three angles of a quadrilateral are 80\u00b0, 100\u00b0, and 90\u00b0, the fourth angle = 360\u00b0 \u2212 80\u00b0 \u2212 100\u00b0 \u2212 90\u00b0 = 90\u00b0.",
    "For any regular polygon with n sides: each interior angle = (n \u2212 2) \u00d7 180\u00b0 \u00f7 n, and each exterior angle = 360\u00b0 \u00f7 n. Example: a regular pentagon (n = 5) has interior angles of (3 \u00d7 180\u00b0) \u00f7 5 = 108\u00b0 each and exterior angles of 72\u00b0 each.",
    "The number of diagonals in a polygon with n sides = n(n \u2212 3) / 2. Example: a hexagon (n = 6) has 6(6 \u2212 3) / 2 = 6 \u00d7 3 / 2 = 9 diagonals. A quadrilateral has 4(1) / 2 = 2 diagonals.",
    "When a parallelogram\u2019s diagonals bisect each other, each diagonal cuts the other into two equal halves. This is true for all parallelograms. In a rectangle, the diagonals are also equal in length. In a rhombus, the diagonals are perpendicular. In a square, the diagonals are both equal and perpendicular."
  ],
  formulas: [
    "Rectangle: Area = l \u00d7 w, Perimeter = 2(l + w), Diagonal = \u221a(l\u00b2 + w\u00b2)",
    "Square: Area = s\u00b2, Perimeter = 4s, Diagonal = s\u221a2",
    "Parallelogram: Area = base \u00d7 height",
    "Trapezoid: Area = \u00bd \u00d7 (b\u2081 + b\u2082) \u00d7 height"
  ],
  tips: [
    "The height of a parallelogram or trapezoid is always the perpendicular distance between the parallel sides\u2014never the slanted side. If the GRE gives you a slanted side, you may need the Pythagorean Theorem to find the actual height.",
    "A square is simultaneously a rectangle, a rhombus, and a parallelogram. If a GRE question says a shape is a square, you can use any formula from those categories.",
    "For irregular quadrilaterals, try dividing the shape into triangles. The total area equals the sum of the triangle areas. This works for any polygon.",
    "If you know the diagonals of a rhombus, use Area = \u00bd \u00d7 d\u2081 \u00d7 d\u2082. This is often faster than base \u00d7 height when diagonal lengths are given directly.",
    "Remember: the angles of any quadrilateral add to 360\u00b0. This is a quick check\u2014if your calculated angles don\u2019t sum to 360\u00b0, you\u2019ve made an error somewhere."
  ],
  questions: [
    {
      q: "A rectangle has a length of 12 and a diagonal of 13. What is its area?",
      a: "Use the Pythagorean Theorem to find the width.\ndiagonal\u00b2 = length\u00b2 + width\u00b2\n13\u00b2 = 12\u00b2 + w\u00b2\n169 = 144 + w\u00b2\nw\u00b2 = 25\nw = 5.\nArea = 12 \u00d7 5 = 60.\n(Note: 5-12-13 is a Pythagorean triple!)"
    },
    {
      q: "A parallelogram has a base of 14 and a height of 9. What is its area?",
      a: "Area of a parallelogram = base \u00d7 height.\nArea = 14 \u00d7 9 = 126."
    },
    {
      q: "A trapezoid has parallel sides of length 8 and 14, and a height of 6. What is its area?",
      a: "Area = \u00bd \u00d7 (b\u2081 + b\u2082) \u00d7 height\n= \u00bd \u00d7 (8 + 14) \u00d7 6\n= \u00bd \u00d7 22 \u00d7 6\n= \u00bd \u00d7 132\n= 66."
    },
    {
      q: "A rhombus has diagonals of length 10 and 24. What is the length of each side?",
      a: "The diagonals of a rhombus bisect each other at right angles.\nHalf-diagonals: 10/2 = 5 and 24/2 = 12.\nEach side is the hypotenuse of a right triangle with legs 5 and 12.\nside = \u221a(5\u00b2 + 12\u00b2) = \u221a(25 + 144) = \u221a169 = 13.\n(5-12-13 Pythagorean triple!)\nEach side of the rhombus is 13."
    },
    {
      q: "The interior angles of a quadrilateral are x\u00b0, 2x\u00b0, 3x\u00b0, and 4x\u00b0. Find the value of x and each angle.",
      a: "The sum of interior angles of a quadrilateral = 360\u00b0.\nx + 2x + 3x + 4x = 360\n10x = 360\nx = 36.\nThe angles are: 36\u00b0, 72\u00b0, 108\u00b0, and 144\u00b0.\nCheck: 36 + 72 + 108 + 144 = 360 \u2713"
    },
    {
      q: "A square has a diagonal of 10. What is the area of the square?",
      a: "For a square, diagonal = s\u221a2.\ns\u221a2 = 10\ns = 10 / \u221a2 = 10\u221a2 / 2 = 5\u221a2.\nArea = s\u00b2 = (5\u221a2)\u00b2 = 25 \u00d7 2 = 50.\nAlternative shortcut: Area = diagonal\u00b2 / 2 = 100 / 2 = 50."
    }
  ]
},
// --- 3.4 Circles ---
{
  id: "circles",
  title: "Circles",
  concepts: [
    "The circumference of a circle is the distance around it. C = 2\u03c0r = \u03c0d, where r is the radius and d is the diameter. Example: a circle with radius 7 has circumference = 2\u03c0(7) = 14\u03c0 \u2248 43.98. Remember: diameter = 2 \u00d7 radius, so d = 14.",
    "The area of a circle is A = \u03c0r\u00b2. Example: radius = 5, area = \u03c0(25) = 25\u03c0 \u2248 78.54. If the diameter is 12, the radius is 6, and the area = \u03c0(36) = 36\u03c0. Always make sure you\u2019re using the radius (not the diameter) in the formula.",
    "An arc is a portion of the circumference. Arc length = (\u03b8 / 360) \u00d7 2\u03c0r, where \u03b8 is the central angle in degrees. Example: central angle = 90\u00b0, radius = 10. Arc length = (90/360) \u00d7 2\u03c0(10) = (1/4) \u00d7 20\u03c0 = 5\u03c0.",
    "A sector is a \u2018pizza slice\u2019 region bounded by two radii and an arc. Sector area = (\u03b8 / 360) \u00d7 \u03c0r\u00b2. Example: central angle = 60\u00b0, radius = 9. Sector area = (60/360) \u00d7 \u03c0(81) = (1/6) \u00d7 81\u03c0 = 13.5\u03c0.",
    "A central angle is an angle whose vertex is at the center of the circle. It equals the arc it intercepts. Example: a central angle of 120\u00b0 intercepts an arc of 120\u00b0. The fraction of the circle it represents is 120/360 = 1/3.",
    "An inscribed angle is an angle whose vertex is on the circle. An inscribed angle is exactly half the central angle that intercepts the same arc. Example: if a central angle is 80\u00b0, an inscribed angle intercepting the same arc is 40\u00b0. Conversely, if an inscribed angle is 35\u00b0, the intercepted arc is 70\u00b0.",
    "An inscribed angle that intercepts a semicircle (a diameter) is always 90\u00b0. This is Thales\u2019 theorem. So if you see a triangle inscribed in a circle with one side as the diameter, the angle opposite the diameter is a right angle.",
    "A tangent line touches the circle at exactly one point and is perpendicular (90\u00b0) to the radius at that point. Example: if a tangent meets a radius at point P, the angle between them is 90\u00b0. Two tangent segments drawn from the same external point are equal in length.",
    "A chord is a line segment with both endpoints on the circle. The diameter is the longest possible chord. A perpendicular from the center to a chord bisects the chord. Example: a chord is 24 units long, and the radius is 13. Distance from center to chord = \u221a(13\u00b2 \u2212 12\u00b2) = \u221a(169 \u2212 144) = \u221a25 = 5."
  ],
  formulas: [
    "Circumference: C = 2\u03c0r = \u03c0d",
    "Area: A = \u03c0r\u00b2",
    "Arc length = (\u03b8 / 360) \u00d7 2\u03c0r",
    "Sector area = (\u03b8 / 360) \u00d7 \u03c0r\u00b2"
  ],
  tips: [
    "Always double-check whether a problem gives you the radius or the diameter. Mixing these up is the most common circle mistake on the GRE.",
    "The inscribed angle is always half the central angle for the same arc. If you see \u2018inscribed angle\u2019 in a problem, immediately think \u2018half.\u2019",
    "For arc and sector problems, find what fraction of the full circle you\u2019re dealing with: \u03b8/360. Then multiply that fraction by the full circumference (for arc length) or full area (for sector area).",
    "When a tangent and a radius meet, that\u2019s a 90\u00b0 angle. This often creates a right triangle\u2014use the Pythagorean Theorem.",
    "Two tangent segments from the same external point are equal. This fact often appears in GRE problems combined with triangle properties."
  ],
  questions: [
    {
      q: "A circle has a radius of 6. What is the area of a sector with a central angle of 150\u00b0?",
      a: "Sector area = (\u03b8 / 360) \u00d7 \u03c0r\u00b2\n= (150 / 360) \u00d7 \u03c0(6)\u00b2\n= (5/12) \u00d7 36\u03c0\n= (5/12) \u00d7 36\u03c0\n= 15\u03c0\n\u2248 47.12."
    },
    {
      q: "An inscribed angle in a circle is 55\u00b0. What is the measure of the central angle that intercepts the same arc?",
      a: "The central angle is always twice the inscribed angle intercepting the same arc.\nCentral angle = 2 \u00d7 55\u00b0 = 110\u00b0."
    },
    {
      q: "A circle has a circumference of 20\u03c0. What is the area of the circle?",
      a: "First find the radius from the circumference.\nC = 2\u03c0r\n20\u03c0 = 2\u03c0r\nr = 10.\nArea = \u03c0r\u00b2 = \u03c0(10)\u00b2 = 100\u03c0 \u2248 314.16."
    },
    {
      q: "A tangent segment from an external point to a circle is 8 units long, and the distance from the external point to the center is 10. What is the radius?",
      a: "The tangent is perpendicular to the radius at the point of tangency, forming a right triangle.\nLet r = radius.\nr\u00b2 + 8\u00b2 = 10\u00b2\nr\u00b2 + 64 = 100\nr\u00b2 = 36\nr = 6.\n(This is a 6-8-10 right triangle, a multiple of the 3-4-5 triple.)"
    },
    {
      q: "An arc of a circle with radius 12 has a length of 4\u03c0. What is the central angle of that arc?",
      a: "Arc length = (\u03b8 / 360) \u00d7 2\u03c0r.\n4\u03c0 = (\u03b8 / 360) \u00d7 2\u03c0(12)\n4\u03c0 = (\u03b8 / 360) \u00d7 24\u03c0\nDivide both sides by 24\u03c0: 4/24 = \u03b8/360\n1/6 = \u03b8/360\n\u03b8 = 360/6 = 60\u00b0."
    },
    {
      q: "A chord of length 16 is 6 units from the center of a circle. What is the radius?",
      a: "A perpendicular from the center to a chord bisects the chord.\nHalf the chord = 16/2 = 8.\nThe radius, half-chord, and distance from center form a right triangle.\nr\u00b2 = 8\u00b2 + 6\u00b2 = 64 + 36 = 100\nr = 10."
    }
  ]
},
// --- 3.5 3D Geometry ---
{
  id: "3d-geometry",
  title: "3D Geometry",
  concepts: [
    "A rectangular box (rectangular solid) has length l, width w, and height h. Volume = l \u00d7 w \u00d7 h. Surface area = 2(lw + lh + wh). Example: a box with dimensions 4 \u00d7 5 \u00d7 6 has volume = 120 and surface area = 2(20 + 24 + 30) = 2(74) = 148.",
    "The space diagonal of a rectangular box (the diagonal that goes through the interior from one corner to the opposite corner) = \u221a(l\u00b2 + w\u00b2 + h\u00b2). Example: a box with dimensions 3 \u00d7 4 \u00d7 12 has space diagonal = \u221a(9 + 16 + 144) = \u221a169 = 13.",
    "A cube is a special rectangular box where all edges are equal: l = w = h = s. Volume = s\u00b3. Surface area = 6s\u00b2 (six identical square faces). Space diagonal = s\u221a3. Example: a cube with side 5 has volume = 125, surface area = 150, and diagonal = 5\u221a3.",
    "A cylinder has a circular base with radius r and height h. Volume = \u03c0r\u00b2h (base area times height). Lateral (side) surface area = 2\u03c0rh (imagine unrolling the side into a rectangle). Total surface area = 2\u03c0rh + 2\u03c0r\u00b2 (side plus two circular bases). Example: r = 3, h = 10. Volume = \u03c0(9)(10) = 90\u03c0. Lateral SA = 2\u03c0(3)(10) = 60\u03c0. Total SA = 60\u03c0 + 18\u03c0 = 78\u03c0.",
    "A sphere has radius r. Volume = (4/3)\u03c0r\u00b3. Surface area = 4\u03c0r\u00b2. Example: r = 6. Volume = (4/3)\u03c0(216) = 288\u03c0. Surface area = 4\u03c0(36) = 144\u03c0. Note that sphere problems on the GRE are less common but do appear.",
    "A cone has a circular base with radius r and height h. Volume = (1/3)\u03c0r\u00b2h (one-third of the corresponding cylinder). Lateral surface area = \u03c0rl, where l is the slant height = \u221a(r\u00b2 + h\u00b2). Example: r = 3, h = 4. Slant height = \u221a(9 + 16) = 5. Volume = (1/3)\u03c0(9)(4) = 12\u03c0. Lateral SA = \u03c0(3)(5) = 15\u03c0.",
    "When you scale all dimensions of a 3D shape by a factor of k, the surface area scales by k\u00b2 and the volume scales by k\u00b3. Example: if you double every dimension (k = 2), the surface area becomes 4 times as large and the volume becomes 8 times as large.",
    "A common GRE question involves filling or emptying containers. Volume represents capacity. Example: a cylindrical tank with r = 5 and h = 20 holds \u03c0(25)(20) = 500\u03c0 cubic units of water. If water flows in at 10\u03c0 cubic units per minute, it takes 500\u03c0 / 10\u03c0 = 50 minutes to fill.",
    "To find how many smaller objects fit inside a larger object, divide the volume of the larger object by the volume of the smaller object (assuming perfect packing or the problem specifies exact fit). Example: how many cubes with side 2 fit in a box that is 6 \u00d7 8 \u00d7 4? By volume: 192 / 8 = 24 cubes. Verify by dimensions: 3 \u00d7 4 \u00d7 2 = 24 cubes."
  ],
  formulas: [
    "Rectangular box: V = lwh, SA = 2(lw + lh + wh), Space diagonal = \u221a(l\u00b2 + w\u00b2 + h\u00b2)",
    "Cube: V = s\u00b3, SA = 6s\u00b2, Space diagonal = s\u221a3",
    "Cylinder: V = \u03c0r\u00b2h, SA = 2\u03c0rh + 2\u03c0r\u00b2",
    "Sphere: V = (4/3)\u03c0r\u00b3, SA = 4\u03c0r\u00b2"
  ],
  tips: [
    "The volume of a cone is exactly 1/3 of the cylinder with the same base and height. Similarly, the volume of a pyramid is 1/3 of the prism with the same base and height. This 1/3 factor is worth memorizing.",
    "When dimensions scale by factor k, areas scale by k\u00b2 and volumes scale by k\u00b3. This is a very common GRE concept. If a sphere\u2019s radius triples, its volume increases by 3\u00b3 = 27 times.",
    "For surface area problems, draw or visualize each face separately. Count carefully\u2014a rectangular box has 3 pairs of identical faces; a cylinder has a side rectangle plus two circles.",
    "When a problem asks for the amount of material to cover a shape, it\u2019s asking for surface area. When it asks how much a shape holds, it\u2019s asking for volume.",
    "The space diagonal of a cube (s\u221a3) appears when the GRE asks for the longest line segment that fits inside a cube. Always check if a problem is asking for a face diagonal (s\u221a2) vs. a space diagonal (s\u221a3)."
  ],
  questions: [
    {
      q: "A rectangular box has dimensions 3 \u00d7 4 \u00d7 5. What is its space diagonal?",
      a: "Space diagonal = \u221a(l\u00b2 + w\u00b2 + h\u00b2)\n= \u221a(9 + 16 + 25)\n= \u221a50\n= 5\u221a2 \u2248 7.07."
    },
    {
      q: "A cylinder has a volume of 200\u03c0 and a radius of 5. What is its height?",
      a: "V = \u03c0r\u00b2h\n200\u03c0 = \u03c0(25)h\nDivide both sides by 25\u03c0:\nh = 200/25 = 8.\nThe height is 8."
    },
    {
      q: "A cube has a surface area of 294. What is its volume?",
      a: "SA = 6s\u00b2\n294 = 6s\u00b2\ns\u00b2 = 49\ns = 7.\nVolume = s\u00b3 = 7\u00b3 = 343."
    },
    {
      q: "If the radius of a sphere is doubled, by what factor does the volume increase?",
      a: "Original volume = (4/3)\u03c0r\u00b3.\nNew volume = (4/3)\u03c0(2r)\u00b3 = (4/3)\u03c0 \u00d7 8r\u00b3.\nThe volume increases by a factor of 8.\n(Scaling factor k = 2, so volume scales by k\u00b3 = 2\u00b3 = 8.)"
    },
    {
      q: "A cone has a radius of 6 and a height of 8. What is its volume?",
      a: "V = (1/3)\u03c0r\u00b2h\n= (1/3)\u03c0(36)(8)\n= (1/3)\u03c0(288)\n= 96\u03c0\n\u2248 301.59."
    },
    {
      q: "A cylindrical container has radius 4 and height 15. How many liters does it hold if 1 liter = 1000 cm\u00b3? (Dimensions are in cm.)",
      a: "Volume = \u03c0r\u00b2h = \u03c0(16)(15) = 240\u03c0 cm\u00b3.\n240\u03c0 \u2248 753.98 cm\u00b3.\n753.98 / 1000 \u2248 0.754 liters.\nThe container holds approximately 0.754 liters (or 240\u03c0 / 1000 liters exactly)."
    }
  ]
},
// --- 3.6 Coordinate Geometry ---
{
  id: "coordinate-geometry",
  title: "Coordinate Geometry",
  concepts: [
    "The distance between two points (x\u2081, y\u2081) and (x\u2082, y\u2082) is given by d = \u221a[(x\u2082 \u2212 x\u2081)\u00b2 + (y\u2082 \u2212 y\u2081)\u00b2]. This is just the Pythagorean Theorem applied to the coordinate plane. Example: distance between (1, 2) and (4, 6) = \u221a[(4 \u2212 1)\u00b2 + (6 \u2212 2)\u00b2] = \u221a[9 + 16] = \u221a25 = 5.",
    "The midpoint of the segment connecting (x\u2081, y\u2081) and (x\u2082, y\u2082) is ((x\u2081 + x\u2082)/2, (y\u2081 + y\u2082)/2). Just average the x-coordinates and average the y-coordinates. Example: midpoint of (2, 8) and (6, 4) = ((2 + 6)/2, (8 + 4)/2) = (4, 6).",
    "The slope of a line through (x\u2081, y\u2081) and (x\u2082, y\u2082) is m = (y\u2082 \u2212 y\u2081) / (x\u2082 \u2212 x\u2081), or \u2018rise over run.\u2019 A positive slope goes up from left to right; a negative slope goes down. Example: slope of the line through (1, 3) and (5, 11) = (11 \u2212 3) / (5 \u2212 1) = 8/4 = 2.",
    "A horizontal line has a slope of 0 (no rise). A vertical line has an undefined slope (division by zero because x\u2082 \u2212 x\u2081 = 0). Example: the line through (2, 5) and (7, 5) is horizontal with slope 0. The line through (3, 1) and (3, 9) is vertical with undefined slope.",
    "Parallel lines have equal slopes. Perpendicular lines have slopes that are negative reciprocals (their product is \u22121). Example: if one line has slope 2/3, a parallel line also has slope 2/3, and a perpendicular line has slope \u22123/2. Check: (2/3) \u00d7 (\u22123/2) = \u22121 \u2713",
    "The slope-intercept form of a line is y = mx + b, where m is the slope and b is the y-intercept (the point where the line crosses the y-axis). Example: y = 3x \u2212 7 has slope 3 and y-intercept \u22127, meaning the line crosses the y-axis at (0, \u22127).",
    "To find the x-intercept, set y = 0 and solve for x. To find the y-intercept, set x = 0 and solve for y. Example: for the line 2x + 3y = 12, the x-intercept is found by setting y = 0: 2x = 12, x = 6, so the x-intercept is (6, 0). The y-intercept: 3y = 12, y = 4, so it is (0, 4).",
    "The point-slope form of a line is y \u2212 y\u2081 = m(x \u2212 x\u2081), where m is the slope and (x\u2081, y\u2081) is any point on the line. This is useful when you know the slope and one point. Example: slope = \u22122, point (3, 5). Equation: y \u2212 5 = \u22122(x \u2212 3), which simplifies to y = \u22122x + 11.",
    "The standard form of a line is Ax + By = C. To convert from slope-intercept: y = 2x + 5 becomes \u22122x + y = 5, or 2x \u2212 y = \u22125. On the GRE, you may need to convert between forms to compare lines or find intercepts.",
    "To find where two lines intersect, set their equations equal or solve the system of equations. Example: y = 2x + 1 and y = \u2212x + 7. Set equal: 2x + 1 = \u2212x + 7 \u2192 3x = 6 \u2192 x = 2. Then y = 2(2) + 1 = 5. Intersection point: (2, 5)."
  ],
  formulas: [
    "Distance: d = \u221a[(x\u2082 \u2212 x\u2081)\u00b2 + (y\u2082 \u2212 y\u2081)\u00b2]",
    "Midpoint: M = ((x\u2081 + x\u2082)/2, (y\u2081 + y\u2082)/2)",
    "Slope: m = (y\u2082 \u2212 y\u2081) / (x\u2082 \u2212 x\u2081)",
    "Slope-intercept form: y = mx + b"
  ],
  tips: [
    "When computing slope, be consistent about which point you label (x\u2081, y\u2081) and (x\u2082, y\u2082). The order doesn\u2019t matter as long as you subtract in the same order for both numerator and denominator.",
    "Parallel lines: same slope. Perpendicular lines: slopes multiply to \u22121 (negative reciprocals). These two facts appear constantly on the GRE.",
    "To quickly check if a point lies on a line, substitute the point\u2019s coordinates into the equation. If both sides are equal, the point is on the line. Example: does (2, 7) lie on y = 3x + 1? Plug in: 7 = 3(2) + 1 = 7. Yes!",
    "The distance formula is the Pythagorean Theorem in disguise. If you forget the formula, draw a right triangle on the coordinate plane using the horizontal and vertical distances as legs.",
    "For GRE coordinate geometry problems, always sketch a quick graph. Even a rough sketch helps you catch sign errors and visualize the answer."
  ],
  questions: [
    {
      q: "Find the distance between the points (\u22123, 4) and (5, \u22122).",
      a: "d = \u221a[(x\u2082 \u2212 x\u2081)\u00b2 + (y\u2082 \u2212 y\u2081)\u00b2]\n= \u221a[(5 \u2212 (\u22123))\u00b2 + (\u22122 \u2212 4)\u00b2]\n= \u221a[(8)\u00b2 + (\u22126)\u00b2]\n= \u221a[64 + 36]\n= \u221a100\n= 10."
    },
    {
      q: "What is the midpoint of the segment connecting (7, \u22121) and (\u22123, 5)?",
      a: "Midpoint = ((x\u2081 + x\u2082)/2, (y\u2081 + y\u2082)/2)\n= ((7 + (\u22123))/2, (\u22121 + 5)/2)\n= (4/2, 4/2)\n= (2, 2)."
    },
    {
      q: "A line passes through (2, 3) and (6, 11). Find its slope and equation in slope-intercept form.",
      a: "Slope m = (11 \u2212 3) / (6 \u2212 2) = 8/4 = 2.\nUsing point-slope form with point (2, 3):\ny \u2212 3 = 2(x \u2212 2)\ny \u2212 3 = 2x \u2212 4\ny = 2x \u2212 1.\nThe slope is 2 and the equation is y = 2x \u2212 1."
    },
    {
      q: "Line A has equation y = (3/4)x + 2. Line B is perpendicular to Line A and passes through (8, 1). Find the equation of Line B.",
      a: "Line A has slope 3/4.\nPerpendicular slope = negative reciprocal = \u22124/3.\nUsing point-slope form with (8, 1):\ny \u2212 1 = (\u22124/3)(x \u2212 8)\ny \u2212 1 = (\u22124/3)x + 32/3\ny = (\u22124/3)x + 32/3 + 1\ny = (\u22124/3)x + 32/3 + 3/3\ny = (\u22124/3)x + 35/3.\nThe equation is y = (\u22124/3)x + 35/3."
    },
    {
      q: "Find the x-intercept and y-intercept of the line 3x \u2212 5y = 30.",
      a: "x-intercept: set y = 0.\n3x \u2212 5(0) = 30\n3x = 30\nx = 10. The x-intercept is (10, 0).\n\ny-intercept: set x = 0.\n3(0) \u2212 5y = 30\n\u22125y = 30\ny = \u22126. The y-intercept is (0, \u22126)."
    },
    {
      q: "Where do the lines y = x + 3 and y = \u22122x + 9 intersect?",
      a: "Set the equations equal:\nx + 3 = \u22122x + 9\nx + 2x = 9 \u2212 3\n3x = 6\nx = 2.\nSubstitute back: y = 2 + 3 = 5.\nThe lines intersect at (2, 5).\nVerify with second equation: y = \u22122(2) + 9 = \u22124 + 9 = 5 \u2713"
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
      // --- 4.1 Statistics ---
{
  id: "4.1",
  title: "Mean, Median, Mode, Range",
  concepts: [
    "The mean (average) is the sum of all values divided by the number of values. Example: For the set {3, 5, 7, 10, 15}, the mean = (3 + 5 + 7 + 10 + 15) \u00f7 5 = 40 \u00f7 5 = 8. The mean is the most commonly tested statistic on the GRE and is sensitive to every value in the data set.",
    "The median is the middle value when the data is arranged in order. If there is an odd number of values, the median is the single middle value. If there is an even number of values, the median is the average of the two middle values. Example (odd): {2, 5, 8, 11, 14} \u2192 median = 8. Example (even): {3, 7, 10, 16} \u2192 median = (7 + 10) \u00f7 2 = 8.5.",
    "The mode is the value that appears most frequently. A data set can have no mode (all values appear once), one mode, or multiple modes. Example: {4, 7, 7, 9, 12} \u2192 mode = 7. Example: {3, 3, 5, 8, 8, 10} \u2192 modes = 3 and 8 (bimodal). Example: {1, 2, 3, 4, 5} \u2192 no mode.",
    "The range is the difference between the largest and smallest values. Range = Maximum \u2212 Minimum. Example: For {3, 8, 12, 15, 22}, the range = 22 \u2212 3 = 19. The range measures the total spread of the data but is sensitive to outliers.",
    "When a constant k is added to every value in a set, the mean, median, and mode each increase by k, but the range and standard deviation remain unchanged. Example: If {2, 5, 8} has mean = 5, then {5, 8, 11} (each value + 3) has mean = 8. The range stays 6 in both cases.",
    "When every value in a set is multiplied by a constant k, the mean, median, mode, and range are all multiplied by k. Example: If {4, 6, 10} has mean = 20/3 and range = 6, then {8, 12, 20} (each value \u00d7 2) has mean = 40/3 and range = 12.",
    "Adding or removing a value from a set changes the mean. If you add a value equal to the current mean, the mean stays the same. If you add a value greater than the mean, the mean increases; if less, the mean decreases. Example: {4, 6, 8, 10, 12} has mean = 8. Adding 14 gives mean = (40 + 14) \u00f7 6 = 54 \u00f7 6 = 9. The mean rose because 14 > 8.",
    "A weighted average accounts for the different importance (weight) of each value. Weighted Mean = \u03a3(value \u00d7 weight) \u00f7 \u03a3(weights). Example: A student scores 80 on a test worth 30% and 95 on a test worth 70%. Weighted average = (80 \u00d7 0.30) + (95 \u00d7 0.70) = 24 + 66.5 = 90.5. The higher-weighted score pulls the average toward it.",
    "In an evenly spaced set (arithmetic sequence), the mean equals the median, and both equal the average of the first and last terms. Example: {10, 15, 20, 25, 30} is evenly spaced with spacing 5. Mean = Median = (10 + 30) \u00f7 2 = 20. This shortcut saves significant time on the GRE.",
    "The GRE often uses the formula Sum = Mean \u00d7 Count. If the average of 8 numbers is 15, then their sum is 8 \u00d7 15 = 120. This is extremely useful when you need to find a missing value. Example: The average of 5 numbers is 12, so their sum = 60. If four of the numbers are 10, 11, 13, and 14, the fifth number = 60 \u2212 (10 + 11 + 13 + 14) = 60 \u2212 48 = 12."
  ],
  formulas: [
    "Mean = \u03a3(all values) \u00f7 n, equivalently Sum = Mean \u00d7 n",
    "Median (even count) = (value at position n/2 + value at position n/2 + 1) \u00f7 2",
    "Range = Maximum value \u2212 Minimum value",
    "Weighted Mean = \u03a3(value\u2081 \u00d7 weight\u2081 + value\u2082 \u00d7 weight\u2082 + ...) \u00f7 \u03a3(all weights)"
  ],
  tips: [
    "When a problem says 'the average (arithmetic mean),' it always means the standard mean\u2014sum divided by count. Use Sum = Mean \u00d7 Count to set up equations quickly.",
    "For evenly spaced sets, the mean = median = (first + last) \u00f7 2. You never need to add all the terms. Also, the number of terms = (last \u2212 first) \u00f7 spacing + 1.",
    "If a GRE problem asks how adding or removing one number affects the mean, compute the old sum, adjust it, then divide by the new count. Do not try to reason abstractly\u2014use the numbers.",
    "The median is resistant to outliers but the mean is not. If a problem mentions an extreme value being added, suspect the mean will shift but the median may stay the same or barely move.",
    "In weighted average problems, the overall average is always between the individual averages and is closer to the group with the larger weight. Use this to eliminate wrong answers before calculating."
  ],
  questions: [
    {
      q: "The average of six numbers is 14. If one of the numbers is removed, the average of the remaining five numbers becomes 12. What number was removed?",
      a: "Step 1: Original sum = mean \u00d7 count = 14 \u00d7 6 = 84.\nStep 2: New sum after removal = 12 \u00d7 5 = 60.\nStep 3: Removed number = original sum \u2212 new sum = 84 \u2212 60 = 24.\nThe answer is 24."
    },
    {
      q: "Set A = {3, 7, 7, 9, 14}. What are the mean, median, and mode of Set A?",
      a: "Step 1: Mean = (3 + 7 + 7 + 9 + 14) \u00f7 5 = 40 \u00f7 5 = 8.\nStep 2: The values in order are {3, 7, 7, 9, 14}. The middle (3rd) value is 7, so the median = 7.\nStep 3: The value 7 appears twice (more than any other value), so the mode = 7.\nMean = 8, Median = 7, Mode = 7."
    },
    {
      q: "In a class of 20 girls with an average score of 85 and 30 boys with an average score of 75, what is the overall class average?",
      a: "Step 1: Sum of girls\u2019 scores = 20 \u00d7 85 = 1700.\nStep 2: Sum of boys\u2019 scores = 30 \u00d7 75 = 2250.\nStep 3: Total sum = 1700 + 2250 = 3950.\nStep 4: Total students = 20 + 30 = 50.\nStep 5: Overall average = 3950 \u00f7 50 = 79.\nThe answer is 79. Note it is closer to 75 than to 85 because the boys\u2019 group is larger."
    },
    {
      q: "The integers from 15 to 45 inclusive form an evenly spaced set. What is the mean of this set?",
      a: "Step 1: This is an evenly spaced set (consecutive integers, spacing = 1).\nStep 2: For an evenly spaced set, mean = (first + last) \u00f7 2 = (15 + 45) \u00f7 2 = 60 \u00f7 2 = 30.\nThe answer is 30."
    },
    {
      q: "Set B = {2, 5, 8, 11, 14}. If every element is multiplied by 3 and then 4 is added to each result, what are the new mean and range?",
      a: "Step 1: Original mean = (2 + 5 + 8 + 11 + 14) \u00f7 5 = 40 \u00f7 5 = 8. Original range = 14 \u2212 2 = 12.\nStep 2: Multiplying every value by 3: new mean = 8 \u00d7 3 = 24, new range = 12 \u00d7 3 = 36.\nStep 3: Adding 4 to every value: new mean = 24 + 4 = 28, range is unchanged = 36.\nNew mean = 28, new range = 36."
    },
    {
      q: "The median of the set {3, x, 8, 12, 17} (arranged in increasing order) is 8. Which of the following could be the value of x?\n(A) 4  (B) 8  (C) 9  (D) Both A and B",
      a: "Step 1: The set has 5 values, so the median is the 3rd value when arranged in order.\nStep 2: The set arranged in order is {3, x, 8, 12, 17}, and the median is 8, which is the 3rd value. This means x must be in the 2nd position, so x \u2264 8.\nStep 3: Also, x must be \u2265 3 (since 3 is in the 1st position and x is 2nd).\nStep 4: Check option (A): x = 4 \u2192 {3, 4, 8, 12, 17}, median = 8. Valid.\nStep 5: Check option (B): x = 8 \u2192 {3, 8, 8, 12, 17}, median = 8. Valid.\nStep 6: Check option (C): x = 9 \u2192 {3, 8, 9, 12, 17}, median = 9 \u2260 8. Invalid.\nThe answer is (D) Both A and B."
    }
  ]
},
// --- 4.2 Standard Deviation ---
{
  id: "4.2",
  title: "Standard Deviation",
  concepts: [
    "Standard deviation (SD) measures how spread out the values in a data set are from the mean. A small SD means the values are clustered close to the mean; a large SD means they are spread far from the mean. The GRE tests conceptual understanding of SD\u2014you will never need to calculate it by hand.",
    "Conceptually, SD is computed by: (1) finding the mean, (2) calculating how far each value is from the mean (the deviations), (3) squaring each deviation, (4) averaging those squared deviations (this gives the variance), and (5) taking the square root. Example: For {2, 4, 6}, the mean is 4, the deviations are \u22122, 0, +2, squared deviations are 4, 0, 4, variance = 8/3, SD = \u221a(8/3) \u2248 1.63.",
    "If all values in a data set are identical, the SD is 0 because there is no spread. Example: {7, 7, 7, 7, 7} has SD = 0. This is the minimum possible SD\u2014standard deviation can never be negative.",
    "Adding a constant to every value in a set does NOT change the SD. The entire distribution shifts, but the spread remains the same. Example: {1, 3, 5} and {101, 103, 105} have the same SD because the values are equally spread from their respective means.",
    "Multiplying every value in a set by a positive constant k multiplies the SD by k. The spread scales proportionally. Example: If {2, 4, 6} has SD \u2248 1.63, then {4, 8, 12} (each value \u00d7 2) has SD \u2248 3.27, which is exactly 2 \u00d7 1.63.",
    "When comparing the SDs of two sets, look at how tightly clustered each set is around its mean. The set whose values are closer to its own mean has the smaller SD. Example: Set A = {48, 49, 50, 51, 52} (tightly clustered around 50) has a smaller SD than Set B = {10, 30, 50, 70, 90} (widely spread around 50), even though both have the same mean.",
    "Outliers dramatically increase the SD. Adding a value far from the mean increases the spread. Example: {8, 9, 10, 11, 12} has a relatively small SD. If we change the set to {8, 9, 10, 11, 50}, the SD increases substantially because 50 is very far from the mean.",
    "If a value equal to the mean is added to a data set, the SD decreases (or stays the same in degenerate cases). This is because the new value has zero deviation from the mean, which reduces the average deviation. Example: {2, 6, 10} has mean 6. Adding 6 to get {2, 6, 6, 10} reduces the SD because the new value contributes zero squared deviation.",
    "For a normal distribution (bell curve), approximately 68% of the data falls within 1 SD of the mean, about 95% within 2 SDs, and about 99.7% within 3 SDs. The GRE rarely tests this directly, but it may appear in data interpretation problems.",
    "The GRE frequently asks you to compare standard deviations of two distributions. A quick visual check: if one set\u2019s values are more \u2018bunched together\u2019 than the other, it has the smaller SD. You do not need exact calculations\u2014just a sense of relative spread."
  ],
  formulas: [
    "Variance = \u03a3(each value \u2212 mean)\u00b2 \u00f7 n",
    "Standard Deviation = \u221a(Variance) = \u221a[\u03a3(each value \u2212 mean)\u00b2 \u00f7 n]",
    "If every value is transformed to (k \u00d7 value + c), the new SD = |k| \u00d7 (old SD). The constant c has no effect on SD."
  ],
  tips: [
    "You will NOT need to compute SD on the GRE. Focus on understanding: which set is more spread out, what happens when you transform the data, and when SD equals zero.",
    "To compare SDs of two sets with the same mean, check which set has values closer to that mean. The one with values closer together has a smaller SD.",
    "Remember: adding or subtracting a constant to every element does NOT change the SD. Multiplying or dividing every element by a constant DOES change the SD (by that same factor).",
    "If a question asks about the effect of adding a data point: if the new value is close to the mean, SD decreases slightly; if far from the mean, SD increases. If exactly at the mean, SD decreases.",
    "When you see two histograms or dot plots and are asked to compare SDs, look at the width and shape. A taller, narrower distribution has a smaller SD than a shorter, wider one."
  ],
  questions: [
    {
      q: "Set X = {10, 10, 10, 10, 10} and Set Y = {8, 9, 10, 11, 12}. Which set has the greater standard deviation?",
      a: "Step 1: Set X has all identical values (every value is 10). When all values are the same, the SD = 0.\nStep 2: Set Y has values that vary: they range from 8 to 12, with a mean of 10. The deviations are \u22122, \u22121, 0, +1, +2, so SD > 0.\nStep 3: Since Set X has SD = 0 and Set Y has SD > 0, Set Y has the greater standard deviation."
    },
    {
      q: "Set A = {3, 5, 7, 9, 11}. Set B is created by adding 20 to each element of Set A. Which set has the greater standard deviation?",
      a: "Step 1: Set B = {23, 25, 27, 29, 31}.\nStep 2: Adding a constant (20) to every value shifts the entire set but does not change the spread.\nStep 3: Therefore, the SD of Set A equals the SD of Set B.\nThe answer is that they have equal standard deviations."
    },
    {
      q: "Set P = {4, 8, 12, 16, 20}. Set Q is created by multiplying each element of Set P by 3. How does the SD of Set Q compare to the SD of Set P?",
      a: "Step 1: Set Q = {12, 24, 36, 48, 60}.\nStep 2: When every value is multiplied by a constant k, the SD is also multiplied by |k|.\nStep 3: Since k = 3, the SD of Set Q = 3 \u00d7 (SD of Set P).\nThe standard deviation of Set Q is exactly 3 times the standard deviation of Set P."
    },
    {
      q: "A data set has a mean of 50 and a standard deviation of 5. If every value is transformed by the rule: new value = 2 \u00d7 (old value) + 10, what are the new mean and new standard deviation?",
      a: "Step 1: The transformation is new = 2 \u00d7 old + 10.\nStep 2: New mean = 2 \u00d7 (old mean) + 10 = 2 \u00d7 50 + 10 = 110.\nStep 3: For SD, the additive constant (+10) has no effect. Only the multiplicative factor matters.\nStep 4: New SD = |2| \u00d7 (old SD) = 2 \u00d7 5 = 10.\nThe new mean is 110 and the new standard deviation is 10."
    },
    {
      q: "Set M = {20, 25, 30, 35, 40} and Set N = {28, 29, 30, 31, 32}. Both sets have the same mean. Which has the smaller standard deviation?",
      a: "Step 1: Both sets have mean = 30.\nStep 2: In Set M, the values deviate from 30 by \u221210, \u22125, 0, +5, +10. These are large deviations.\nStep 3: In Set N, the values deviate from 30 by \u22122, \u22121, 0, +1, +2. These are small deviations.\nStep 4: Since Set N\u2019s values are much closer to the mean than Set M\u2019s values, Set N has the smaller standard deviation."
    },
    {
      q: "A data set has 10 values with a mean of 20 and a certain standard deviation. A new value of 20 is added to the set. Does the standard deviation increase, decrease, or stay the same?",
      a: "Step 1: The new value (20) is exactly equal to the mean.\nStep 2: The new value\u2019s deviation from the mean is 20 \u2212 20 = 0.\nStep 3: Adding a value with zero deviation reduces the average squared deviation because the new value contributes 0\u00b2 = 0 to the sum of squared deviations, while the count increases by 1.\nStep 4: This makes the variance smaller, and therefore the SD decreases.\nThe standard deviation decreases."
    }
  ]
},
// --- 4.3 Probability ---
{
  id: "4.3",
  title: "Probability",
  concepts: [
    "Probability measures the likelihood of an event occurring, always between 0 and 1 (or 0% and 100%). P(event) = (number of favorable outcomes) \u00f7 (total number of equally likely outcomes). Example: A fair die is rolled. P(rolling a 3) = 1/6 because there is 1 favorable outcome out of 6 equally likely outcomes.",
    "The complement rule states that P(event NOT happening) = 1 \u2212 P(event happening). Example: If P(rain) = 0.3, then P(no rain) = 1 \u2212 0.3 = 0.7. This rule is especially powerful for \u2018at least one\u2019 problems where calculating the complement is easier than the direct probability.",
    "Two events are independent if the occurrence of one does not affect the probability of the other. For independent events, P(A and B) = P(A) \u00d7 P(B). Example: A coin is flipped and a die is rolled. P(heads AND rolling a 4) = (1/2) \u00d7 (1/6) = 1/12. Flipping the coin has no effect on the die.",
    "Two events are mutually exclusive (disjoint) if they cannot both occur at the same time. For mutually exclusive events, P(A or B) = P(A) + P(B). Example: When rolling a single die, P(rolling a 2 or rolling a 5) = 1/6 + 1/6 = 2/6 = 1/3. You cannot roll both a 2 and a 5 simultaneously on one die.",
    "The general addition rule works for any two events (whether mutually exclusive or not): P(A or B) = P(A) + P(B) \u2212 P(A and B). The subtraction prevents double-counting the overlap. Example: In a class of 30 students, 18 play soccer, 12 play basketball, and 6 play both. P(soccer or basketball) = 18/30 + 12/30 \u2212 6/30 = 24/30 = 4/5.",
    "Conditional probability is the probability of an event given that another event has already occurred. P(A | B) = P(A and B) \u00f7 P(B). Example: A bag has 3 red and 5 blue marbles. You draw one marble (without replacement) and it is red. P(second marble is red | first was red) = 2/7 because after removing one red marble, 2 red and 5 blue remain (7 total).",
    "A permutation is an arrangement where order matters. The number of ways to arrange r items from n distinct items is nPr = n! \u00f7 (n \u2212 r)!. Example: How many ways can a president, vice president, and secretary be chosen from 10 people? \u2081\u2080P\u2083 = 10! \u00f7 7! = 10 \u00d7 9 \u00d7 8 = 720.",
    "A combination is a selection where order does NOT matter. The number of ways to choose r items from n distinct items is nCr = n! \u00f7 [r! \u00d7 (n \u2212 r)!]. Example: How many ways can a committee of 3 be chosen from 10 people? \u2081\u2080C\u2083 = 10! \u00f7 (3! \u00d7 7!) = (10 \u00d7 9 \u00d7 8) \u00f7 (3 \u00d7 2 \u00d7 1) = 120.",
    "The \u2018at least one\u2019 strategy uses the complement: P(at least one) = 1 \u2212 P(none). Example: A coin is flipped 4 times. P(at least one head) = 1 \u2212 P(no heads) = 1 \u2212 P(all tails) = 1 \u2212 (1/2)\u2074 = 1 \u2212 1/16 = 15/16. Calculating directly (exactly 1 head + exactly 2 heads + ...) would be much harder.",
    "When drawing items without replacement, the probabilities change after each draw because the total number of items decreases. Example: A jar has 4 red and 6 blue marbles. P(drawing 2 red in a row without replacement) = (4/10) \u00d7 (3/9) = 12/90 = 2/15. After the first red marble is drawn, only 3 red and 6 blue remain."
  ],
  formulas: [
    "P(event) = favorable outcomes \u00f7 total outcomes (all equally likely)",
    "P(A or B) = P(A) + P(B) \u2212 P(A and B) [general addition rule]",
    "nPr = n! \u00f7 (n \u2212 r)! [permutations: order matters]",
    "nCr = n! \u00f7 [r! \u00d7 (n \u2212 r)!] [combinations: order does not matter]"
  ],
  tips: [
    "If a problem says \u2018at least one,\u2019 immediately think complement: P(at least one) = 1 \u2212 P(none). This is almost always the fastest approach on the GRE.",
    "To decide between permutations and combinations, ask: \u2018Does the order of selection matter?\u2019 If choosing a president and VP (different roles), use permutations. If choosing a committee (no roles), use combinations.",
    "For \u2018and\u2019 probability problems with independent events, multiply the probabilities. For \u2018or\u2019 problems, add them (and subtract the overlap if they are not mutually exclusive).",
    "When drawing without replacement, update the total count and favorable count after each draw. Many students forget to reduce the denominator\u2014this is a common trap.",
    "Probabilities must be between 0 and 1 inclusive. If your calculation gives a negative number or a number greater than 1, you have made an error. Use this as a quick sanity check."
  ],
  questions: [
    {
      q: "A bag contains 5 red, 3 blue, and 2 green marbles. If one marble is drawn at random, what is the probability that it is NOT green?",
      a: "Step 1: Total marbles = 5 + 3 + 2 = 10.\nStep 2: P(green) = 2/10 = 1/5.\nStep 3: P(NOT green) = 1 \u2212 P(green) = 1 \u2212 1/5 = 4/5.\nThe answer is 4/5."
    },
    {
      q: "Two fair dice are rolled. What is the probability that the sum is 7?",
      a: "Step 1: Total possible outcomes = 6 \u00d7 6 = 36.\nStep 2: List the combinations that sum to 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 favorable outcomes.\nStep 3: P(sum = 7) = 6/36 = 1/6.\nThe answer is 1/6."
    },
    {
      q: "A committee of 4 people is to be selected from a group of 9. How many different committees are possible?",
      a: "Step 1: Since order does not matter for a committee, use combinations.\nStep 2: \u2089C\u2084 = 9! \u00f7 (4! \u00d7 5!) = (9 \u00d7 8 \u00d7 7 \u00d7 6) \u00f7 (4 \u00d7 3 \u00d7 2 \u00d7 1) = 3024 \u00f7 24 = 126.\nThe answer is 126."
    },
    {
      q: "A fair coin is flipped 5 times. What is the probability of getting at least one tail?",
      a: "Step 1: Use the complement: P(at least one tail) = 1 \u2212 P(no tails).\nStep 2: P(no tails) = P(all heads) = (1/2)\u2075 = 1/32.\nStep 3: P(at least one tail) = 1 \u2212 1/32 = 31/32.\nThe answer is 31/32."
    },
    {
      q: "In a group of 40 students, 25 study French, 20 study Spanish, and 10 study both. If a student is chosen at random, what is the probability that the student studies French or Spanish?",
      a: "Step 1: Use the general addition rule: P(French or Spanish) = P(French) + P(Spanish) \u2212 P(both).\nStep 2: P(French) = 25/40, P(Spanish) = 20/40, P(both) = 10/40.\nStep 3: P(French or Spanish) = 25/40 + 20/40 \u2212 10/40 = 35/40 = 7/8.\nThe answer is 7/8."
    },
    {
      q: "From a standard deck of 52 cards, two cards are drawn without replacement. What is the probability that both cards are aces?",
      a: "Step 1: There are 4 aces in a standard deck of 52 cards.\nStep 2: P(first card is an ace) = 4/52.\nStep 3: After drawing one ace, there are 3 aces left among 51 remaining cards. P(second card is an ace | first was an ace) = 3/51.\nStep 4: P(both aces) = (4/52) \u00d7 (3/51) = 12/2652 = 1/221.\nThe answer is 1/221."
    }
  ]
},
// --- 4.4 Data Interpretation ---
{
  id: "4.4",
  title: "Data Interpretation",
  concepts: [
    "Data interpretation questions present information in tables, graphs, or charts and ask you to analyze, compare, or calculate values from the data. The key skill is reading the data accurately before calculating. Always check titles, axis labels, units, and footnotes before answering any question.",
    "Bar graphs display data using rectangular bars whose heights (or lengths) represent values. They are used to compare quantities across categories. Example: A bar graph shows sales by month. If the January bar reaches 150 and the February bar reaches 200, then February\u2019s sales are 200 \u2212 150 = 50 more than January\u2019s. Watch for broken axes or non-zero starting points that can visually distort comparisons.",
    "Pie charts (circle graphs) show parts of a whole, with each slice representing a percentage or fraction of the total. All slices must add up to 100% (or 360\u00b0). Example: If a pie chart shows that 25% of a company\u2019s $800,000 revenue comes from Product A, then Product A\u2019s revenue = 0.25 \u00d7 $800,000 = $200,000. To find the actual value of a slice, multiply the percentage by the total.",
    "Line graphs show trends over time by connecting data points with lines. They are ideal for showing how a value changes across time periods. Example: If a line graph shows population growing from 10,000 in 2010 to 15,000 in 2020, the increase is 5,000 and the percent increase = (5,000 \u00f7 10,000) \u00d7 100 = 50%. Pay attention to the steepness of the line\u2014a steeper segment indicates a faster rate of change.",
    "Tables organize data into rows and columns. They are precise (exact values are given) but can contain a lot of information. Example: A table shows revenue and expenses for 5 years. To find profit for any year, compute Revenue \u2212 Expenses. To find which year had the highest profit margin, compute Profit \u00f7 Revenue for each year and compare. Read row and column headers carefully.",
    "Scatterplots display the relationship between two variables as points on a coordinate plane. Each point represents one observation. A positive trend means both variables increase together; a negative trend means one increases as the other decreases; no trend means the points are randomly scattered. A line of best fit can be drawn to estimate the overall relationship.",
    "Correlation describes the strength and direction of the linear relationship between two variables. It ranges from \u22121 (perfect negative) to +1 (perfect positive), with 0 meaning no linear correlation. Important: Correlation does NOT imply causation. Example: Ice cream sales and drowning incidents are positively correlated, but ice cream does not cause drowning\u2014both are related to a third variable (warm weather).",
    "Estimation is a critical GRE skill for data interpretation. You often need to estimate values from graphs rather than reading exact numbers. Round to convenient numbers and use mental math. Example: If a bar appears to reach about 47 and you need 47% of 312, estimate as 47% of 300 \u2248 141, then adjust upward slightly. The answer choices are usually spread far enough apart that estimation works.",
    "Percent of total is a common calculation: (Part \u00f7 Whole) \u00d7 100. Example: If a table shows that Region A had $45 million in sales out of a $150 million total, Region A represents (45/150) \u00d7 100 = 30% of total sales. When a pie chart is given alongside a table, multiply the pie chart percentage by the total from the table to find the actual value.",
    "Multi-figure data sets are common on the GRE. You might see a pie chart and a table together, and a single question may require data from both. Example: A pie chart shows that 40% of employees are in the Marketing department. A table shows the company has 250 employees total. Number of Marketing employees = 0.40 \u00d7 250 = 100. Always identify which figure provides each piece of information."
  ],
  formulas: [
    "Percent of total = (Part \u00f7 Whole) \u00d7 100",
    "Percent change = [(New value \u2212 Old value) \u00f7 Old value] \u00d7 100",
    "Sector angle in a pie chart = (percentage \u00f7 100) \u00d7 360\u00b0",
    "Value from a pie chart = (percentage of slice \u00f7 100) \u00d7 total value"
  ],
  tips: [
    "Before answering ANY data interpretation question, spend 15\u201320 seconds studying the graph or table: read the title, axis labels, units, legends, and any footnotes. Many errors come from misreading the data.",
    "Estimation is your friend. GRE answer choices for data interpretation are typically spread apart. You rarely need an exact reading from a graph\u2014a good estimate is sufficient. Round numbers to make arithmetic easier.",
    "For percent change problems, always use the OLD value as the base (denominator). The formula is (New \u2212 Old) \u00f7 Old \u00d7 100. A common mistake is dividing by the new value instead.",
    "When a graph has a non-zero starting point on the y-axis (truncated axis), differences between bars may look much larger than they actually are. Always read the actual values, not just the visual heights.",
    "In multi-part data sets (e.g., a pie chart + table), read the question carefully to determine which figure to use for each piece of data. Often you need to combine information from multiple sources."
  ],
  questions: [
    {
      q: "A pie chart shows the distribution of 600 employees across departments: Engineering 30%, Sales 25%, Marketing 20%, HR 15%, Other 10%. How many employees are in Marketing, and how many more employees are in Sales than in HR?",
      a: "Step 1: Marketing employees = 20% of 600 = 0.20 \u00d7 600 = 120.\nStep 2: Sales employees = 25% of 600 = 0.25 \u00d7 600 = 150.\nStep 3: HR employees = 15% of 600 = 0.15 \u00d7 600 = 90.\nStep 4: Difference = Sales \u2212 HR = 150 \u2212 90 = 60.\nMarketing has 120 employees, and Sales has 60 more employees than HR."
    },
    {
      q: "A company\u2019s revenue was $200,000 in 2020 and $260,000 in 2021. What was the percent increase from 2020 to 2021?",
      a: "Step 1: Change in revenue = $260,000 \u2212 $200,000 = $60,000.\nStep 2: Percent increase = (change \u00f7 original) \u00d7 100 = ($60,000 \u00f7 $200,000) \u00d7 100.\nStep 3: $60,000 \u00f7 $200,000 = 0.30.\nStep 4: 0.30 \u00d7 100 = 30%.\nThe percent increase is 30%."
    },
    {
      q: "A bar graph shows monthly sales (in thousands): Jan = 40, Feb = 55, Mar = 50, Apr = 70, May = 65, Jun = 80. During which month was the increase from the previous month the greatest?",
      a: "Step 1: Calculate the change from each month to the next:\nFeb \u2212 Jan = 55 \u2212 40 = +15\nMar \u2212 Feb = 50 \u2212 55 = \u22125 (a decrease)\nApr \u2212 Mar = 70 \u2212 50 = +20\nMay \u2212 Apr = 65 \u2212 70 = \u22125 (a decrease)\nJun \u2212 May = 80 \u2212 65 = +15\nStep 2: The greatest increase is +20, which occurred from March to April.\nThe answer is April (the increase from March to April was the greatest)."
    },
    {
      q: "A table shows that Country X exported $3.5 billion worth of goods in 2019 and $4.2 billion in 2020. Country Y exported $5.0 billion in 2019 and $5.5 billion in 2020. Which country had a greater percent increase in exports?",
      a: "Step 1: Country X percent increase = (4.2 \u2212 3.5) \u00f7 3.5 \u00d7 100 = 0.7 \u00f7 3.5 \u00d7 100 = 20%.\nStep 2: Country Y percent increase = (5.5 \u2212 5.0) \u00f7 5.0 \u00d7 100 = 0.5 \u00f7 5.0 \u00d7 100 = 10%.\nStep 3: Compare: 20% > 10%.\nCountry X had the greater percent increase (20% vs. 10%), even though Country Y\u2019s exports were larger in absolute terms."
    },
    {
      q: "In a scatterplot, 20 data points are plotted. As the x-values increase from 10 to 50, the y-values generally decrease from 80 to 20. What type of correlation does this suggest, and would the correlation coefficient be closer to \u22121, 0, or +1?",
      a: "Step 1: As x increases, y decreases. This is a negative trend.\nStep 2: The relationship appears consistent (y generally decreases as x increases), suggesting a strong negative correlation.\nStep 3: A strong negative correlation has a correlation coefficient close to \u22121.\nStep 4: The correlation coefficient would be closest to \u22121.\nThe scatterplot suggests a strong negative correlation, with a coefficient near \u22121."
    },
    {
      q: "A pie chart shows that 35% of a school\u2019s budget goes to salaries, 25% to facilities, 20% to programs, and the rest to other expenses. If the total budget is $2 million, how much is spent on other expenses?",
      a: "Step 1: Total of listed categories = 35% + 25% + 20% = 80%.\nStep 2: Other expenses = 100% \u2212 80% = 20%.\nStep 3: Amount for other expenses = 20% of $2,000,000 = 0.20 \u00d7 $2,000,000 = $400,000.\nThe answer is $400,000."
    }
  ]
}
    ]
  },

  // ============================================================
  // CHAPTER 5: QC STRATEGIES
  // ============================================================
  {
    id: "qc-strategy",
    title: "QC Strategies",
    emoji: "\ud83d\udcca",
    color: "#7c3aed",
    sections: [
      // --- 5.1 Number Properties for QC ---
{
  id: "number-properties-qc",
  title: "Number Properties for QC",
  concepts: [
    "The key to Quantitative Comparison (QC) questions is testing SPECIAL CASES. The GRE designs QC problems so that 'obvious' answers break when you plug in tricky numbers. Your job is to hunt for those tricky cases. The four QC answer choices are: (A) Column A is always greater, (B) Column B is always greater, (C) The two columns are always equal, (D) The relationship cannot be determined from the information given.",
    "MUST-TEST: Zero (0). Zero is the most common trap number. It is even, it is neither positive nor negative, and it behaves uniquely under multiplication (anything \u00d7 0 = 0), division (0 \u00f7 anything = 0, but anything \u00f7 0 is undefined), and exponentiation (0\u00b2 = 0, 0\u00b0 = 1 by convention). Example: 'x is a non-negative integer. Col A: x\u00b2, Col B: x.' If you only test x = 2 (4 > 2, A wins), you miss x = 0 (0 = 0, C) and x = 1 (1 = 1, C). Answer is D.",
    "MUST-TEST: One (1). The number 1 is the multiplicative identity: 1 \u00d7 anything = that thing. It also has unique exponent behavior: 1 raised to ANY power equals 1. Example: 'x > 0. Col A: x\u00b3, Col B: x.' Test x = 2: 8 > 2, A wins. Test x = 1: 1 = 1, C. Since results differ, the answer is D. Also note: 1 is not prime, which is another common trap.",
    "MUST-TEST: Negative one (\u22121). This value flips signs and has alternating exponent behavior: (\u22121)\u00b2 = 1, (\u22121)\u00b3 = \u22121, (\u22121)\u2074 = 1, etc. Example: 'x is a non-zero integer. Col A: x\u00b2, Col B: x\u00b3.' Test x = 2: 4 vs 8 \u2192 B. Test x = \u22121: 1 vs \u22121 \u2192 A. Answer is D.",
    "MUST-TEST: Fractions between 0 and 1. Numbers like 1/2, 1/3, 1/4 behave OPPOSITE to integers under many operations. Squaring a fraction between 0 and 1 makes it SMALLER: (1/2)\u00b2 = 1/4 < 1/2. Cubing makes it even smaller: (1/2)\u00b3 = 1/8. Taking the square root makes it BIGGER: \u221a(1/4) = 1/2 > 1/4. This reversal is one of the most heavily tested GRE concepts.",
    "MUST-TEST: Negative fractions between \u22121 and 0. Values like \u22121/2 combine the weirdness of fractions with negative-sign behavior. Example: x = \u22121/2 \u2192 x\u00b2 = 1/4 (positive, smaller magnitude), x\u00b3 = \u22121/8 (negative, even smaller magnitude). When a problem says 'x < 0,' always test both a negative integer AND a negative fraction.",
    "MUST-TEST: Large numbers. Sometimes two columns look equal or close for small values, but diverge for large ones. Example: 'n > 1. Col A: 2n, Col B: n + 5.' Test n = 2: 4 vs 7 \u2192 B. Test n = 10: 20 vs 15 \u2192 A. Answer is D. Large numbers can also help confirm a pattern: if A wins for n = 100 and n = 1000, it likely always wins for large n.",
    "Squaring negatives vs. cubing negatives: For any negative number x < 0, x\u00b2 > 0 (squaring makes it positive) but x\u00b3 < 0 (cubing keeps it negative). This means x\u00b2 > x\u00b3 whenever x < 0. More generally, even powers of negatives are positive and odd powers are negative. Example: (\u22123)\u00b2 = 9, (\u22123)\u00b3 = \u221227, (\u22123)\u2074 = 81, (\u22123)\u2075 = \u2212243.",
    "Even/Odd testing: Many QC problems involve expressions that behave differently for even vs. odd integers. Example: '(\u22121)^n. Col A: (\u22121)^n, Col B: (\u22121)^(n+1).' If n is even: Col A = 1, Col B = \u22121, so A > B. If n is odd: Col A = \u22121, Col B = 1, so B > A. Answer is D. Always test one even and one odd value when exponents or parity are involved.",
    "Summary of number behavior for 0 < x < 1: x\u00b2 < x (squaring shrinks it), x\u00b3 < x\u00b2 < x (cubing shrinks further), \u221ax > x (square root enlarges it), 1/x > 1 (reciprocal is greater than 1). For x > 1: x\u00b2 > x, x\u00b3 > x\u00b2 > x, \u221ax < x, 0 < 1/x < 1. These opposite behaviors are the #1 source of QC traps."
  ],
  formulas: [
    "For 0 < x < 1: x\u00b3 < x\u00b2 < x < \u221ax < \u00b3\u221ax. Each successive power shrinks the value; each successive root enlarges it.",
    "For x > 1: \u00b3\u221ax < \u221ax < x < x\u00b2 < x\u00b3. Powers grow the value; roots shrink it. This is the REVERSE of the 0-to-1 case.",
    "Sign rule for powers: x^(even) \u2265 0 for all real x. x^(odd) has the same sign as x. So (\u22122)\u2074 = 16 > 0 but (\u22122)\u2075 = \u221232 < 0."
  ],
  tips: [
    "If the problem gives NO constraints on a variable (or says 'x is a real number'), your must-test list is: \u22122, \u22121, \u22121/2, 0, 1/2, 1, 2. Testing all seven covers negatives, zero, fractions, and positives. If any two tests give different comparison results, the answer is D.",
    "If the problem says 'x > 0,' still test x = 1/2 and x = 1 alongside larger values. If it says 'x is a positive integer,' test 1 and 2 at minimum. The constraint narrows your list but NEVER skip edge cases within the allowed range.",
    "When both columns give the SAME result for every special case you try, suspect the answer is A, B, or C \u2014 but try to confirm algebraically. Plugging in only proves D (by finding a counterexample); it cannot fully prove A, B, or C.",
    "A quick check: if a QC problem has NO variables and only concrete numbers, the answer is NEVER D. You can always compute both sides. Answer D only applies when the relationship genuinely depends on an unknown value.",
    "Organize your scratch work in a table: make a column for the test value, a column for Column A's result, and a column for Column B's result. This prevents errors and makes it easy to spot when the relationship switches."
  ],
  questions: [
    {
      q: "x is a non-zero number.\nColumn A: x\u00b2\nColumn B: x\u00b3",
      a: "Answer: D. Test x = 2: Col A = 4, Col B = 8, so B > A. Test x = 1/2: Col A = 1/4, Col B = 1/8, so A > B. Since the comparison flips, the relationship cannot be determined. (You could also test x = \u22121: Col A = 1, Col B = \u22121, so A > B \u2014 confirming D with the first test.)"
    },
    {
      q: "x is an integer.\nColumn A: (\u22121)^x\nColumn B: (\u22121)^(2x)",
      a: "Answer: D. Note that (\u22121)^(2x) = [(\u22121)\u00b2]^x = 1^x = 1, so Col B is always 1. For Col A: if x is even, (\u22121)^x = 1, so A = B. If x is odd, (\u22121)^x = \u22121, so B > A. Since the result changes depending on whether x is even or odd, the answer is D."
    },
    {
      q: "0 < x < 1\nColumn A: x\nColumn B: \u221ax",
      a: "Answer: B. For any number between 0 and 1, the square root is LARGER than the number itself. Example: x = 1/4, \u221a(1/4) = 1/2, and 1/2 > 1/4. Example: x = 0.01, \u221a0.01 = 0.1, and 0.1 > 0.01. Algebraically: \u221ax \u2212 x = \u221ax(1 \u2212 \u221ax). Since 0 < x < 1, we have 0 < \u221ax < 1, so both factors are positive, meaning \u221ax > x always. Column B is greater."
    },
    {
      q: "y is a negative number.\nColumn A: y\u00b2\nColumn B: y\u00b3",
      a: "Answer: A. When y < 0, y\u00b2 is always positive (squaring a negative gives a positive). Meanwhile y\u00b3 is always negative (cubing a negative stays negative). A positive number is always greater than a negative number, so Col A > Col B for ALL negative y. Test y = \u22122: Col A = 4, Col B = \u22128, A > B \u2713. Test y = \u22121/2: Col A = 1/4, Col B = \u22121/8, A > B \u2713. Column A is always greater."
    },
    {
      q: "x is a positive number.\nColumn A: x\nColumn B: 1/x",
      a: "Answer: D. Test x = 2: Col A = 2, Col B = 1/2, so A > B. Test x = 1/3: Col A = 1/3, Col B = 3, so B > A. Test x = 1: Col A = 1, Col B = 1, so A = B. The relationship changes depending on whether x > 1, x = 1, or 0 < x < 1. The answer is D."
    },
    {
      q: "n is a positive integer greater than 1.\nColumn A: (\u22121)^n + (\u22121)^(n+1)\nColumn B: 0",
      a: "Answer: C. Regardless of whether n is even or odd, consecutive powers of \u22121 have opposite signs, so they always sum to zero. If n is even: (\u22121)^n = 1 and (\u22121)^(n+1) = \u22121, sum = 0. If n is odd: (\u22121)^n = \u22121 and (\u22121)^(n+1) = 1, sum = 0. Col A always equals 0 = Col B. The answer is C."
    }
  ]
},
// --- 5.2 Estimation & Comparison Techniques ---
{
  id: "estimation-comparison",
  title: "Estimation & Comparison Techniques",
  concepts: [
    "The golden rule of QC: you do NOT need to calculate exact values. You only need to determine which column is bigger (or if they are equal, or if it cannot be determined). This means approximation, simplification, and clever manipulation save enormous time. Never compute more than necessary.",
    "Technique 1 \u2014 Add or subtract the same value from both columns. This does not change the relationship. Example: Col A: 5 + \u221a3, Col B: 3 + \u221a3. Subtract \u221a3 from both \u2192 Col A becomes 5, Col B becomes 3. Clearly 5 > 3, so A > B. You turned a messy comparison into a trivial one.",
    "Technique 2 \u2014 Multiply or divide both columns by the SAME POSITIVE number. This preserves the inequality direction. Example: Col A: 3/7, Col B: 5/11. Multiply both by 77 (= 7 \u00d7 11) \u2192 Col A becomes 33, Col B becomes 35. Since 35 > 33, Column B is greater. WARNING: If you multiply or divide by a NEGATIVE number, the inequality FLIPS. Only multiply/divide by positives unless you explicitly flip the comparison.",
    "Technique 3 \u2014 Square both columns. You can square both columns ONLY when both columns are non-negative (or you know their signs). Squaring preserves the order for non-negative values. Example: Col A: \u221a50, Col B: 7. Both are positive, so square: Col A\u00b2 = 50, Col B\u00b2 = 49. Since 50 > 49, Column A is greater. This avoids computing \u221a50 \u2248 7.07.",
    "Technique 4 \u2014 Compare both columns to a common benchmark. Instead of directly comparing Col A to Col B, compare each to a third value. Example: Col A: 7/15, Col B: 11/23. Is each greater or less than 1/2? 7/15 < 7.5/15 = 1/2 and 11/23 < 11.5/23 = 1/2, so both are less than 1/2. Not enough. Try: 7/15 = 0.4667 and 11/23 = 0.4783, so B > A. Alternatively, cross-multiply (since denominators are positive): 7 \u00d7 23 = 161 vs 11 \u00d7 15 = 165. Since 165 > 161, Col B > Col A.",
    "Technique 5 \u2014 Cross-multiplication for fractions. To compare a/b and c/d (where b, d > 0), compare a\u00d7d vs c\u00d7b. If a\u00d7d > c\u00d7b, then a/b > c/d. Example: Compare 13/17 vs 19/25. Compute 13 \u00d7 25 = 325 vs 19 \u00d7 17 = 323. Since 325 > 323, Col A (13/17) is slightly greater.",
    "Technique 6 \u2014 Simplify expressions by factoring. When columns share common terms, factor them out. Example: Col A: 3\u00b9\u2070 + 3\u00b9\u2070, Col B: 3\u00b9\u00b9. Simplify Col A: 3\u00b9\u2070 + 3\u00b9\u2070 = 2 \u00d7 3\u00b9\u2070. Simplify Col B: 3\u00b9\u00b9 = 3 \u00d7 3\u00b9\u2070. Now compare 2 \u00d7 3\u00b9\u2070 vs 3 \u00d7 3\u00b9\u2070. Divide both by 3\u00b9\u2070 (positive) \u2192 compare 2 vs 3. Column B is greater.",
    "Technique 7 \u2014 Use estimation for roots and powers. Key benchmarks: \u221a2 \u2248 1.414, \u221a3 \u2248 1.732, \u221a5 \u2248 2.236, \u03c0 \u2248 3.14159. Example: Col A: \u221a2 + \u221a3, Col B: \u221a10. Estimate: Col A \u2248 1.414 + 1.732 = 3.146. Col B = \u221a10 \u2248 3.162. So B > A. To verify, square both (both positive): (\u221a2 + \u221a3)\u00b2 = 2 + 2\u221a6 + 3 = 5 + 2\u221a6. Compare to (\u221a10)\u00b2 = 10. Need: 5 + 2\u221a6 vs 10, i.e., 2\u221a6 vs 5, i.e., \u221a6 vs 2.5, i.e., 6 vs 6.25. Since 6 < 6.25, Col A < Col B. B wins.",
    "Technique 8 \u2014 Make denominators or bases the same. When comparing exponential expressions, rewrite with the same base. Example: Col A: 4\u00b3\u2070, Col B: 8\u00b9\u2070. Rewrite: 4 = 2\u00b2, so 4\u00b3\u2070 = 2\u2076\u2070. 8 = 2\u00b3, so 8\u00b9\u2070 = 2\u00b3\u2070. Since 2\u2076\u2070 > 2\u00b3\u2070, Column A is greater. Same idea works for fractions: rewrite with a common denominator before comparing.",
    "Technique 9 \u2014 Percentage and ratio shortcuts. If Col A is '30% of 500' and Col B is '50% of 280,' don't calculate: 30% of 500 = 150, and 50% of 280 = 140, so A > B. For ratios, simplify: if Col A: 144/360 and Col B: 2/5, note 144/360 = 2/5 exactly (since 144 \u00d7 5 = 720 = 360 \u00d7 2), so they are equal. Always check if simplification reveals equality."
  ],
  formulas: [
    "Cross-multiply to compare fractions: a/b vs c/d (b, d > 0) \u2192 compare a\u00d7d vs c\u00d7b. If ad > bc, then a/b > c/d.",
    "Squaring both sides: If A, B \u2265 0, then A > B \u21d4 A\u00b2 > B\u00b2. This lets you eliminate square roots. Example: \u221a50 vs 7 \u2192 50 vs 49 \u2192 \u221a50 > 7.",
    "Difference technique: Compute Col A \u2212 Col B. If the result is always positive \u2192 A wins. Always negative \u2192 B wins. Always zero \u2192 equal. Changes sign \u2192 D."
  ],
  tips: [
    "NEVER multiply or divide both columns by a variable unless you know its sign. If x could be negative, multiplying both sides by x reverses the inequality. This is one of the most common QC errors.",
    "When comparing square roots, squaring is almost always faster than estimating. \u221a51 vs \u221a50 + 0.1? Square both (if valid) instead of converting to decimals.",
    "Benchmark fractions to memorize: 1/3 \u2248 0.333, 1/4 = 0.25, 1/5 = 0.2, 1/6 \u2248 0.167, 1/7 \u2248 0.143, 1/8 = 0.125, 2/3 \u2248 0.667, 3/4 = 0.75, 2/7 \u2248 0.286, 3/8 = 0.375. These help you quickly estimate fractional comparisons.",
    "When both columns are complicated expressions, look for what they share. Subtract or divide out common pieces to simplify. A problem that looks hard often reduces to comparing two small numbers.",
    "If you are stuck, try rephrasing: 'Is Col A \u2212 Col B positive, negative, or zero?' This reframes the QC into a single-expression sign analysis, which may be easier."
  ],
  questions: [
    {
      q: "Column A: \u221a(150)\nColumn B: 12",
      a: "Answer: A. Both columns are positive, so we can square both sides. Col A\u00b2 = 150. Col B\u00b2 = 144. Since 150 > 144, \u221a150 > 12. Column A is greater."
    },
    {
      q: "Column A: (3\u2078 + 3\u2078 + 3\u2078)\nColumn B: 3\u2079",
      a: "Answer: C. Simplify Col A: 3\u2078 + 3\u2078 + 3\u2078 = 3 \u00d7 3\u2078 = 3\u2079. Col B = 3\u2079. They are equal. The answer is C."
    },
    {
      q: "Column A: 7/13\nColumn B: 11/20",
      a: "Answer: B. Cross-multiply (both denominators positive): 7 \u00d7 20 = 140 vs 11 \u00d7 13 = 143. Since 143 > 140, Col B (11/20) > Col A (7/13). Column B is greater."
    },
    {
      q: "Column A: 45% of 220\nColumn B: 50% of 200",
      a: "Answer: A. Col A = 0.45 \u00d7 220 = 99. Col B = 0.50 \u00d7 200 = 100. Wait \u2014 Col B = 100 > 99. Column B is greater. Let me recheck: 0.45 \u00d7 220 = 45 \u00d7 2.2 = 99. Yes, Col B = 100 > 99. Answer: B."
    },
    {
      q: "Column A: 2\u2074\u2070\nColumn B: 3\u00b2\u2075",
      a: "Answer: B. We need to compare 2\u2074\u2070 and 3\u00b2\u2075. Rewrite 2\u2074\u2070 = (2\u2078)\u2075 = 256\u2075 and 3\u00b2\u2075 = (3\u2075)\u2075 = 243\u2075. Since 256 > 243, we get 256\u2075 > 243\u2075, so A > B. Wait \u2014 let me recheck: 2\u2074\u2070 = (2\u2078)\u2075 = 256\u2075 and 3\u00b2\u2075 = (3\u2075)\u2075 = 243\u2075. 256 > 243, so 256\u2075 > 243\u2075. Answer: A. Column A is greater."
    },
    {
      q: "Column A: \u221a2 + \u221a3\nColumn B: \u221a10",
      a: "Answer: B. Both columns are positive, so square both. Col A\u00b2 = (\u221a2 + \u221a3)\u00b2 = 2 + 2\u221a6 + 3 = 5 + 2\u221a6. Col B\u00b2 = 10. Compare: 5 + 2\u221a6 vs 10 \u2192 2\u221a6 vs 5 \u2192 4 \u00d7 6 vs 25 (squaring again, both sides positive) \u2192 24 vs 25. Since 24 < 25, Col A\u00b2 < Col B\u00b2, so Col A < Col B. Column B is greater."
    }
  ]
},
// --- 5.3 Plugging Numbers & Testing Cases ---
{
  id: "plugging-numbers",
  title: "Plugging Numbers & Testing Cases",
  concepts: [
    "Plugging in numbers is the single most powerful QC strategy. The goal: test specific values for the variable(s) to see if the relationship between columns changes. If you find two test cases that give different results (one where A wins and one where B wins, or one where they are equal and one where they are not), the answer is D. If every test case gives the same result, you gain confidence in A, B, or C \u2014 but should confirm algebraically if possible.",
    "The MUST-TEST list (memorize this): When a variable has no constraints or minimal constraints, systematically test these values: (1) A negative integer, like \u22122. (2) \u22121. (3) A negative fraction, like \u22121/2. (4) Zero (if allowed). (5) A positive fraction, like 1/2. (6) One (1). (7) A positive integer greater than 1, like 2 or 3. This covers all the 'danger zones' where expressions change behavior.",
    "When to answer D: You answer D as soon as you find TWO test cases that produce DIFFERENT outcomes. Example: If x = 1 makes Col A > Col B, but x = \u22121 makes Col A < Col B, stop immediately. The answer is D. You do NOT need to test all seven values; D is confirmed the moment you get conflicting results.",
    "When the answer is NOT D: If you test 3\u20134 strategically chosen values and they ALL give the same result (say Col A > Col B every time), the answer is probably A. But 'probably' is not 'definitely.' On the real GRE, try to verify algebraically. Example: Col A: x\u00b2 + 1, Col B: 2x (for all real x). Testing x = 0: 1 vs 0 (A). x = 1: 2 vs 2 (C). Different results \u2192 D. But if we had gotten A every time, we could verify: x\u00b2 + 1 \u2212 2x = (x \u2212 1)\u00b2 \u2265 0 always, with equality only at x = 1.",
    "Systematic approach step by step: (1) Read the problem and identify what variable(s) you can choose. (2) Note the constraints ('x > 0,' 'n is a positive integer,' etc.) to narrow your test list. (3) Start with the EASIEST numbers that satisfy the constraints (usually 0 or 1). (4) If the first test gives Col A > Col B, your NEXT test should try to make Col B win \u2014 pick numbers that work against the current leader. (5) If you get conflicting results, answer D. If consistent, try to prove algebraically or test one more extreme value.",
    "Trying to 'break' the result: After your first plug-in, actively try to make the OTHER column win. This adversarial approach is much more efficient than random testing. Example: Col A: x + 3, Col B: x\u00b2 (x > 0). Test x = 1: 4 vs 1, A wins. Now try to make B win \u2014 pick a large x like x = 10: 13 vs 100, B wins. Done: answer is D. If you had lazily tested x = 1, 2, 3, you would have seen A, A, A and might have wrongly concluded A.",
    "When to use algebra AFTER plugging: If all your tests give the same result, try to confirm with algebra. Common techniques: (1) Compute Col A \u2212 Col B and see if the expression is always positive/negative/zero. (2) Factor the difference. (3) Recognize a perfect square or known identity. Example: Col A: a\u00b2 + b\u00b2, Col B: 2ab. Difference = a\u00b2 + b\u00b2 \u2212 2ab = (a \u2212 b)\u00b2 \u2265 0 always. So A \u2265 B always, with equality when a = b. If the problem says a \u2260 b, the answer is A. If a could equal b, the answer depends on whether C is possible too.",
    "Plugging in for geometry QCs: When a QC involves geometric figures (triangles, circles, etc.) with a variable, you can often assign specific lengths or angles. For triangles with a constraint like 'the perimeter is 12,' test equilateral (4, 4, 4) vs. elongated (1, 5.5, 5.5) to see if a quantity like area changes. The answer is often D because geometry allows many configurations.",
    "Multiple variables: When a QC has two or more unknowns, test cases where (1) both are equal, (2) one is much larger than the other, (3) one is zero (if allowed), (4) they have opposite signs (if allowed). Example: 'x + y = 10. Col A: xy, Col B: 24.' Test x = 5, y = 5: xy = 25 > 24, A wins. Test x = 1, y = 9: xy = 9 < 24, B wins. Answer is D."
  ],
  formulas: [
    "Col A \u2212 Col B method: Compute the difference expression. If it simplifies to a perfect square or always-positive form (like (x \u2212 k)\u00b2 + c where c > 0), then A > B always.",
    "Key algebraic identities for verification: a\u00b2 \u2212 b\u00b2 = (a+b)(a\u2212b). a\u00b2 + b\u00b2 \u2212 2ab = (a\u2212b)\u00b2 \u2265 0. a\u00b2 + b\u00b2 \u2265 2ab (AM-GM consequence).",
    "AM \u2265 GM inequality: For non-negative a and b, (a+b)/2 \u2265 \u221a(ab), with equality iff a = b. Useful for proving Col A \u2265 Col B in many QCs involving sums vs. products."
  ],
  tips: [
    "Speed tip: Start with 0, 1, and \u22121 as your first three tests (if all are allowed by constraints). These are the fastest to compute and catch most traps. If the relationship is the same for all three, try 1/2 next.",
    "If a problem says 'x is a positive integer,' your must-test list shortens to: 1, 2, and maybe a larger number like 10. You cannot test fractions, negatives, or zero. Respect the constraints.",
    "Never test just one value and declare the answer. Even if the first value gives A > B, you MUST test at least one more \u2014 ideally a very different type of number. One test proves nothing; two consistent tests are suggestive; a proof is conclusive.",
    "For problems with the constraint 'x > 1' or 'x < \u22121,' fractions between 0 and 1 (or between \u22121 and 0) are off the table. But DO test values close to the boundary, like x = 1.01 or x = \u22121.01, as well as extreme values like x = 100.",
    "If the QC has no variables at all (just concrete numbers), do NOT waste time plugging in. Just compute or simplify. The answer cannot be D when everything is determined."
  ],
  questions: [
    {
      q: "x is a real number.\nColumn A: (x + 1)\u00b2\nColumn B: x\u00b2 + 1",
      a: "Answer: D. Expand Col A: (x+1)\u00b2 = x\u00b2 + 2x + 1. So Col A \u2212 Col B = (x\u00b2 + 2x + 1) \u2212 (x\u00b2 + 1) = 2x. If x > 0, then 2x > 0, so A > B. If x = 0, then 2x = 0, so A = B. If x < 0, then 2x < 0, so B > A. The relationship changes with x, so the answer is D. Test verification: x = 1 \u2192 4 vs 2 (A). x = 0 \u2192 1 vs 1 (C). x = \u22121 \u2192 0 vs 2 (B). Confirmed D."
    },
    {
      q: "a and b are positive numbers and a \u2260 b.\nColumn A: a\u00b2 + b\u00b2\nColumn B: 2ab",
      a: "Answer: A. Col A \u2212 Col B = a\u00b2 + b\u00b2 \u2212 2ab = (a \u2212 b)\u00b2. Since a \u2260 b, (a \u2212 b)\u00b2 > 0 always. So Col A is always greater than Col B. Test: a = 3, b = 1: 9 + 1 = 10 vs 2(3)(1) = 6. A > B \u2713. Test: a = 5, b = 4: 25 + 16 = 41 vs 2(5)(4) = 40. A > B \u2713. Algebraic proof confirms: (a\u2212b)\u00b2 > 0, so A > B always."
    },
    {
      q: "x + y = 10, x > 0, y > 0.\nColumn A: xy\nColumn B: 25",
      a: "Answer: D. Test x = 5, y = 5: xy = 25 = Col B, so A = B. Test x = 1, y = 9: xy = 9 < 25, so B > A. Already two different results (equal and B wins), so D. Note: By AM-GM, xy \u2264 (x+y)\u00b2/4 = 25, with equality when x = y = 5. So xy \u2264 25 always, and xy = 25 only when x = y. Since x = y = 5 IS allowed and x = 1, y = 9 IS allowed, the answer is D."
    },
    {
      q: "n is a positive integer.\nColumn A: 3^n\nColumn B: n\u00b3",
      a: "Answer: D. Test n = 1: 3\u00b9 = 3 vs 1\u00b3 = 1. A > B. Test n = 2: 3\u00b2 = 9 vs 2\u00b3 = 8. A > B. Test n = 3: 3\u00b3 = 27 vs 3\u00b3 = 27. A = B. Since we get A > B for n = 1 but A = B for n = 3, the relationship is not constant \u2014 answer is D. (For n = 4: 81 vs 64, A > B. For large n, 3^n grows exponentially while n\u00b3 grows polynomially, so A eventually dominates. But the tie at n = 3 means D.)"
    },
    {
      q: "x < 0\nColumn A: x\u00b2 \u2212 x\nColumn B: 0",
      a: "Answer: A. Since x < 0, we know x\u00b2 > 0 (squaring a negative is positive) and \u2212x > 0 (negating a negative is positive). Therefore x\u00b2 \u2212 x = x\u00b2 + (\u2212x) = positive + positive > 0 always. Test: x = \u22121: (\u22121)\u00b2 \u2212 (\u22121) = 1 + 1 = 2 > 0 \u2713. Test: x = \u22121/2: (1/4) \u2212 (\u22121/2) = 1/4 + 1/2 = 3/4 > 0 \u2713. Column A is always greater."
    },
    {
      q: "p is a prime number.\nColumn A: p\u00b2 \u2212 1\nColumn B: p + 1",
      a: "Answer: D. Simplify: p\u00b2 \u2212 1 = (p\u22121)(p+1). So Col A = (p\u22121)(p+1) and Col B = (p+1). Divide both by (p+1), which is positive since p \u2265 2, to get Col A' = p \u2212 1 vs Col B' = 1. If p = 2: p \u2212 1 = 1 = 1, so A = B. If p = 3: p \u2212 1 = 2 > 1, so A > B. If p = 5: p \u2212 1 = 4 > 1, so A > B. We get equality at p = 2 but A > B for all other primes, so the answer is D."
    }
  ]
},
// --- 5.4 High-Frequency GRE Topics ---
{
  id: "high-frequency-topics",
  title: "High-Frequency GRE Topics",
  concepts: [
    "PERCENTAGES & RATIOS: Percent means 'per hundred.' 25% = 25/100 = 0.25. Key formulas: Percent change = (New \u2212 Old)/Old \u00d7 100%. A 20% increase on $50 = $50 \u00d7 1.20 = $60. A 20% decrease on $60 = $60 \u00d7 0.80 = $48. TRAP: A 20% increase followed by a 20% decrease does NOT return to the original \u2014 it returns to 96% of the original (1.20 \u00d7 0.80 = 0.96). Successive percentage changes multiply: two 10% increases = 1.10 \u00d7 1.10 = 1.21, which is a 21% increase, not 20%.",
    "PERCENTAGES & RATIOS (continued): Ratios compare quantities. If a:b = 3:5, then a = 3k and b = 5k for some value k. To find actual values, you need an additional equation (like a + b = 40 \u2192 3k + 5k = 40 \u2192 k = 5, so a = 15, b = 25). Proportions: a/b = c/d can be cross-multiplied to ad = bc. Part-to-whole: if the ratio of boys to girls is 3:5, the fraction of boys is 3/(3+5) = 3/8. GRE loves mixing percentages with ratios: 'If 30% of students are seniors and the ratio of senior boys to senior girls is 2:3, what fraction of all students are senior girls?' Answer: 30% \u00d7 3/5 = 18%.",
    "ALGEBRA \u2014 Equations: Solve linear equations by isolating the variable. Example: 3x + 7 = 22 \u2192 3x = 15 \u2192 x = 5. For systems of two equations with two unknowns, use substitution or elimination. Example: 2x + y = 10 and x \u2212 y = 2. Add: 3x = 12, x = 4, y = 2. GRE trick: sometimes you don't need individual values. If asked for x + y, you might combine equations directly without solving for x and y separately.",
    "ALGEBRA \u2014 Inequalities: Solve like equations BUT flip the sign when multiplying/dividing by a negative. Example: \u22123x > 12 \u2192 x < \u22124 (sign flips). Combining inequalities: if 2 < x < 5 and 3 < y < 7, then 2+3 < x+y < 5+7, so 5 < x+y < 12. For products/quotients of ranges, consider all four endpoint combinations. Absolute value inequalities: |x| < 5 means \u22125 < x < 5. |x| > 5 means x > 5 or x < \u22125.",
    "ALGEBRA \u2014 Quadratics & Factoring: Standard form: ax\u00b2 + bx + c = 0. Factor or use the quadratic formula: x = (\u2212b \u00b1 \u221a(b\u00b2\u22124ac))/(2a). Key factoring patterns: x\u00b2 \u2212 y\u00b2 = (x+y)(x\u2212y), x\u00b2 + 2xy + y\u00b2 = (x+y)\u00b2, x\u00b2 \u2212 2xy + y\u00b2 = (x\u2212y)\u00b2. Sum of roots = \u2212b/a, product of roots = c/a. Example: x\u00b2 \u2212 5x + 6 = 0 \u2192 (x\u22122)(x\u22123) = 0 \u2192 x = 2 or 3.",
    "WORD PROBLEMS \u2014 Rate/Speed: Distance = Rate \u00d7 Time (D = RT). Average speed for a round trip is NOT the average of the two speeds. It is: 2d/(d/r\u2081 + d/r\u2082) = 2r\u2081r\u2082/(r\u2081 + r\u2082). Example: Drive to work at 30 mph, return at 60 mph. Average speed = 2(30)(60)/(30+60) = 3600/90 = 40 mph (not 45). Relative speed: objects moving toward each other \u2192 add speeds. Moving apart \u2192 add speeds. Moving same direction \u2192 subtract speeds.",
    "WORD PROBLEMS \u2014 Work: If A can finish a job in 'a' hours and B can finish it in 'b' hours, together they finish in ab/(a+b) hours. Their combined rate is 1/a + 1/b = (a+b)/(ab). Example: Pipe A fills a tank in 6 hours, Pipe B in 3 hours. Together: 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2, so they fill it in 2 hours. Negative work (draining): subtract the rate. If C drains in 4 hours, net rate = 1/6 + 1/3 \u2212 1/4 = 2/12 + 4/12 \u2212 3/12 = 3/12 = 1/4, so 4 hours.",
    "WORD PROBLEMS \u2014 Mixtures: Use the weighted average formula or set up a 'total amount of solute' equation. Example: Mix 10 liters of 30% salt solution with 5 liters of 60% salt. Total salt = 10(0.30) + 5(0.60) = 3 + 3 = 6 liters. Total volume = 15 liters. Concentration = 6/15 = 40%. Key insight: the mixture's concentration ALWAYS falls between the two original concentrations, closer to whichever has more volume.",
    "NUMBER PROPERTIES \u2014 Divisibility & Remainders: Divisibility rules \u2014 by 2: last digit even. By 3: digit sum divisible by 3. By 4: last two digits divisible by 4. By 5: ends in 0 or 5. By 6: divisible by both 2 and 3. By 8: last three digits divisible by 8. By 9: digit sum divisible by 9. Remainders: If a = qd + r (0 \u2264 r < d), then r is the remainder when a is divided by d. Key property: (a + b) mod d = (a mod d + b mod d) mod d. Same for multiplication.",
    "PROBABILITY & STATISTICS: Probability = favorable outcomes / total outcomes. P(A or B) = P(A) + P(B) \u2212 P(A and B). For independent events: P(A and B) = P(A) \u00d7 P(B). Mean = sum/count. Median = middle value (or average of two middle values). Mode = most frequent. Range = max \u2212 min. Standard deviation measures spread from the mean: larger SD = more spread out. Adding a constant to all values does NOT change SD. Multiplying all values by k multiplies SD by |k|.",
    "COORDINATE GEOMETRY: Slope = (y\u2082 \u2212 y\u2081)/(x\u2082 \u2212 x\u2081). Positive slope: line rises left to right. Negative: falls. Zero: horizontal. Undefined: vertical. Slope-intercept form: y = mx + b (m = slope, b = y-intercept). Point-slope form: y \u2212 y\u2081 = m(x \u2212 x\u2081). Distance between two points: \u221a[(x\u2082\u2212x\u2081)\u00b2 + (y\u2082\u2212y\u2081)\u00b2]. Midpoint: ((x\u2081+x\u2082)/2, (y\u2081+y\u2082)/2). Parallel lines have equal slopes. Perpendicular lines have slopes that are negative reciprocals (m\u2081 \u00d7 m\u2082 = \u22121)."
  ],
  formulas: [
    "Percent change = ((New \u2212 Old) / Old) \u00d7 100%. Successive changes: multiply the multipliers. Example: 20% increase then 10% decrease = 1.20 \u00d7 0.90 = 1.08, or an 8% net increase.",
    "Distance = Rate \u00d7 Time. Combined work rate: 1/T = 1/a + 1/b. Average speed (round trip) = 2r\u2081r\u2082/(r\u2081 + r\u2082).",
    "Quadratic formula: x = (\u2212b \u00b1 \u221a(b\u00b2 \u2212 4ac)) / (2a). Discriminant b\u00b2 \u2212 4ac: if > 0 \u2192 2 real roots, if = 0 \u2192 1 repeated root, if < 0 \u2192 no real roots.",
    "Slope = (y\u2082 \u2212 y\u2081)/(x\u2082 \u2212 x\u2081). Distance = \u221a[(x\u2082 \u2212 x\u2081)\u00b2 + (y\u2082 \u2212 y\u2081)\u00b2]. Midpoint = ((x\u2081 + x\u2082)/2, (y\u2081 + y\u2082)/2).",
    "Probability: P(A or B) = P(A) + P(B) \u2212 P(A and B). For independent events: P(A and B) = P(A) \u00d7 P(B). Combinations: C(n,r) = n! / (r!(n\u2212r)!)."
  ],
  tips: [
    "For percentage QCs, watch for the 'reverse percentage' trap. If a price increases by 25%, you need a 20% decrease (not 25%) to return to the original: 100 \u00d7 1.25 = 125, and 125 \u00d7 0.80 = 100. The decrease percentage is always SMALLER than the increase percentage for the same dollar change.",
    "For rate/work problems, always set up a rate table with columns for Rate, Time, and Work (or Distance). Fill in what you know, solve for what you don't. This prevents errors in setting up equations.",
    "For coordinate geometry QCs, sketch a quick graph. Many problems become visually obvious once you plot the points or lines. Don't try to solve everything algebraically \u2014 a picture is often faster.",
    "For probability, draw a tree diagram or use a table for conditional probability. The GRE tests 'at least one' problems frequently: P(at least one) = 1 \u2212 P(none). Example: probability of at least one head in 3 flips = 1 \u2212 (1/2)\u00b3 = 7/8.",
    "For statistics QCs comparing means or medians: adding a value above the mean raises the mean. Adding a value equal to the median doesn't change the median if the set has odd count. Standard deviation = 0 only when ALL values are identical."
  ],
  questions: [
    {
      q: "A price increases by 20% and then decreases by 20%.\nColumn A: The final price\nColumn B: The original price",
      a: "Answer: B. Let the original price be 100. After a 20% increase: 100 \u00d7 1.20 = 120. After a 20% decrease: 120 \u00d7 0.80 = 96. The final price (96) is less than the original (100). This always happens because the percentage decrease applies to a LARGER base. Algebraically: P \u00d7 1.20 \u00d7 0.80 = P \u00d7 0.96 = 0.96P < P. Column B is greater."
    },
    {
      q: "Machine A produces 100 widgets in 5 hours. Machine B produces 100 widgets in 4 hours.\nColumn A: The number of widgets both machines produce together in 2 hours\nColumn B: 90",
      a: "Answer: C. Rate of A = 100/5 = 20 widgets/hour. Rate of B = 100/4 = 25 widgets/hour. Combined rate = 45 widgets/hour. In 2 hours: 45 \u00d7 2 = 90 widgets. Col A = 90 = Col B. The answer is C."
    },
    {
      q: "Set S = {3, 5, 7, 9, 11}. Set T is formed by adding 10 to each element of S, so T = {13, 15, 17, 19, 21}.\nColumn A: Standard deviation of S\nColumn B: Standard deviation of T",
      a: "Answer: C. Adding the same constant (10) to every element shifts the entire data set but does NOT change the spread. The deviations from the mean remain the same because the mean also shifts by 10. Therefore the standard deviation is unchanged. Col A = Col B. The answer is C."
    },
    {
      q: "Line m has slope 2 and passes through (1, 3). Line n is perpendicular to m.\nColumn A: Slope of line n\nColumn B: \u22121",
      a: "Answer: A. Perpendicular lines have slopes that are negative reciprocals. Slope of m = 2, so slope of n = \u22121/2. Col A = \u22121/2. Col B = \u22121. Since \u22121/2 > \u22121 (on the number line, \u22121/2 is to the right of \u22121), Column A is greater."
    },
    {
      q: "A bag contains 5 red and 3 blue marbles. Two marbles are drawn at random without replacement.\nColumn A: Probability that both are red\nColumn B: Probability that one is red and one is blue",
      a: "Answer: B. P(both red) = (5/8)(4/7) = 20/56 = 5/14. P(one red, one blue) = P(red then blue) + P(blue then red) = (5/8)(3/7) + (3/8)(5/7) = 15/56 + 15/56 = 30/56 = 15/28. Compare 5/14 = 10/28 vs 15/28. Since 15/28 > 10/28, Column B is greater."
    },
    {
      q: "x and y are positive integers such that x + y = 12.\nColumn A: xy\nColumn B: 35",
      a: "Answer: D. By AM-GM, the maximum of xy occurs when x = y = 6: xy = 36. Test other splits: x = 1, y = 11: xy = 11 < 35, B wins. x = 5, y = 7: xy = 35, A = B. x = 6, y = 6: xy = 36 > 35, A wins. Since we get B > A, A = B, and A > B for different valid values, the answer is D."
    }
  ]
}
    ]
  }
];
