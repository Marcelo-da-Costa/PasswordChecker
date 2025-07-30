import re

def is_secure(password, weak_passwords):
    if password.lower() in weak_passwords:
        return False, "Senha está na lista de senhas fracas."

    if len(password) < 8:
        return False, "A senha deve ter no mínimo 8 caracteres."

    if not re.search(r"[A-Z]", password):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search(r"[a-z]", password):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    if not re.search(r"\d", password):
        return False, "A senha deve conter pelo menos um número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "A senha deve conter pelo menos um caractere especial."

    return True, "Senha segura!"

if __name__ == "__main__":
    with open("weak_passwords.txt", "r") as f:
        weak_passwords = [line.strip() for line in f]

    senha = input("Digite a senha para verificar: ")
    segura, msg = is_secure(senha, weak_passwords)
    print(f"✅ {msg}" if segura else f"⚠️ {msg}")
