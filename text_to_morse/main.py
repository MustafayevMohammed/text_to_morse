morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  '0': '-----'
}

reverse_morse = {v: k for k, v in morse_code.items()}


def encode(text):
    encoded_text = ""
    text = text.upper()

    for char in text:
        if char == " ":
            encoded_text += " "
        try:
            encoded_text += " "
            encoded_text += morse_code[char]
        except KeyError:
            continue
    
    return encoded_text


def decode(code):
    words = code.split("   ")

    final_txt = ""
    for word in words:
        word_txt = ""

        for letter in word.split(" "):
            try:
                decoded_letter = reverse_morse[letter]
            except KeyError:
                print("Make sure that you have spaced your letters correctly, and sent the standart chars")
            else:
                word_txt += decoded_letter
        final_txt += f"{word_txt} "
    
    return final_txt


def main():
    is_continue = True
    while is_continue:
        enc_or_dec = input("Do you want to encode or decode?(q to quit) ")
        
        if enc_or_dec.lower() == "encode":
            user_input = input("Enter the text you want to encode: ")
            encoded = encode(user_input)
            print(encoded)

        elif enc_or_dec.lower() == "decode":
            user_input = input("Enter the code you want to decode: ")
            decoded = decode(user_input)
            print(decoded)

        elif enc_or_dec == "q":
            is_continue = False



if __name__ == '__main__': 
    main()
