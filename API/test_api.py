import requests
import pytest # Kita tetap pakai Pytest untuk assertion
import json

def test_get_single_user():
    """Tes untuk mengambil data satu user dan memverifikasinya."""
    
    # 1. Tentukan alamat (endpoint) API
    # Ini seperti memberitahu pelayan meja nomor berapa yang mau kita tanya
    url = "https://jsonplaceholder.typicode.com/posts/99"

    # 2. Kirim permintaan GET
    # Ini adalah aksi kita 'bertanya' ke pelayan
    response = requests.get(url)

    # 3. Verifikasi (Assertion)
    # A. Pastikan pelayan merespons dengan 'OK' (status code 200)
    assert response.status_code == 200
    print(f"\nStatus Code: {response.status_code} (OK)")

    # B. Ubah respons (yang formatnya JSON) menjadi dictionary Python
    response_data = response.json()
    
    # Cetak respons agar kita bisa lihat isinya
    print("Respons Data:")
    print(response_data)

    # C. Cek apakah ID user sudah benar
    assert response_data["id"] == 99

    # D. Cek apakah email user sudah benar
    expected_title = "temporibus sit alias delectus eligendi possimus magni"
    actual_title = response_data["title"]
    assert actual_title == expected_title
    print(f"Verifikasi Email Berhasil: {actual_title}")