import random


def generate_gamma(key, length):
    gamma = ''
    for i in range(length):
        gamma += key[i % len(key)]
    return gamma


def encrypt(text, alphabet, gamma, alphabet_len):
    encrypted_text = ''
    for i in range(len(text)):
        encrypted_char_code = alphabet[(alphabet.index(text[i]) + gamma.index(gamma[i])) % alphabet_len]
        encrypted_text += encrypted_char_code
    return encrypted_text

def decrypt(text, alphabet, gamma, alphabet_len):
    decrypted_text = ''
    for i in range(len(text)):
        decrypted_char_code = alphabet[(alphabet.index(text[i]) - gamma.index(gamma[i])) % alphabet_len]
        decrypted_text += decrypted_char_code
    return decrypted_text


def read_input_file(file_name):
    result = ""
    with open(file_name, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            result += line
    return result


def write_output_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)
    f.close()


def main():
    key = "моєхобі"
    input_file_name = "input_ua.txt"
    output_file_name = "output_ua.txt"
    uk_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    alphabet_len = len(uk_alphabet)

    shuffled_alphabet = random.sample(uk_alphabet, alphabet_len)
    original_text = read_input_file(input_file_name).lower()
    gamma = generate_gamma(key, len(original_text))

    encrypted_text = encrypt(original_text, shuffled_alphabet, gamma, alphabet_len)
    write_output_file(output_file_name, encrypted_text)
    decrypted_text = decrypt(encrypted_text, shuffled_alphabet, gamma, alphabet_len)

    print("Оригінальний текст:", original_text)
    print("Зашифрований текст:", encrypted_text)
    print("Дешифрований текст:", decrypted_text)


if __name__ == "__main__":
    main()