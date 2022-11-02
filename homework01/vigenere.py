alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
encrypt = True
result=''
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
<<<<<<< HEAD
     for i in range(len(plaintext)):
        letter_n = alphabet.index(plaintext[i])
        key_n = alphabet.index(keyword[i % len(keyword)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


def vigenere_encrypt(text, key):
    return vigenere(text=text, key=key, encrypt=True)


def vigenere_decrypt(text, key):
    return vigenere(text=text, key=key, encrypt=False)
=======
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = alphabet.lower()
    key_length = len(keyword)

    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            shift = ord(keyword[i % key_length]) - ord("A")
            ciphertext += alphabet[(alphabet.find(plaintext[i]) + shift) % 26]
        elif plaintext[i] in alphabet_low:
            shift = ord(keyword[i % key_length]) - ord("a")
            ciphertext += alphabet_low[(alphabet_low.find(plaintext[i]) + shift) % 26]
        else:
            ciphertext += plaintext[i]

    return ciphertext
>>>>>>> afbc1ae0dbe194732a292ec69f4f22927a4aa3d1


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = alphabet.lower()
    key_length = len(keyword)

    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            shift = ord(keyword[i % key_length]) - ord("A")
            plaintext += alphabet[(alphabet.find(ciphertext[i]) - shift) % 26]
        elif ciphertext[i] in alphabet_low:
            shift = ord(keyword[i % key_length]) - ord("a")
            plaintext += alphabet_low[(alphabet_low.find(ciphertext[i]) - shift) % 26]
        else:
            plaintext += ciphertext[i]

    return plaintext

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    keyword *= len(plaintext) // len(keyword) + 1
    ciphertext = ""
    for i, j in enumerate(plaintext):
        if keyword[i] == 'a' or keyword[i] == "A":
            ciphertext += j
        else:
            bukva = (ord(j) + ord(keyword[i]))
            ciphertext += chr(bukva % 26 + 65)
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    keyword *= len(ciphertext) // len(keyword) + 1
    plaintext = ""
    for i, j in enumerate(ciphertext):
        if (keyword[i] == 'a' or keyword[i] == "A"):
            plaintext += j
        else:
            bukva = (ord(j) - ord(keyword[i]))
            plaintext += chr(bukva % 26 + 65)
    return plaintext

