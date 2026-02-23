# ═══════════════════════════════════════════════════════════════
# GRE Verbal Practice — Question Data
# Extracted from GRE Verbal practice sets (high-band difficulty)
# ═══════════════════════════════════════════════════════════════

VERBAL_CATEGORIES = [
    {"id": "text-completion", "name": "Text Completion", "icon": "TC"},
    {"id": "sentence-equivalence", "name": "Sentence Equivalence", "icon": "SE"},
    {"id": "reading-comp", "name": "Reading Comprehension", "icon": "RC"},
]

# ───────────────────────────────────────────────────
# TEXT COMPLETION — 1 BLANK
# ───────────────────────────────────────────────────
_tc_1blank = {
    "id": "tc-1-blank",
    "title": "Text Completion — 1 Blank",
    "icon": "1",
    "category": "text-completion",
    "sections": [
        {
            "type": "Text Completion — 1 Blank",
            "instructions": "For each blank select <strong>one</strong> entry from the corresponding column of choices. Fill all blanks in the way that best completes the text.",
            "questions": [
                {
                    "id": 1,
                    "stem": "What seemed at first to be an innovative framework turned out to be largely _____, drawing heavily from earlier, uncredited theories.",
                    "choices": ["(A) derivative", "(B) groundbreaking", "(C) iconoclastic", "(D) prescient", "(E) revolutionary"],
                    "answer": "(A) derivative",
                    "explanation": "The sentence contrasts initial perception ('innovative') with reality ('drawing from earlier theories'), indicating the framework was unoriginal — i.e., derivative."
                },
                {
                    "id": 2,
                    "stem": "The researcher's findings were not merely controversial; they were genuinely _____, challenging foundational assumptions in the field.",
                    "choices": ["(A) derivative", "(B) incendiary", "(C) orthodox", "(D) pedestrian", "(E) conventional"],
                    "answer": "(B) incendiary",
                    "explanation": "'Not merely controversial' signals something even stronger. 'Incendiary' means provocative/inflammatory — stronger than controversial and consistent with 'challenging foundational assumptions.'"
                },
                {
                    "id": 3,
                    "stem": "Far from being a spontaneous uprising, the movement was carefully _____, orchestrated by a small cadre of strategists.",
                    "choices": ["(A) improvised", "(B) orchestrated", "(C) haphazard", "(D) organic", "(E) impetuous"],
                    "answer": "(B) orchestrated",
                    "explanation": "'Far from being spontaneous' and 'orchestrated by a small cadre' both point to deliberate planning. The blank is restated by the appositive."
                },
                {
                    "id": 4,
                    "stem": "The study's conclusions were not merely tentative; they were explicitly _____, acknowledging the provisional nature of the evidence.",
                    "choices": ["(A) dogmatic", "(B) categorical", "(C) circumspect", "(D) unequivocal", "(E) definitive"],
                    "answer": "(C) circumspect",
                    "explanation": "'Acknowledging the provisional nature of the evidence' indicates caution and careful consideration — circumspect."
                },
                {
                    "id": 5,
                    "stem": "His explanation was so _____ that it raised more questions than it answered.",
                    "choices": ["(A) comprehensive", "(B) convoluted", "(C) lucid", "(D) methodical", "(E) systematic"],
                    "answer": "(B) convoluted",
                    "explanation": "If an explanation raises more questions than it answers, it must be confusing and overly complex — convoluted."
                },
                {
                    "id": 6,
                    "stem": "The scientist's explanation was so _____ that even specialists disagreed about its implications.",
                    "choices": ["(A) lucid", "(B) transparent", "(C) convoluted", "(D) straightforward", "(E) accessible"],
                    "answer": "(C) convoluted",
                    "explanation": "If even specialists disagree about implications, the explanation must be complex and hard to parse — convoluted."
                },
                {
                    "id": 7,
                    "stem": "Though marketed as revolutionary, the product was largely _____.",
                    "choices": ["(A) derivative", "(B) groundbreaking", "(C) unprecedented", "(D) innovative", "(E) radical"],
                    "answer": "(A) derivative",
                    "explanation": "'Though' sets up a contrast with 'revolutionary.' Derivative (unoriginal) is the opposite."
                },
                {
                    "id": 8,
                    "stem": "His apology sounded sincere but ultimately felt _____.",
                    "choices": ["(A) heartfelt", "(B) contrite", "(C) perfunctory", "(D) candid", "(E) earnest"],
                    "answer": "(C) perfunctory",
                    "explanation": "'Sounded sincere but' sets up a contrast. Perfunctory means done without care or genuine feeling."
                },
                {
                    "id": 9,
                    "stem": "The theory's influence proved surprisingly _____, reshaping debates across multiple disciplines.",
                    "choices": ["(A) negligible", "(B) trivial", "(C) catalytic", "(D) marginal", "(E) inconsequential"],
                    "answer": "(C) catalytic",
                    "explanation": "'Reshaping debates across multiple disciplines' shows major impact. Catalytic means sparking significant change."
                },
                {
                    "id": 10,
                    "stem": "Far from being impulsive, her decision was thoroughly _____.",
                    "choices": ["(A) rash", "(B) impetuous", "(C) calculated", "(D) erratic", "(E) spontaneous"],
                    "answer": "(C) calculated",
                    "explanation": "'Far from impulsive' and 'thoroughly' indicate deliberate planning — calculated."
                },
                {
                    "id": 11,
                    "stem": "The CEO's response was so _____ that investors questioned whether she grasped the severity of the crisis.",
                    "choices": ["(A) alarmist", "(B) measured", "(C) complacent", "(D) decisive", "(E) urgent"],
                    "answer": "(C) complacent",
                    "explanation": "If investors question whether she understands the severity, her response must have seemed too unconcerned — complacent."
                },
                {
                    "id": 12,
                    "stem": "What critics described as caution was, in reality, calculated _____.",
                    "choices": ["(A) recklessness", "(B) restraint", "(C) impulsiveness", "(D) imprudence", "(E) rashness"],
                    "answer": "(B) restraint",
                    "explanation": "Critics called it 'caution' and the sentence says it was 'calculated' — restraint is deliberate self-control, consistent with both."
                },
                {
                    "id": 13,
                    "stem": "The scientist's findings were hardly _____; they fundamentally altered prevailing assumptions.",
                    "choices": ["(A) revolutionary", "(B) trivial", "(C) groundbreaking", "(D) transformative", "(E) radical"],
                    "answer": "(B) trivial",
                    "explanation": "'Hardly _____' + 'fundamentally altered' = the findings WERE significant. So the blank needs a word meaning insignificant — trivial."
                },
                {
                    "id": 14,
                    "stem": "Her humor, though subtle, was unmistakably _____.",
                    "choices": ["(A) caustic", "(B) genial", "(C) benign", "(D) affable", "(E) cordial"],
                    "answer": "(A) caustic",
                    "explanation": "'Though subtle' sets up a contrast with something sharp or biting. 'Unmistakably' reinforces that the sharpness is clear despite subtlety. Caustic = sharply critical."
                },
                {
                    "id": 15,
                    "stem": "The article's tone was so _____ that readers struggled to discern the author's true position.",
                    "choices": ["(A) unequivocal", "(B) strident", "(C) equivocal", "(D) dogmatic", "(E) categorical"],
                    "answer": "(C) equivocal",
                    "explanation": "If readers can't discern the author's position, the tone must be ambiguous — equivocal."
                },
            ]
        }
    ]
}

# ───────────────────────────────────────────────────
# TEXT COMPLETION — 2 BLANK
# ───────────────────────────────────────────────────
_tc_2blank = {
    "id": "tc-2-blank",
    "title": "Text Completion — 2 Blank",
    "icon": "2",
    "category": "text-completion",
    "sections": [
        {
            "type": "Text Completion — 2 Blank",
            "instructions": "For each blank select <strong>one</strong> entry from the corresponding column of choices. Blank (i) corresponds to the first group of three choices; Blank (ii) corresponds to the second group.",
            "questions": [
                {
                    "id": 1,
                    "stem": "The scientist's objections were not <strong>Blank (i)</strong>; rather, they were couched in language so <strong>Blank (ii)</strong> that their critical thrust was almost imperceptible.",
                    "blank_choices": [
                        ["(A) strident", "(B) effusive", "(C) equivocal"],
                        ["(D) explicit", "(E) muted", "(F) vociferous"]
                    ],
                    "answer": "(A) strident, (E) muted",
                    "explanation": "'Not _____; rather, so _____ that critical thrust was imperceptible.' The objections weren't loud (strident); they were quiet (muted)."
                },
                {
                    "id": 2,
                    "stem": "The CEO's apology was so carefully worded that it appeared less an admission of fault than a calculated attempt to <strong>Blank (i)</strong> responsibility while projecting an image of <strong>Blank (ii)</strong> concern.",
                    "blank_choices": [
                        ["(A) assume", "(B) deflect", "(C) indifference"],
                        ["(D) contrition", "(E) apathy", "(F) sincerity"]
                    ],
                    "answer": "(B) deflect, (F) sincerity",
                    "explanation": "A 'calculated' apology that isn't a real admission of fault aims to deflect responsibility while appearing sincere."
                },
                {
                    "id": 3,
                    "stem": "The biographer's tone is not overtly critical; instead, it is so <strong>Blank (i)</strong> that her disapproval emerges only through faint but persistent notes of <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) caustic", "(B) measured", "(C) irony"],
                        ["(D) adulation", "(E) derision", "(F) restraint"]
                    ],
                    "answer": "(B) measured, (E) derision",
                    "explanation": "The tone is restrained (measured), and criticism comes through subtle mockery (derision)."
                },
                {
                    "id": 4,
                    "stem": "The editor's revisions were so <strong>Blank (i)</strong> that the original author scarcely recognized her own prose, which had been stripped of its characteristic <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) heavy-handed", "(B) meticulous", "(C) restraint"],
                        ["(D) flamboyance", "(E) subtlety", "(F) precision"]
                    ],
                    "answer": "(A) heavy-handed, (D) flamboyance",
                    "explanation": "If the author can't recognize her work, the revisions were extreme (heavy-handed), and they removed her distinctive style (flamboyance)."
                },
                {
                    "id": 5,
                    "stem": "The researcher expected the data to confirm her hypothesis; instead, the results were so <strong>Blank (i)</strong> that she was compelled to <strong>Blank (ii)</strong> her original claims.",
                    "blank_choices": [
                        ["(A) ambiguous", "(B) unequivocal", "(C) retract"],
                        ["(D) substantiate", "(E) revise", "(F) corroborate"]
                    ],
                    "answer": "(B) unequivocal, (E) revise",
                    "explanation": "'Instead' signals reversal. The results were clear (unequivocal) in contradicting her hypothesis, forcing her to revise her claims."
                },
                {
                    "id": 6,
                    "stem": "Although the mayor projected confidence, her policies were marked by <strong>Blank (i)</strong> and administrative <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) decisiveness", "(B) vacillation", "(C) efficiency"],
                        ["(D) paralysis", "(E) resolve", "(F) agility"]
                    ],
                    "answer": "(B) vacillation, (D) paralysis",
                    "explanation": "'Although' sets up contrast with 'confidence.' Her policies showed indecision (vacillation) and inability to act (paralysis)."
                },
                {
                    "id": 7,
                    "stem": "Because the evidence was so <strong>Blank (i)</strong>, the board felt compelled to <strong>Blank (ii)</strong> its earlier conclusions.",
                    "blank_choices": [
                        ["(A) compelling", "(B) ambiguous", "(C) reaffirm"],
                        ["(D) retract", "(E) ignore", "(F) substantiate"]
                    ],
                    "answer": "(A) compelling, (D) retract",
                    "explanation": "Compelling evidence that contradicts earlier conclusions would force the board to retract them."
                },
                {
                    "id": 8,
                    "stem": "The report initially appears balanced; closer inspection reveals it to be subtly <strong>Blank (i)</strong> and rhetorically <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) objective", "(B) partisan", "(C) restrained"],
                        ["(D) manipulative", "(E) neutral", "(F) measured"]
                    ],
                    "answer": "(B) partisan, (D) manipulative",
                    "explanation": "'Initially appears balanced' but 'closer inspection reveals' a hidden bias (partisan) and persuasion tactics (manipulative)."
                },
                {
                    "id": 9,
                    "stem": "Her critique was so <strong>Blank (i)</strong> that it bordered on <strong>Blank (ii)</strong>, despite its sharp implications.",
                    "blank_choices": [
                        ["(A) mild", "(B) scathing", "(C) praise"],
                        ["(D) condemnation", "(E) restraint", "(F) hostility"]
                    ],
                    "answer": "(A) mild, (C) praise",
                    "explanation": "The critique had 'sharp implications' but was delivered so mildly it almost sounded like praise."
                },
                {
                    "id": 10,
                    "stem": "The reform was intended to reduce complexity but instead <strong>Blank (i)</strong> bureaucracy and <strong>Blank (ii)</strong> confusion.",
                    "blank_choices": [
                        ["(A) streamlined", "(B) intensified", "(C) clarified"],
                        ["(D) exacerbated", "(E) minimized", "(F) simplified"]
                    ],
                    "answer": "(B) intensified, (D) exacerbated",
                    "explanation": "'Intended to reduce but instead' signals the opposite effect: bureaucracy was intensified and confusion was exacerbated (made worse)."
                },
                {
                    "id": 11,
                    "stem": "The findings are not entirely <strong>Blank (i)</strong>; rather, they are insufficiently <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) invalid", "(B) conclusive", "(C) tentative"],
                        ["(D) definitive", "(E) erroneous", "(F) precise"]
                    ],
                    "answer": "(A) invalid, (D) definitive",
                    "explanation": "The findings aren't completely wrong (invalid), but they lack sufficient certainty — they're insufficiently definitive."
                },
                {
                    "id": 12,
                    "stem": "The experiment's design was both elegant and <strong>Blank (i)</strong>, balancing innovation with <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) cumbersome", "(B) meticulous", "(C) clarity"],
                        ["(D) chaos", "(E) precision", "(F) confusion"]
                    ],
                    "answer": "(B) meticulous, (E) precision",
                    "explanation": "'Elegant and _____' are parallel positives. 'Balancing innovation with _____' = precision complements innovation."
                },
                {
                    "id": 13,
                    "stem": "The initiative aimed to simplify regulations but instead <strong>Blank (i)</strong> compliance procedures and <strong>Blank (ii)</strong> administrative burdens.",
                    "blank_choices": [
                        ["(A) streamlined", "(B) complicated", "(C) reduced"],
                        ["(D) intensified", "(E) minimized", "(F) alleviated"]
                    ],
                    "answer": "(B) complicated, (D) intensified",
                    "explanation": "'Aimed to simplify but instead' signals opposite: procedures became complicated and burdens intensified."
                },
                {
                    "id": 14,
                    "stem": "The speech appears conciliatory; its underlying message, however, is unmistakably <strong>Blank (i)</strong> and politically <strong>Blank (ii)</strong>.",
                    "blank_choices": [
                        ["(A) moderate", "(B) inflammatory", "(C) pragmatic"],
                        ["(D) divisive", "(E) temperate", "(F) restrained"]
                    ],
                    "answer": "(B) inflammatory, (D) divisive",
                    "explanation": "'Appears conciliatory; however' signals contrast. The true message is inflammatory and politically divisive."
                },
            ]
        }
    ]
}

# ───────────────────────────────────────────────────
# TEXT COMPLETION — 3 BLANK
# ───────────────────────────────────────────────────
_tc_3blank = {
    "id": "tc-3-blank",
    "title": "Text Completion — 3 Blank",
    "icon": "3",
    "category": "text-completion",
    "sections": [
        {
            "type": "Text Completion — 3 Blank",
            "instructions": "For each blank select <strong>one</strong> entry from the corresponding column of choices. Blank (i) = first pair, Blank (ii) = second pair, Blank (iii) = third pair.",
            "questions": [
                {
                    "id": 1,
                    "stem": "Although the biographer claims neutrality, her portrayal of the reformer is subtly <strong>Blank (i)</strong>, selectively emphasizing episodes that <strong>Blank (ii)</strong> his failures while simultaneously <strong>Blank (iii)</strong> his rivals.",
                    "blank_choices": [
                        ["(A) hagiographic", "(B) impartial"],
                        ["(C) obscure", "(D) mitigate"],
                        ["(E) exacerbate", "(F) vilifying"]
                    ],
                    "answer": "(A) hagiographic, (D) mitigate, (F) vilifying",
                    "explanation": "Despite claiming neutrality, the biographer is hagiographic (worshipful), mitigating (downplaying) the subject's failures, and vilifying (attacking) his rivals."
                },
                {
                    "id": 2,
                    "stem": "Although the novelist was once dismissed as <strong>Blank (i)</strong>, recent scholarship has revealed the <strong>Blank (ii)</strong> sophistication of her narrative structures, which subtly <strong>Blank (iii)</strong> conventional genre expectations.",
                    "blank_choices": [
                        ["(A) formulaic", "(B) innovative"],
                        ["(C) latent", "(D) superficial"],
                        ["(E) subvert", "(F) replicate"]
                    ],
                    "answer": "(A) formulaic, (C) latent, (E) subvert",
                    "explanation": "Dismissed as formulaic (unoriginal), but scholarship reveals latent (hidden) sophistication that subverts (undermines) genre expectations."
                },
                {
                    "id": 3,
                    "stem": "Although the economist's early work was dismissed as <strong>Blank (i)</strong>, later analyses revealed a theoretical rigor that not only <strong>Blank (ii)</strong> prevailing assumptions but also <strong>Blank (iii)</strong> alternative models once thought incompatible.",
                    "blank_choices": [
                        ["(A) speculative", "(B) orthodox"],
                        ["(C) destabilized", "(D) reinforced"],
                        ["(E) reconciled", "(F) trivialized"]
                    ],
                    "answer": "(A) speculative, (C) destabilized, (E) reconciled",
                    "explanation": "Dismissed as speculative, but the work destabilized (challenged) prevailing assumptions and reconciled (harmonized) seemingly incompatible models."
                },
                {
                    "id": 4,
                    "stem": "Though the philosopher is often portrayed as a political radical, her writings reveal a fundamentally <strong>Blank (i)</strong> disposition, one that seeks not to <strong>Blank (ii)</strong> existing institutions but to <strong>Blank (iii)</strong> them through gradual reform.",
                    "blank_choices": [
                        ["(A) incendiary", "(B) conservative"],
                        ["(C) dismantle", "(D) preserve"],
                        ["(E) recalibrate", "(F) destabilize"]
                    ],
                    "answer": "(B) conservative, (C) dismantle, (E) recalibrate",
                    "explanation": "Portrayed as radical but actually conservative — not seeking to dismantle institutions but to recalibrate (adjust) them gradually."
                },
                {
                    "id": 5,
                    "stem": "The activist's rhetoric, once celebrated as visionary, now strikes many observers as <strong>Blank (i)</strong>; what was previously seen as bold has become, in a changed political climate, merely <strong>Blank (ii)</strong>, and her proposals appear less designed to <strong>Blank (iii)</strong> injustice than to provoke attention.",
                    "blank_choices": [
                        ["(A) prescient", "(B) anachronistic"],
                        ["(C) incendiary", "(D) banal"],
                        ["(E) remedy", "(F) court"]
                    ],
                    "answer": "(B) anachronistic, (D) banal, (E) remedy",
                    "explanation": "Once visionary, now anachronistic (outdated). Bold became banal (trite). Proposals seem less about remedying injustice than provoking attention."
                },
                {
                    "id": 6,
                    "stem": "Although once dismissed as <strong>Blank (i)</strong>, the theory later proved <strong>Blank (ii)</strong>, offering insights that <strong>Blank (iii)</strong> conventional wisdom.",
                    "blank_choices": [
                        ["(A) trivial", "(B) profound"],
                        ["(C) reinforced", "(D) challenged"],
                        ["(E) ignored", "(F) superficial"]
                    ],
                    "answer": "(A) trivial, (B) profound, (D) challenged",
                    "explanation": "Dismissed as trivial but proved profound, with insights that challenged conventional wisdom."
                },
                {
                    "id": 7,
                    "stem": "Because the diplomat's remarks were so <strong>Blank (i)</strong>, they neither <strong>Blank (ii)</strong> tensions nor <strong>Blank (iii)</strong> suspicion.",
                    "blank_choices": [
                        ["(A) conciliatory", "(B) inflamed"],
                        ["(C) eased", "(D) heightened"],
                        ["(E) resolved", "(F) aggravated"]
                    ],
                    "answer": "(A) conciliatory, (C) eased, (F) aggravated",
                    "explanation": "Conciliatory remarks would be expected to ease tensions and not aggravate suspicion — but 'neither...nor' means they failed at both."
                },
                {
                    "id": 8,
                    "stem": "The movement's rhetoric seems <strong>Blank (i)</strong>, yet its objectives are distinctly <strong>Blank (ii)</strong>, designed less to disrupt than to <strong>Blank (iii)</strong>.",
                    "blank_choices": [
                        ["(A) incendiary", "(B) moderate"],
                        ["(C) dismantle", "(D) stabilize"],
                        ["(E) preserve", "(F) radical"]
                    ],
                    "answer": "(A) incendiary, (B) moderate, (E) preserve",
                    "explanation": "Rhetoric seems incendiary (radical), but objectives are moderate — designed to preserve rather than disrupt."
                },
                {
                    "id": 9,
                    "stem": "Though framed as a critique, the essay is surprisingly <strong>Blank (i)</strong>, its arguments ultimately serving to <strong>Blank (ii)</strong> the institution it purports to <strong>question</strong>.",
                    "blank_choices": [
                        ["(A) deferential", "(B) subversive"],
                        ["(C) undermine", "(D) reinforce"],
                        ["(E) destabilize", "(F) attack"]
                    ],
                    "answer": "(A) deferential, (D) reinforce",
                    "explanation": "Though framed as critique, the essay is deferential (respectful) and actually reinforces the institution — the opposite of what you'd expect."
                },
                {
                    "id": 10,
                    "stem": "What once appeared <strong>Blank (i)</strong> now seems merely <strong>Blank (ii)</strong>, its novelty having been <strong>Blank (iii)</strong> by repetition.",
                    "blank_choices": [
                        ["(A) revolutionary", "(B) banal"],
                        ["(C) diminished", "(D) magnified"],
                        ["(E) groundbreaking", "(F) intensified"]
                    ],
                    "answer": "(A) revolutionary, (B) banal, (C) diminished",
                    "explanation": "What was revolutionary now seems banal (boring/commonplace), its novelty diminished by repetition."
                },
                {
                    "id": 11,
                    "stem": "Because the data were so <strong>Blank (i)</strong>, critics struggled to <strong>Blank (ii)</strong> the study's conclusions, which in turn <strong>Blank (iii)</strong> further research.",
                    "blank_choices": [
                        ["(A) compelling", "(B) ambiguous"],
                        ["(C) dispute", "(D) substantiate"],
                        ["(E) encouraged", "(F) curtailed"]
                    ],
                    "answer": "(A) compelling, (C) dispute, (E) encouraged",
                    "explanation": "Compelling data made it hard for critics to dispute the conclusions, which encouraged further research."
                },
                {
                    "id": 12,
                    "stem": "Though initially regarded as <strong>Blank (i)</strong>, the initiative proved unexpectedly <strong>Blank (ii)</strong>, gradually <strong>Blank (iii)</strong> public support.",
                    "blank_choices": [
                        ["(A) trivial", "(B) influential"],
                        ["(C) eroding", "(D) garnering"],
                        ["(E) negligible", "(F) marginal"]
                    ],
                    "answer": "(A) trivial, (B) influential, (D) garnering",
                    "explanation": "Initially regarded as trivial but proved influential, garnering (gaining) public support."
                },
                {
                    "id": 13,
                    "stem": "The philosopher's critique, while seemingly <strong>Blank (i)</strong>, is fundamentally <strong>Blank (ii)</strong>, aiming to <strong>Blank (iii)</strong> rather than dismantle prevailing theories.",
                    "blank_choices": [
                        ["(A) radical", "(B) reformist"],
                        ["(C) refine", "(D) destroy"],
                        ["(E) incendiary", "(F) temperate"]
                    ],
                    "answer": "(A) radical, (B) reformist, (C) refine",
                    "explanation": "Seems radical but is fundamentally reformist, aiming to refine (improve) rather than dismantle."
                },
                {
                    "id": 14,
                    "stem": "Although the novelist's early work was dismissed as <strong>Blank (i)</strong>, later critics recognized its <strong>Blank (ii)</strong> depth and the way it subtly <strong>Blank (iii)</strong> genre conventions.",
                    "blank_choices": [
                        ["(A) formulaic", "(B) profound"],
                        ["(C) subverted", "(D) reinforced"],
                        ["(E) derivative", "(F) superficial"]
                    ],
                    "answer": "(A) formulaic, (B) profound, (C) subverted",
                    "explanation": "Dismissed as formulaic, but later recognized for profound depth and subverting genre conventions."
                },
                {
                    "id": 15,
                    "stem": "The policy's rhetoric appears <strong>Blank (i)</strong>, yet its implementation has proven remarkably <strong>Blank (ii)</strong>, designed less to disrupt markets than to <strong>Blank (iii)</strong> them.",
                    "blank_choices": [
                        ["(A) radical", "(B) moderate"],
                        ["(C) destabilize", "(D) stabilize"],
                        ["(E) incendiary", "(F) reform"]
                    ],
                    "answer": "(A) radical, (B) moderate, (D) stabilize",
                    "explanation": "Rhetoric appears radical but implementation is moderate, aiming to stabilize rather than disrupt."
                },
                {
                    "id": 16,
                    "stem": "Because the data were so <strong>Blank (i)</strong>, researchers struggled to <strong>Blank (ii)</strong> the anomaly, which in turn <strong>Blank (iii)</strong> confidence in the model.",
                    "blank_choices": [
                        ["(A) consistent", "(B) anomalous"],
                        ["(C) explain", "(D) ignore"],
                        ["(E) undermined", "(F) reinforced"]
                    ],
                    "answer": "(B) anomalous, (C) explain, (E) undermined",
                    "explanation": "Anomalous data made it hard to explain the irregularity, which undermined confidence in the model."
                },
            ]
        }
    ]
}

# ───────────────────────────────────────────────────
# SENTENCE EQUIVALENCE — 50 Questions
# ───────────────────────────────────────────────────
_se_practice = {
    "id": "se-practice",
    "title": "Sentence Equivalence",
    "icon": "=",
    "category": "sentence-equivalence",
    "sections": [
        {
            "type": "Sentence Equivalence",
            "instructions": "Select <strong>two</strong> answer choices that, when used to complete the sentence, fit the meaning of the sentence as a whole and produce completed sentences that are alike in meaning.",
            "multi_select": True,
            "questions": [
                {"id": 1, "stem": "The CEO's response to the crisis was so _____ that investors lost confidence in her leadership.", "choices": ["(A) decisive", "(B) resolute", "(C) vacillating", "(D) wavering", "(E) steadfast", "(F) adamant"], "answer": "(C) vacillating, (D) wavering", "explanation": "Both mean showing indecision, which would cause investors to lose confidence."},
                {"id": 2, "stem": "The professor's lecture was so _____ that even advanced students struggled to follow it.", "choices": ["(A) lucid", "(B) transparent", "(C) abstruse", "(D) recondite", "(E) accessible", "(F) straightforward"], "answer": "(C) abstruse, (D) recondite", "explanation": "Both mean difficult to understand, fitting 'even advanced students struggled.'"},
                {"id": 3, "stem": "Though initially dismissed, the theory proved surprisingly _____ in shaping subsequent research.", "choices": ["(A) negligible", "(B) catalytic", "(C) transformative", "(D) trivial", "(E) inconsequential", "(F) marginal"], "answer": "(B) catalytic, (C) transformative", "explanation": "Both indicate significant impact — catalytic (sparking change) and transformative (fundamentally altering)."},
                {"id": 4, "stem": "The diplomat's tone was carefully _____, avoiding both praise and condemnation.", "choices": ["(A) strident", "(B) measured", "(C) inflammatory", "(D) restrained", "(E) vitriolic", "(F) caustic"], "answer": "(B) measured, (D) restrained", "explanation": "Both mean controlled and moderate in expression."},
                {"id": 5, "stem": "The critic's review was so _____ that it was nearly indistinguishable from mild approval.", "choices": ["(A) scathing", "(B) tepid", "(C) caustic", "(D) lukewarm", "(E) vitriolic", "(F) incendiary"], "answer": "(B) tepid, (D) lukewarm", "explanation": "Both mean lacking enthusiasm or force — so mild it seemed like faint approval."},
                {"id": 6, "stem": "Her explanation was so _____ that it clarified even the most complex details.", "choices": ["(A) convoluted", "(B) lucid", "(C) opaque", "(D) pellucid", "(E) abstruse", "(F) arcane"], "answer": "(B) lucid, (D) pellucid", "explanation": "Both mean extremely clear and easy to understand."},
                {"id": 7, "stem": "The proposal was dismissed as _____, offering little more than recycled ideas.", "choices": ["(A) innovative", "(B) derivative", "(C) groundbreaking", "(D) original", "(E) trite", "(F) unprecedented"], "answer": "(B) derivative, (E) trite", "explanation": "Both mean unoriginal — derivative (borrowed) and trite (overused)."},
                {"id": 8, "stem": "The ambassador's remarks were deliberately _____, revealing little about her actual position.", "choices": ["(A) candid", "(B) forthright", "(C) evasive", "(D) equivocal", "(E) transparent", "(F) explicit"], "answer": "(C) evasive, (D) equivocal", "explanation": "Both mean avoiding direct or clear communication."},
                {"id": 9, "stem": "The historian's account was not hostile but subtly _____, casting doubt through understatement.", "choices": ["(A) laudatory", "(B) deferential", "(C) skeptical", "(D) incredulous", "(E) admiring", "(F) effusive"], "answer": "(C) skeptical, (D) incredulous", "explanation": "Both convey doubt — skeptical (questioning) and incredulous (disbelieving)."},
                {"id": 10, "stem": "The researcher's findings were so _____ that they overturned decades of consensus.", "choices": ["(A) trivial", "(B) revolutionary", "(C) transformative", "(D) negligible", "(E) marginal", "(F) inconsequential"], "answer": "(B) revolutionary, (C) transformative", "explanation": "Both indicate dramatic, paradigm-shifting impact."},
                {"id": 11, "stem": "The committee's recommendation was so _____ that it satisfied no one.", "choices": ["(A) categorical", "(B) unequivocal", "(C) ambiguous", "(D) equivocal", "(E) decisive", "(F) resolute"], "answer": "(C) ambiguous, (D) equivocal", "explanation": "Both mean unclear or open to multiple interpretations, frustrating all parties."},
                {"id": 12, "stem": "His generosity was so _____ that even competitors acknowledged it.", "choices": ["(A) grudging", "(B) magnanimous", "(C) benevolent", "(D) resentful", "(E) reluctant", "(F) miserly"], "answer": "(B) magnanimous, (C) benevolent", "explanation": "Both mean showing generous and kind spirit."},
                {"id": 13, "stem": "The scientist's conclusions were appropriately _____, reflecting the limited scope of the data.", "choices": ["(A) dogmatic", "(B) categorical", "(C) tentative", "(D) provisional", "(E) unequivocal", "(F) definitive"], "answer": "(C) tentative, (D) provisional", "explanation": "Both mean cautious and not final — appropriate given limited data."},
                {"id": 14, "stem": "The author's satire was so _____ that many readers failed to detect its criticism.", "choices": ["(A) blatant", "(B) subtle", "(C) understated", "(D) obvious", "(E) overt", "(F) explicit"], "answer": "(B) subtle, (C) understated", "explanation": "Both mean not immediately apparent, explaining why readers missed the criticism."},
                {"id": 15, "stem": "The policy's impact was unexpectedly _____, reshaping institutions far beyond its intended scope.", "choices": ["(A) negligible", "(B) catalytic", "(C) marginal", "(D) transformative", "(E) trivial", "(F) inconsequential"], "answer": "(B) catalytic, (D) transformative", "explanation": "Both indicate significant, far-reaching influence."},
                {"id": 16, "stem": "The lawyer's argument was so _____ that even experts disagreed about its meaning.", "choices": ["(A) transparent", "(B) lucid", "(C) convoluted", "(D) intricate", "(E) obvious", "(F) straightforward"], "answer": "(C) convoluted, (D) intricate", "explanation": "Both mean complex and difficult to follow."},
                {"id": 17, "stem": "The executive's apology sounded sincere but felt strangely _____.", "choices": ["(A) heartfelt", "(B) genuine", "(C) perfunctory", "(D) mechanical", "(E) earnest", "(F) candid"], "answer": "(C) perfunctory, (D) mechanical", "explanation": "Both suggest going through the motions without genuine feeling."},
                {"id": 18, "stem": "The novelist's early work was unfairly dismissed as _____, though later critics recognized its depth.", "choices": ["(A) superficial", "(B) trivial", "(C) profound", "(D) insightful", "(E) significant", "(F) meaningful"], "answer": "(A) superficial, (B) trivial", "explanation": "Both mean lacking depth — the unfair dismissal, later corrected."},
                {"id": 19, "stem": "Her criticism was so _____ that it bordered on hostility.", "choices": ["(A) mild", "(B) caustic", "(C) scathing", "(D) restrained", "(E) temperate", "(F) moderate"], "answer": "(B) caustic, (C) scathing", "explanation": "Both mean harshly critical, approaching hostility."},
                {"id": 20, "stem": "The philosopher's theory is so _____ that it resists simplistic categorization.", "choices": ["(A) reductive", "(B) nuanced", "(C) simplistic", "(D) multifaceted", "(E) elementary", "(F) rudimentary"], "answer": "(B) nuanced, (D) multifaceted", "explanation": "Both mean complex with many aspects, resisting oversimplification."},
                {"id": 21, "stem": "The CEO's strategy was so _____ that employees struggled to anticipate her decisions.", "choices": ["(A) predictable", "(B) erratic", "(C) consistent", "(D) capricious", "(E) stable", "(F) steady"], "answer": "(B) erratic, (D) capricious", "explanation": "Both mean unpredictable and changeable."},
                {"id": 22, "stem": "The biologist's explanation was both _____ and precise.", "choices": ["(A) vague", "(B) lucid", "(C) opaque", "(D) clear", "(E) ambiguous", "(F) obscure"], "answer": "(B) lucid, (D) clear", "explanation": "Both mean easy to understand — parallel with 'precise.'"},
                {"id": 23, "stem": "The report's tone was so _____ that it provoked immediate backlash.", "choices": ["(A) conciliatory", "(B) inflammatory", "(C) incendiary", "(D) moderate", "(E) temperate", "(F) restrained"], "answer": "(B) inflammatory, (C) incendiary", "explanation": "Both mean provoking strong reactions, consistent with immediate backlash."},
                {"id": 24, "stem": "His enthusiasm bordered on _____, overwhelming even supportive colleagues.", "choices": ["(A) indifference", "(B) zeal", "(C) fervor", "(D) apathy", "(E) lethargy", "(F) passivity"], "answer": "(B) zeal, (C) fervor", "explanation": "Both mean intense enthusiasm or passion."},
                {"id": 25, "stem": "The study's findings were so _____ that they demanded immediate reconsideration of policy.", "choices": ["(A) trivial", "(B) consequential", "(C) insignificant", "(D) momentous", "(E) marginal", "(F) negligible"], "answer": "(B) consequential, (D) momentous", "explanation": "Both mean highly significant and important."},
                {"id": 26, "stem": "The diplomat's carefully worded statement was deliberately _____, avoiding clear commitments.", "choices": ["(A) explicit", "(B) unequivocal", "(C) ambiguous", "(D) equivocal", "(E) direct", "(F) forthright"], "answer": "(C) ambiguous, (D) equivocal", "explanation": "Both mean intentionally unclear."},
                {"id": 27, "stem": "The critic's dismissal of the film was so _____ that it seemed almost personal.", "choices": ["(A) benign", "(B) caustic", "(C) acerbic", "(D) mild", "(E) genial", "(F) cordial"], "answer": "(B) caustic, (C) acerbic", "explanation": "Both mean sharply critical and biting."},
                {"id": 28, "stem": "The proposal's modest appearance masked its _____ implications.", "choices": ["(A) trivial", "(B) far-reaching", "(C) superficial", "(D) profound", "(E) minor", "(F) negligible"], "answer": "(B) far-reaching, (D) profound", "explanation": "Both indicate significant, deep implications hidden behind a modest exterior."},
                {"id": 29, "stem": "The engineer's design was remarkably _____, combining simplicity with elegance.", "choices": ["(A) cumbersome", "(B) unwieldy", "(C) streamlined", "(D) efficient", "(E) chaotic", "(F) disorderly"], "answer": "(C) streamlined, (D) efficient", "explanation": "Both describe a design that is well-optimized and elegant."},
                {"id": 30, "stem": "Her remarks were so _____ that they revealed nothing of substance.", "choices": ["(A) candid", "(B) forthright", "(C) vacuous", "(D) empty", "(E) sincere", "(F) genuine"], "answer": "(C) vacuous, (D) empty", "explanation": "Both mean lacking content or substance."},
                {"id": 31, "stem": "The scholar's interpretation was quietly _____, subtly challenging established views.", "choices": ["(A) orthodox", "(B) subversive", "(C) conservative", "(D) revisionist", "(E) traditional", "(F) conventional"], "answer": "(B) subversive, (D) revisionist", "explanation": "Both mean challenging the established order, though in a subtle way."},
                {"id": 32, "stem": "The presentation was so _____ that audience members lost interest midway through.", "choices": ["(A) riveting", "(B) tedious", "(C) captivating", "(D) monotonous", "(E) engaging", "(F) compelling"], "answer": "(B) tedious, (D) monotonous", "explanation": "Both mean boring and repetitive."},
                {"id": 33, "stem": "The policy's effects were so _____ that regulators could not ignore them.", "choices": ["(A) negligible", "(B) pervasive", "(C) widespread", "(D) trivial", "(E) marginal", "(F) insignificant"], "answer": "(B) pervasive, (C) widespread", "explanation": "Both mean extending broadly, making them impossible to ignore."},
                {"id": 34, "stem": "The CEO's optimism appeared _____ given the mounting evidence of failure.", "choices": ["(A) justified", "(B) warranted", "(C) misplaced", "(D) unfounded", "(E) reasonable", "(F) rational"], "answer": "(C) misplaced, (D) unfounded", "explanation": "Both mean lacking a proper basis — inappropriate given evidence of failure."},
                {"id": 35, "stem": "The article's tone was so _____ that readers could not determine whether it was satire.", "choices": ["(A) earnest", "(B) ironic", "(C) sincere", "(D) deadpan", "(E) candid", "(F) forthright"], "answer": "(B) ironic, (D) deadpan", "explanation": "Both describe a tone that masks true intent, making it hard to tell if it's satire."},
                {"id": 36, "stem": "The lawyer's strategy was surprisingly _____, prioritizing compromise over confrontation.", "choices": ["(A) combative", "(B) conciliatory", "(C) aggressive", "(D) accommodating", "(E) hostile", "(F) adversarial"], "answer": "(B) conciliatory, (D) accommodating", "explanation": "Both mean seeking agreement rather than conflict."},
                {"id": 37, "stem": "The scientist's conclusions were so _____ that they left little room for doubt.", "choices": ["(A) tentative", "(B) definitive", "(C) conclusive", "(D) provisional", "(E) uncertain", "(F) ambiguous"], "answer": "(B) definitive, (C) conclusive", "explanation": "Both mean final and decisive, leaving no doubt."},
                {"id": 38, "stem": "The CEO's leadership style was widely regarded as _____, fostering loyalty and trust.", "choices": ["(A) tyrannical", "(B) benevolent", "(C) magnanimous", "(D) oppressive", "(E) despotic", "(F) autocratic"], "answer": "(B) benevolent, (C) magnanimous", "explanation": "Both mean kind and generous, inspiring loyalty."},
                {"id": 39, "stem": "The debate grew increasingly _____, with participants interrupting one another.", "choices": ["(A) cordial", "(B) civil", "(C) acrimonious", "(D) contentious", "(E) amicable", "(F) congenial"], "answer": "(C) acrimonious, (D) contentious", "explanation": "Both mean angry and hostile in dispute."},
                {"id": 40, "stem": "The experiment's outcome was so _____ that it required replication.", "choices": ["(A) predictable", "(B) anomalous", "(C) routine", "(D) aberrant", "(E) typical", "(F) standard"], "answer": "(B) anomalous, (D) aberrant", "explanation": "Both mean deviating from what's expected, requiring verification."},
                {"id": 41, "stem": "Her response was so _____ that it betrayed her underlying frustration.", "choices": ["(A) measured", "(B) terse", "(C) expansive", "(D) curt", "(E) elaborate", "(F) verbose"], "answer": "(B) terse, (D) curt", "explanation": "Both mean rudely brief, revealing frustration beneath the surface."},
                {"id": 42, "stem": "The novelist's prose is so _____ that readers often mistake irony for sincerity.", "choices": ["(A) blatant", "(B) subtle", "(C) understated", "(D) obvious", "(E) overt", "(F) explicit"], "answer": "(B) subtle, (C) understated", "explanation": "Both mean not immediately apparent, causing readers to miss the irony."},
                {"id": 43, "stem": "The CEO's explanation was so _____ that stakeholders demanded clarification.", "choices": ["(A) lucid", "(B) clear", "(C) ambiguous", "(D) equivocal", "(E) transparent", "(F) explicit"], "answer": "(C) ambiguous, (D) equivocal", "explanation": "Both mean unclear, prompting demands for clarification."},
                {"id": 44, "stem": "The proposal was so _____ that it unified previously divided factions.", "choices": ["(A) divisive", "(B) polarizing", "(C) conciliatory", "(D) unifying", "(E) contentious", "(F) inflammatory"], "answer": "(C) conciliatory, (D) unifying", "explanation": "Both mean bringing parties together."},
                {"id": 45, "stem": "The scientist's tone was so _____ that it conveyed skepticism without hostility.", "choices": ["(A) caustic", "(B) measured", "(C) vitriolic", "(D) restrained", "(E) incendiary", "(F) hostile"], "answer": "(B) measured, (D) restrained", "explanation": "Both mean carefully controlled, allowing skepticism without aggression."},
                {"id": 46, "stem": "The film's plot was so _____ that viewers could predict every twist.", "choices": ["(A) convoluted", "(B) predictable", "(C) intricate", "(D) formulaic", "(E) surprising", "(F) unexpected"], "answer": "(B) predictable, (D) formulaic", "explanation": "Both mean following expected patterns, making twists obvious."},
                {"id": 47, "stem": "The article's conclusions were so _____ that they provoked immediate controversy.", "choices": ["(A) mundane", "(B) incendiary", "(C) inflammatory", "(D) routine", "(E) trivial", "(F) ordinary"], "answer": "(B) incendiary, (C) inflammatory", "explanation": "Both mean likely to provoke strong reactions."},
                {"id": 48, "stem": "Her confidence bordered on _____, alienating colleagues.", "choices": ["(A) humility", "(B) arrogance", "(C) hubris", "(D) modesty", "(E) diffidence", "(F) reserve"], "answer": "(B) arrogance, (C) hubris", "explanation": "Both mean excessive pride or self-importance."},
                {"id": 49, "stem": "The critic's remarks were so _____ that they were barely perceptible.", "choices": ["(A) overt", "(B) explicit", "(C) subtle", "(D) understated", "(E) blatant", "(F) obvious"], "answer": "(C) subtle, (D) understated", "explanation": "Both mean not immediately noticeable."},
                {"id": 50, "stem": "The proposal's logic was so _____ that it resisted simplistic interpretation.", "choices": ["(A) reductive", "(B) simplistic", "(C) intricate", "(D) multifaceted", "(E) elementary", "(F) basic"], "answer": "(C) intricate, (D) multifaceted", "explanation": "Both mean complex with many interconnected parts."},
            ]
        },
        {
            "type": "Sentence Equivalence — From Practice Sets",
            "instructions": "Select <strong>two</strong> answer choices that, when used to complete the sentence, fit the meaning of the sentence as a whole and produce completed sentences that are alike in meaning.",
            "multi_select": True,
            "questions": [
                {"id": 51, "stem": "The ambassador's response to the crisis was hardly decisive; instead, it was marked by a persistent _____ that frustrated both allies and adversaries.", "choices": ["(A) vacillation", "(B) resolve", "(C) equivocation", "(D) tenacity", "(E) certitude", "(F) steadfastness"], "answer": "(A) vacillation, (C) equivocation", "explanation": "Both mean indecisiveness, consistent with 'hardly decisive.'"},
                {"id": 52, "stem": "The philosopher's argument is so _____ that even sympathetic readers struggle to follow its progression.", "choices": ["(A) lucid", "(B) abstruse", "(C) transparent", "(D) recondite", "(E) accessible", "(F) pellucid"], "answer": "(B) abstruse, (D) recondite", "explanation": "Both mean extremely difficult to understand."},
                {"id": 53, "stem": "Though initially dismissed, the theory proved surprisingly _____, shaping debates across multiple disciplines.", "choices": ["(A) marginal", "(B) negligible", "(C) seminal", "(D) inconsequential", "(E) influential", "(F) trivial"], "answer": "(C) seminal, (E) influential", "explanation": "Both indicate major lasting impact — seminal (pioneering) and influential (widely affecting)."},
                {"id": 54, "stem": "The committee's recommendation was so _____ that it satisfied neither reformers nor traditionalists.", "choices": ["(A) equivocal", "(B) decisive", "(C) ambiguous", "(D) categorical", "(E) unequivocal", "(F) resolute"], "answer": "(A) equivocal, (C) ambiguous", "explanation": "Both mean unclear, failing to satisfy anyone."},
                {"id": 55, "stem": "The mathematician's lectures were notoriously _____, requiring students to grapple with densely layered abstractions.", "choices": ["(A) lucid", "(B) abstruse", "(C) arcane", "(D) accessible", "(E) transparent", "(F) straightforward"], "answer": "(B) abstruse, (C) arcane", "explanation": "Both mean obscure and difficult to understand."},
                {"id": 56, "stem": "Though modest in scope, the policy proved surprisingly _____ in reshaping regulatory debates.", "choices": ["(A) negligible", "(B) catalytic", "(C) transformative", "(D) trivial", "(E) inert", "(F) inconsequential"], "answer": "(B) catalytic, (C) transformative", "explanation": "Both mean causing significant change despite modest beginnings."},
                {"id": 57, "stem": "The historian's interpretation was not radical but quietly _____, subtly reshaping conventional narratives without overtly rejecting them.", "choices": ["(A) subversive", "(B) incendiary", "(C) revisionist", "(D) orthodox", "(E) reactionary", "(F) conservative"], "answer": "(A) subversive, (C) revisionist", "explanation": "Both mean quietly challenging established views."},
                {"id": 58, "stem": "The philosopher's prose is so _____ that even seasoned scholars must reread passages multiple times to grasp her argument.", "choices": ["(A) limpid", "(B) arcane", "(C) pellucid", "(D) opaque", "(E) transparent", "(F) lucid"], "answer": "(B) arcane, (D) opaque", "explanation": "Both mean difficult to understand or see through."},
                {"id": 59, "stem": "What appeared to be a minor regulatory adjustment proved surprisingly _____, influencing policy debates far beyond its original scope.", "choices": ["(A) trivial", "(B) catalytic", "(C) marginal", "(D) transformative", "(E) negligible", "(F) inconsequential"], "answer": "(B) catalytic, (D) transformative", "explanation": "Both mean producing significant, far-reaching effects."},
                {"id": 60, "stem": "The reviewer's assessment was not openly hostile but unmistakably _____, offering praise so faint it bordered on dismissal.", "choices": ["(A) laudatory", "(B) tepid", "(C) perfunctory", "(D) effusive", "(E) enthusiastic", "(F) glowing"], "answer": "(B) tepid, (C) perfunctory", "explanation": "Both mean unenthusiastic — tepid (lukewarm) and perfunctory (done without care)."},
            ]
        }
    ]
}

# ───────────────────────────────────────────────────
# READING COMPREHENSION — SHORT PASSAGES
# ───────────────────────────────────────────────────
_rc_short = {
    "id": "rc-short",
    "title": "RC — Short Passages",
    "icon": "S",
    "category": "reading-comp",
    "sections": [
        {
            "type": "Short Passage — Urban Planning",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Contemporary urban planners increasingly reject the assumption that density inherently diminishes quality of life. Instead, they argue that density, when paired with deliberate infrastructural design, can foster social cohesion and economic vitality. Critics, however, contend that such optimism overlooks persistent inequities embedded in urban development policies.",
            "questions": [
                {"id": 1, "stem": "The primary purpose of the passage is to:", "choices": ["(A) Advocate unconditionally for urban density", "(B) Present a debate regarding the effects of urban density", "(C) Refute criticisms of infrastructural planning", "(D) Demonstrate that density reduces inequality", "(E) Describe historical urban policies"], "answer": "(B) Present a debate regarding the effects of urban density", "explanation": "The passage presents both the planners' view (density can be positive) and critics' view (optimism overlooks inequities)."},
                {"id": 2, "stem": "The passage implies that critics of density-focused planning believe that:", "choices": ["(A) Density always reduces economic vitality", "(B) Infrastructure has no effect on urban outcomes", "(C) Social cohesion is impossible in cities", "(D) Structural inequalities may persist despite improved design", "(E) Urban planners ignore economic considerations"], "answer": "(D) Structural inequalities may persist despite improved design", "explanation": "Critics 'contend that such optimism overlooks persistent inequities embedded in urban development policies.'"},
            ]
        },
        {
            "type": "Short Passage — Climate Models",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "While early climate models assumed relatively linear relationships between emissions and temperature increases, more recent simulations suggest the presence of nonlinear feedback loops that may amplify minor fluctuations. Such findings complicate predictions, as small policy miscalculations could produce disproportionately large environmental consequences.",
            "questions": [
                {"id": 3, "stem": "The primary purpose of the passage is to:", "choices": ["(A) Criticize early climate models as fundamentally flawed", "(B) Describe recent developments that complicate climate prediction", "(C) Argue that emissions no longer influence temperature", "(D) Advocate abandoning predictive climate modeling", "(E) Demonstrate that policy interventions are ineffective"], "answer": "(B) Describe recent developments that complicate climate prediction", "explanation": "The passage describes how nonlinear feedback loops complicate predictions."},
                {"id": 4, "stem": "The passage implies that nonlinear feedback loops:", "choices": ["(A) Eliminate uncertainty in climate projections", "(B) Reduce the impact of policy decisions", "(C) May intensify the effects of small changes", "(D) Are fully understood by scientists", "(E) Operate independently of emissions"], "answer": "(C) May intensify the effects of small changes", "explanation": "'Amplify minor fluctuations' and 'small policy miscalculations could produce disproportionately large consequences.'"},
            ]
        },
        {
            "type": "Short Passage — Cognitive Biases",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Behavioral scientists once assumed that cognitive biases operated uniformly across cultural contexts. Recent cross-cultural studies, however, indicate that certain biases are attenuated — or even absent — within societies that emphasize collective decision-making over individual autonomy. These findings challenge claims of universality in cognitive theory.",
            "questions": [
                {"id": 5, "stem": "The primary purpose of the passage is to:", "choices": ["(A) Argue that cognitive biases do not exist", "(B) Refute cross-cultural research methods", "(C) Present findings that complicate assumptions of universality", "(D) Advocate collective decision-making", "(E) Describe the history of cognitive science"], "answer": "(C) Present findings that complicate assumptions of universality", "explanation": "The passage shows how cross-cultural studies challenge the universal applicability of cognitive bias theory."},
                {"id": 6, "stem": "The passage suggests that earlier researchers may have:", "choices": ["(A) Overgeneralized from culturally limited data", "(B) Rejected the existence of bias entirely", "(C) Ignored individual autonomy", "(D) Proven universality conclusively", "(E) Focused exclusively on collective societies"], "answer": "(A) Overgeneralized from culturally limited data", "explanation": "If biases vary across cultures, earlier claims of universality must have been based on too-narrow data."},
            ]
        },
        {
            "type": "Short Passage — Economic History",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Economic historians once attributed industrial growth primarily to technological innovation. More recent analyses, however, emphasize institutional frameworks — property rights, legal systems, and financial networks — that enabled such innovations to diffuse widely. This shift does not deny the importance of technology but reframes it as one component within a broader systemic context.",
            "questions": [
                {"id": 7, "stem": "The primary purpose of the passage is to:", "choices": ["(A) Reject technological explanations of industrial growth", "(B) Describe a shift in emphasis within economic history", "(C) Argue that institutions are irrelevant", "(D) Demonstrate flaws in financial systems", "(E) Advocate legal reform"], "answer": "(B) Describe a shift in emphasis within economic history", "explanation": "The passage traces a shift from technology-centered to institution-centered explanations."},
                {"id": 8, "stem": "The passage implies that recent scholars believe technological innovation:", "choices": ["(A) Is insignificant in industrial growth", "(B) Functions independently of institutions", "(C) Requires supportive frameworks to achieve widespread impact", "(D) Replaced financial networks", "(E) Was misunderstood by early historians"], "answer": "(C) Requires supportive frameworks to achieve widespread impact", "explanation": "Institutional frameworks 'enabled innovations to diffuse widely,' implying technology alone is insufficient."},
            ]
        },
        {
            "type": "Short Passage — Remote Work",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "A recent study claims that remote work increases productivity by eliminating commuting time. However, the study measures productivity primarily through self-reported output rather than independent performance metrics. Critics argue that such methodology may inflate perceived gains.",
            "questions": [
                {"id": 9, "stem": "Which of the following, if true, would most strengthen the critics' argument?", "choices": ["(A) Employees prefer remote work to office work", "(B) Independent performance metrics show little change in output", "(C) Commuting time has decreased overall", "(D) Many companies have adopted hybrid models", "(E) Remote work reduces office costs"], "answer": "(B) Independent performance metrics show little change in output", "explanation": "If independent metrics show no productivity change, then the self-reported gains are indeed inflated."},
                {"id": 10, "stem": "The critics' argument depends on which of the following assumptions?", "choices": ["(A) Self-reported output may not accurately reflect actual productivity", "(B) Remote work eliminates commuting entirely", "(C) Employees intentionally misrepresent their output", "(D) Productivity is impossible to measure objectively", "(E) Independent metrics are always reliable"], "answer": "(A) Self-reported output may not accurately reflect actual productivity", "explanation": "The critics' point that self-reports 'may inflate perceived gains' depends on self-reports being potentially inaccurate."},
            ]
        },
        {
            "type": "Short Passage — Graduate Survey",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "In a survey of graduate students, 68% reported that access to mentorship significantly influenced their academic satisfaction, whereas only 42% cited financial support as the primary determinant. Researchers caution, however, that respondents were permitted to select multiple factors.",
            "questions": [
                {"id": 11, "stem": "The information provided most strongly suggests that:", "choices": ["(A) Financial support is unimportant to most graduate students", "(B) Mentorship and financial support are mutually exclusive", "(C) Some students likely selected both mentorship and financial support", "(D) Exactly 26% valued mentorship but not financial support", "(E) Academic satisfaction depends solely on mentorship"], "answer": "(C) Some students likely selected both mentorship and financial support", "explanation": "Since 68% + 42% > 100% and respondents could select multiple factors, there must be overlap."},
            ]
        }
    ]
}

# ───────────────────────────────────────────────────
# READING COMPREHENSION — LONG PASSAGES
# ───────────────────────────────────────────────────
_rc_long = {
    "id": "rc-long",
    "title": "RC — Long Passages",
    "icon": "L",
    "category": "reading-comp",
    "sections": [
        {
            "type": "Long Passage — The Enlightenment",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Historians once characterized the Enlightenment as a unified intellectual movement grounded in universal reason. Recent scholarship, however, challenges this portrayal, arguing that the Enlightenment encompassed a diverse array of competing perspectives, many of which were deeply embedded in local political contexts. Yet to emphasize fragmentation alone risks obscuring the shared methodological commitments that distinguished Enlightenment thinkers from their predecessors. A comprehensive account must therefore reconcile diversity with coherence, acknowledging both the plurality of viewpoints and the common intellectual aspirations that animated them.",
            "questions": [
                {"id": 1, "stem": "The author's attitude toward recent scholarship is best described as:", "choices": ["(A) Unqualified endorsement", "(B) Hostile dismissal", "(C) Qualified approval", "(D) Complete indifference", "(E) Nostalgic preference for earlier views"], "answer": "(C) Qualified approval", "explanation": "The author accepts recent scholarship's emphasis on diversity but notes its limitation ('to emphasize fragmentation alone risks obscuring...')."},
                {"id": 2, "stem": "According to the passage, Enlightenment thinkers were united primarily by:", "choices": ["(A) Identical political ideologies", "(B) Local political contexts", "(C) Shared methodological commitments", "(D) Opposition to universal reason", "(E) Fragmented intellectual traditions"], "answer": "(C) Shared methodological commitments", "explanation": "The passage states they shared 'methodological commitments that distinguished Enlightenment thinkers from their predecessors.'"},
                {"id": 3, "stem": "The passage suggests that an adequate account of the Enlightenment must:", "choices": ["(A) Reject the concept of diversity", "(B) Focus exclusively on fragmentation", "(C) Balance unity and plurality", "(D) Privilege political explanations over intellectual ones", "(E) Dismiss recent scholarship"], "answer": "(C) Balance unity and plurality", "explanation": "'A comprehensive account must therefore reconcile diversity with coherence.'"},
                {"id": 4, "stem": "The third sentence of the passage serves primarily to:", "choices": ["(A) Introduce empirical evidence", "(B) Present a limitation of the recent scholarship", "(C) Define methodological commitments", "(D) Offer a historical example", "(E) Summarize the traditional view"], "answer": "(B) Present a limitation of the recent scholarship", "explanation": "'Yet to emphasize fragmentation alone risks obscuring...' critiques the one-sidedness of recent scholarship."},
            ]
        },
        {
            "type": "Long Passage — Autobiographical Fiction",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Literary critics have long debated whether autobiographical fiction should be evaluated primarily as imaginative literature or as veiled confession. Those favoring the former approach argue that to privilege biographical interpretation risks diminishing the artistry of narrative construction. Others contend that ignoring the author's lived experience obscures the text's most salient meanings. Yet both positions presuppose a rigid separation between invention and experience that may be untenable. Autobiographical fiction often operates precisely in the ambiguous space where memory and imagination intersect, rendering attempts to categorize it exclusively as either artifice or testimony reductive.",
            "questions": [
                {"id": 5, "stem": "The author's attitude toward the two critical positions is best described as:", "choices": ["(A) Complete endorsement of the first", "(B) Complete endorsement of the second", "(C) Impartial neutrality without evaluation", "(D) Skeptical of both as overly rigid", "(E) Enthusiastic support for biographical analysis"], "answer": "(D) Skeptical of both as overly rigid", "explanation": "'Both positions presuppose a rigid separation...that may be untenable.'"},
                {"id": 6, "stem": "According to the passage, critics who favor evaluating autobiographical fiction as imaginative literature are concerned that biographical readings may:", "choices": ["(A) Reveal too much about the author", "(B) Undermine appreciation of narrative artistry", "(C) Ignore historical context", "(D) Encourage imaginative invention", "(E) Promote rigid categorization"], "answer": "(B) Undermine appreciation of narrative artistry", "explanation": "'To privilege biographical interpretation risks diminishing the artistry of narrative construction.'"},
                {"id": 7, "stem": "The passage suggests that autobiographical fiction:", "choices": ["(A) Is best classified strictly as confession", "(B) Cannot meaningfully incorporate imagination", "(C) Blurs the distinction between memory and invention", "(D) Should be evaluated only through biography", "(E) Rejects lived experience entirely"], "answer": "(C) Blurs the distinction between memory and invention", "explanation": "'Operates precisely in the ambiguous space where memory and imagination intersect.'"},
                {"id": 8, "stem": "The final sentence serves primarily to:", "choices": ["(A) Introduce new empirical evidence", "(B) Summarize a critic's argument", "(C) Propose a synthesis that challenges both earlier views", "(D) Offer a historical example", "(E) Define autobiographical fiction"], "answer": "(C) Propose a synthesis that challenges both earlier views", "explanation": "The final sentence argues that autobiographical fiction operates in an in-between space, rejecting both rigid positions."},
            ]
        },
        {
            "type": "Long Passage — Political Legitimacy",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Political theorists frequently distinguish between legitimacy derived from procedural fairness and legitimacy grounded in substantive outcomes. Advocates of proceduralism maintain that fair processes confer authority regardless of policy results. Critics counter that outcomes matter: a procedurally flawless system that consistently produces unjust results cannot plausibly claim moral legitimacy. Yet framing the debate as process versus outcome obscures a deeper interdependence. Procedural norms often shape substantive results, while assessments of outcomes inevitably inform judgments about the adequacy of procedures. Legitimacy, therefore, may not reside exclusively in either domain but rather in their dynamic interaction.",
            "questions": [
                {"id": 9, "stem": "The author's attitude toward the process-versus-outcome framing is best described as:", "choices": ["(A) Complete endorsement", "(B) Qualified rejection", "(C) Indifference", "(D) Uncritical acceptance", "(E) Hostile dismissal"], "answer": "(B) Qualified rejection", "explanation": "The author doesn't entirely dismiss it but argues it 'obscures a deeper interdependence.'"},
                {"id": 10, "stem": "According to the passage, critics of proceduralism argue that:", "choices": ["(A) Outcomes are irrelevant to legitimacy", "(B) Fair processes guarantee just results", "(C) Unjust outcomes undermine claims of legitimacy", "(D) Procedural norms are unnecessary", "(E) Substantive outcomes determine procedures"], "answer": "(C) Unjust outcomes undermine claims of legitimacy", "explanation": "'A procedurally flawless system that consistently produces unjust results cannot plausibly claim moral legitimacy.'"},
                {"id": 11, "stem": "The passage suggests that legitimacy:", "choices": ["(A) Is determined solely by outcomes", "(B) Is unrelated to procedures", "(C) Emerges from interaction between process and outcome", "(D) Exists independently of moral considerations", "(E) Is inherently unstable"], "answer": "(C) Emerges from interaction between process and outcome", "explanation": "'Legitimacy...may not reside exclusively in either domain but rather in their dynamic interaction.'"},
                {"id": 12, "stem": "The final sentence primarily:", "choices": ["(A) Introduces a new theoretical framework", "(B) Summarizes the proceduralist position", "(C) Offers a synthesis reconciling competing views", "(D) Dismisses the critics' argument", "(E) Provides historical evidence"], "answer": "(C) Offers a synthesis reconciling competing views", "explanation": "The final sentence proposes that legitimacy resides in the interaction of both process and outcome."},
            ]
        },
        {
            "type": "Long Passage — Aesthetic Theory",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Aesthetic theorists have debated whether artistic value resides intrinsically within the artwork or emerges from interpretive communities. Proponents of intrinsic value argue that formal properties — composition, structure, and technique — determine merit regardless of audience reception. Advocates of the communal perspective contend that meaning and value arise through socially mediated interpretation. Yet the dichotomy may be overstated. Formal properties influence interpretation, but interpretive traditions also shape which properties are deemed significant. Artistic value, therefore, may not be fixed solely within the object nor wholly constructed by audiences, but instead generated through the interaction between form and reception.",
            "questions": [
                {"id": 13, "stem": "The author's attitude toward the intrinsic-versus-communal debate is best described as:", "choices": ["(A) Complete endorsement of intrinsic theory", "(B) Complete endorsement of communal theory", "(C) Neutral reporting without evaluation", "(D) Critical of the rigid opposition between the two", "(E) Indifferent to aesthetic theory"], "answer": "(D) Critical of the rigid opposition between the two", "explanation": "'The dichotomy may be overstated' — the author argues both sides are too rigid."},
                {"id": 14, "stem": "According to the passage, proponents of intrinsic value believe that artistic merit is determined by:", "choices": ["(A) Audience interpretation", "(B) Social traditions", "(C) Formal properties of the artwork", "(D) Political context", "(E) Historical reception"], "answer": "(C) Formal properties of the artwork", "explanation": "'Formal properties — composition, structure, and technique — determine merit.'"},
                {"id": 15, "stem": "The passage suggests that artistic value:", "choices": ["(A) Exists independently of interpretation", "(B) Is entirely socially constructed", "(C) Emerges from interaction between artwork and audience", "(D) Is objectively measurable", "(E) Cannot be meaningfully discussed"], "answer": "(C) Emerges from interaction between artwork and audience", "explanation": "'Generated through the interaction between form and reception.'"},
                {"id": 16, "stem": "The final sentence primarily:", "choices": ["(A) Summarizes the communal theory", "(B) Introduces a new unrelated concept", "(C) Offers a synthesis reconciling competing perspectives", "(D) Provides empirical evidence", "(E) Rejects intrinsic value entirely"], "answer": "(C) Offers a synthesis reconciling competing perspectives", "explanation": "The final sentence proposes a middle ground between intrinsic and communal views."},
            ]
        },
        {
            "type": "Long Passage — Evolutionary Biology",
            "instructions": "Read the passage and answer the questions that follow.",
            "passage": "Evolutionary biologists have long debated whether certain traits persist because they confer direct adaptive advantages or because they are byproducts of other selected characteristics. The adaptationist perspective emphasizes natural selection's efficiency in refining advantageous traits. Critics argue that some features may be evolutionary \"spandrels\" — incidental consequences rather than optimized adaptations. Yet recent research suggests that this dichotomy may obscure complex developmental pathways in which traits initially emerging as byproducts acquire adaptive functions over time. Thus, rigidly classifying traits as either adaptations or spandrels may oversimplify evolutionary dynamics.",
            "questions": [
                {"id": 17, "stem": "In the passage, the term \"spandrels\" most nearly refers to:", "choices": ["(A) Highly efficient adaptations", "(B) Deliberately engineered traits", "(C) Incidental structural byproducts", "(D) Genetic mutations", "(E) Optimized characteristics"], "answer": "(C) Incidental structural byproducts", "explanation": "Defined in the passage as 'incidental consequences rather than optimized adaptations.'"},
                {"id": 18, "stem": "The main point of the passage is that:", "choices": ["(A) Adaptationism is fundamentally flawed", "(B) All traits are evolutionary byproducts", "(C) The adaptation-versus-spandrel debate may be overly simplistic", "(D) Natural selection operates inefficiently", "(E) Developmental pathways are irrelevant to evolution"], "answer": "(C) The adaptation-versus-spandrel debate may be overly simplistic", "explanation": "'Rigidly classifying traits as either adaptations or spandrels may oversimplify evolutionary dynamics.'"},
                {"id": 19, "stem": "Which of the following would the author most likely agree with?", "choices": ["(A) A trait initially emerging as a byproduct can later become advantageous", "(B) Natural selection eliminates all non-adaptive features", "(C) Evolutionary theory should abandon adaptationism entirely", "(D) Spandrels never acquire functional significance", "(E) Evolutionary classifications are unnecessary"], "answer": "(A) A trait initially emerging as a byproduct can later become advantageous", "explanation": "'Traits initially emerging as byproducts acquire adaptive functions over time.'"},
            ]
        }
    ]
}

# ───────────────────────────────────────────────────
# ASSEMBLE ALL TOPICS
# ───────────────────────────────────────────────────
VERBAL_TOPICS = [_tc_1blank, _tc_2blank, _tc_3blank, _se_practice, _rc_short, _rc_long]

# Assign category auto-tag (already done inline above)
for t in VERBAL_TOPICS:
    if 'category' not in t:
        t['category'] = 'text-completion'


# ───────────────────────────────────────────────────
# HELPER: Build JSON-safe topics for frontend
# ───────────────────────────────────────────────────
def _build_verbal_topics_json():
    out = []
    for t in VERBAL_TOPICS:
        topic = {
            'id': t['id'],
            'title': t['title'],
            'icon': t['icon'],
            'category': t['category'],
            'sections': []
        }
        for s in t['sections']:
            sec = {
                'type': s['type'],
                'instructions': s.get('instructions', ''),
                'multi_select': s.get('multi_select', False),
                'passage': s.get('passage', ''),
                'questions': []
            }
            for q in s['questions']:
                qd = {
                    'id': q['id'],
                    'stem': q['stem'],
                    'answer': q.get('answer', ''),
                    'explanation': q.get('explanation', ''),
                }
                if 'choices' in q:
                    qd['choices'] = q['choices']
                if 'blank_choices' in q:
                    qd['blank_choices'] = q['blank_choices']
                sec['questions'].append(qd)
            topic['sections'].append(sec)
        out.append(topic)
    return out


def _build_verbal_categories_json():
    return [{'id': c['id'], 'name': c['name'], 'icon': c['icon']} for c in VERBAL_CATEGORIES]
