# Enter any text to convert it into morse code
def encrypt(value):
    Morse_code_dict = {'A': '.-', 'B': '-...',

                       'C': '-.-.', 'D': '-..', 'E': '.',

                       'F': '..-.', 'G': '--.', 'H': '....',

                       'I': '..', 'J': '.---', 'K': '-.-',

                       'L': '.-..', 'M': '--', 'N': '-.',

                       'O': '---', 'P': '.--.', 'Q': '--.-',

                       'R': '.-.', 'S': '...', 'T': '-',

                       'U': '..-', 'V': '...-', 'W': '.--',

                       'X': '-..-', 'Y': '-.--', 'Z': '--..',

                       '1': '.----', '2': '..---', '3': '...--',

                       '4': '....-', '5': '.....', '6': '-....',

                       '7': '--...', '8': '---..', '9': '----.',

                       '0': '-----', ', ': '--..--', '.': '.-.-.-',

                       '?': '..--..', '/': '-..-.', '-': '-....-',

                       '(': '-.--.', ')': '-.--.-', ' ': ' '}

    print(f"Input: {value}\nOutput: ", end="")

    for i in value:
        print(Morse_code_dict[i], end=" ")


value = input("Enter any text to convert it into morse code: ").upper()

encrypt(value)
input("Press Enter to continue: ")
