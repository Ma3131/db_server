

from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()

cipher = Fernet(cipher_key)
text = ('My super secret message').encode('utf-8')
encrypted_text = cipher.encrypt(text)
 
print(encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
decrypted_text = decrypted_text.decode('utf-8')
print(decrypted_text) # 'My super secret message'
decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text)
