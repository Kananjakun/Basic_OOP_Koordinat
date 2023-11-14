class CTitik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def tambah_titik(self, titik_lain):
        if isinstance(titik_lain, CTitik):
            x_hasil = self.x + titik_lain.x
            y_hasil = self.y + titik_lain.y
            return CTitik(x_hasil, y_hasil)


# memasukan input pada kedua titik
titik1 = CTitik(int(input(("Masukan angka x pada titik 1 :"))), (int(input(("Masukan angka Y pada titik 1:")))))
titik2 = CTitik(int(input(("Masukan angka x pada titik 2 :"))), (int(input(("Masukan angka Y pada titik 2:")))))

# Soal A yaitu memodelkan titik dari class CTitik diatas 
print("Titik 1:", titik1)
print("Titik 2:", titik2)

# Soal B yaitu method untuk melakukan penjumlahan kedua titik
titik3 = titik1 .tambah_titik(titik2)
print("Penjumlahan titik1 dan titik2:", titik3)