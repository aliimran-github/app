from . import matching_speed, getArgument, print_text

def search_pattern(text, df, mode='boyer_more', list=['pattern']):
    """
    Mencari pola dalam teks menggunakan mode pencocokan tertentu.

    Args:
        text (str): Teks yang akan dicari polanya.
        df (pd.DataFrame): DataFrame yang berisi pola yang akan dicocokkan.
        mode (str, optional): Metode pencocokan (default: 'boyer_more').
        list (list, optional): Daftar kolom dalam DataFrame untuk pencarian pola (default: ['pattern']).

    Returns:
        tuple: (hasil pencarian dalam format string, daftar teknik yang ditemukan)
    """
    
    args = getArgument(); v = args.verbose
    # patterns, match, tekniks = [], [], []
    patterns, match, tekniks = set(), set(), set()

    # Logging input
    print_text(f"[*] {" input ".center(50, '-')} [*]", v, 2)
    print_text(f'    text \t\t: {text}', v, 1)
    print_text(f'    mode \t\t: {mode}', v, 1)
    print_text(f"[-] {" pattern ".center(50, '-')}", v, 2)

    for index, row in df.iterrows():
        pattern = row[list[0]] # Ambil pola dari kolom pertama dalam 'list'
        position, elapsed_time = matching_speed(text.lower(), pattern.lower(), mode)
        if position != -1: # Jika pola ditemukan dalam teks
            value = row[list[1]] # Ambil nilai dari kolom kedua dalam 'list'
            teknik = row[list[3]] # Ambil teknik dari kolom keempat dalam 'list'
            if pattern not in patterns:
                patterns.add(pattern)
                match.add(value)
            elif value not in match:
                match.add(value)
                print_text(f'    {pattern[:19].ljust(19)} : {value[:50].ljust(50)} \t found at {elapsed_time}s', v, 2)
            if teknik not in tekniks:
                tekniks.add(teknik)

    # Logging hasil
    print_text(f"[-] {" result ".center(50, '-')}", v, 2)
    print_text(f"    pattern \t\t: {', '.join(patterns)}", v, 1)
    print_text(f"    teknik \t\t: {', '.join(tekniks)}", v, 1)
    print_text(f"    value \t\t: {', '.join(match)[:200].ljust(20)} \n", v, 1)
    
    # Jika ada hasil yang ditemukan
    if len(match) != 0:
        result = ', '.join(match)
        
        # print(result)
        header = f'*[+] teknik:* \n- `{"`\n- `".join(tekniks)} `\n'
        body = f"""\n*[+] solusi:* \n{'\n'.join([f"- {item}" for item in result.split(', ')]) + '\n'}"""

        # Logging output
        print_text(f"[*] {" output ".center(50, '-')}", v, 2)
        print_text(header + body, v, 2)
        return header + body, tekniks
    return 0, []