alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text: str, shift: int, direction: str) -> str:
  multiplier = 0
  if direction == "encode":
    multiplier = 1
  elif direction == "decode":
    multiplier = -1
  else:
    print("No idea, what you are doing, I'm just gonna give you your text back")
  new_text = ""
  for char in text:
    if char not in alphabet:
      new_text += char
      continue
    char_position = alphabet.index(char)
    new_char_position = (char_position + shift * multiplier) % len(alphabet)
    new_text += alphabet[new_char_position]
  return new_text

print(f"Result text is: {caesar(text, shift, direction)}")