# Advanced Assignment: Quiz Analytics System

You already know how to create basic classes. Now build a system that actually works together.

## Data

Use the same `student-data.py` file.

## Task

Create a mini analytics system for quiz results using three classes: `Problem`, `Student`, and `Quiz`.

### Class: Problem

- `number`, `text`, `points`
- Difficulty is determined automatically based on points
- `avg_score(students)` — returns the average score all students got on this problem
- A problem can return its info as a dictionary

### Class: Student

- `name`, `group`, `problems` (dict of problem number → score), `extra_points`
- Can calculate total score
- Can return a list of solved and failed problems
- Can calculate N, V, K values
- `print(student)` should return a readable string (use `__str__`)

### Class: Quiz

This is the main class. It takes a list of `Problem` objects and a list of `Student` objects.

It should be able to:

- `top(n)` — return top N students sorted by score
- `hardest_problem()` — return the problem that the fewest students solved
- `easiest_problem()` — return the problem that the most students solved
- `average_score()` — return the average score across all students
- `above_average()` — return a list of students who scored above average
- `report()` — print a full formatted report: all students ranked by score, all problems with how many students solved each and average score, overall average, and top 3

### Requirements

- All logic must live inside the classes
- Use `__str__` in Student
- No global variables — everything goes through objects
- Student objects must be created from `student-data.py`, not hardcoded
- Code must be clean and readable
