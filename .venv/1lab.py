import random
alph = 'йцукенгшщзхъфывапролджэячсмитьбю,. '
message = 'я тебя люблю'
key_matr_2x2 = [[2, 5], [3, 8]]
key_matr_3x3 = [[2, 4, 6], [3, 5, 8], [1, 6, 9]]
key_matr_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
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
print(hill_cipher_encrypt(message, key_matr_2x2, alph))
print(hill_cipher_encrypt(message,key_matr_3x3,alph))
print(hill_cipher_encrypt(message,key_matr_4x4,alph))

def random_change(message,alph):
    message=list(message)
    for i in range(3):
        index_change=random.randint(0,len(message)-1)
        random_char=random.choice(alph)
        message[index_change]=random_char
    return ''.join(message)
print(random_change(message,alph))