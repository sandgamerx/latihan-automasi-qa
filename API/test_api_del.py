import requests
import pytest
import json

# ... (fungsi-fungsi tes sebelumnya bisa tetap ada) ...

def test_delete_post():
    """Tes untuk menghapus postingan dan memverifikasi bahwa ia sudah hilang."""

    # --- LANGKAH A: HAPUS POSTINGAN ---
    
    # 1. Tentukan URL dari data yang mau dihapus
    url_delete = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Kirim permintaan DELETE
    response_delete = requests.delete(url_delete)

    # 3. Verifikasi (Assertion)
    # Status code untuk DELETE yang berhasil biasanya 200 (OK)
    assert response_delete.status_code == 200
    print(f"\nStatus Code DELETE: {response_delete.status_code} (OK)")
    
    # Respons body dari DELETE biasanya kosong, menandakan data sudah dihapus
    print(f"Respons Body DELETE: {response_delete.json()}")


    # --- LANGKAH B: PASTIKAN DATA BENAR-BENAR HILANG ---
    
    print("\nMemverifikasi bahwa data sudah tidak ada...")
    # 1. Kirim permintaan GET ke URL yang sama
    response_get = requests.get(url_delete)

    # 2. Verifikasi (Assertion)
    # Server HARUS merespons dengan 404 Not Found, ini bukti data sudah dihapus
    assert response_get.status_code == 404
    print(f"Status Code GET setelah DELETE: {response_get.status_code} (Not Found)")
    print("Verifikasi Berhasil: Data postingan #1 sudah tidak bisa ditemukan.")
    print("--- TEST PASSED ---")