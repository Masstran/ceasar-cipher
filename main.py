alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text: str, shift: int) -> str:
  encrypted_text = ""
  for char in text:
    if char not in alphabet:
      encrypted_text += char
      continue
    char_position = alphabet.index(char)
    encrypted_char_position = (char_position + shift) % len(alphabet)
    encrypted_text += alphabet[encrypted_char_position]
  return encrypted_text

print(encrypt(text, shift))
