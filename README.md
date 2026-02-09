# 🔐 SecureFileVault  
### Advanced File Encryption Tool (Python + Cryptography)

SecureFileVault is a **professional file & directory encryption tool** built using the Python `cryptography` library (Fernet AES-128).  
It is designed as a **real-world cybersecurity project** that demonstrates:

- 🔥 Strong Encryption  
- 🔑 Secure Key Management  
- 🎯 CLI-Based Cybersecurity Tooling  
- 📂 Folder-Level Encryption  
- ♻️ Key Rotation  
- 🛡️ Error Handling & Validation  
- 🧠 Clean, Clear, Well-Commented Code  

This tool is useful for **blue-team ops, secure data handling, forensics environments, and personal security**.

---

# 📌 Features

### ✅ File Encryption  
Encrypt any file using AES-128 (Fernet standard).

### ✅ File Decryption  
Recover original files securely.

### ✅ Directory Encryption  
Encrypt *every file* in a folder at once.

### ✅ Directory Decryption  
Decrypt every `.enc` file recursively.

### ✅ Key Generation  
Create strong Fernet keys & store them safely.

### ✅ Key Rotation  
Rotate keys without breaking the application.

### ✅ Detailed Logging & Error Handling  
Made for real-world use cases.

---

# 🧪 Installation

```bash
git clone https://github.com/YOUR_USERNAME/SecureFileVault.git
cd SecureFileVault
pip install cryptography
```

---

# 🚀 Usage

### 🎯 Generate a new key
```bash
python secure_file_vault.py --generate-key --key-file vault.key
```

---

### 🔐 Encrypt a file
```bash
python secure_file_vault.py --encrypt secret.txt --output secret.enc --key-file vault.key
```

---

### 🔓 Decrypt a file
```bash
python secure_file_vault.py --decrypt secret.enc --output secret.txt --key-file vault.key
```

---

### 📂 Encrypt a whole directory
```bash
python secure_file_vault.py --encrypt-dir myfolder --key-file vault.key
```

---

### 📂 Decrypt a directory
```bash
python secure_file_vault.py --decrypt-dir myfolder --key-file vault.key
```

---

### ♻️ Rotate encryption key
```bash
python secure_file_vault.py --rotate-key --key-file vault.key
```

---

# 🔐 How Encryption Works (Simplified)

SecureFileVault uses **Fernet** from the Python `cryptography` library.

Fernet guarantees:

- AES-128 encryption  
- HMAC authentication  
- Timestamped tokens  
- No silent corruption  

This ensures **confidentiality + integrity** of your data.

---

# 🧳 Real-World Use Cases

- ✔️ Protecting sensitive logs  
- ✔️ Encrypting incident-response evidence  
- ✔️ Safeguarding credentials  
- ✔️ Backing up sensitive config files  
- ✔️ Secure local storage for small businesses  
- ✔️ Cybersecurity learning & demonstrations  

---

# 🛡️ Security Notes

- Keep your key file (`vault.key`) private  
- Do NOT upload the key to GitHub  
- Rotate keys periodically  
- Delete original unencrypted files after encryption  
- For forensic-level deletion, use tools like:  
  - `shred`, `srm`, `wipe`

---

# 👨‍💻 Author

**Cleveland Henry Lore**  
Cybersecurity | Penetration Testing | Blue Team Ops | Python Security Tools  
