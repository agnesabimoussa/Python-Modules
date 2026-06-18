*This project has been created as part of the 42 curriculum by aabi-mou*

# Description
This module introduces functional programming and it's importance in Python.

# Exercises
- **ex0**: Lambda functions and functional operations (sorted, filter, map) - introduces anonymous functions and functional programming basics
- **ex1**: Higher-order functions - functions that return functions and compose behavior dynamically
- **ex2**: Closures and scope - using nonlocal keyword to maintain state privately within nested functions
- **ex3**: functools tools (reduce, partial, singledispatch, memoization) - advanced functional programming techniques for composition and optimization
- **ex4**: Decorators and metaprogramming - creating custom decorators for timing, validation, retry logic, and class methods

# Instructions
Clone the repo:
```bash
git clone git@vogsphere.42beirut.com:vogsphere/intra-uuid-1f0007ec-3038-4d18-9698-cda47df83d36-7326813-aabi-mou
```

Check flake8:
```bash
flake8 .
```

Test each exercise:
```bash
python ex0/lambda_spells.py
python ex1/higher_magic.py
python ex2/scope_mysteries.py
python ex3/functools_artifacts.py
python ex4/decorator_mastery.py
```
The outputs show the functionalities of each function implemented with sample data generated from the data generator tools

# Resources and AI Usage
- functools.reduce: https://docs.python.org/3/library/functools.html#functools.reduce
- functools.partial: https://medium.com/@vishalyadav8887690/using-functools-partial-in-python-a-comprehensive-guide-c24362845c3e
- functools.singledispatch: https://elshad-karimov.medium.com/unleashing-the-power-of-functools-singledispatch-in-python-853a4a60b364
- functools.wraps: http://medium.com/@blueberry92450/using-functools-wraps-in-python-decorator-952030a70615
- AI usage: creating main function bodies to test each function, ensuring all type hints are present
