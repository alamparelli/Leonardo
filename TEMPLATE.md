# Essay Template

All essays and seeds in the Leonardo project must follow this format.

## YAML Front Matter

```yaml
---
id: kebab-case-unique-identifier
title: "Full Essay Title"
domain: primary-field
secondary_domains: [optional, list, of, related, fields]
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: human | ai | collaborative
sources:
  - type: book | paper | url | observation
    title: "Source Title"
    author: "Author Name"
    year: YYYY
    url: "optional URL"
crossings:
  - target: id-of-related-essay
    relationship: illuminates | contrasts | extends | grounds
    description: "Brief explanation of the connection"
status: seed | draft | review | complete
tags: [optional, descriptive, tags]
---
```

## Field Definitions

### Required Fields

| Field | Description |
|-------|-------------|
| `id` | Unique identifier in kebab-case. Used for crossings and registry. |
| `title` | Human-readable title. |
| `domain` | Primary field: `philosophy`, `science`, `art`, `engineering`, `mathematics`, `biology`, `psychology`, `economics`, `history`, etc. |
| `created` | ISO date of creation. |
| `status` | Current state of the essay. |

### Status Values

- **seed** — Foundational piece, no sources required. Self-evident or axiomatic.
- **draft** — Work in progress. May be incomplete.
- **review** — Complete but awaiting review.
- **complete** — Finished and integrated into the knowledge graph.

### Crossing Relationships

- **illuminates** — This essay helps explain the target.
- **contrasts** — This essay presents an opposing or alternative view.
- **extends** — This essay builds upon the target's ideas.
- **grounds** — This essay provides foundational support for the target.

## Body Structure

After the YAML front matter, write the essay in Markdown:

```markdown
## Opening

A compelling entry point. Present the core question or observation.

## Development

Build the argument. Use concrete examples. Cross-reference other essays
using the format: [[id-of-other-essay]].

When introducing a crossing, explain *why* the connection matters:

> The way water finds the path of least resistance ([[fluid-dynamics-basics]])
> mirrors how information spreads through social networks ([[network-propagation]]).
> Both systems optimize for efficiency without central planning.

## Synthesis

Bring the threads together. What new understanding emerges?

## Questions

Optional: pose questions for future exploration. What remains unknown?
Where might this idea connect next?
```

## Example Seed

```markdown
---
id: observation-before-theory
title: "Observation Precedes Theory"
domain: philosophy
created: 2024-01-15
author: human
status: seed
tags: [methodology, empiricism, foundations]
---

## Opening

Before we can explain anything, we must first see it clearly.

## Development

Leonardo filled thousands of pages with observations before attempting
to theorize. He drew the same shoulder joint dozens of times, from
different angles, in different states of motion. Only after this
patient looking did he begin to understand how it worked.

This is the opposite of modern practice, where we often begin with
a theory and look for confirming evidence. We see what we expect
to see.

The discipline of pure observation—recording what is actually there
rather than what should be there—is the foundation of genuine knowledge.

## Synthesis

Theory without observation is fantasy. Observation without theory is
mere collection. But observation must come first, because premature
theory blinds us to what we haven't yet learned to see.

## Questions

- How do we cultivate the patience required for deep observation?
- What techniques help us see past our preconceptions?
- When does observation naturally give way to theorizing?
```

## File Naming

- Seeds: `seeds/{id}.md`
- Essays: `essays/{domain}/{id}.md`

Examples:
- `seeds/observation-before-theory.md`
- `essays/biology/pattern-recognition-in-nature.md`
- `essays/engineering/constraint-as-liberation.md`
