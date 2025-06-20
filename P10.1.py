import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

world_coords = np.array([
    [20, 80],   # P1
    [80, 80],   # P2
    [80, 20],   # P3
    [20, 20],   # P4
    [20, 80]    # P1 (penutup)
])

wxmin, wymin = 20, 20
wxmax, wymax = 80, 80

vxmin, vymin = 0, 0
vxmax, vymax = 400, 300

def world_to_viewport(x, y):
    sx = (vxmax - vxmin) / (wxmax - wxmin)
    sy = (vymax - vymin) / (wymax - wymin)
    vx = vxmin + (x - wxmin) * sx
    vy = vymin + (y - wymin) * sy
    return vx, vy

viewport_coords = np.array([world_to_viewport(x, y) for x, y in world_coords])

df_world = pd.DataFrame(world_coords, columns=['x', 'y'])
df_world['space'] = 'World'
df_world['label'] = ['P1', 'P2', 'P3', 'P4', 'P1']

df_viewport = pd.DataFrame(viewport_coords, columns=['x', 'y'])
df_viewport['space'] = 'Viewport'
df_viewport['label'] = ['P1', 'P2', 'P3', 'P4', 'P1']

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(df_world['x'], df_world['y'], marker='o', color='blue')
axs[0].set_title('Koordinat Dunia (Window)')
axs[0].set_xlim(0, 100)
axs[0].set_ylim(0, 100)
axs[0].grid(True)
for i, row in df_world.iterrows():
    axs[0].text(row['x'] + 1, row['y'] + 1, row['label'], fontsize=9)

axs[1].plot(df_viewport['x'], df_viewport['y'], marker='o', color='orange')
axs[1].set_title('Koordinat Layar (Viewport)')
axs[1].set_xlim(0, 450)
axs[1].set_ylim(0, 350)
axs[1].grid(True)
for i, row in df_viewport.iterrows():
    axs[1].text(row['x'] + 5, row['y'] + 5, row['label'], fontsize=9)

plt.suptitle('Transformasi Viewing: Window ke Viewport', fontsize=14)
plt.tight_layout()
plt.show()
