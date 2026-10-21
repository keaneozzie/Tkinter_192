# ==========================================
# 1. chore: import library tkinter dan ttk
# ==========================================
import tkinter as tk
from tkinter import ttk

# ==========================================
# 2. feat: tambah fungsi prediksi prodi
# ==========================================
def prediksi_prodi():
    label_hasil_var.set("Hasil Prediksi: Teknologi Informasi")

# ==========================================
# 3. feat: inisialisasi jendela utama
# ==========================================
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.resizable(False, False)

# ==========================================
# 4. style: atur tema aplikasi menggunakan clam
# ==========================================
style = ttk.Style()
style.theme_use("clam")
