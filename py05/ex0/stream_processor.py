from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    This is an abstract class
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    """
    This is a subclass of DataProcessor
    """

    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if data.__class__ is not list:
            return False

        for x in data:
            if x.__class__ is not int and x.__class__ is not float:
                return False
        return True

    def process(self, data: Any) -> str:
        try:
            list[int](data)
            count = len(data)
            total_sum = sum(data)
            avg = total_sum / count
            return f"{count},{total_sum},{avg}"
        except ValueError:
            return "Error! Invalid data."

    def format_output(self, result: str) -> str:
        res_list = result.split(",")
        if len(res_list) != 3:
            return f"Error! Unexpected numeric format: {result}"
        return (f"Processed {res_list[0]} numeric values, "
                f"sum={res_list[1]}, avg={res_list[2]}")


class TextProcessor(DataProcessor):
    """
    This is a subclass of DataProcessor
    """

    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            str(data)
            count = len(data)
            words = data.split(" ")
            return f"{count},{len(words)}"
        except ValueError:
            return "Error! Invalid data."

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        return False

    def format_output(self, result: str) -> str:
        res_list = result.split(",")
        if len(res_list) != 2:
            return f"Error! Unexpected text format: {result}"
        return f"Processed text: {res_list[0]} characters, {res_list[1]} words"


class LogProcessor(DataProcessor):
    """
    This is a subclass of DataProcessor
    """

    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            error = str(data).split(":")
            if len(error) != 2:
                raise ValueError
            return f"{error[0].strip()},{error[1].strip()}"
        except ValueError:
            return "Error! Invalid data."

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            lower_data = str(data).lower()
            if (lower_data.startswith("error:") or
                    lower_data.startswith("info:")):
                return True
        return False

    def format_output(self, result: str) -> str:
        res_list = result.split(",")
        if len(res_list) != 2:
            return f"Error! Unexpected log format: {result}"
        if res_list[0].lower() == "error":
            return (f"[ALERT] {res_list[0]} level detected: "
                    f"{res_list[1]}")
        elif res_list[0].lower() == "info":
            return (f"[INFO] {res_list[0]} level detected: "
                    f"{res_list[1]}")
