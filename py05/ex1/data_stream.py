from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_data = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        metadata = {"stream_id": self.stream_id,
                    "processed_data": self.processed_data}
        return metadata


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.temp = 0
        self.humidity = 0
        self.pressure = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_data = 0
        try:
            for data in data_batch:
                setting = str(data).split(":")
                if len(setting) != 2:
                    raise ValueError
                key = setting[0].strip().lower()
                if key == "temp":
                    self.temp = float(setting[1])
                elif key == "humidity":
                    self.humidity = int(setting[1])
                elif key == "pressure":
                    self.pressure = int(setting[1])
                else:
                    raise ValueError
                self.processed_data += 1
            msg = (f"Sensor analysis: {self.processed_data} readings "
                   f"processed, avg temp: {self.temp}°C")
            return msg
        except ValueError:
            return f"Error processing invalid data: {data_batch}"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            threshold = float(criteria)
            filtered = []
            for data in data_batch:
                key, value = str(data).split(":")
                if key.strip().lower() == "temp" and float(value) > threshold:
                    filtered.append(data)
            return filtered
        except ValueError:
            print("Criteria should be a number for SensorStream")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_data": self.processed_data,
            "temperature": self.temp,
            "humidity": self.humidity,
            "pressure": self.pressure
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.bought = 0
        self.sold = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_data = 0
        try:
            batch_bought = 0
            batch_sold = 0

            for data in data_batch:
                setting = str(data).split(":")
                if len(setting) != 2:
                    raise ValueError
                key = setting[0].strip().lower()
                value = int(setting[1])
                if key == "buy":
                    batch_bought += value
                elif key == "sell":
                    batch_sold += value
                else:
                    raise ValueError
                self.processed_data += 1
            self.bought += batch_bought
            self.sold += batch_sold
            net_flow = batch_bought - batch_sold
            msg = (f"Transaction analysis: {self.processed_data} "
                   f"operations, net flow: {net_flow:+d} units")
            return msg
        except ValueError:
            return f"Error processing invalid data: {data_batch}"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            threshold = int(criteria)
            filtered = []
            for data in data_batch:
                key, value = str(data).split(":")
                if int(value) > threshold:
                    filtered.append(data)
            return filtered
        except ValueError:
            print("Criteria should be a number for TransactionStream")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_data": self.processed_data,
            "total_bought": self.bought,
            "total_sold": self.sold,
            "net_flow": self.bought - self.sold
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.login = 0
        self.logout = 0
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_data = 0
        self.login = 0
        self.logout = 0
        self.error = 0
        try:
            for data in data_batch:
                d = str(data).strip().lower()
                if d == "login":
                    self.login += 1
                elif d == "logout":
                    self.logout += 1
                elif d == "error":
                    self.error += 1
                else:
                    raise ValueError
                self.processed_data += 1
            total_events = self.login + self.logout + self.error
            msg = (f"Event analysis: {total_events} events, "
                   f"{self.error} error detected")
            return msg
        except ValueError:
            return f"Error processing invalid data: {data_batch}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch
        event_type = str(criteria).strip().lower()
        if (event_type != "login" and event_type != "logout" and
                event_type != "error"):
            return []
        return [item for item in data_batch
                if str(item).strip().lower() == event_type]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        metadata = {"stream_id": self.stream_id,
                    "processed_data": self.processed_data,
                    "total_login": self.login,
                    "total_logout": self.logout,
                    "total_error": self.error}
        return metadata


class StreamProcessor:
    def __init__(self, streams: Dict[DataStream, List[Any]]) -> None:
        self.streams: Dict[DataStream, List[Any]] = {}
        for stream, data_list in streams.items():
            if isinstance(stream, (EventStream, TransactionStream,
                                   SensorStream)):
                self.streams[stream] = data_list

    def process_streams(self) -> None:
        for stream, data_list in self.streams.items():
            if isinstance(stream, SensorStream):
                stream.process_batch(data_list)
                print(f"- Sensor data: {stream.processed_data} "
                      f"readings processed")
            elif isinstance(stream, TransactionStream):
                stream.process_batch(data_list)
                print(f"- Transaction data: {stream.processed_data} "
                      f"operations processed")
            elif isinstance(stream, EventStream):
                stream.process_batch(data_list)
                print(
                    f"- Event data: {stream.processed_data} events processed")

    def filter_streams(self) -> None:
        """
        keeps only high priority data from each stream
        """
        count_sensor = 0
        count_transaction = 0
        count_event = 0
        filtered_data: List[Any]
        for stream, data_list in self.streams.items():
            filtered_data = []
            if isinstance(stream, SensorStream):
                filtered_data = stream.filter_data(data_list, "25")
                count_sensor += len(filtered_data)
            elif isinstance(stream, TransactionStream):
                filtered_data = stream.filter_data(data_list, "100")
                count_transaction += len(filtered_data)
            elif isinstance(stream, EventStream):
                filtered_data = stream.filter_data(data_list, "error")
                count_event += len(filtered_data)
        print(
            f"Filtered results: {count_sensor} critical sensor "
            f"alerts, {count_transaction} large transaction, "
            f"{count_event} total error events")


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
