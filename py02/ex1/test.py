def garden_operations() -> None:
    """Demonstrate different error types with separate handling."""

    # 1. ValueError - converting non-numeric string
    try:
        num = int("abc")
    except ValueError as e:
        print("Caught ValueError: invalid literal for int()")

    # 2. ZeroDivisionError - dividing by zero
    try:
        result = 2 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError: division by zero")

    # 3. FileNotFoundError - opening non-existent file
    try:
        f = open("missing.txt", "r")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    # 4. KeyError - accessing missing dictionary key
    try:
        my_dict = {"rose": 5, "tulip": 3}
        value = my_dict["cactus"]
    except KeyError as e:
        print("Caught KeyError: 'missing_plant'")

    # 5. Multiple errors with one except block
    try:
        # Could raise ValueError or ZeroDivisionError
        x = int("xyz")  # This will raise ValueError
        y = 10 / 0      # Won't reach here
    except (ValueError, ZeroDivisionError) as e:
        print("Caught multiple errors together...")
        print(f"Error type: {type(e).__name__}, Message: {e}")


def test_error_types() -> None:
    """Test all error types and show program continues."""
    print("Testing ValueError...")
    garden_operations()  # This will run all demonstrations


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("\nAll error types tested successfully!")
