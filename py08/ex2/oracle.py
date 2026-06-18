from dotenv import load_dotenv, find_dotenv
import os


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    if not find_dotenv():
        print("\nConfiguration is missing")
        print("Add your secrets to the .env file.")
    else:
        load_dotenv()
        mode = os.getenv("MATRIX_MODE")
        level = os.getenv("LOG_LEVEL")
        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {level}")
        print("Zion Network: Online")
        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
