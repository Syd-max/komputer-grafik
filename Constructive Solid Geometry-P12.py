import trimesh
# Benda dasar
cube = trimesh.creation.box(extents=[2, 2, 2])
sphere = trimesh.creation.icosphere(radius=1.3)
sphere.apply_translation([1.0, 1.0, 0.0])
# Union
result = cube.union(sphere)
# Tampilkan (pakai viewer dari Trimesh)
result.show()