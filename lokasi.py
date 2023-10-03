import geocoder

# Alamat yang ingin Anda cek lokasinya
alamat = "Jalan Contoh No. 123, Kota Contoh, Indonesia"

# Mencari lokasi berdasarkan alamat
lokasi = geocoder.osm(alamat)

if lokasi.ok:
    print(f"Lokasi: {lokasi.address}")
    print(f"Latitude: {lokasi.latlng[0]}")
    print(f"Longitude: {lokasi.latlng[1]}")
else:
    print("Tidak dapat menemukan lokasi.")
