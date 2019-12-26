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

                       '(': '-.--.', ')': '-.--.-', ' ': ''}

def encrypt(value):
    
    result = ''
    for i in value:
        result += Morse_code_dict[i] + ' '
        
    return result

def decrypt(value):
    
    result = ''
    
    for i in (value.split(' ')):
        
        if ' ' == i:
            continue
        result += list(Morse_code_dict.keys())[list(Morse_code_dict.values()).index(i)]
        
    return result
    
    

choice = ''
first_encrypt = False
while choice != '2':
    
    choice = input("\nEnter 0 to encrypt and 1 to decrypt and 2 to exit: ")
    
    if choice == '0':
        
        first_encrypt = True
        
        value = input("\nEnter the text you want to encrypt: ")
        result = encrypt(value.upper())
        prev_enrypt = result
        print("Input: {}\nEncrypted Text: {}".format(value,result))
        
        
    if choice == '1':
        
        if first_encrypt:
            choice2 = input("\nDo you want to use previously encrypted value? (yes/no): ")
            
            if choice2.upper().startswith('Y'):
                result = decrypt(prev_enrypt)
                print("Input: {}\nDecrypted Text: {}".format(prev_enrypt,result))
            
        if (not first_encrypt) or choice2.upper().startswith('N'):
            
            value = input("\nEnter the morse code you want to decrypt: ")
            result = decrypt(value)
            print("Input: {}\nDecrypted Text: {}".format(value,result))
             
