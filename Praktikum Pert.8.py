import matplotlib.pyplot as plt
import numpy as np

# Fungsi menggambar segitiga
def plot_triangle(points, style='b-', label='Original'):
    x = [p[0] for p in points] + [points[0][0]]
    y = [p[1] for p in points] + [points[0][1]]
    plt.plot(x, y, style, label=label)

# 1. Titik awal segitiga
triangle = [(10, 10), (30, 10), (10, 30)]

# === Translasi ===
def translate(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

# === Rotasi terhadap titik pusat tertentu ===
def rotate(points, angle_deg, pivot=(0, 0)):
    angle_rad = np.radians(angle_deg)
    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)
    xp, yp = pivot
    result = []
    for x, y in points:
        x_new = xp + (x - xp) * cos_theta - (y - yp) * sin_theta
        y_new = yp + (x - xp) * sin_theta + (y - yp) * cos_theta
        result.append((round(x_new), round(y_new)))
    return result

# --- Proses ---
translated = translate(triangle, 10, 20)
rotated = rotate(triangle, 90, pivot=(0, 0))  # Rotasi 90° terhadap titik (0,0)

# --- Visualisasi ---
plt.figure(figsize=(8, 8))
plot_triangle(triangle, 'b-', 'Original')
plot_triangle(translated, 'g--', 'Translated')
plot_triangle(rotated, 'r-.', 'Rotated 90°')

plt.legend()
plt.title('Transformasi Geometri: Translasi dan Rotasi')
plt.grid(True)
plt.axis('equal')
plt.show()