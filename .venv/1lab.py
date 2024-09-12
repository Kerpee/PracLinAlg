import random
import numpy as np
alph = 'йцукенгшщзхъфывапролджэячсмитьбю,. '
message = 'я тебя люблю'
key_matr_2x2 = [[2, 7], [14, 5]]
key_matr_3x3 = [[2, 4, 6], [3, 5, 8], [1, 6, 9]]
key_matr_4x4 = [[4, 7, 14, 2], [5, 6, 11, 8], [11, 19, 17, 12], [13, 14, 15, 16]]
def char_to_index(char, alph): # Перевод алфавита в численные значения
    return alph.index(char)
def index_to_char(index, alph): # Перевод численного значения в символ алфавита
    return alph[index % len(alph)]
def mult_matrix(msg, key, alph_len): # Функция для перемножения матриц
    res = []
    for row in key:
        part_of_res = sum(x * y for x, y in zip(row, msg)) % alph_len
        res.append(part_of_res)
    return res
def hill_cipher_encrypt(message, key, alphabet): # Функция для шифрования Хилла
    alphabet_len = len(alphabet)
    block_size = len(key)
    encrypted_message = ""

    for i in range(0, len(message), block_size): # Разбиение сообщения на блоки, которые будут шифроватсья
        block = message[i:i + block_size] # Создание блока сообщения
        if len(block) < block_size:
            block += " " * (block_size - len(block))
        block_indexes = [char_to_index(char, alphabet) for char in block] # Каждый символ блока индексируется
        encrypted_indexes = mult_matrix(block_indexes, key, alphabet_len) # Перемножаем ключ на блок сообщения для зашифровки
        encrypted_block = ''.join(index_to_char(index, alphabet) for index in encrypted_indexes) # Преобразуем индексы снова в алфавит
        encrypted_message += encrypted_block
    return encrypted_message
encrypted_2x2 = hill_cipher_encrypt(message, key_matr_2x2, alph)
encrypted_3x3 = hill_cipher_encrypt(message, key_matr_3x3, alph)
encrypted_4x4 = hill_cipher_encrypt(message, key_matr_4x4, alph)

print("Зашифрованные сообщения:")
print(f"2x2: {encrypted_2x2}")
print(f"3x3: {encrypted_3x3}")
print(f"4x4: {encrypted_4x4}")

def random_change(message,alph):
    message=list(message)
    for i in range(3):
        index_change=random.randint(0,len(message)-1)
        random_char=random.choice(alph)
        message[index_change]=random_char
    return ''.join(message)

def inv_det(det,mod): # Вспомогательная функция, которая находит обратный элемент определителя
    det=det%mod
    for x in range(1,mod):
        if (det*x)%mod==1:
            return x
    raise ValueError('это гг')
def inv_matrix(matr,mod): # Функция для нахождения обратной матрицы
    deter=round(np.linalg.det(matr))
    det_inv=inv_det(deter,mod)
    adju=np.round(deter*np.linalg.inv(matr)).astype(int)
    return (det_inv*adju)%mod
def hill_decrypt(encrypt_msg,key,alph): # Расшифорвка сообщения по аналогии с зашифровкой
    alph_len=len(alph)
    block_size=len(key)
    decr_msg=''
    inv_key=inv_matrix(key,alph_len)
    for i in range(0,len(encrypt_msg),block_size):
        block=encrypt_msg[i:i+block_size]
        block_indexes=[char_to_index(char,alph) for char in block]
        decr_indexes=mult_matrix(block_indexes,inv_key,alph_len)
        decr_block=''.join(index_to_char(index,alph) for index in decr_indexes)
        decr_msg+=decr_block
    return decr_msg
decrypted_random_2x2 = hill_decrypt(random_change(encrypted_2x2,alph), key_matr_2x2, alph)
decrypted_random_3x3 = hill_decrypt(random_change(encrypted_3x3,alph), key_matr_3x3, alph)
decrypted_random_4x4 = hill_decrypt(random_change(encrypted_4x4,alph), key_matr_4x4, alph)

print("\nРасшифрованные сообщения с вторжением:")
print(f"2x2: {decrypted_random_2x2}")
print(f"3x3: {decrypted_random_3x3}")
print(f"4x4: {decrypted_random_4x4}")

decrypted_2x2 = hill_decrypt(encrypted_2x2, key_matr_2x2, alph)
decrypted_3x3 = hill_decrypt(encrypted_3x3, key_matr_3x3, alph)
decrypted_4x4 = hill_decrypt(encrypted_4x4, key_matr_4x4, alph)

print("\nРасшифрованные сообщения без вторжения:")
print(f"2x2: {decrypted_2x2}")
print(f"3x3: {decrypted_3x3}")
print(f"4x4: {decrypted_4x4}")