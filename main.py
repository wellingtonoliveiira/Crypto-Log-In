def login_user():
    email = input("Digite seu email: ")
    password = int(input("Digite sua senha: "))

    print("\nAluno cadastrado!")
    print(f"E-mail: {email}")
    print(f"Password: {password}")


def main():
    print("=== Crypto Log In ===")
    login_user()


if __name__ == "__main__":
    main()