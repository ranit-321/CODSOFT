#%%
import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) 
                and any(c.isupper() for c in password) 
                and any(c.isdigit() for c in password) 
                and any(c in string.punctuation for c in password)):
            return password

def main():
    print("Password Generator")
    print("------------------")

    while True:
        length = input("Enter the desired length of the password (min 12): ")
        if length.isdigit() and int(length) >= 12:
            length = int(length)
            break
        else:
            print("Invalid input. Please enter a number greater than or equal to 12.")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
# %%
