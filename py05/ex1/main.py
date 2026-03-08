from data_stream import (
    SensorStream,
    TransactionStream,
    EventStream,
    StreamProcessor
)

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    stream_id = "SENSOR_001"
    sensor_stream = SensorStream(stream_id)
    print(f"Stream ID: {stream_id}, Type: Environmental Data")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    res = sensor_stream.process_batch(sensor_batch)
    print(res)

    print("\nInitializing Transaction Stream...")
    stream_id = "TRANS_001"
    transaction_stream = TransactionStream(stream_id)
    print(f"Stream ID: {stream_id}, Type: Financial Data")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")
    res = transaction_stream.process_batch(transaction_batch)
    print(res)

    print("\nInitializing Event Stream...")
    stream_id = "EVENT_001"
    event_stream = EventStream(stream_id)
    print(f"Stream ID: {stream_id}, Type: System Events")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    res = event_stream.process_batch(event_batch)
    print(res)

    print("\n=== Polymorphic Stream Processing ==")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    streams = {sensor_stream: ["temp:26", "humidity:65"],
               transaction_stream: ["buy:100", "sell:150",
                                    "buy:75", "sell:25"],
               event_stream: ["login", "error", "logout"]}
    stream_processor = StreamProcessor(streams)
    stream_processor.process_streams()
    print("\nStream filtering active: High-priority data only")
    stream_processor.filter_streams()
    print("\nAll streams processed successfully. Nexus throughput optimal.")
