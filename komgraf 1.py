import tkinter as tk

class KomputerGrafik1(tk.Canvas):
    def __init__(self, root):
        super().__init__(root, width=300, height=250, bg='white')
        self.pack()
        self.gambar_bingkai()

    def gambar_bingkai(self):

        points = [
            10, 10,
            200, 10,
            200, 110,
            30, 110,
            10, 125,
            20, 110,
            10, 110
        ]
        self.create_polygon(points, fill='yellow', outline='black')
      
        self.create_text(150, 50, text="Komputer Grafik 1", font=("Arial", 14, "bold"))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("UAS Komputer Grafik")
    app = KomputerGrafik1(root)
    root.mainloop()

