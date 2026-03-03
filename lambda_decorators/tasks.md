
##  Section 1: *args & **kwargs (Flexible Data)

### Task 1: The Average Grade (*args)
Write a function `calculate_average(student_name, *grades)` that:
1. Takes a student's name.
2. Takes any number of grades (integers).
3. Returns a string: `"Student [Name] has an average grade of [Result]"`.

### Task 2: Weather Report (**kwargs)
Write a function `print_weather(city, **details)` that:
1. Takes the name of a city.
2. Takes details like `temp=30`, `sky="Sunny"`, `wind="5km/h"`.
3. Prints it like a weather forecast: `"In [City]: temp is 30, sky is Sunny..."`

---

## Section 2: Lambda Functions (Quick Logic)

### Task 3: Sorting Students by Age
You have a list of students:
`students = [("Ali", 22), ("Vali", 19), ("Zuhra", 20)]`.
Use `sorted()` and a **lambda** to sort them from the youngest to the oldest.

### Task 4: Filtering Hot Days
You have temperatures for the week: `temps = [25, 38, 42, 28, 33, 41]`.
Use `filter()` and a **lambda** to create a new list containing only days hotter than 35 degrees.

### Task 5: Student Name Formatter
Use `map()` and a **lambda** to take a list of names `["ali", "vali", "sami"]` and capitalize them: `["Ali", "Vali", "Sami"]`.

---

##  Section 3: Generators (Memory Saving)

### Task 6: Infinite "Next Student"
Write a generator `get_student(list_of_students)` that yields names from a list one by one. When you reach the end, it should stop.
* **Test:** Use `next()` to get the first 3 students.

### Task 7: Daily Temperature Monitor
Write a generator `weather_tracker(start_temp)` that:
1. Starts with a given temperature.
2. Every time you call `next()`, it yields the temperature increased by 1 degree (simulating the sun rising).

---

##  Section 4: Decorators (Functions "Wrappers")

### Task 8: The "Logged In" Check
Write a decorator `check_auth` that:
1. Prints `"Checking access to the Gradebook..."` before the function runs.
2. Then calls the function.
* **Use it on:** A function `view_grades()`.

### Task 9: The "Celsius to Fahrenheit" Converter
Write a decorator `to_fahrenheit` that:
1. Takes the result of a function (which is in Celsius).
2. Converts it to Fahrenheit using the formula: `(C * 9/5) + 32`.
3. Returns the new value.

### Task 10: The Secret Student Note
Write a decorator `make_bold` that adds `***` before and after the result of a function.
* **Example:** If the function returns `"Ali is a top student"`, the result should be `"*** Ali is a top student ***"`.