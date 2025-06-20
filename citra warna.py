import cv2
import numpy as np


image = cv2.imread(r"C:\Users\Solid Komputer\Documents\pertemuan 7\download.nasi.jpeg")



B, G, R = cv2.split(image)


zeros = np.zeros_like(B)

blue_image = cv2.merge([B, zeros, zeros])
green_image = cv2.merge([zeros, G, zeros])
red_image = cv2.merge([zeros, zeros, R])


cv2.imshow("Gambar Asli", image)
cv2.imshow("Channel Biru", blue_image)
cv2.imshow("Channel Hijau", green_image)
cv2.imshow("Channel Merah", red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
