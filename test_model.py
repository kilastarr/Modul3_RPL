from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

buku_model = BukuModel()
anggota_model = AnggotaModel()

print("--- PENGUJAN BUKU MODEL (UPDATE & DELETE) ---")

# 1. Update Buku (sesuaikan ID buku, misal ID 7)
buku_model.update_buku(7, "Pemrograman Python MVC (Edisi Revisi)", "Guido van Rossum", 2024)
print("Data buku berhasil diperbarui!")

print("\nDaftar Buku Setelah Update:")
for buku in buku_model.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 2. Delete Buku (misal ID 7)
print("\n--- Menghapus Buku ID 7 ---")
buku_model.delete_buku(7)
print("Data buku berhasil dihapus!")

print("\nDaftar Buku Setelah Delete:")
for buku in buku_model.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


print("\n--- PENGUJAN ANGGOTA MODEL (CREATE & READ) ---")

# 1. Create Anggota
anggota_model.create_anggota("Nalla Azzura", "Jl.Garuda")
print("Data anggota berhasil ditambahkan!")

# 2. Read Anggota
print("\nDaftar Anggota:")
for anggota in anggota_model.get_all_anggota():
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")