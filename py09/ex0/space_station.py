from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, lt=20)
    power_level: float = Field(ge=0.0, lt=100.0)
    oxygen_level: float = Field(ge=0.0, lt=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)


def main() -> None:
    station = SpaceStation(
        station_id="SS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-03-21T00:00:00",
        notes=None)
    print("\nSpace Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status: ", end="")
    print("Operational" if station.is_operational else "Not operational")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=55,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-03-21T00:00:00",
            notes=None)
    except ValueError:
        print("Expected validation error:")
        print("Input should be less than or equal to 20")


if __name__ == "__main__":
    main()
