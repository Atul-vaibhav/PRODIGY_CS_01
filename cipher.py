def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():  
            
            offset = 65 if char.isupper() else 97
            
            shifted = (ord(char) - offset + shift) % 26 + offset if encrypt else (ord(char) - offset - shift) % 26 + offset
            result += chr(shifted)
        else:
            result += char 
    return result

def main():
    message = input("Enter the message to encrypt or decrypt: ")
    shift = int(input("Enter the shift value (a positive integer): "))
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
