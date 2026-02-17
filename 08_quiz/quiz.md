# Practice Assignment: Classes and Objects in Python

## Data

You are given a file `student-data.py` containing a dictionary with quiz results. Each key is a student's name, and the value is a list of scores for 17 problems. A score of 0 means the problem was not solved. An empty list means the student was absent.

Import this data in your code:
```python
from quiz_data import student_data
```

---

## Task 1 — Student

### Step 1: Create the class

Create a `Student` class with the following attributes:

- `name` — student's full name
- `group` — group number
- `problems` — a dictionary where keys are problem numbers (1–17) and values are the score the student received for that problem (0 if not solved)
- `extra_points` — bonus points added by the teacher (default is 0)

The class should have the following methods:

- `get_score()` — returns the total score calculated from solved problems plus extra points
- `add_extra(points)` — adds bonus points to the student
- `solved_list()` — returns a list of problem numbers the student solved
- `failed_list()` — returns a list of problem numbers the student did not solve
- `display()` — prints the student's name, solved/failed problems, extra points, and total score in a readable format

### Step 2: Create objects

Read the data from `student-data.py` and create a `Student` object for each student. Convert the list into a dictionary (problem 1 → first score, problem 2 → second score, etc.). Students with empty lists should still be created with all problems scored as 0.

### Step 3: Add extra points

If a student received extra points during the quiz, add them using the `add_extra()` method.

### Step 4: Display results

Call `display()` for every student. The output should be clean and easy to read.

### Step 5: N, V, K

Add methods to the `Student` class that calculate **N**, **V**, and **K** values. Call these methods for all students and print the results.

---

## Task 2 — Problem

Create a `Problem` class with the following attributes:

- `number` — problem number
- `text` — short description of the problem
- `points` — maximum possible points for this problem
- `difficulty` — determined automatically in `__init__` based on points:
  - 1–3 points → `"easy"`
  - 4–6 points → `"medium"`
  - 7+ points → `"hard"`

The class should have the following methods:

- `avg_score(students)` — takes a list of `Student` objects and returns the average score all students got on this problem
- `display()` — prints the problem number, description, points, difficulty, and average score

Create a `Problem` object for each of the 17 quiz problems, calculate the average score for each, and print them all.

---

## Requirements

- Total score must be calculated inside the `Student` class
- Average score per problem must be calculated inside the `Problem` class
- All logic must live inside classes, not outside
- Use `__init__` for initialization
- Student objects must be created from `student-data.py`, not hardcoded one by one
- Code must be clean and readable

## Submission

Upload your `.py` file to the shared folder before the end of the class.
