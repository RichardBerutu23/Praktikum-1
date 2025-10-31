import tkinter as tk
from tkinter import messagebox

# =======================
# LATIHAN 1 - Operasi Aritmatika
# =======================
def buka_latihan1():
    win = tk.Toplevel(root)
    win.title("Latihan 1 - Operasi Aritmatika")
    win.geometry("400x300")

    tk.Label(win, text="Masukkan Angka 1:").pack(pady=5)
    e1 = tk.Entry(win)
    e1.pack()

    tk.Label(win, text="Masukkan Angka 2:").pack(pady=5)
    e2 = tk.Entry(win)
    e2.pack()

    hasil = tk.StringVar()

    def hitung():
        try:
            a = float(e1.get())
            b = float(e2.get())
            hasil.set(f"""
            Penjumlahan: {a+b}
            Pengurangan: {a-b}
            Perkalian: {a*b}
            Pembagian: {a/b if b!=0 else 'Error (bagi 0)'}
            """)
        except ValueError:
            messagebox.showerror("Error", "Input harus angka!")

    tk.Button(win, text="Hitung", command=hitung, bg="#3498db", fg="white").pack(pady=10)
    tk.Label(win, textvariable=hasil, fg="blue").pack(pady=10)

# =======================
# LATIHAN 2 - Kalkulator
# =======================
def buka_latihan2():
    win = tk.Toplevel(root)
    win.title("Latihan 2 - Kalkulator")
    win.geometry("400x300")

    tk.Label(win, text="Masukkan Angka 1:").pack(pady=5)
    e1 = tk.Entry(win)
    e1.pack()

    tk.Label(win, text="Masukkan Angka 2:").pack(pady=5)
    e2 = tk.Entry(win)
    e2.pack()

    tk.Label(win, text="Operator (+, -, *, /):").pack(pady=5)
    eop = tk.Entry(win)
    eop.pack()

    hasil = tk.StringVar()

    def hitung():
        try:
            a = float(e1.get())
            b = float(e2.get())
            op = eop.get()
            if op == '+':
                res = a+b
            elif op == '-':
                res = a-b
            elif op == '*':
                res = a*b
            elif op == '/':
                res = "Error (bagi 0)" if b==0 else a/b
            else:
                res = "Operator tidak valid"
            hasil.set(f"Hasil: {res}")
        except ValueError:
            messagebox.showerror("Error", "Input harus angka!")

    tk.Button(win, text="Hitung", command=hitung, bg="#2ecc71", fg="white").pack(pady=10)
    tk.Label(win, textvariable=hasil, fg="blue", font=("Arial",12,"bold")).pack(pady=10)

# =======================
# LATIHAN 3 - Nilai Akademik
# =======================
def buka_latihan3():
    def hitung_nilai_akhir(sikap, tugas, uts, uas):
        return (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

    def tentukan_grade(nilai):
        if 81 <= nilai <= 100: return "A", 4
        elif 76 <= nilai <= 80: return "B+", 3.5
        elif 71 <= nilai <= 75: return "B", 3
        elif 66 <= nilai <= 70: return "C+", 2.5
        elif 56 <= nilai <= 65: return "C", 2
        elif 46 <= nilai <= 55: return "D", 1
        else: return "E", 0

    def proses_hitung():
        try:
            sikap = float(entry_sikap.get())
            tugas = float(entry_tugas.get())
            uts = float(entry_uts.get())
            uas = float(entry_uas.get())

            total = hitung_nilai_akhir(sikap, tugas, uts, uas)
            grade, bobot = tentukan_grade(total)
            status = "Lulus" if total >= 56 else "Tidak Lulus"

            hasil.set(f"📊 Total Nilai: {total:.2f}\n"
                      f"🏅 Grade: {grade} (Bobot {bobot})\n"
                      f"📌 Keterangan: {status}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 3 - Nilai Akademik")
    win.geometry("500x400")

    tk.Label(win, text="Form Hitung Nilai Akhir Akademik", font=("Arial",14,"bold")).pack(pady=10)

    frame = tk.Frame(win, padx=10, pady=10)
    frame.pack()

    labels = ["Sikap/Kehadiran:", "Tugas:", "UTS:", "UAS:"]
    entries = []
    for i, lbl in enumerate(labels):
        tk.Label(frame, text=lbl).grid(row=i, column=0, sticky="w", pady=5)
        ent = tk.Entry(frame)
        ent.grid(row=i, column=1, pady=5)
        entries.append(ent)

    entry_sikap, entry_tugas, entry_uts, entry_uas = entries

    tk.Button(frame, text="Hitung", command=proses_hitung, bg="#e67e22", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

    hasil = tk.StringVar()
    tk.Label(frame, textvariable=hasil, font=("Arial",12), fg="blue").grid(row=5, column=0, columnspan=2, pady=10)

# =======================
# MENU UTAMA (FORM)
# =======================
root = tk.Tk()
root.title("Menu Utama - Latihan Program")
root.geometry("400x300")
root.configure(bg="#ecf0f1")

tk.Label(root, text="Pilih Latihan", font=("Arial",16,"bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=20)

tk.Button(root, text="Latihan 1 - Operasi Aritmatika", font=("Arial",12),
          bg="#3498db", fg="white", width=30, command=buka_latihan1).pack(pady=10)

tk.Button(root, text="Latihan 2 - Kalkulator", font=("Arial",12),
          bg="#2ecc71", fg="white", width=30, command=buka_latihan2).pack(pady=10)

tk.Button(root, text="Latihan 3 - Nilai Akademik", font=("Arial",12),
          bg="#e67e22", fg="white", width=30, command=buka_latihan3).pack(pady=10)

root.mainloop()
