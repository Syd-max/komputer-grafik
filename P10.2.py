import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid")

xmin, xmax = 100, 300
ymin, ymax = 100, 300

lines = {
    "Inside": {"points": [(150, 150), (250, 250)], "color": "green"},
    "Outside": {"points": [(50, 50), (90, 90)], "color": "red"}, 
    "Cross": {"points": [(50, 150), (350, 150)], "color": "orange"},
    "Diagonal": {"points": [(50, 50), (350, 350)], "color": "blue"}
}

plt.figure(figsize=(10, 10))

plt.plot([xmin, xmax, xmax, xmin, xmin], 
         [ymin, ymin, ymax, ymax, ymin], 
         'k--', linewidth=2, label='Clipping Window')

for name, data in lines.items():
    (x1, y1), (x2, y2) = data["points"]
    plt.plot([x1, x2], [y1, y2], 
             color=data["color"], 
             linewidth=3,
             linestyle='-',
             marker='o',
             markersize=8,
             label=f"{name} Line")

plt.xlim(0, 400)
plt.ylim(0, 400)
plt.title("Line Clipping Visualization (All Lines Visible)", pad=20)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
