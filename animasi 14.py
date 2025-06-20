import tkinter as tk
import time
import random

class AnimasiOrang:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=500, height=300, bg='black')
        self.canvas.pack()
        
        self.teks = self.canvas.create_text(250, 30, text="UAS - DWI SUTIKNO",
                                            font=("Comic Sans MS", 24, "bold"),
                                            fill="white")
        
        self.orang = self.gambar_orang(-50, 150)
        self.x_orang = -50
        self.v = 10

        self.animasi()

    def gambar_orang(self, x, y):
        
        kepala = self.canvas.create_oval(x+10, y-40, x+50, y, fill='white')
    
        badan = self.canvas.create_line(x+30, y, x+30, y+50, fill='white', width=3)
     
        tangan_kiri = self.canvas.create_line(x+30, y+10, x+10, y+40, fill='white', width=3)
        tangan_kanan = self.canvas.create_line(x+30, y+10, x+50, y+40, fill='white', width=3)
       
        kaki_kiri = self.canvas.create_line(x+30, y+50, x+10, y+80, fill='white', width=3)
        kaki_kanan = self.canvas.create_line(x+30, y+50, x+50, y+80, fill='white', width=3)

        return [kepala, badan, tangan_kiri, tangan_kanan, kaki_kiri, kaki_kanan]

    def update_orang(self):
        for bagian in self.orang:
            self.canvas.move(bagian, self.v, 0)
        self.x_orang += self.v
        if self.x_orang > 500:
            for bagian in self.orang:
                self.canvas.move(bagian, -self.x_orang - 50, 0)
            self.x_orang = -50

    def update_teks(self):
        dx = random.randint(-3, 3)
        dy = random.randint(-3, 3)
        self.canvas.move(self.teks, dx, dy)

    def animasi(self):
        self.update_orang()
        self.update_teks()
        self.canvas.after(100, self.animasi)

root = tk.Tk()
root.title("Animasi Orang - UAS Komputer Grafik")
app = AnimasiOrang(root)
root.mainloop()
