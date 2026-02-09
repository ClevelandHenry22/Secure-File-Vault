#!/usr/bin/env python3
"""
SecureFileVault - Advanced File Encryption Tool
Author: Cleveland Henry Lore

This tool encrypts and decrypts files using Fernet (AES-128 internally),
with options for key generation, key rotation, directory encryption,
and full error handling.
"""

import os
import argparse
from cryptography.fernet import Fernet



# KEY MANAGEMENT


def generate_key():
    """Generate a secure Fernet encryption key."""
    return Fernet.generate_key()


def save_key(key, key_file):
    """Save the key into a .key file."""
    with open(key_file, 'wb') as file:
        file.write(key)


def load_key(key_file):
    """Load an existing key from a .key file."""
    if not os.path.exists(key_file):
        raise FileNotFoundError(f"Key file '{key_file}' not found.")
    with open(key_file, 'rb') as file:
        return file.read()


def rotate_key(old_key, key_file):
    """
    Rotates the encryption key.
    NOTE: Old files encrypted with the old key must be re-encrypted manually.
    """
    new_key = generate_key()
    save_key(new_key, key_file)
    return new_key



# FILE OPERATIONS


def encrypt_file(input_file, output_file, key):
    """Encrypt a single file."""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    with open(input_file, 'rb') as file:
        data = file.read()

    encrypted_data = Fernet(key).encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(input_file, output_file, key):
    """Decrypt a single file."""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Encrypted file '{input_file}' not found.")

    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = Fernet(key).decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)



# DIRECTORY ENCRYPTION 


def encrypt_directory(directory, key):
    """Encrypt every file in a directory."""
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory.")

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            encrypt_file(path, path + ".enc", key)
            os.remove(path)  # Secure delete (simple version)


def decrypt_directory(directory, key):
    """Decrypt every .enc file in a directory."""
    for filename in os.listdir(directory):
        if filename.endswith(".enc"):
            path = os.path.join(directory, filename)
            original_path = path.replace(".enc", "")
            decrypt_file(path, original_path, key)
            os.remove(path)


# COMMAND-LINE INTERFACE

def main():
    parser = argparse.ArgumentParser(
        description="SecureFileVault - Advanced File Encryption Tool"
    )

    parser.add_argument("--generate-key", help="Generate a new encryption key", action="store_true")
    parser.add_argument("--rotate-key", help="Rotate existing key file", action="store_true")
    parser.add_argument("--key-file", type=str, default="vault.key", help="Path to key file")

    parser.add_argument("--encrypt", type=str, help="Encrypt a file")
    parser.add_argument("--decrypt", type=str, help="Decrypt a file")
    parser.add_argument("--output", type=str, help="Output file path")

    parser.add_argument("--encrypt-dir", type=str, help="Encrypt a whole directory")
    parser.add_argument("--decrypt-dir", type=str, help="Decrypt a directory containing .enc files")

    args = parser.parse_args()

    # Handle key generation
    if args.generate_key:
        key = generate_key()
        save_key(key, args.key_file)
        print(f"[+] New key generated and saved to {args.key_file}")
        return

    # Load key if needed
    try:
        key = load_key(args.key_file)
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # Rotate key
    if args.rotate_key:
        rotate_key(key, args.key_file)
        print("[+] Key rotated successfully.")
        return

    # Encrypt file
    if args.encrypt and args.output:
        encrypt_file(args.encrypt, args.output, key)
        print(f"[+] Encrypted '{args.encrypt}' → '{args.output}'")
        return

    # Decrypt file
    if args.decrypt and args.output:
        decrypt_file(args.decrypt, args.output, key)
        print(f"[+] Decrypted '{args.decrypt}' → '{args.output}'")
        return

    # Directory encryption
    if args.encrypt_dir:
        encrypt_directory(args.encrypt_dir, key)
        print(f"[+] Directory '{args.encrypt_dir}' encrypted.")
        return

    if args.decrypt_dir:
        decrypt_directory(args.decrypt_dir, key)
        print(f"[+] Directory '{args.decrypt_dir}' decrypted.")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
