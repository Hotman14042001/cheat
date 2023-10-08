# Impor modul yang diperlukan
import os

# Fungsi untuk mengatur jumlah diamond
def set_diamond_count(count):
    # Gantilah kode ini dengan cara yang sesuai dengan game Anda
    # Misalnya, jika game Anda menyimpan jumlah diamond dalam file 'diamond.txt':
    with open('diamond.txt', 'w') as file:
        file.write(str(count))

# Fungsi untuk mendapatkan jumlah diamond saat ini
def get_diamond_count():
    # Gantilah kode ini dengan cara yang sesuai dengan game Anda
    # Misalnya, jika game Anda menyimpan jumlah diamond dalam file 'diamond.txt':
    with open('diamond.txt', 'r') as file:
        count = file.read()
    return int(count)

# Main program
while True:
    print("1. Set jumlah diamond")
    print("2. Tampilkan jumlah diamond")
    print("3. Keluar")
    choice = input("Pilih aksi: ")

    if choice == "1":
        new_count = int(input("Masukkan jumlah diamond baru: "))
        set_diamond_count(new_count)
        print("Jumlah diamond telah diatur.")
    elif choice == "2":
        current_count = get_diamond_count()
        print(f"Jumlah diamond saat ini: {current_count}")
    elif choice == "3":
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
