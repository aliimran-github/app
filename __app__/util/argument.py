import argparse

def getArgument():
    """
    Mendapatkan argumen dari baris perintah.

    Returns:
        Namespace: Objek dengan atribut sesuai argumen yang diterima.
    """
    
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=f'desc', # Deskripsi singkat tentang program
        epilog='epilog' # Teks yang ditampilkan di akhir help message
    )


    # Menambahkan argumen untuk verbosity (tingkat detail output)
    parser.add_argument("-v", "--verbose", action="count", default=0, help="verbose 1, 2") # Bisa dipanggil dengan `-v`, `-vv`, dll.

    # Menambahkan flag untuk menampilkan sesuatu (boolean flag)
    parser.add_argument("-l", "--show", action="store_true", help="show") # True jika `-l` dipanggil, False jika tidak.

    return parser.parse_args()