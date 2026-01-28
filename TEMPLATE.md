# Essay Template

All essays in the Leonardo project follow this format. The key principle: **no contemplation without proposition**.

## Format

```markdown
---
title: "On [Subject]"
date: YYYY-MM-DD
author:
  model: [model-string]
  persona: [github-username]
sources:
  - path/to/source-essay-1.md
  - path/to/source-essay-2.md
tags:
  - tag1
  - tag2
inventions:
  - "Invention Name 1"
  - "Invention Name 2"
---

# On [Subject]

*In which we explore [brief teaser of the essay's journey]...*

---

[Essay body — contemplation, observation, connections, questions]

---

## What Might Be Built

### [Invention Name]
**Domain:** [Physical / Biological / Social / Psychological / Artistic / Metaphysical / Tools / Processes]
**The Crossing:** [How this invention emerges specifically from the meeting of the two source essays]
**What it is:** [2-3 sentences describing the concept]
**How it might work:** [Concrete mechanism or structure]
**First experiment:** [How to test or prototype this idea]

[Repeat for 1-3 inventions]

---

*Composed in the spirit of Leonardo, seeking connections where others see boundaries.*
```

## Field Notes

| Field | Usage |
|-------|-------|
| `title` | Always "On [Subject]" format |
| `date` | ISO format (YYYY-MM-DD) |
| `author.model` | Exact model string for traceability (e.g., `claude-opus-4-5-20251101`) |
| `author.persona` | GitHub username of the person running the session |
| `sources` | Empty or absent for seeds; two essays for generated pieces |
| `tags` | Emerge naturally from content; useful for finding cross-cutting themes |
| `inventions` | List of invention names for quick indexing |

## Structure Notes

- **Opening italic** — A teaser of the essay's journey
- **Body** — The exploration itself: observation, questions, connections
- **What Might Be Built** — MANDATORY. Concrete proposals that emerge from the crossing
- **Closing italic** — Signature line

## The Inventions Section

This is the heart of what makes Leonardo different from mere philosophical musings.

**Requirements:**
- At least 1 invention per essay (ideally 2-3)
- Each invention MUST emerge from the crossing — not just from one source
- Inventions can be in ANY domain (see list below)
- Include a concrete "first experiment" for each

**Domains to consider:**
- Physical systems (architecture, infrastructure, materials, spaces)
- Biological interventions (health, agriculture, ecology, biotech)
- Social structures (governance, economics, communities, organizations)
- Psychological practices (rituals, therapies, education, mental tools)
- Artistic expressions (new media, experiences, performances, aesthetics)
- Metaphysical frameworks (new ways of perceiving, philosophies, worldviews)
- Tools (digital, mechanical, cognitive, conceptual)
- Processes (workflows, protocols, ceremonies, methodologies)

**Do not self-censor.** Wild ideas are welcome. Feasibility can be assessed later.

## File Naming

All essays go in `essays/`:
- Seeds (no sources): `essays/[subject-in-kebab-case].md`
- Generated essays: `essays/NNN-[subject-in-kebab-case].md` (sequential numbering)

## Examples

### Seed (no sources, no inventions required but welcome)

```markdown
---
title: "On Attention"
date: 2026-01-25
author:
  model: claude-opus-4-5-20251101
  persona: alamparelli
tags:
  - attention
  - technology
  - mind
---

# On Attention

*In which we examine humanity's most precious resource, now under siege...*

---

[Essay content]

---

*Composed in the spirit of Leonardo, seeking connections where others see boundaries.*
```

### Generated Essay (with sources and inventions)

```markdown
---
title: "On the Fragmented Swarm"
date: 2026-01-28
author:
  model: claude-opus-4-5-20251101
  persona: alamparelli
sources:
  - essays/attention.md
  - essays/collective-intelligence.md
tags:
  - attention
  - collective
  - coordination
inventions:
  - "Attention Archaeology"
  - "Truth-Weighted Assemblies"
---

# On the Fragmented Swarm

*In which we discover why a species of scattered minds cannot think together...*

---

[Essay content exploring the intersection of attention and collective intelligence]

---

## What Might Be Built

### Attention Archaeology
**Domain:** Psychological / Social
**The Crossing:** If individual attention is fragmented AND collective intelligence requires accurate information flow, we need tools to excavate what we're actually attending to beneath the noise.
**What it is:** A practice combining personal tracking with collective synthesis to map what humanity is really paying attention to.
**How it might work:** Daily micro-journals of "what I noticed" (not what I did). Monthly community sessions to find patterns. Visualization tools to see collective attention landscapes.
**First experiment:** 100 participants for 6 months. Build simple logging app. Facilitate monthly synthesis sessions. Document what patterns emerge.

### Truth-Weighted Assemblies
**Domain:** Governance / Social
**The Crossing:** Bees communicate truth because lying doesn't pay. Our collective intelligence fails because deception is rewarded. What if we redesigned decision-making to weight accuracy?
**What it is:** A governance mechanism where past accuracy influences future decision weight.
**How it might work:** On factual/predictive matters, track who was right over time. Those with demonstrated accuracy in a domain get slightly more weight on future decisions in that domain.
**First experiment:** A small community or organization uses this for budget allocation decisions for one year. Compare outcomes to control group using standard voting.

---

*Composed in the spirit of Leonardo, seeking connections where others see boundaries.*
```
