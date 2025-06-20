import cv2
import numpy as np


image = cv2.imread(r"C:\Users\Solid Komputer\Documents\pertemuan 7\download.nasi.jpeg")


if image is None:
    print("Gambar tidak ditemukan! Periksa path.")
    exit()


bright_image = cv2.convertScaleAbs(image, alpha=1, beta=50)


dark_image = cv2.convertScaleAbs(image, alpha=1, beta=-50)


cv2.imshow("Gambar Asli", image)
cv2.imshow("Lebih Cerah (Brightness +50)", bright_image)
cv2.imshow("Lebih Gelap (Brightness -50)", dark_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
