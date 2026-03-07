class TooLowTemp(Exception):
    pass


class TooHightTemp(Exception):
    pass


def check_temperature(temp_str: str) -> int:
    try:
        tmp = int(temp_str)
        if tmp >= 0 and tmp <= 40:
            print(f"Temperature {tmp}C is perfect for plants!")
            return (tmp)
        elif tmp < 0:
            raise TooLowTemp
        else:
            raise TooHightTemp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    except TooLowTemp:
        print(f"Error: {temp_str}C is too cold for plants (min 0C)")
    except TooHightTemp:
        print(f"Error: {temp_str}C is too hot for plants (max 40C)")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    print("Testing  temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
