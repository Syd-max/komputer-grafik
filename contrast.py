import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Solid Komputer\Documents\pertemuan 7\download.nasi.jpeg")


if image is None:
    print("Gambar tidak ditemukan! Periksa path.")
    exit()

high_contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)

low_contrast = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
cv2.imshow("Gambar Asli", image)
cv2.imshow("Kontras Tinggi (alpha=1.5)", high_contrast)
cv2.imshow("Kontras Rendah (alpha=0.5)", low_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()
