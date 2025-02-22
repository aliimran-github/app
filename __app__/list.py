def list(df, _row):
    """
    Mengembalikan daftar unik dari kolom tertentu dalam DataFrame.

    Args:
        df (pd.DataFrame): DataFrame yang berisi data.
        _row (str): Nama kolom yang akan diambil datanya.

    Returns:
        list: Daftar nilai unik dari kolom yang diberikan.
    """
    
    patterns = [] # Inisialisasi list kosong untuk menyimpan pola unik
    
    # Iterasi setiap baris dalam DataFrame
    for index, row in df.iterrows():
        pattern = row[_row] # Ambil nilai dari kolom yang ditentukan
        if pattern not in patterns: # Cek apakah nilai sudah ada dalam list
            patterns.append(pattern) # Tambahkan ke list jika belum ada
    
    return patterns # Kembalikan daftar pola unik