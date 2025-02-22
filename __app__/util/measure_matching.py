import time
from .. import kmp, boyer_more, brute_force

def measure_matching_speed(text, pattern, mode='boyer_more'):
    """
    Mengukur waktu eksekusi algoritma pencocokan string.

    Args:
        text (str): Teks yang akan dicari pola di dalamnya.
        pattern (str): Pola yang dicari.
        mode (str, optional): Algoritma yang digunakan ('boyer_more', 'brute_force', 'kmp').
    
    Returns:
        tuple: (position, elapsed_time)
    """
    
    start_time = time.perf_counter()
    
    if mode == boyer_more:
        position = boyer_more(text, pattern)
    elif mode == brute_force:
        position = brute_force(text, pattern)
    else:
        position = kmp(text, pattern)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    formatted_elapsed_time = '{:.10f}'.format(elapsed_time)

    return position, formatted_elapsed_time