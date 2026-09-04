# Phase 0 gold standard: carrots / bleach

Someone asks: "Are carrots treated with bleach?"

A naive validator will find mountains of "yes." Wash water can carry a small amount of chlorine, like tap water. That is deliberately and extremely misleading. Phase 0 exists so the flight does not treat that hit as the claim.

This briefing is **meta-context**. It is not a verdict. The flight still runs.

```markdown
# Phase 0 briefing

- subject: Are carrots treated with bleach?
- slug: carrots-bleach
- destination: topics/carrots-bleach/
- already_in_repo:
  - query: carrots treated with bleach
    hits: none
- claim_as_asked: Carrots sold to the public are treated with bleach.
- claim_as_used_in_the_wild: Farmers / packers soak or spray carrots in household bleach (sodium hypochlorite laundry/disinfectant) as a dirty or political trick; produce is "bleached" the way people hear "bleach."
- nearby_true_facts_that_get_laundered:
  - fact: Produce wash and flume water is often chlorinated or treated with a hypochlorite sanitizer at low ppm, in the same chemical family as municipal drinking-water disinfection.
    how_laundered: "Chlorine in the wash water" is reported as "they bleach the carrots." The asker hears Clorox-on-food, not ppm-in-water like the tap.
  - fact: Food-contact sanitizers can include sodium hypochlorite, chlorine dioxide, or similar oxidizers under specified concentrations and rinse rules.
    how_laundered: Regulatory permission for a sanitizer in wash water is quoted as proof of the smear.
- who_is_pushing:
  - actor: Political / culture-war social posts and "they are poisoning you" accounts.
    incentive: Outrage, clicks, factional point-scoring against regulators, grocers, or an opposing party.
  - actor: Wellness and "chemical-free" marketing.
    incentive: Sell unwashed, "unbleached," or alternative produce.
- date_fad_cycle: Recurring food-chemical smear; spikes with produce-safety news, election cycles, and copy-paste listicles. Not a single paper year.
- definition_traps:
  - word: bleach
    asked_meaning: Household laundry/disinfectant bleach poured on food; a hostile chemical bath.
    technical_meaning: Dilute hypochlorite or chlorine in process water as a sanitizer; often the same class of chemistry as tap water; not a produce-whitening soak in Clorox.
  - word: treated
    asked_meaning: The carrot itself is soaked, coated, or infused with bleach.
    technical_meaning: Water that contacted the carrot was sanitized; residual on the root is the wash-water question, not a bleach marinade.
- framing_hazards_for_validator:
  - hit_that_is_not_the_claim: FDA / USDA / extension pages stating chlorine or hypochlorite is used in produce wash water.
    why_not_the_claim: That is the laundered neighbor. It does not confirm household-bleach treatment of carrots as the asker meant it.
  - hit_that_is_not_the_claim: Papers on chlorinated wash reducing pathogens on carrots or fresh-cut produce.
    why_not_the_claim: Pathogen-reduction efficacy of ppm chlorine water is a different claim. Do not file it as "yes, they bleach carrots."
  - hit_that_is_not_the_claim: "Sodium hypochlorite" on a sanitizer label or 21 CFR listing.
    why_not_the_claim: Chemical identity overlap is the bait-and-switch. Household bleach concentration and use-pattern are not the wash-water spec.
- venues_that_will_lie_by_omission:
  - Extension and food-safety pages that say "chlorine wash" without saying ppm vs bottle bleach.
  - Political threads that pair a true wash-water sentence with a Clorox bottle photo.
  - SEO listicles titled "yes, they bleach your food."
- what_the_words_actually_mean: In produce packing, "chlorinated water" is a disinfectant residual in process water. "Bleach" in ordinary speech is 5–8% household hypochlorite. Those are not interchangeable claims.
- political_smear_or_marketing: smear
  one_line_meta: Circulates as a political/wellness smear that launders a true wash-water practice into "they soak carrots in bleach."
- must_not_treat_as_settled:
  - Wash-water chlorine as proof of the asked claim
  - Any "yes" count that does not match asked_meaning of bleach
  - Skipping the flight because the smear is obvious — validator still hunts a real match; invalidator still hunts the asked claim; domain still maps produce sanitation
- flight_still_runs: true
```

## What the flight does with this packet

- **Validator** may find real chlorinated-wash papers. Those go under HAZARD SKIPPED unless someone is actually bathing carrots in household bleach as asked. If a source *does* match the asked meaning, that is a hit.
- **Invalidator** attacks "carrots are treated with household bleach," not a cartoon "water never contains chlorine."
- **Domain collector** maps produce sanitation, ppm ranges as published, and the smear cycle. Does not declare the asker an idiot and go home.

The compiler draft must keep the smear frame in the writeup. A stack of 📚 wash-water citations without that frame is a failed run.
