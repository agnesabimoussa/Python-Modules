*This project has been created as part of the 42 curriculum by aabi-mou*

# Description
This module teaches about the Pydantic module in Python. Pydantic is a data validation tool used in Python, used to handle messy data and perform automatic type conversions when needed. It is useful for data validation and ensuring all data are in their required types and formats. The BaseModel class defines a data model and provides functionality like data validation and automatic conversions. The Field function is used to apply constraints to data, define default values and marking data as required. To start using Pydantic:
```bash
pip install pydantic
```

Example script
```bash
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id='1', name='Alice', email='alice@example.com')
print(user)
```
In this example, Pydantic will automatically convert '1' to 1 and ensure all types are valid, else a ValidationError exception is raised

# Exercises
- ex0: Learn about pydantic BaseModel and Field function
- ex1: Learn how the model_validator decorator can help implement stronger policies
- ex2: Learn nested pydantic modules

# Installation and Testing

Clone the repo:
```bash
git clone git@vogsphere.42beirut.com:vogsphere/intra-uuid-b3c692d6-2182-4416-9fc5-2a2aca9aa81b-7326398-aabi-mou
```

Check flake8:
```bash
flake8 .
```

Install pydantic version 2+ using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install "pydantic>=2"
```

Run each exercise:
```bash
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py
```

Deactivate virtual environment:
```bash
deactivate
```


# Resources and AI Usage
- Pydantic introduction: https://docsaid.org/en/blog/pydantic-intro/
- AI usage: Repetitive tasks, like writing a function just to match the output