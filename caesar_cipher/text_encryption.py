
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    
    for char in message.lower():
        if char == ' ':
            encrypted_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_message += alphabet[new_index]
    return encrypted_message

def uncaesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ''
    
    for char in message.lower():
        if char == ' ':
            decrypted_message += char
        else:
            index = alphabet.find(char)
            new_index = (index - offset) % len(alphabet)
            decrypted_message += alphabet[new_index]
    return decrypted_message

def write_encrypted_to_file(text, filename = "encrypted_message.txt"):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Encrypted text written to {filename}")

def encryption():
    text = input("Enter your message: ")
    key = int(input("Enter any integer number: "))
    
    encrypted_text = caesar(text, key)
    write_encrypted_to_file(encrypted_text)
    
    print("Original Text:", text)
    print("Encrypted Text: ", encrypted_text)
    
def read_encrypted_from_file(filename = "encrypted_message.txt"):
    try:
        with open(filename, 'r') as file:
            encrypted_text = file.read()
        return encrypted_text
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    
def write_decrypted_to_file(text, filename = "decrypted_message.txt"):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Decrypted text written to {filename}")
    
def decryption():
    text = read_encrypted_from_file()
    key = int(input("Enter your encryption key: "))
    
    decrypted_text = uncaesar(text, key)
    write_decrypted_to_file(decrypted_text)
    
    print("Encrypted Text:", text)
    print("Decrypted Text: ", decrypted_text)
    
def main():
    print("!!!_Welcome to Text Encryption Service_!!!")
    print("Enter-1: Encryption Service")
    print("Enter-2: Decryption Service")
    
    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        encryption()
    elif user_choice == 2:
        decryption()
    else:
        print("Invalid Choice! Try Again")
    
if __name__ == '__main__':
    main()
    