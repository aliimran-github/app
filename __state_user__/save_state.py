from . import json

def save_state(state_id, state_value, valid_modes, STATE_FILE='user_states.json'):
    """
    Menyimpan state pengguna ke dalam file JSON.

    Args:
        state_id (str): ID pengguna yang state-nya akan disimpan.
        state_value (str): Nilai state yang akan disimpan.
        valid_modes (list): Daftar mode yang diperbolehkan.
        STATE_FILE (str): Nama file JSON tempat menyimpan state pengguna (default: 'user_states.json').

    Returns:
        int: 1 jika penyimpanan berhasil, 0 jika nilai state tidak valid.
    """
    
    if state_value not in valid_modes:
        return 0  # Mengembalikan 0 jika nilai state tidak valid

    try:
        # Mencoba membaca file JSON yang berisi data state
        with open(STATE_FILE, 'r') as file:
            data = json.load(file) # Memuat data JSON ke dalam dictionary
    except (FileNotFoundError, json.JSONDecodeError):
        # Jika file tidak ditemukan atau rusak, inisialisasi data sebagai dictionary kosong
        data = {}

    # Memperbarui atau menambahkan state pengguna ke dalam dictionary
    data[state_id] = state_value

    # Menulis kembali data ke dalam file JSON
    with open(STATE_FILE, 'w') as file:
        json.dump(data, file)

    return 1 #  Mengembalikan 1 jika penyimpanan berhasil