import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    return points

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    circle_points = []

    while x <= y:
        circle_points.extend(plot_circle_points(xc, yc, x, y))
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x + 1 - 2 * y

    return circle_points

# Gambar lingkaran dengan pusat (0,0) dan jari-jari 6
points = midpoint_circle(0, 0, 6)

# Plot hasil
x_vals, y_vals = zip(*points)
plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='blue')
plt.gca().set_aspect('equal')
plt.title('Midpoint Circle (0,0) radius 6')
plt.grid(True)
plt.show()