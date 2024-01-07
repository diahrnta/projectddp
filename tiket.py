import tkinter as tk
from datetime import datetime


class AplikasiParkir(tk.Tk):
    def __init__(self):
        super().__init__()
        

        self.title("Biaya Parkir")
        self.geometry("300x200")

        self.label_masuk = tk.Label(self, text="Waktu Masuk:")
        self.label_masuk.pack(pady=5)

        self.masuk_var = tk.StringVar()
        self.entry_masuk = tk.Entry(self, textvariable=self.masuk_var)
        self.entry_masuk.pack(pady=5)

        self.label_keluar = tk.Label(self, text="Waktu Keluar:")
        self.label_keluar.pack(pady=5)

        self.keluar_var = tk.StringVar()
        self.entry_keluar = tk.Entry(self, textvariable=self.keluar_var)
        self.entry_keluar.pack(pady=5)

        self.button_hitung = tk.Button(self, text="Hitung Biaya Parkir", command=self.hitung_biaya, bg="blue")
        self.button_hitung.pack(pady=10)

        self.label_hasil = tk.Label(self, text="")
        self.label_hasil.pack(pady=10)

    def hitung_biaya(self):
        waktu_masuk = datetime.strptime(self.masuk_var.get(), "%H:%M")
        waktu_keluar = datetime.strptime(self.keluar_var.get(), "%H:%M")

        selisih_waktu = waktu_keluar - waktu_masuk
        biaya_parkir = selisih_waktu.seconds // 3600 * 5000  # Biaya per jam, misalnya 5000 per jam

        self.label_hasil.config(text=f"Biaya Parkir: Rp {biaya_parkir:,}")

if __name__ == "__main__":
    aplikasi = AplikasiParkir()
    aplikasi.mainloop()
