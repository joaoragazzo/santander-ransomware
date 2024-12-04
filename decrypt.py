from Crypto.Cipher import AES
import os
import base64


def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    
    nonce = data[:8] 
    encrypted_data = data[8:]
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    decrypted_data = cipher.decrypt(encrypted_data)
    
    original_file = file_path.replace('.ransomwaretroll', '')
    with open(original_file, 'wb') as f:
        f.write(decrypted_data)
    
    os.remove(file_path)  
    print(f"Arquivo '{file_path}' decriptografado como '{original_file}'!")

def main():
    key_file = input("Insira o caminho do arquivo contendo a chave: ")
    if not os.path.exists(key_file):
        print(f"Arquivo de chave '{key_file}' não encontrado!")
        return
    
    with open(key_file, 'r') as f:
        key = base64.b64decode(f.read())
    
    target_file = input("Insira o caminho do arquivo a ser decriptografado: ")
    if os.path.exists(target_file) and target_file.endswith('.ransomwaretroll'):
        decrypt_file(target_file, key)
    else:
        print(f"Arquivo '{target_file}' não encontrado ou não é um arquivo válido para decriptografia!")

if __name__ == '__main__':
    main()
