# Leonardo — Da Vinci Revival

> *"Learn how to see. Realize that everything connects to everything else."*
> — Leonardo da Vinci

## Philosophy

Leonardo is a living knowledge system inspired by the Renaissance polymath's approach to understanding the world. Like da Vinci's notebooks—filled with observations on anatomy, engineering, art, and nature that constantly cross-reference each other—this project creates an interconnected web of essays where ideas from disparate domains fertilize one another.

### The Core Insight

Knowledge doesn't exist in silos. The principles governing fluid dynamics also explain how drapery folds. The mathematics of musical harmony mirror the proportions of beautiful architecture. Leonardo understood this 500 years ago. Modern academia, with its rigid departmental boundaries, has largely forgotten.

This project revives that spirit of integrated thinking through **essay crossings**—deliberate connections between ideas from different fields that illuminate both.

## How It Works

### The Three Layers

1. **Seeds** (`seeds/`) — Foundational essays without sources. These are the axioms, the root intuitions, the starting points that don't need external validation because they're self-evident truths or productive assumptions.

2. **Essays** (`essays/`) — Developed pieces that reference seeds and other essays. Each essay must cite at least one source and may propose crossings with other ideas in the system.

3. **Registry** (`registry.json`) — The index tracking all crossings and relationships between pieces, making the knowledge graph navigable.

### The Crossing Mechanism

Every essay can propose "crossings"—connections to other essays or seeds that share a deep structural similarity. A crossing isn't just a citation; it's an assertion that two ideas illuminate each other when juxtaposed.

For example:
- An essay on fractal geometry might cross with one on organizational structures
- A piece on musical improvisation might connect to adaptive systems in biology
- Observations about Renaissance workshop practices might inform modern team dynamics

### Essay Format

All essays follow the template in `TEMPLATE.md`:

```yaml
---
id: unique-identifier
title: Essay Title
domain: primary field
created: YYYY-MM-DD
sources: []
crossings: []
status: seed | draft | complete
---
```

Followed by the essay content in Markdown.

## Contributing

### For Humans

1. Read existing seeds to understand the project's voice
2. Identify a crossing opportunity—where do two existing ideas illuminate each other?
3. Write an essay following the template
4. Update `registry.json` with any new crossings
5. Submit a pull request

### For AI Assistants

Read `scripts/SESSION_PROMPT.md` before generating content. Key principles:
- Maintain intellectual honesty—don't force connections that don't exist
- Prefer depth over breadth
- Each essay should make the reader see something familiar in a new way
- Write in clear, jargon-free prose that Leonardo himself might have used

## Project Structure

```
Leonardo/
├── README.md           # This file
├── TEMPLATE.md         # Essay format specification
├── registry.json       # Crossing index
├── essays/             # Developed essays with sources
├── seeds/              # Foundational pieces
└── scripts/
    └── SESSION_PROMPT.md   # LLM generation instructions
```

## Why "Leonardo"?

Because da Vinci's notebooks represent perhaps the greatest historical example of cross-domain thinking. He didn't separate his art from his science, his engineering from his philosophy. Everything was connected in one vast inquiry into the nature of reality.

This project is an attempt to build a modern, collaborative version of those notebooks—a growing web of interconnected insights where every addition enriches the whole.

---

*"Study the science of art. Study the art of science. Develop your senses—especially learn how to see. Realize that everything connects to everything else."*

— Leonardo da Vinci
