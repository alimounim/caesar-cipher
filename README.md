# 🗝️ Caesar Cipher – Python Encryption Program

This project is a Python implementation of the Caesar Cipher, a classic encryption technique where each letter in the message is shifted by a fixed number of positions in the alphabet.
It allows you to encode (encrypt) and decode (decrypt) messages using a user-defined shift value.

- The program supports:
  - Encoding messages
  - Decoding messages
  - Preserving numbers, spaces, and symbols
  - Repeating the game until the user chooses to stop

## 📌 Features
- 🔐 Encrypt (encode) plain text messages
- 🔓 Decrypt (decode) encrypted messages
- 🔁 Replay option to run multiple encryptions/decryptions
- 🧠 Automatically wraps around the alphabet (e.g., shifting “z” by 2 becomes “b”)
- 🔤 Handles non-alphabet characters (numbers, punctuation, whitespace) correctly
- 🎨 Includes ASCII art banner (from art module)

## 🚀 How It Works

1. The user chooses whether to encode or decode.
2. The program asks for:
    - The message text
    - A shift number (integer)
3. The cipher function:
    - Shifts each letter forward/backward in the alphabet
    - Leaves symbols, spaces, and numbers unchanged
    - Wraps around from z → a
4. The output is displayed to the user.
5. The user can choose to play again.

## 📘 What I Learned
- This project teaches:
- How to use lists and indexing
- How to write reusable functions
- Loop control and input handling
- Basic string manipulation
- Modulo arithmetic (%) to wrap alphabet indexes
- Error-proofing by handling numbers/symbols correctly

## 📜 License

This project is open-source and free to use.
