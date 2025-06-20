import cv2


image = cv2.imread(r"C:\Users\Solid Komputer\Documents\pertemuan 7\download.nasi.jpeg")


if image is None:
    print("Gambar tidak ditemukan.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)


contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


output = image.copy()
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)  


cv2.imshow("Gambar Asli", image)
cv2.imshow("Kontur (Hijau)", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
