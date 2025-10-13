import requests
import pytest
import json

def test_update_post():
    """Tes untuk memperbarui/mengubah data postingan yang sudah ada."""

    # 1. Siapkan payload dengan data baru.
    # Kita akan mengubah total data dari postingan nomor 1.
    payload = {
        "id": 99, # Sebaiknya sertakan ID yang sama
        "title": 'Sandra update data',
        "body": 'Sandra was here untuk update',
        "userId": 1
    }

    # 2. Tentukan URL, HARUS menyertakan ID dari data yang mau diubah
    url = "https://jsonplaceholder.typicode.com/posts/99"

    # 3. Kirim permintaan PUT
    response = requests.put(url, json=payload)

    # 4. Verifikasi (Assertion)
    # A. Status code untuk PUT yang berhasil biasanya 200 (OK)
    assert response.status_code == 200
    print(f"\nStatus Code: {response.status_code} (OK)")

    # B. Ubah respons menjadi JSON
    response_data = response.json()
    print("Respons Data:")
    print(json.dumps(response_data, indent=4))

    # C. Verifikasi bahwa judul di respons sudah sesuai dengan yang kita kirim
    assert response_data["title"] == payload["title"]
    print(f"Verifikasi Judul Berhasil: '{response_data['title']}'")

    # D. Pastikan kita mengubah ID yang benar
    assert response_data["id"] == 99