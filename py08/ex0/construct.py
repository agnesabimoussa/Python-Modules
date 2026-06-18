import sys
import os
import site

# This function will check wether the program is running
# from a virtual environment or not
# sys.prefix: without venv -> system-wide python installation directory
# with venv -> root directory of venv
# sys.base_prefix holds the path to the specific python installation


def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


# This function will print the correct message to the user
# to tell them whether they are in a
#  venv or not and guide you to create a virtual environment
def main() -> None:
    current_python = sys.executable
    if is_venv():
        env_name = os.path.basename(sys.prefix)
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {os.environ.get("VIRTUAL_ENV")}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"\nPackage installation path: {site.getsitepackages()[0]}")
        print()
    else:
        print("\nMATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {current_python}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env/Scripts/activate # On Windows")
        print("\nThen run this program again.")


# This is used to print the main function body only
# if the name variable is set to main
if __name__ == "__main__":
    main()
