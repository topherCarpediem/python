def long_substring(string):
    c_start = 0
    c_end = 0
    f_start = 0
    f_end = 0
    prev_char = chr(0)

    for char in string:
        if char < prev_char:
            c_start = c_end
        c_end += 1

        if c_end - c_start > f_end - f_start:
            f_start, f_end = c_start, c_end
        prev_char = char
    return string[f_start:f_end]

print(long_substring("abcbcd"))