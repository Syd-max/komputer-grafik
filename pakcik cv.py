import cv2


image = cv2.imread(r'c:\Users\Solid Komputer\Documents\pertemuan 7\download.nasi.jpeg') 

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


threshold_value = 127 
max_value = 255       
_, binary_image = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY)


cv2.imshow('Gambar Asli', image)
cv2.imshow('Gambar Grayscale', gray_image)
cv2.imshow('Gambar Biner', binary_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
