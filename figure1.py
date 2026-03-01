import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(7, 5.8))
ax.set_xlim(-0.8, 10.8)
ax.set_ylim(-0.8, 10.8)

# Quadrant dividers
ax.axvline(x=5, color='#dddddd', linestyle='-', alpha=0.6, linewidth=0.8)
ax.axhline(y=5, color='#dddddd', linestyle='-', alpha=0.6, linewidth=0.8)

# Axis labels with endpoint descriptors
ax.set_xlabel('Task Generality', fontsize=11, fontweight='bold', labelpad=8)
ax.set_ylabel('Individuality', fontsize=11, fontweight='bold', labelpad=8)
ax.text(0.5, -0.6, 'Single-task', fontsize=7, color='#999999', ha='center')
ax.text(10, -0.6, 'Any task', fontsize=7, color='#999999', ha='center')
ax.text(-0.6, 0.5, 'Stateless', fontsize=7, color='#999999', ha='center', rotation=90)
ax.text(-0.6, 10, 'Persistent\nidentity', fontsize=7, color='#999999', ha='center', rotation=90)

ax.set_xticks([])
ax.set_yticks([])

# Quadrant labels — all four, same style
for label, pos in [('Specialist Actor', (2.5, 9.2)), ('AGI Target', (7.5, 9.2)),
                    ('Narrow Tool', (2.5, 0.6)), ('Frontier LLM', (7.5, 0.6))]:
    ax.text(pos[0], pos[1], label, fontsize=9.5, ha='center', va='center',
            color='#aaaaaa', fontweight='bold')

# System markers with shapes
# Frontier LLMs (blue circles)
for name, pos in [('GPT-4o', (8.5, 2.0)), ('Claude 3.5', (7.5, 2.5)), ('Gemini', (8.0, 1.5))]:
    ax.plot(pos[0], pos[1], 'o', color='#2166ac', markersize=7, zorder=5)
    ax.annotate(name, pos, fontsize=7, ha='center', va='bottom',
                xytext=(0, 7), textcoords='offset points', color='#333333')

# Specialist actors (orange triangles)
for name, pos in [('Domain expert\nagent', (2.2, 7.2)), ('Urban sim\nagent', (3.2, 8.0))]:
    ax.plot(pos[0], pos[1], '^', color='#d6604d', markersize=8, zorder=5)
    ax.annotate(name, pos, fontsize=7, ha='center', va='bottom',
                xytext=(0, 8), textcoords='offset points', color='#333333')

# Narrow tools (gray squares)
for name, pos in [('Calculator', (1.5, 1.2)), ('Rules-based\nchatbot', (2.8, 1.8))]:
    ax.plot(pos[0], pos[1], 's', color='#999999', markersize=6, zorder=5)
    ax.annotate(name, pos, fontsize=7, ha='center', va='bottom',
                xytext=(0, 7), textcoords='offset points', color='#333333')

# AGI target star — empty quadrant emphasis
rect = mpatches.FancyBboxPatch((5.3, 5.3), 4.7, 4.7, boxstyle="round,pad=0.2",
                                 facecolor='#fff8e1', edgecolor='#e6ab02', 
                                 alpha=0.25, linewidth=1, linestyle='--', zorder=1)
ax.add_patch(rect)
ax.plot(7.5, 7.5, marker='*', markersize=22, color='#e6ab02',
        markeredgecolor='#b8860b', markeredgewidth=1, zorder=5)
ax.text(7.5, 8.3, 'No current\nsystem', fontsize=8, ha='center',
        color='#b8860b', fontweight='bold')

# Research direction arrows — standardized, both originating from frontier LLM cluster
# Current effort: horizontal
ax.annotate('', xy=(10.2, 2.0), xytext=(8.8, 2.0),
            arrowprops=dict(arrowstyle='->', color='#2166ac', lw=2.2))
ax.text(10.3, 2.0, 'Current\nresearch\neffort', fontsize=7, ha='left', va='center',
        color='#2166ac', fontstyle='italic')

# Missing direction: vertical
ax.annotate('', xy=(8.0, 5.2), xytext=(8.0, 2.8),
            arrowprops=dict(arrowstyle='->', color='#d6604d', lw=2.2, linestyle='dashed'))
ax.text(8.8, 4.0, 'Missing\nresearch\ndirection', fontsize=7, ha='left', va='center',
        color='#d6604d', fontstyle='italic')

# Application spectrum diagonal
ax.plot([8.2, 2.5], [2.2, 7.8], ':', color='#888888', alpha=0.5, linewidth=1.2)
spec_labels = [('Productivity', (9.0, 2.8)), ('Companion', (6.5, 4.2)),
               ('Education', (5.0, 5.5)), ('Simulation', (3.0, 7.2))]
for label, pos in spec_labels:
    ax.text(pos[0], pos[1], label, fontsize=6.5, ha='center', color='#777777', fontstyle='italic')

# Legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#2166ac', markersize=7, label='Frontier LLM'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#d6604d', markersize=7, label='Identity-oriented'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#999999', markersize=6, label='Narrow tool'),
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='#e6ab02', markersize=10, label='AGI target'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=7, framealpha=0.9,
          edgecolor='#cccccc', bbox_to_anchor=(0.02, 0.02))

# Clean up
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.2)
ax.spines['left'].set_linewidth(1.2)

plt.tight_layout()
plt.savefig('figure1.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure1.png', dpi=300, bbox_inches='tight')
print('Figure 1 v2 saved')
