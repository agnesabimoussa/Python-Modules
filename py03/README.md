# Data Quest: Mastering Python Collections for Data Engineering (py03)

This repository contains solutions for exercises 0–6, focusing on Python collections and data-processing patterns. Each exercise demonstrates the targeted data structure or technique with clear, minimal examples that follow the subject’s constraints.

## Project Layout
- ex0/ft_command_quest.py — command-line argument inspection
- ex1/ft_score_analytics.py — list-based score analytics with error handling
- ex2/ft_coordinate_system.py — tuple-based 3D coordinates and distance
- ex3/ft_achievement_tracker.py — set operations for achievement analytics
- ex4/ft_inventory_system.py — dictionary-based inventory with statistics
- ex5/ft_data_stream.py — generator-based streaming analysis
- ex6/ft_analytics_dashboard.py — comprehension-driven analytics dashboard

## Running the Exercises
Use Python 3.10+.

- Exercise 0: Command Quest
  - Examples:
    - python3 ex0/ft_command_quest.py
    - python3 ex0/ft_command_quest.py hello world 42

- Exercise 1: Score Cruncher
  - Example: python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950

- Exercise 2: Position Tracker
  - Examples:
    - python3 ex2/ft_coordinate_system.py "3,4,0"
    - python3 ex2/ft_coordinate_system.py 3 4 0

- Exercise 3: Achievement Hunter
  - Example: python3 ex3/ft_achievement_tracker.py

- Exercise 4: Inventory Master
  - Example: python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1

- Exercise 5: Stream Wizard
  - Example: python3 ex5/ft_data_stream.py

- Exercise 6: Data Alchemist
  - Example: python3 ex6/ft_analytics_dashboard.py

## What Each Exercise Demonstrates
- ex0: sys.argv basics, counting and listing arguments, friendly messages.
- ex1: Lists for sequential numeric data; computing sum, average, min/max; input validation.
- ex2: Tuples for immutable (x, y, z) coordinates; parsing inputs and calculating Euclidean distance; tuple unpacking.
- ex3: Sets for unique achievements; union, intersection, difference for analytics.
- ex4: Dictionaries to model items with nested attributes; computing totals, percentages, and most/least abundant items using dict operations.
- ex5: Generators (yield) for streaming; iterating events and computing basic stats with constant memory.
- ex6: List, dict, and set comprehensions to filter, transform, aggregate, and derive insights; a small combined analysis (totals, averages, top performer).

## Notes
- Code targets Python 3.10+ and follows the per-exercise authorized operations outlined in the subject.
- No file I/O is used for exercise logic; everything is in-memory or via CLI arguments as required.
