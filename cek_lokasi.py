import geocoder
import pygame

# Alamat yang ingin Anda cek lokasinya
alamat = "Jalan Contoh No. 123, Kota Contoh, Indonesia"

# Mencari lokasi berdasarkan alamat
lokasi = geocoder.osm(alamat)

if lokasi.ok:
    print(f"Lokasi: {lokasi.address}")
    print(f"Latitude: {lokasi.latlng[0]}")
    print(f"Longitude: {lokasi.latlng[1]}")

    # Inisialisasi pygame
    pygame.mixer.init()

    # Nama file musik atau suara yang ingin Anda putar
    file_musik = "manullang11404.mp3"  # Ganti "nama_file_musik.mp3" dengan nama file Anda

    # Memutar musik
    pygame.mixer.music.load(file_musik)
    pygame.mixer.music.play()

else:
    print("Tidak dapat menemukan lokasi.")
