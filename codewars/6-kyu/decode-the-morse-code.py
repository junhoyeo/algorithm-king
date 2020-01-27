def decodeMorse(morse_code):
    morse = morse_code.replace('   ', ' _ ').split(' ')
    MORSE_CODE['_'] = ' '
    return ''.join([MORSE_CODE[c] for c in morse if c != '']).strip()
