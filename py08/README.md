*This project has been created as part of the 42 curriculum by aabi-mou*

# Description
Imagine you need a specific version of a package for a project you have, and another version of the same package for a second project. Without using virtual environments, you would have to install the version of the package OS-wide, and one of the projects will not work. This is where virtual environments are powerful: they let you create an isolated environment for each project where you can install packages and even test your project with different python versions, without interfering with other projects or the original python installation.

Small tutorial using linux commands:

- Create a virtual environment:
```bash
python -m venv venv
```

- Activate virtual environment:
```bash
source venv/bin/activate
```

- Install any packages you need inside the virtual environment:
```bash
pip install <package_name>
```

- Deactivate virtual environment:
```bash
deactivate
```


# Exercises

- ex0: Teaches how to detect wether the program is running from a virtual environment or not
- ex1: Use of pip and and poetry and demonstration of the difference between them
- ex2: Learn how to keep your secrets in a .env file


# Installation and Testing

Clone the repo:
```bash
git clone git@vogsphere.42beirut.com:vogsphere/intra-uuid-a98a5cef-20a6-42ff-befe-3202486c97d2-7325513-aabi-mou eval
```

Check flake8:
```bash
flake8 .
```

Test ex0, try with and without venv:
```bash
cd ex0
python construct.py #without venv
python -m venv venv
source venv/bin/activate
python construct.py
deactivate
cd ..
```

Test ex1, try before and after installing required dependencies:
```bash
cd ex1
python ex1
python loading.py
cd ..
```

Test ex2, try with and without a .env file:
```bash
cd ex2
python oracle.py
cd ..
```


# Resources and AI Usage
- Python Virtual Environment: https://www.w3schools.com/python/python_virtualenv.asp
- Python documentation: https://docs.python.org/3/
- AI usage: How to use all the dependencies in ex2 for a simple logic