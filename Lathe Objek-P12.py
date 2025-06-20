import numpy as np
import pyvista as pv
def create_profile():
    z = np.linspace(-1, 1, 50)
    x = np.sqrt(1 - z**2)
    return np.column_stack((x, np.zeros_like(x), z))
profile_points = create_profile()
angle_steps = 60 
theta = np.linspace(0, 2*np.pi, angle_steps)
mesh_points = []
for angle in theta:
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    for x, y, z in profile_points:
        mesh_points.append([x*cos_a, x*sin_a, z])
mesh_points = np.array(mesh_points)
faces = []
n_profile = len(profile_points)
for i in range(angle_steps - 1):
    for j in range(n_profile - 1):
        a = i * n_profile + j
        b = a + 1
        c = a + n_profile
        d = c + 1
        faces.append([4, a, b, d, c])
faces = np.hstack(faces)
lathed_mesh = pv.PolyData(mesh_points, faces)
plotter = pv.Plotter()
plotter.add_mesh(lathed_mesh, color='orange', show_edges=True)
plotter.show()