#!/usr/bin/env python3
"""
Gera arquivos de teste na pasta lab_files/
Uso: python generate_test_files.py
"""
import os

def main():
    os.makedirs("lab_files", exist_ok=True)
    texts = [
        ("doc1.txt", "Este é um arquivo de teste 1."),
        ("doc2.txt", "Este é um arquivo de teste 2."),
        ("secrets.txt", "Segredo: senhas-fake-123")
    ]
    for name, content in texts:
        path = os.path.join("lab_files", name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    print("Arquivos de teste gerados em ./lab_files/")

if __name__ == "__main__":
    main()
