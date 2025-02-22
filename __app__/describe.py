from . import print_text, getArgument

def describe(item, df):
    """
    Mencari deskripsi dari suatu item berdasarkan data dalam DataFrame.

    Args:
        item (str): Nama item yang akan dicari deskripsinya.
        df (pd.DataFrame): DataFrame yang berisi informasi tentang teknik, masalah, dan tanda serangan.

    Returns:
        tuple: (teknik, masalah, tanda_serangan) dalam bentuk list.
    """
    
    
    args = getArgument(); v = args.verbose # Mengambil argument verbose untuk debugging/logging
    teknik, masalah, tanda_serangan = [], [], [] # Inisialisasi list kosong untuk menyimpan hasil pencarian

    print_text(f'[*] Deskripsi untuk item: {item}', v, 1) # Menampilkan log pencarian jika verbose aktif

    for index, row in df.iterrows(): # Iterasi setiap baris dalam DataFrame
        _teknik = row['teknik']
        _masalah = row['masalah']
        _tanda_serangan = row['tanda serangan']

        # Jika nama teknik dalam DataFrame cocok dengan item yang dicari (case insensitive)
        # dan pengecekan agar datanya tidak duplikat
        if _teknik.lower() in item.lower():            
            if _teknik not in teknik:
                teknik.append(_teknik)
            if _masalah not in masalah:
                masalah.append(_masalah)
            if _tanda_serangan not in tanda_serangan:
                tanda_serangan.append(_tanda_serangan)

    # Mengembalikan hasil dalam bentuk tuple (list teknik, list masalah, list tanda serangan)
    return teknik, masalah, tanda_serangan