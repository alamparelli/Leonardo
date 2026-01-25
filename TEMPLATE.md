# Essay Template

All essays in the Leonardo project follow this format.

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
---

# On [Subject]

*In which we explore [brief teaser of the essay's journey]...*

---

[Essay body]

---

*Composed in the spirit of Leonardo, seeking connections where others see boundaries.*
```

## Field Notes

| Field | Usage |
|-------|-------|
| `title` | Always "On [Subject]" format |
| `date` | ISO format (YYYY-MM-DD) |
| `author.model` | Exact model string for traceability (e.g., `claude-opus-4-5-20251101`, `gpt-4o-2024-11-20`) |
| `author.persona` | GitHub username of the person running the session |
| `sources` | Empty or absent for seeds; filled for generated essays |
| `tags` | Emerge naturally from content; useful for finding cross-cutting themes later |

## Structure Notes

- **Opening italic** — A teaser of the essay's journey
- **Body** — The exploration itself
- **Closing italic** — Optional signature line, provides cohesive voice

## File Naming

All essays go in `essays/`:
- Seeds (no sources): `essays/[subject-in-kebab-case].md`
- Generated essays: `essays/NNN-[subject-in-kebab-case].md` (sequential numbering)

## Examples

### Seed (no sources)

```markdown
---
title: "On Attention"
date: 2026-01-25
author:
  model: claude-opus-4-5-20251101
  persona: alamparelli
tags:
  - technology
  - mind
  - distraction
---

# On Attention

*In which we examine humanity's most precious resource, now under siege...*

---

[Essay content]

---

*Composed in the spirit of Leonardo, seeking connections where others see boundaries.*
```

### Generated Essay (with sources)

```markdown
---
title: "On the Fragmented Present"
date: 2026-01-25
author:
  model: claude-opus-4-5-20251101
  persona: alamparelli
sources:
  - essays/attention.md
  - essays/acceleration.md
tags:
  - time
  - presence
  - technology
---

# On the Fragmented Present

*In which we discover how speed shatters attention...*

---

[Essay content]

---

*Composed in the spirit of Leonardo, seeking connections where others see boundaries.*
```
