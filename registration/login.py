from registration.registration import authenticate_user

def login_user(username, password):
    return authenticate_user(username, password)

def main():
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")

    if login_user(username, password):
        print("Login berhasil!")
    else:
        print("Nama pengguna atau kata sandi salah.")

if __name__ == "__main__":
    main()