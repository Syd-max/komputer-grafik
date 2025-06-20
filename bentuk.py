import cv2


image = cv2.imread(r"C:\Users\Solid Komputer\Documents\pertemuan 7\download.nasi.jpeg")

if image is None:
    print("Gambar tidak ditemukan")
    exit()


height, width, channels = image.shape
print("Tinggi :", height)
print("Lebar  :", width)
print("Channel:", channels)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
  
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)

    if len(approx) == 3:
        bentuk = "Segitiga"
    elif len(approx) == 4:
        bentuk = "Persegi/Panjang"
    elif len(approx) > 4:
        bentuk = "Lingkaran/Oval"
    else:
        bentuk = "Tidak dikenal"

    
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.putText(image, bentuk, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("Deteksi Bentuk", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
