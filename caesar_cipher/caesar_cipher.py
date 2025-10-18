# Function for Caesar Cipher
def caesar(message, offset, direction = 1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ''
    
    for char in message.lower():
        
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
          
        # Define the new index  
        else:
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
            
    return final_message

# Function to write encrypted message in a text file  
def write_encrypted_to_file(text, filename = "encrypted.txt"):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Encrypted text written to {filename}")

# Function to encrypt message
def encrypt():
    text = input("Enter text to encrypt: ")
    key = int(input("Enter any integer number: "))
    
    final_text = caesar(text, key)
    write_encrypted_to_file(final_text)
    
    print(f"Original Message: {text}")
    print(f"Encrypted Message: {final_text}")

# Function to read encrypted message from the text file    
def read_encrypted_from_file(filename = "encrypted.txt"):
    try:
        with open(filename, 'r') as file:
            encrypted_text = file.read()
        return encrypted_text
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
 
# Function to write decrypted message in a text file   
def write_decrypted_to_file(text, filename = "decrypted.txt"):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Decrypted text written to {filename}")

# Function to decrypt message
def decrypt():
    text = read_encrypted_from_file()
    key = int(input("Enter your integer key: "))
    
    final_text = caesar(text, key, -1)
    write_decrypted_to_file(final_text)
    
    print(f"Encrypted Message: {text}")
    print(f"Decrypted Message: {final_text}")

# Main function
def main():
    print("Welcome to Caesar Cipher")
    print("Enter-1: Encryption Service")
    print("Enter-2: Decryption Service")
    
    user_choice = int(input("Enter your choice: \n"))
    
    if user_choice == 1:
        encrypt()
    elif user_choice == 2:
        decrypt()

if __name__ == '__main__':
    main()