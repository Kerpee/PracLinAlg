import random
import numpy as np
alph = 'йцукенгшщзхъфывапролджэячсмитьбю.ё '
message = 'я тебя люблю'
key_matr_2x2 = [[2, 7], [14, 5]]
key_matr_3x3 = [[2, 4, 6], [3, 5, 8], [1, 6, 9]]
key_matr_4x4 = [[4, 7, 14, 2], [5, 6, 11, 8], [11, 19, 17, 12], [13, 14, 15, 16]]
def char_to_index(char, alph): # Перевод алфавита в численные значения
    return alph.index(char)
def index_to_char(index, alph): # Перевод численного значения в символ алфавита
    return alph[index%len(alph)]
def mult_matrix(msg, key, alph_len):
    res = np.dot(msg, key) % alph_len  # Перемножаем матрицы
    return res.astype(int)
def hill_cipher_encrypt(message, key, alphabet): # Функция для шифрования Хилла
    alphabet_len = len(alphabet)
    block_size = len(key)
    encrypted_message = ""

    for i in range(0, len(message), block_size): # Разбиение сообщения на блоки, которые будут шифроватсья
        block = message[i:i + block_size] # Создание блока сообщения
        if len(block) < block_size:
            block += " " * (block_size - len(block))
        block_indexes = [char_to_index(char, alphabet) for char in block]# Каждый символ блока индексируется
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

def inv_det(det, mod):
    det = det % mod
    for x in range(1, mod):
        if (det * x) % mod == 1:
            return x
    raise ValueError('Обратного элемента не существует')

def inv_matrix(matr, mod):
    deter = round(np.linalg.det(matr))
    det_inv = inv_det(deter, mod)
    adju = np.round(deter * np.linalg.inv(matr)).astype(int)
    return (det_inv * adju) % mod
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


# 2 ЗАДАНИЕ
def gen_key(size,mod):
    while True:
        matrix = np.random.randint(1, mod, size=(size, size))
        if np.gcd(int(round(np.linalg.det(matrix))), mod) == 1:
            return matrix

def from_msg_to_mat(message, block_size, alphabet):
    if len(message) % block_size != 0:
        message += ' ' * (block_size - len(message) % block_size)

    matrix = []
    for i in range(0, len(message), block_size):
        block = message[i:i + block_size]
        block_indexes = [char_to_index(char, alphabet) for char in block]
        matrix.append(block_indexes)

    return np.array(matrix).T


def find_key(orig_msg, encrypt_msg, alph, block_size):
    if len(orig_msg) % block_size != 0:
        raise ValueError("Длина сообщения должна быть кратна размеру блока.")
    orig_msg_matr = from_msg_to_mat(orig_msg, block_size, alph)
    encrypt_msg_matr = from_msg_to_mat(encrypt_msg, block_size, alph)
    total_blocks = len(orig_msg) // (block_size ** 2)
    for i in range(total_blocks):
        orig_block = orig_msg_matr[:, i * block_size:(i + 1) * block_size]
        enc_block = encrypt_msg_matr[:, i * block_size:(i + 1) * block_size]
        deter = round(np.linalg.det(orig_block))
        if deter % len(alph) == 0:
            continue
        try:
            det_inv = inv_det(deter, len(alph))
        except ValueError:
            continue
        inv_orig_block = inv_matrix(orig_block, len(alph))
        key_matr = np.dot(enc_block, inv_orig_block) % len(alph)
        return key_matr.astype(int).T
    raise ValueError('Не удалось найти подходящий блок для вычисления ключа.')
rand_key_2x2=gen_key(2,len(alph))
first_msg = 'я тебя люблю'
sec_msg = 'прекрати это'
enc_first_msg = hill_cipher_encrypt(first_msg, rand_key_2x2, alph)
enc_sec_msg = hill_cipher_encrypt(sec_msg, rand_key_2x2, alph)
rec_key = find_key(first_msg, enc_first_msg, alph, 2)
print("Найденный ключ:")
print(rec_key)
try:
    decr_sec_msg = hill_decrypt(enc_sec_msg, rec_key, alph)
    print("Расшифрованное сообщение:")
    print(decr_sec_msg)
except ValueError as e:
    print(f"Ошибка при расшифровке: {e}")




# 3 ЗАДАНИЕ
import numpy as np
import random

# Алфавит
alph = 'йцукенгшщзхъфывапролджэячсмитьбю'

#словарь, который сопоставляет каждому символу его двоичное представление в виде строки длиной 5 бит (например, 'й' → '00000')
char_to_bin = {char: format(i, '05b') for i, char in enumerate(alph)}
#обратный словарь, преобразующий 5-битные двоичные строки обратно в символы (например, '00000' → 'й').
bin_to_char = {v: k for k, v in char_to_bin.items()}

#Генерирующая матрица, которая преобразует 4-битные блоки данных в 7-битные кодовые слова. Она используется для кодирования
G = np.array([
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1]
], dtype=int)

#Проверочная матрица, которая используется для обнаружения и исправления ошибок при декодировании.
H = np.array([
    [1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1]
], dtype=int)


def encode_word(word, G):
    #Преобразуем слово в бинарный код, используя char_to_bin
    bin_msg = ''.join([char_to_bin[char] for char in word])
    print('Бинарное сообщение:', bin_msg)

    #Разбиваем бинарное сообщение на 4-битные блоки.
    blocks = [bin_msg[i:i + 4] for i in range(0, len(bin_msg), 4)]

    #Кодируем каждый блок, умножая на матрицу G и беря результат по модулю 2.
    enc_blocks = []
    for block in blocks:
        data_bits = np.array([int(bit) for bit in block], dtype=int)
        enc_block = np.dot(data_bits, G) % 2
        enc_blocks.append(''.join(map(str, enc_block)))
    #Возвращаем закодированное сообщение как объединение всех закодированных блоков.
    return ''.join(enc_blocks)


def make_err(num_err, msg):
    arr_msg = list(msg)#Списковое представление сообщения
    leng = len(arr_msg)#Длина сообщения
    #Генерация ошибки зависит от num_err - введенного количества ошибок
    for _ in range(num_err):
        #Генерация рандомной позиции для ошибки
        rand_pos = random.randint(0, leng - 1)
        #Инвертирования бита на месте ошибки
        arr_msg[rand_pos] = '0' if arr_msg[rand_pos] == '1' else '1'
    return ''.join(arr_msg)


def find_error(block, H):
    #Преобразуем блок в массив чисел.
    block_vector = np.array([int(bit) for bit in block], dtype=int)

    #Вычисляем синдром ошибки как произведение H * block по модулю 2.
    syndrome = np.dot(H, block_vector) % 2  #Синдром ошибки показывает, в какой позиции произошла ошибка.
    return syndrome


def correct_error(block, syndrome):
    #Преобразование блока сообщения в массив чисел
    block = np.array([int(bit) for bit in block], dtype=int)

    #Сравниваем синдром ошибки с каждым столбцом матрицы H.
    for i in range(7):
        if np.array_equal(H[:, i], syndrome):

            #Если совпадение найдено, инвертирует соответствующий бит в блоке.
            block[i] = 1 - block[i]
            break

    #Возвращаем исправленный блок.
    return block


def decoding(enc_msg, H):
    length = len(enc_msg)#Длина зашифрованного сообщения
    num_blocks = length // 7#Количество блоков в зашифрованном сообщении
    dec_msg = ''

    for i in range(num_blocks):
        # Разделение сообщения на блоки
        block = enc_msg[i * 7:(i + 1) * 7]

        #Поиск ошибки, выявление синдрома
        syndrome = find_error(block, H)

        # Проверка наличия ошибки
        if np.any(syndrome):
            #Исправление ошибки в блоке сообщения
            block = correct_error(block, syndrome)

        # Добавление исправленного блока
        dec_msg += ''.join(map(str, block[:4]))  # Используем только первые 4 бита

    # Преобразование двоичного кода обратно в символы
    decoded_chars = []
    for i in range(0, len(dec_msg), 5):
        char_bin = dec_msg[i:i + 5]
        decoded_chars.append(bin_to_char[char_bin])

    return ''.join(decoded_chars)



msg = encode_word('пчел', G)
print("Закодированное сообщение:", msg)

err_msg = make_err(4, msg)
print("Сообщение с ошибкой:", err_msg)

dec_msg = decoding(err_msg, H)
print("Декодированное сообщение:", dec_msg)

