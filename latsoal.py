import tkinter as tk

class BingkaiBulat(tk.Canvas):
    def __init__(self, root):
        super().__init__(root, width=400, height=300, bg='white')
        self.pack()
        self.gambar_bingkai_dan_teks()

    def gambar_bingkai_dan_teks(self):
       
        self.create_oval(80, 50, 320, 270, fill='yellow', outline='black', width=3)

        
        self.create_text(200, 130, text="Selamat Datang", font=("Arial", 18, "bold"))
        self.create_text(200, 170, text="Tangerang", font=("Arial", 18, "bold"))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Selamat Datang Tangerang")
    app = BingkaiBulat(root)
    root.mainloop()
