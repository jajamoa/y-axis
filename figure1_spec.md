# Figure 1 Specification

## Purpose
The central visual of the paper. Every reader should be able to reconstruct the paper's argument from this figure alone.

## Content

### Axes
- **X-axis label:** Task Generality (breadth × depth of capability)
- **Y-axis label:** Individuality (structural sedimentation of identity)
- Both axes: LOW → HIGH, labeled at endpoints

### Four Quadrants
| Quadrant | Label | Example Systems |
|----------|-------|-----------------|
| Top-left (low-X, high-Y) | **Specialist Actor** | Domain-expert system with persistent user models; character.ai persistent persona; urban simulation agent |
| Top-right (high-X, high-Y) | **AGI Target** ★ | No current system. The goal. |
| Bottom-left (low-X, low-Y) | **Narrow Tool** | Calculator, spell-checker, rules-based chatbot |
| Bottom-right (high-X, low-Y) | **Frontier LLM** | GPT-4o, Claude 3.5, Gemini Ultra |

### Key annotations
1. Arrow labeled **"Current research effort"** pointing right along bottom band (X-axis direction)
2. Arrow labeled **"Missing research direction"** pointing up along Y-axis
3. Dashed diagonal: **"Application spectrum"** from bottom-right to top-left (productivity → companion → simulation → education)
4. Star (★) in top-right quadrant: **"AGI target"** — unfilled, showing it's aspirational

### Text callout (caption)
**Figure 1 | Two design orientations for intelligent agents.**
Current AGI benchmarks (ARC-AGI, MMLU, BIG-bench) measure progress along the X-axis of task generality. Virtually all frontier AI systems cluster in the bottom-right quadrant: high capability, low individuality. The top-right quadrant—high generality with structural individuality—represents the full target of artificial general intelligence and is currently unoccupied. Different applications prioritize different positions on this plane: productivity assistants optimize for X; companion systems and social simulations optimize for Y. The two axes are largely independent; scaling along X does not produce movement along Y.

## Design notes (for actual figure creation)
- Clean white background, two perpendicular axes
- Quadrant labels in gray, non-intrusive
- System names in bold black circles/dots at approximate positions
- AGI Target as unfilled star (★) in top-right
- Application spectrum as dashed diagonal line with small labels
- Color: X-axis blue, Y-axis orange, AGI target gold star
- Format: vector (SVG preferred), fallback PNG 300dpi
- Size: single-column NMI figure (~85mm wide) or double-column (~180mm wide)

## ASCII preview
```
Y: Individuality
▲
│   Specialist Actor │ ★ AGI Target
│   (domain expert,  │ (no current system)
│   persistent agent)│
│                    │
├────────────────────┼──────────────────► X: Task Generality
│                    │
│   Narrow Tool      │ Frontier LLMs
│   (calculator,     │ (GPT-4, Claude,
│   rules-based)     │  Gemini)
│                    │
         LOW                    HIGH
```

## Tools suggestion
Python matplotlib (recommended for publication), or Inkscape/Illustrator for manual.

Sample matplotlib code scaffold:
```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.axvline(x=5, color='gray', linestyle='--', alpha=0.3)
ax.axhline(y=5, color='gray', linestyle='--', alpha=0.3)
ax.set_xlabel('Task Generality (X)', fontsize=12)
ax.set_ylabel('Individuality (Y)', fontsize=12)

# Systems
systems = {
    'GPT-4o\nClaude 3.5': (8, 1.5),
    'Narrow Tool\n(calculator)': (1.5, 1),
    'Specialist Actor\n(domain agent)': (2, 7.5),
    '★ AGI Target': (8, 8),
}
for name, (x, y) in systems.items():
    ax.annotate(name, (x, y), ha='center', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

ax.set_title('Two Design Orientations for Intelligent Agents', fontsize=11)
plt.tight_layout()
plt.savefig('figure1.pdf', dpi=300, bbox_inches='tight')
```
