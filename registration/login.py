from registration.registration import authenticate_user, create_db

def login_user(username, password):
    return authenticate_user(username, password)

def login():
    create_db()

    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")

    if login_user(username, password):
        print(f"Selamat datang, {username}!")
    else:
        print("Nama pengguna atau kata sandi salah.")

if __name__ == "__main__":
    login()