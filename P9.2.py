import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

objek = np.array([
    [1, 3, 3, 1, 1],  # x
    [1, 1, 3, 3, 1]   # y
])

shx = 1
shy = 1

shear_x = np.array([
    [1, shx],
    [0, 1]
])

shear_y = np.array([
    [1, 0],
    [shy, 1]
])

hasil_shear_x = shear_x @ objek
hasil_shear_y = shear_y @ objek

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(objek[0], objek[1], 'bo-', label='Awal')
plt.plot(hasil_shear_x[0], hasil_shear_x[1], 'ro-', label='Shear X')
plt.title('Shear terhadap Sumbu X')
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(objek[0], objek[1], 'bo-', label='Awal')
plt.plot(hasil_shear_y[0], hasil_shear_y[1], 'go-', label='Shear Y')
plt.title('Shear terhadap Sumbu Y')
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
