import requests
import pytest
import json

def test_create_new_post():
    """Tes untuk membuat postingan baru di JSONPlaceholder."""

    # 1. Siapkan payload. Sesuai 'kontrak' JSONPlaceholder, 
    #    mereka mengharapkan title, body, dan userId.
    payload = {
        "title": 'Latihan Sandra kedua',
        "body": 'Ini adalah konten postingan kedua.',
        "userId": 1
    }

    # 2. Ganti URL ke endpoint JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"

    # 3. Kirim permintaan POST
    response = requests.post(url, json=payload)

    # 4. Verifikasi (Assertion)
    # A. Pastikan status code adalah 201 (Created)
    assert response.status_code == 201
    print(f"\nStatus Code: {response.status_code} (Created)")

    # B. Ubah respons menjadi format JSON
    response_data = response.json()
    print("Respons Data:")
    print(json.dumps(response_data, indent=4))

    # C. Verifikasi bahwa data yang kita kirim sebagian ada di respons
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]
    assert response_data["userId"] == payload["userId"]
    
    # D. Server akan memberikan 'id' baru untuk postingan kita
    assert "id" in response_data
    print(f"Postingan baru berhasil dibuat dengan ID: {response_data['id']}")