import matplotlib.pyplot as plt

def draw_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    # Region 1
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    ellipse_points = []

    while dx < dy:
        ellipse_points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)
        ])

        if p1 < 0:
            x += 1
            dx = dx + 2 * ry**2
            p1 = p1 + dx + ry**2
        else:
            x += 1
            y -= 1
            dx = dx + 2 * ry**2
            dy = dy - 2 * rx**2
            p1 = p1 + dx - dy + ry**2

    # Region 2
    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2

    while y >= 0:
        ellipse_points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y)
        ])

        if p2 > 0:
            y -= 1
            dy = dy - 2 * rx**2
            p2 = p2 + rx**2 - dy
        else:
            y -= 1
            x += 1
            dx = dx + 2 * ry**2
            dy = dy - 2 * rx**2
            p2 = p2 + dx - dy + rx**2

    return ellipse_points

# Contoh pemanggilan fungsi
rx, ry = 50, 30  # jari-jari ellipse
xc, yc = 100, 100  # titik pusat ellipse

points = draw_ellipse(rx, ry, xc, yc)

# Plot
x_vals, y_vals = zip(*points)
plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, color='blue', s=1)
plt.title('Midpoint Ellipse Algorithm')
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()