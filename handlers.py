import telebot
import __app__ as __app__
import __state_user__
from __data__ import DataLoader
from error_messages import ERROR_MESSAGES

# Mengambil argumen dari aplikasi dan menentukan apakah mode verbose aktif
args = __app__.getArgument()  
v = args.verbose

valid_modes = ['kmp', 'boyer_more', 'brute_force'] # Daftar mode yang valid untuk suatu operasi
user_states = __state_user__.load_state() # Memuat status pengguna dari sistem penyimpanan state

file = 'data.xlsx' # Nama file yang akan diproses (file Excel)
pattern = ['pattern', 'solusi', 'prioritas', 'teknik', 'masalah', 'tanda serangan'] # Daftar kolom yang akan digunakan dalam pemrosesan data
df_data = DataLoader(file, pattern).load_data(sort=True) # Memuat dataFrame dari file excel

# Jika argumen --show diberikan, maka tampilkan data dan keluar dari program
if args.show:  
    __app__.print_text(df_data, v, 0)
    print(df_data.to_string(index=False))  # Mencetak file excel
    exit()  # Menghentikan eksekusi program

def register_handlers(bot):
    @bot.message_handler(commands=['start', 'help'])
    def start_and_help(message):
        try:
            __app__.print_text(f'{message.from_user.id} (command): {message.text}', v, 0) # Mencetak log command yang dikirim oleh pengguna
            
            # Pesan panduan penggunaan bot
            response_message = (
                "🔰 *Panduan Penggunaan Bot Pentest & Solusi Keamanan* 🔰\n\n"
                "Gunakan perintah berikut untuk memulai:\n"
                "📌 */search* – 🔍 Cari pola terkait serangan atau teknik eksploitasi.\n"
                "📌 */describe* – 📖 Lihat informasi tentang teknik serangan atau mitigasi.\n"
                "📌 */list* – 📜 Lihat daftar pola yang tersedia dalam database.\n"
                "📌 */use* – ⚙️ Pilih metode pencarian (`kmp`, `boyer_more`, `brute_force`).\n"
                "📌 */get* – 🛠 Lihat metode pencarian yang sedang digunakan.\n"
                "📌 */help* – 📚 Lihat daftar perintah dan panduan penggunaan.\n\n"
                "Coba ketik */list* untuk melihat daftar pola yang tersedia!"
            )
            
            # Jika pengguna menggunakan perintah /start, tambahkan pesan selamat datang
            if message.text.startswith('/start'):
                response_message = (
                    "🚀 *Selamat Datang di Bot Pentest & Solusi Keamanan!* 🔍\n\n"
                    "Bot ini dirancang untuk membantu dalam proses pengujian keamanan dengan mendeteksi pola eksploitasi dan memberikan informasi solusi.\n\n"
                    + response_message
                )
            
            # Membuat markup untuk tombol keyboard
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

            # Membuat tombol yang akan ditampilkan pada keyboard
            btn1 = telebot.types.KeyboardButton("/help")
            btn2 = telebot.types.KeyboardButton("/list")
            btn3 = telebot.types.KeyboardButton("/list all")
            btn4 = telebot.types.KeyboardButton("/get")
            btn5 = telebot.types.KeyboardButton("/use boyer_more")
            btn6 = telebot.types.KeyboardButton("/use kmp")
            btn7 = telebot.types.KeyboardButton("/use brute_force")       
            btn8 = telebot.types.KeyboardButton("/search deauthentication")
            btn9 = telebot.types.KeyboardButton("/describe Deauthentication Attack")

            # Menambahkan tombol ke dalam markup dalam bentuk beberapa baris
            markup.row(btn1, btn2, btn3)
            markup.row(btn4, btn5)
            markup.row(btn6, btn7)
            markup.row(btn8)
            markup.row(btn9)
            
            # Mengirim pesan balasan ke pengguna dengan markup keyboard
            bot.reply_to(message, response_message, reply_markup=markup, parse_mode="markdown")
        except Exception as e:
            # Tangani error dan kirim pesan error kepada user
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')

    @bot.message_handler(commands=['list'])
    def list_patterns(message):
        __app__.print_text(f'{message.from_user.id} (command): {message.text}', v, 0) # Mencetak log command yang dikirim oleh pengguna
        command = message.text[6:].strip() # Mengambil parameter tambahan setelah "/list" (misalnya "/list all" menjadi all (karena sudah di ambil 6 huruf diari depan))
        
        result = __app__.list(df_data, 'pattern') # Mengambil daftar pola (patterns) dari data
        text = f"""\n*[+] List:* \n- `{'`\n- `'.join([f"{item}" for item in result]) + '`\n'}""" # Format daftar pola menjadi teks dengan markdown

        # Membuat markup inline keyboard
        markup = telebot.types.InlineKeyboardMarkup() 

        buttons = [] # List untuk menyimpan tombol yang akan dibuat
        MAX_BUTTONS = len(result) if command == "all" else 7 # Menentukan jumlah maksimal tombol yang akan ditampilkan

        # Membuat tombol untuk setiap pola yang tersedia
        for i, pattern in enumerate(result):
            if pattern.strip(): # Pastikan tidak ada pola kosong
                # Membuat callback_data agar bisa digunakan di handler callback
                callback_data = f"search_{pattern.lower().replace(' ', '_')}"
                button = telebot.types.InlineKeyboardButton(f"🔍 Cari {pattern}", callback_data=callback_data)
                buttons.append(button)

            # Berhenti jika jumlah tombol sudah mencapai batas maksimal
            if len(buttons) >= MAX_BUTTONS:
                break

        # Menambahkan tombol ke dalam markup dengan maksimal 2 tombol per baris
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        markup.add(*buttons)

        if MAX_BUTTONS != len(result):
            text += "\ngunakan `/list all` untuk menampilkan semua pattern yang tersedia"

        # Mengirim pesan balasan dengan daftar pola dan inline keyboard
        bot.reply_to(message, text, parse_mode="Markdown", reply_markup=markup)

    @bot.message_handler(commands=['search'])
    def search(message, query=None):
        try:
            # Jika fungsi dipanggil secara langsung dengan parameter query, gunakan query
            # Jika tidak, ambil input dari pesan yang dikirim oleh pengguna setelah "/search"
            command = query if query else message.text[8:]
            source = "query" if query else "command"

            # Cetak log sesuai sumber perintah (query atau command dari user)
            if source != "query":
                __app__.print_text(f'{message.from_user.id} ({source}): {message.text}', v, 0)
            else:
                __app__.print_text(f'{message.from_user.id} ({source}): {command}', v, 0)

            # Jika tidak ada input setelah /search, kirim pesan error dan hentikan fungsi
            if (len(command) < 1):
                bot.reply_to(message, ERROR_MESSAGES['search']['empty'], parse_mode="markdown")
                return

            # Ambil mode pencarian dari user state, default ke "boyer_more"
            mode = user_states.get(str(message.from_user.id), "boyer_more")

            # Cari pola berdasarkan command yang diberikan oleh user
            result, tekniks = __app__.search_pattern(command, df_data, mode, pattern)
            
            # Buat inline keyboard untuk menampilkan teknik yang ditemukan
            markup = telebot.types.InlineKeyboardMarkup()
            buttons = []
            for teknik in tekniks:
                if teknik.strip(): # Pastikan teknik tidak kosong
                    # Callback untuk tombol yang mengarah ke deskripsi teknik
                    callback_data = f"describe_{teknik.lower().replace(' ', '_')}"
                    button = telebot.types.InlineKeyboardButton(f"📝 Describe {teknik}", callback_data=callback_data)
                    buttons.append(button)
            
            # Atur layout inline keyboard dengan maksimal 2 tombol per baris
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            markup.add(*buttons)
            
            if result == 0:
                bot.reply_to(message, ERROR_MESSAGES["search"]['not_found'].format(name=command), parse_mode="markdown")
                return
            
            # Kirim hasil pencarian kepada pengguna dengan daftar teknik yang ditemukan
            bot.reply_to(message, str(result), parse_mode="markdown", reply_markup=markup)
        except Exception as e:
            # Tangani error dan kirim pesan error kepada user
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    @bot.message_handler(commands=['describe'])
    def describe(message, query=None):
        try:
            # Jika fungsi dipanggil dengan parameter query, gunakan query
            # Jika tidak, ambil input dari pesan pengguna setelah "/describe"
            command = query if query else message.text[10:].strip()
            source = "query" if query else "command" 

            # Cetak log sesuai sumber perintah (query atau command dari user)
            if source != "query":
                __app__.print_text(f'{message.from_user.id} ({source}): {message.text}', v, 0)
            else:
                __app__.print_text(f'{message.from_user.id} ({source}): {command}', v, 0)
            
            # Jika tidak ada input setelah /describe, kirim pesan error dan hentikan fungsi
            if (len(command) < 1):
                bot.reply_to(message, ERROR_MESSAGES['describe']['empty'], parse_mode="markdown")
                return

            match = []; # List untuk menyimpan hasil pencocokan
            items = command.split(', ') # Pisahkan input berdasarkan koma jika ada lebih dari satu teknik yang diminta

            # Loop melalui setiap item yang diminta user
            for i, item in enumerate(items, start=1):
                # Ambil informasi dari database terkait teknik yang diminta
                teknik, masalah, tanda_serangan = __app__.describe(item, df_data)

                # Jika tidak ditemukan data terkait, lanjut ke item berikutnya
                if not teknik and not masalah and not tanda_serangan:
                    continue

                # Format header, body, footer
                header = f"*{i}. {', '.join(teknik)}*\n"
                body = f"""*[+] Masalah* \t: \n{'\n'.join([f"- {item}" for item in masalah]) + '\n'}\n"""
                footer = f"""*[+] tanda serangan* \t: \n{'\n'.join([f"- {item}" for item in tanda_serangan])}"""

                # Gabungkan bagian-bagian tersebut menjadi satu respons
                match.append(header + body + footer)

            if len(match) >= 1:
                # Jika ada data yang ditemukan, kirim ke pengguna
                bot.reply_to(message, '\n\n'.join(match), parse_mode="markdown")
            else:
                # Jika tidak ada yang ditemukan, kirim pesan error
                bot.reply_to(message, ERROR_MESSAGES["describe"]['not_found'].format(name=command), parse_mode="markdown")
        except Exception as e:
            # Tangani error dan kirim pesan error kepada user
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    @bot.message_handler(commands=['use'])
    def use(message):
        try:
            __app__.print_text(f'{message.from_user.id} (command): {message.text}', v, 0) # Mencetak log bahwa pengguna telah menggunakan perintah /use
            args = message.text.split() # Memisahkan teks perintah menjadi list berdasarkan spasi

            # Jika pengguna hanya mengetik "/use" tanpa memilih mode, berikan pesan error
            if len(args) < 2:
                bot.reply_to(message, ERROR_MESSAGES["use"]["empty"], parse_mode="markdown")
                return

            # Mengambil mode yang dimasukkan oleh user
            mode_value = args[1].lower()
            
            # Memeriksa apakah mode yang dimasukkan valid
            if mode_value not in valid_modes:
                bot.reply_to(message, ERROR_MESSAGES["use"]["invalid"], parse_mode="markdown")
                return

            # Menyimpan mode yang dipilih ke dalam user state
            user_id = str(message.from_user.id)
            user_states[user_id] = mode_value

            # Menyimpan status mode pengguna ke dalam sistem
            save_status = __state_user__.save_state(user_id, mode_value, valid_modes)

            if save_status == 0:
                # Jika penyimpanan gagal, kirim pesan error
                bot.reply_to(message, ERROR_MESSAGES["use"]["invalid"], parse_mode="markdown")
            else:
                # Jika berhasil, kirim pesan sukses dengan mode yang dipilih
                bot.reply_to(message, ERROR_MESSAGES["use"]["success"].format(mode=mode_value), parse_mode="markdown")
        except Exception as e:
            # Tangani error dan kirim pesan error kepada user
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    '''/get'''
    @bot.message_handler(commands=['get'])
    def get(message):
        try:
            __app__.print_text(f'{message.from_user.id} (command): {message.text}', v, 0) # Mencetak log bahwa pengguna telah menggunakan perintah /get

            user_id = str(message.from_user.id) # Mengambil ID pengguna sebagai string
            state = user_states.get(user_id) # Mendapatkan mode pencarian pengguna dari user_states

            if state is None:
                # Jika tidak ada mode yang tersimpan, kirim pesan bahwa data tidak ditemukan
                bot.reply_to(message, ERROR_MESSAGES["get"]["not_found"], parse_mode="markdown")
            else:
                # Jika ada mode yang tersimpan, kirim pesan dengan mode yang sedang digunakan
                bot.reply_to(message, ERROR_MESSAGES["get"]["success"].format(mode=state), parse_mode="markdown")

        except Exception as e:
            # Jika terjadi error, cetak ke log dan beri tahu pengguna
            bot.reply_to(message, f'❌ *Terjadi kesalahan:* `{str(e)}`', parse_mode="markdown")
    
    '''callback handlers'''
    @bot.callback_query_handler(func=lambda call: call.data.startswith("search_"))
    def handle_search(call):
        # Mengambil query dari data callback dengan mengganti "search_" menjadi string pencarian yang sesuai
        query = call.data.replace("search_", "").replace("_", " ")

        # Memanggil fungsi search dengan parameter message dari callback dan query yang sudah diformat
        search(call.message, query)
    
    @bot.callback_query_handler(func=lambda call: call.data.startswith("describe_"))
    def handle_describe(call):
         # Mengambil query dari data callback dengan mengganti "describe_" menjadi string yang sesuai
        query = call.data.replace("describe_", "").replace("_", " ")
        
        # Memanggil fungsi describe dengan parameter message dari callback dan query yang sudah diformat
        describe(call.message, query)