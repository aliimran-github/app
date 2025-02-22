from . import json

def load_state(STATE_FILE = 'user_states.json'):
    try:
        with open(STATE_FILE, 'r') as file: # Membuka file dalam mode baca
            return json.load(file) # Membaca dan mengonversi isi file JSON menjadi dictionary
    except (FileNotFoundError, json.JSONDecodeError):
        # Jika file tidak ditemukan atau terjadi kesalahan saat parsing JSON
        return {} # Mengembalikan dictionary kosong sebagai default