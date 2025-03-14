import pandas as pd

class DataLoader:
    """
    Kelas untuk memuat data dari file Excel dengan opsi pemrosesan tertentu.
    
    Attributes:
        file (str): Nama file Excel yang akan dibaca.
        row (list): Daftar kolom yang akan diambil dari file.
        sheet (str): Nama sheet dalam file Excel (default: 'Sheet1').
    """
    
    def __init__(self, file_name, row_list, sheet = 'Sheet1'):
        """
        Inisialisasi objek DataLoader.

        Args:
            file_name (str): Nama file Excel.
            row_list (list): Daftar kolom yang akan dimuat.
            sheet (str): Nama sheet di dalam file (default: 'Sheet1').
        """
        self.file = file_name
        self.row = row_list
        self.sheet = sheet
    
    def load_data(self, sort=False): 
        """
        Memuat data dari file Excel, mengisi nilai kosong, dan mengurutkan jika diperlukan.

        Args:
            sort (bool): Jika True, data akan diurutkan berdasarkan kolom ke-3 dalam daftar `row`.

        Returns:
            pd.DataFrame: Data yang telah dimuat dan diproses.
        """
        try:
            # Membaca data dari file Excel berdasarkan kolom yang diberikan
            df = pd.read_excel(self.file, sheet_name=self.sheet, usecols=self.row)

            # Mengisi nilai kosong pada setiap kolom dengan nilai sebelumnya (forward fill)
            for row in self.row:
                df[row] = df[row].ffill()
            
        except ValueError as e:
            # Jika terjadi error (misalnya kolom tidak ditemukan), cetak pesan error dan keluar
            print(str(e))
            exit()

        if sort == True:
            df = df.sort_values(self.row[2], ascending=True).reset_index(drop=True)

        return df # Mengembalikan DataFrame yang telah diproses