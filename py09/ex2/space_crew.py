from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import List


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_id(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("mission ID must start with M")
        return self

    @model_validator(mode="after")
    def check_members(self) -> 'SpaceMission':
        is_captain = False
        is_commander = False
        for crew in self.crew:
            if crew.rank is Rank.CAPTAIN:
                is_captain = True
            elif crew.rank is Rank.COMMANDER:
                is_commander = True
        if not (is_captain or is_commander):
            raise ValueError(
                "Mission must have at least one Commander and Captain")
        return self

    @model_validator(mode="after")
    def check_experience(self) -> 'SpaceMission':
        if self.duration_days > 365:
            experienced_count = sum(
                1 for crew in self.crew if crew.years_experience >= 5)
            experienced_percentage = (experienced_count / len(self.crew)) * 100
            if experienced_percentage < 50:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew"
                    "(5+ years)")
        return self

    @model_validator(mode="after")
    def check_activity(self) -> 'SpaceMission':
        for crew in self.crew:
            if crew.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    crew_members = [
        CrewMember(
            member_id="CM_001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=42,
            specialization="Mission Command",
            years_experience=15,
            is_active=True
        ),
        CrewMember(
            member_id="CM_002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=10,
            is_active=True
        ),
        CrewMember(
            member_id="CM_003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )
    ]
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-06-01T00:00:00",
        duration_days=900,
        crew=crew_members,
        mission_status="planned",
        budget_millions=2500.0
    )
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")
    print("=========================================")
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Venus",
            launch_date="2024-06-01T00:00:00",
            duration_days=100,
            crew=[
                CrewMember(
                    member_id="CM_004",
                    name="Bob Wilson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Science",
                    years_experience=3,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=500.0
        )
    except ValidationError as e:
        error_msg = e.errors()[0]['msg']
        print(error_msg)


if __name__ == "__main__":
    main()
