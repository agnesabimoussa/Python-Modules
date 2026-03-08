from stream_processor import (
    NumericProcessor, LogProcessor, TextProcessor
)

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    res = numeric_processor.process(data)
    if (numeric_processor.validate(data)):
        print("Validation: Numeric data verified")
        print(f"Output: {numeric_processor.format_output(res)}")
    else:
        print("Validation: Numeric data is invalid")

    print("\nInitializing Text Processor...")
    text_processor = TextProcessor()
    data = "Hello Nexus World"
    print(f"Processing data: \"{data}\"")
    res = text_processor.process(data)
    if (text_processor  .validate(data)):
        print("Validation: Text data verified")
        print(f"Output: {text_processor.format_output(res)}")
    else:
        print("Validation: Text data is invalid")

    print("\nInitializing Log Processor...")
    log_processor = LogProcessor()
    data = "ERROR: Connection timeout"
    print(f"Processing data: \"{data}\"")
    res = log_processor.process(data)
    if (log_processor  .validate(data)):
        print("Validation: Log data verified")
        print(f"Output: {log_processor.format_output(res)}")
    else:
        print("Validation: Log data is invalid")

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")
    list_data = [1, 2, 3]
    res = numeric_processor.process(list_data)
    print(f"Result 1: {numeric_processor.format_output(res)}")
    text_data = "Hello World!"
    res = text_processor.process(text_data)
    print(f"Result 2: {text_processor.format_output(res)}")
    log_data = "INFO: System ready"
    res = log_processor.process(log_data)
    print(f"Result 3: {log_processor.format_output(res)}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")
