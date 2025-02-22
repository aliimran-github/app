ERROR_MESSAGES = {
    "search": {
        "empty": "❌ *Kesalahan!* Anda harus memasukkan teks yang ingin dicari.\n\n"
                 "📌 *Contoh penggunaan:*\n"
                 "`/search deauthentication`\n"
                 "`/search unauthorized`",
        "not_found": "⚠️ *Hasil Tidak Ditemukan!*\n"
                     "Pola yang Anda cari tidak ada dalam database.\n"
                     "Coba periksa kembali penulisannya atau gunakan `/list` untuk melihat daftar pattern yang tersedia."
    },
    "describe": {
        "empty": "❌ *Kesalahan!* Anda harus memasukkan nama teknik yang ingin dijelaskan.\n\n"
                 "📌 *Contoh penggunaan:*\n"
                 "`/describe Deauthentication Attack`\n"
                 "`/describe Unauthorized Access`",
        "not_found": "⚠️ *Teknik `{name}` tidak ditemukan!*\n"
                     "Coba periksa kembali penulisannya atau gunakan `/list` untuk melihat daftar pattern yang tersedia."
    },
    "use": {
            "empty": "❌ *Kesalahan!* Anda harus memilih mode pencarian.\n\n"
                    "📌 *Contoh penggunaan:*\n"
                    "`/use kmp`\n"
                    "`/use boyer_more`\n"
                    "`/use brute_force`",
            "invalid": "⚠️ *Mode tidak valid!*\n"
                    "Silakan pilih salah satu dari berikut:\n"
                    "- `kmp`\n- `boyer_more`\n- `brute_force`",
            "success": "✅ *Mode berhasil disimpan!*\n"
                    "Anda sekarang menggunakan mode: `{mode}`."
    },
    "get": {
        "not_found": "⚠️ *State tidak ditemukan!*\n"
                     "Anda belum memilih mode pencarian.\n"
                     "Gunakan `/use <mode>` untuk menyimpan mode pencarian.",
        "success": "✅ *Mode pencarian Anda saat ini:* `{mode}`"
    }
}