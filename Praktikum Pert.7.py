import numpy as np
import matplotlib.pyplot as plt

# Titik 3D (x, y, z)
points = np.array([
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1]
])

# Edge of cube (for drawing)
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # front face
    [4, 5], [5, 6], [6, 7], [7, 4],  # back face
    [0, 4], [1, 5], [2, 6], [3, 7]   # side edges
]

def plot_projection(projected, title):
    plt.figure()
    for edge in edges:
        p1, p2 = projected[edge[0]], projected[edge[1]]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b')
    plt.title(title)
    plt.gca().set_aspect('equal')
    plt.grid(True)

# === A. ORTHOGRAPHIC PROJECTION ===
orthographic = points[:, :2]  # Ambil x, y saja
plot_projection(orthographic, "Orthographic Projection")

# === B. OBLIQUE PROJECTION ===
alpha = np.deg2rad(45)  # sudut terhadap sumbu x
L = 1  # panjang proyeksi z
oblique_matrix = np.array([
    [1, 0, L * np.cos(alpha)],
    [0, 1, L * np.sin(alpha)]
])
oblique = np.dot(points, oblique_matrix.T)
plot_projection(oblique, "Oblique Projection (Cavalier)")

# === C. PERSPECTIVE PROJECTION ===
d = 2  # Jarak dari proyektor ke bidang proyeksi
perspective = np.array([
    [d * x / (z + d), d * y / (z + d)]
    for x, y, z in points
])
plot_projection(perspective, "Perspective Projection")

plt.show()