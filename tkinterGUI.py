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

# ==========================================
# 5. layout: buat frame utama pembungkus
# ==========================================
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# ==========================================
# 6. feat: tambah label judul aplikasi
# ==========================================
label_judul = ttk.Label(
    main_frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Helvetica", 16, "bold"),
    anchor="center",
)
label_judul.pack(pady=(0, 20))

# ==========================================
# 7. layout: buat frame penampung input
# ==========================================
frame_input = ttk.Frame(main_frame)
frame_input.pack(fill=tk.X, pady=5)

# ==========================================
# 8. refactor: definisikan daftar mata pelajaran
# ==========================================
mata_pelajaran = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sosiologi", "Geografi", "Informatika"
]
entries_nilai = []

# ==========================================
# 9. feat: buat label nilai secara dinamis
# ==========================================
for i, mapel in enumerate(mata_pelajaran):
    lbl = ttk.Label(frame_input, text=f"Nilai {mapel}:", font=("Helvetica", 10))
    lbl.grid(row=i, column=0, sticky=tk.W, pady=4, padx=(0, 10))
    
    # ==========================================
    # 10. feat: buat input entry nilai secara dinamis
    # ==========================================
    entry = ttk.Entry(frame_input, width=25)
    entry.grid(row=i, column=1, sticky=tk.E, pady=4)
    frame_input.grid_columnconfigure(1, weight=1)
    entries_nilai.append(entry)

