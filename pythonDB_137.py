import tkinter as tk
import sqlite3

# Array untuk perulangan entry dan label dibawah
arrEntry = ['Nama', 'Biologi', 'Fisika', 'Bahasa']

# Fungsi Pernyataan Pilihan untuk mencari nilai tertinggi dari ketiga nilai
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak dapat diprediksi" 

# Fungsi memasukan nilai ke database
def masuknilai(A, B, C, D, E):
    conn = sqlite3.connect("D:\Brilliance\pythonDB_137\DatabasePY_7_TGS.db")
    cursor = conn.cursor()

    # Membuat Tabel di database jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Nama_Siswa TEXT, 
                       Biologi INTEGER, 
                       Fisika INTEGER,
                       Bahasa INTEGER,
                       Prediksi_Fakultas TEXT)''')
    
    # Memasukan Nilai ke database
    cursor.execute("INSERT INTO nilai_siswa (Nama_Siswa, Biologi, Fisika, Bahasa, Prediksi_Fakultas) VALUES (?, ?, ?, ?, ?)",
                   (A, B, C, D, E))
    
    conn.commit()  # Melakukan commit untuk menyimpan perubahan ke database
    conn.close()   # Menutup koneksi ke database

# Fungsi yang dipanggil saat tombol "Hasil Prediksi" ditekan
def callback():
    nilai1 = str(entries[0].get())  # Mengambil Nilai dari entries
    nilai2 = int(entries[1].get())
    nilai3 = int(entries[2].get())
    nilai4 = int(entries[3].get())

    # Memasukan hasil prediksi ke nilai5
    nilai5 = prediksi_fakultas(nilai2, nilai3, nilai4)

    # Memanggil fungsi database
    masuknilai(nilai1, nilai2, nilai3, nilai4, nilai5)

    # Mengubah text pada label hasil_prediksi
    hasil_prediksi.config(text="Hasil Prediksi " + nilai5)

# Membuat Main Window
window = tk.Tk()
window.geometry("800x800")
window.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat frame
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
frame1 = tk.Frame(window)
frame1.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Label judul
judul = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", anchor=tk.CENTER, font=("Lobster 1.4", 22))
judul.pack()

# Membuat entry dan label menggunakan perulangan
entries = []
for i in range(4):
    nilai_label = tk.Label(frame, text=arrEntry[i] + ":", font=("Helvetica", 10))
    nilai_label.pack()
    
    entry = tk.Entry(frame)
    entry.pack()
    entries.append(entry)

# Tombol untuk memanggil fungsi callback
prediksi_button = tk.Button(frame, text="Hasil Prediksi", command=callback)
prediksi_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
hasil_prediksi = tk.Label(frame1, font=("Book Antiqua", 20))
hasil_prediksi.grid(row=1, column=0, columnspan=2, pady=10)

# Memulai loop utama
window.mainloop()
