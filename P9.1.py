import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

objek = np.array([
    [1, 2, 2, 1],  # x
    [1, 1, 2, 1]   # y
])

dilatasi_180 = np.array([
    [-1, 0],
    [ 0, -1]
])

rot_neg_45 = np.array([
    [np.cos(-np.pi/4), -np.sin(-np.pi/4)],
    [np.sin(-np.pi/4),  np.cos(-np.pi/4)]
])

refleksi_y = np.array([
    [-1, 0],
    [ 0, 1]
])

rot_45 = np.array([
    [np.cos(np.pi/4), -np.sin(np.pi/4)],
    [np.sin(np.pi/4),  np.cos(np.pi/4)]
])

dilatasi_y_eq_x = rot_45 @ refleksi_y @ rot_neg_45

hasil_180 = dilatasi_180 @ objek
hasil_y_eq_x = dilatasi_y_eq_x @ objek

plt.figure(figsize=(8,8))
plt.plot(objek[0], objek[1], 'bo-', label='Objek Awal')
plt.plot(hasil_180[0], hasil_180[1], 'ro-', label='Dilatasi 180°')
plt.plot(hasil_y_eq_x[0], hasil_y_eq_x[1], 'go-', label='Dilatasi y = x')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.legend()
plt.title("Transformasi Dilatasi")
plt.axis('equal')
plt.show()
