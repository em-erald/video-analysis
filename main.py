from dotenv import dotenv_values

secrets = dotenv_values(".env")

def main():
    print(secrets["API_KEY"])


if __name__ == "__main__":
    main()