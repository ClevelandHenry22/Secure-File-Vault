
#  Secure_File_Vault  

### Advanced File Encryption Tool (Python + Cryptography)

SecureFileVault is a **professional file & directory encryption tool** built using the Python `cryptography` library (Fernet AES-128).  
It is designed to look and function as a project that demonstrates:

-  Strong Encryption  
-  Secure Key Management  
-  CLI-Based Cybersecurity Tooling  
-  Folder-Level Encryption  
-  Key Rotation  
-  Error Handling & Validation  
-  Clean, Clear, Well-Commented Code  

This tool is useful for **blue-team operations, secure data handling, forensics environments, and personal security**.

---

### **What Is Encryption?**

*Encryption transforms readable data (plaintext) into unreadable data (ciphertext) using a secret key.*
*Only someone with the correct key can decrypt it.*

**Fernet encryption (used in this project) provides**:

-**AES-128 encryption**: Encrypts files using a strong 128-bit key to keep data confidential.

-**HMAC for integrity verification**: Ensures the file has not been altered by generating a secure hash.

-**Protection against tampering**: Detects and blocks any unauthorized changes to encrypted files.

-**Timestamp-based tokens**: Adds time-limited token to prevent reuse of old or expired access requests.

This means **your data will stay confidential, verified, and safe**.

#  Features

###  File Encryption  
Encrypt any file using AES-128 (Fernet standard).

###  File Decryption  
Recover original files securely.

###  Directory Encryption  
Encrypt *every file* in a folder at once.

###  Directory Decryption  
Decrypt every `.enc` file recursively.

###  Key Generation  
Create strong Fernet keys & store them safely.

###  Key Rotation  
Change keys without breaking the encrypted files.

###  Detailed Logging & Error Handling  
For real use cases.



#  Installation

```
git clone https://github.com/YOUR_USERNAME/SecureFileVault.git
cd SecureFileVault
pip install cryptography
```
>**Kali Linux Note:**
>If `cryptography` is already installed, you're good to go.

## Creating the `Secure_file_vault.py` Script (Kali Linux)

Before using SecureFileVault, you must create the main Python script that contains all encryption and decryption logic.

**Steps**
1. *Create a directory named Secure_File_Vault* - `mkdir Secure-File_Vault`

2. *Open your project folder* - `cd Secure_File_Vault`

3. *Create a python script using nano* - `nano Secure_File_Vault.py`

4. *Paste the full encryption program code inside this file*

   -[Secure_File_Vault.py](secure_file_vault.py)

6. *Save and exit*

   -**nano**:

      Press `CTRL + O`, ENTER --> then CTRL + X 

7. *Confirm the fiel exists*: `ls`
---

#  Usage Guide
*Below are the main commands and what they do.*

---

###  Generate a new key

-**Make sure you are in the Secure-File-Vault directory**
```
python Secure_File_Vault.py --generate-key --key-file vault.key
```

![Key generation command](docs/screenshots/key_generation.png)

-*Creates a brand-new Fernet Key and stores it safely in `vault.key`.*
-*This key is the “secret” that protects all encrypted files.*
-*Anyone with this key can decrypt your data — so it must remain private.*

---

###  Encrypt a file
```
python Secure_File_Vault.py --encrypt secret.txt --output secret.enc --key-file vault.key
```
-*Reads the original file*

-*Encrypts it*

-*Saves encrypted output as `.enc`*

---

###  Decrypt a file
```bash
python Secure_File_Vault.py --decrypt secret.enc --output secret.txt --key-file vault.key
```
-*Restores the file to its original readable form*.

![File encryption decryption](docs/screenshots/file-encryption-decryption.png)

-*This screenshot shows the encrypted version of the file.*

-*After running the encryption command, the original readable text was transformed into a long block of random-looking characters.*

-*These characters are Fernet tokens, which include*: **AES-128 encrypted data, HMAC authentication hash, and Timestamp.**

**The original content is no longer visible or readable, proving that encryption succeeded and confidentiality is preserved**.

![contents of encrypted and decrypted file](docs/screenshots/file-encr-decr-content.png)

-*This screenshot shows the successful decryption process.*

-*The encrypted .enc file was fully restored back to its original plaintext form using the same Fernet key*.

-*The decrypted content matches the original data exactly, proving that*:

***The key was correct***

***The encrypted file wasn't tampered with***

***Integrity and confidentiality were both maintained***

---

###  Encrypt a whole directory
```bash
python Secure_File_Vault.py --encrypt-dir myfolder --key-file vault.key
```
-*Encrypts every file inside `myfolder`*.

---

###  Decrypt a directory
```bash
python Secure_File_Vault.py --decrypt-dir myfolder --key-file vault.key
```
-*Decrypts all encrypted files.*

![Directory encryption decryption](docs/screenshots/directory-encrypt-decrypt)

-*This image shows the tool decrypting each encrypted file in the directory.
All .enc files were processed and restored back to their readable versions.*

-*This confirms that SecureFileVault handles bulk decryption just as smoothly as encryption.*

![Encrypted files in the folder](docs/screenshots/enc_files_in_folder.png)

---

###  Rotate encryption key
```bash
python Secure_File_Vault.py --rotate-key --key-file vault.key
```
-*Generates a new key and updates the old one securely.*

-*The tool creates a new Fernet key and updates the existing vault.key.*

-*Key rotation improves security by limiting how long any single key is used.*

---

#  Real-World Use Cases

-  Protecting sensitive logs  
-  Encrypting incident-response evidence  
-  Safeguarding credentials  
-  Backing up sensitive config files  
-  Secure local storage for small businesses  
-  Cybersecurity learning & demonstrations  

---

#  Security Notes

- Keep your key file (`vault.key`) private  
- Do NOT upload the key to GitHub  
- Rotate keys periodically  
- Delete original unencrypted files after encryption  
- For forensic-level deletion, use tools like:  
  - `shred`, `srm`, `wipe`

---

#  Author

**Cleveland Henry Lore**  
*Cybersecurity Enthusiast* | *Penetration Testing* 
