# 🔐 Message Encoder & Decoder (Python)

A **fun Python program** that encodes and decodes secret messages using **string manipulation and random characters**.  
Perfect for beginners learning about strings, loops, functions, and conditional logic.

---

## 📌 Project Overview

This program allows the user to:
- Enter a message
- Choose whether to **encode (coding)** or **decode (decoding)** the message
- Transform each word using a custom encryption logic

The encoded message can be decoded back to its original form using the same program.

---

## ⚙️ How Encoding Works

For each word in the message:

### ✔ If word length ≥ 3:
1. Generate **3 random lowercase letters**
2. Move the **first letter to the end**
3. Add random letters at the **start and end**

**Example:**
```

hello → abcellohrxy

```

### ✔ If word length < 3:
- The word is simply **reversed**

---

## 🔓 How Decoding Works

For each word in the encoded message:

### ✔ If word length ≥ 3:
1. Remove the **first 3 and last 3 characters**
2. Move the **last character back to the front**

### ✔ If word length < 3:
- The word is **reversed back**

---

## ▶️ How to Run the Program

1. Make sure Python is installed
2. Save the file as:

```

message_encoder_decoder.py

```

3. Run the program:

```

python message_encoder_decoder.py

```

---

## 🧾 Sample Run

### Encoding
```

Enter message: hello world
coding or decoding: coding
abcellohr xyzorldwabc

```

### Decoding
```

Enter message: abcellohr xyzorldwabc
coding or decoding: decoding
hello world

```

---

## 🛠️ Concepts Used

- Strings & slicing
- Lists
- Loops
- Functions
- Random module
- Conditional statements
- Boolean logic

---

## 🚀 Future Enhancements

- Allow uppercase letters
- Add symbols and numbers
- Improve encryption strength
- Add menu-based interface
- Save encoded messages to a file

---

## 👩‍💻 Author

Python Practice Project  
Built to understand **string manipulation and logic building** 🐍

---

⭐ If you enjoyed this project, feel free to star the repository!
```
