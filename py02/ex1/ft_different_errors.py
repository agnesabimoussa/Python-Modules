def garden_operations() -> None:
    try:
        int("abc")
        5 / 0
        open("missing.txt", 'r')
        my_dict = {
            "brand": "Ford",
            "year": 1964
        }
        my_dict["model"]
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Caught ")