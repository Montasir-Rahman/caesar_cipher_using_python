
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

def main():
    text = input("Enter your message: ")
    key = int(input("Enter any integer number: "))
    
    encrypted_text = caesar(text, key)
    
    print("Original Text:", text)
    print("Encrypted Text: ", encrypted_text)
    
if __name__ == '__main__':
    main()
    