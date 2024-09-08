import base64

def hex2ascii():
    print("")
    hexvalue = str(input('Enter Value: ')) 
    #hexvalue is used to store the hexadecimal value inputted by the user.
    # hexvalue: '48656c6c6f'
    
    hexbyte = bytes.fromhex(hexvalue)
    #Next we convert to byte using bytes.fromhex
    #hexbyte: b'Hello'
    
    ascii_value = hexbyte.decode('ascii')
    #Now we convert the bytes to ascii

    print(f"Ascii: {ascii_value}")
     # Output: 'Hello'
    
    
def ascii2hex():
    print("")
    asciistr = str(input('Enter Value: '))
    #asciivalue is used to store the ascii value inputted by the user.
    # asciivalue: 'Hello'
    
    asciibyte = asciistr.encode('ascii')
    #We have converted the string value to bytes
    #byte: b'Hello'
    
    hexvalue = asciibyte.hex()
    #Now we convert the bytes to hexadecimal
    # hexvalue: '48656c6c6f'

    print(f"Hexadecimal: {hexvalue}")
    # Output: '48656c6c6f'

def hex2bin():
    print("")
    hexvalue = str(input('Enter Value: '))
    #hexvalue is used to store the hexadecimal value inputted by the user.
    # hexvalue: '48656c6c6f'
    
    hexint = int(hexvalue, 16)
    #hexvalue has been converted to an integer
    #hexint: 310939249775
    
    hexbin = bin(hexint)
    #hexint has been converted to binary format
    #hexbin: 0b100100001100101011011000110110001101111
    
    print(hexbin[2:])
    #This prints out the binary without the 0b prefix
    #output: 100100001100101011011000110110001101111

    
def bin2hex():
    print("")
    binstr = str(input('Enter Value: '))
    #binstr is used to store the binary value inputted by the user.
    # binstr: 100100001100101011011000110110001101111
    
    binint = int(binstr, 2)
    #binstr has been converted to an integer
    #binint: 310939249775
    
    hexvalue = hex(binint)
    #binint has been converted to binary format
    #hexvalue: 0x48656c6c6f
    
    print(f"Hexadecimal: {hexvalue}")
    #This prints out the hexadecimal value without the 0x prefix
    #output: 48656c6c6f
    
    
def hex2dec():
    print("")
    hexvalue = str(input('Enter Value: '))
    #hexvalue is used to store the hexadecimal value inputted by the user.
    # hexvalue: '48656c6c6f'
    
    hexint = int(hexvalue, 16)
    #output: 310939249775
    
    print(f"Decimal: {hexint}")


def dec2hex():
    print("")
    decvalue = int(input('Enter Value: '))
    #decvalue is used to store the decimal value inputted by the user.
    # decvalue: 310939249775
    
    hexvalue = hex(decvalue)
    # hexvalue: '0x48656c6c6f'

    print(f"Hexadecimal: {hexvalue[2:]}")
    #This prints out the hexadecimal value without the 0x prefix

def encbase64():
    print("")
    text = str(input('Enter Value: '))
    
    textbyte = text.encode('utf-8')
    #convert string to bytes
    
    base64byte = base64.b64encode(textbyte)
    #convert bytes to base64
    
    base64string = base64byte.decode('utf-8')
    
    print(f"Base64 Encoded String: {base64string}")
    

def decbase64():
    print("")
    base64string = str(input('Enter Value: '))
    # text holds encoded base64 string
    
    textbyte = base64string.encode('utf-8')
    #convert base64 encoded string to bytes
    
    base64byte = base64.b64decode(textbyte)
    #decode babse64 bytes
    
    text = base64byte.decode('utf-8')
    
    print(f"Base64 Encoded String: {text}")


def print_menu ():
    print("")
    print("What would you like to do:")
    print("")
    
    print("[1] Convert Hexadecimal to Ascii")
    print("[2] Convert Ascii to Hexadecimal")
    print("[3] Convert Hexadecimal to Binary")
    print("[4] Convert Binary to Hexadecimal")
    print("[5] Convert Hexadecimal to Decimal")
    print("[6] Convert Decimal to Hexadecimal")
    print("[7] Encode Base64")
    print("[8] Decode Base64")
    print("[0] Enter 0 to exit")
    print("")
    handle_input()

def handle_input():
    user_choice = int(input("Select a Conversion Operation: "))
    if user_choice == 1:
        hex2ascii()
                
    elif user_choice == 2:
        ascii2hex()
        
    elif user_choice == 3:
        hex2bin()
        
    elif user_choice == 4:
        bin2hex()
        
    elif user_choice == 5:
        hex2dec()
        
    elif user_choice == 6:
        dec2hex()
        
    elif user_choice == 7:
        encbase64()
        
    elif user_choice == 8:
        decbase64()
        
    elif user_choice == 0:
        print('Thank you for using Inside Out!')
        quit()
                
    else:
        print('You Entered an Invalid Input\n')
    
    print_menu()
    
def main ():
    print("")
    print("Welcome to Inside Out 1.0")
    print_menu()




if __name__ == "__main__":
    main()
    