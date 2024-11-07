from dotenv import dotenv_values

secrets = dotenv_values(".env")
key = secrets["API_KEY"]

def main():
    print(secrets["API_KEY"])


if __name__ == "__main__":
    main()