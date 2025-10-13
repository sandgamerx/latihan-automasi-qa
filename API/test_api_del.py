import requests
import pytest
import json

def test_delete_post():
    """Tes untuk mengirim permintaan hapus dan memverifikasi responsnya."""

    # Tentukan URL dari data yang mau dihapus
    url_delete = "https://jsonplaceholder.typicode.com/posts/1"

    # Kirim permintaan DELETE
    response_delete = requests.delete(url_delete)

    # Verifikasi (Assertion)
    # Status code untuk DELETE yang berhasil adalah 200 (OK)
    assert response_delete.status_code == 200
    print(f"\nStatus Code DELETE: {response_delete.status_code} (OK)")
    
    # Respons body dari DELETE biasanya kosong
    print(f"Respons Body DELETE: {response_delete.json()}")
    assert response_delete.json() == {}

    # --- LANGKAH B DIHAPUS KARENA TIDAK BERLAKU UNTUK JSONPLACEHOLDER ---