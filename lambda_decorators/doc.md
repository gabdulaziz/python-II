# 
**Topics:** *args, **kwargs, Lambda Functions, Generators, and Decorators.

---

## Flexible Arguments (`*args` & `**kwargs`)

###  The Concept
* **`*args`**: Allows a function to accept any number of **positional** arguments. It stores them in a **Tuple**.
* **`**kwargs`**: Allows a function to accept any number of **keyword** (named) arguments. It stores them in a **Dictionary**.

###  Practical Example
```python
def student_profile(name, *grades, **extra_info):
    print(f"Student Name: {name}")
    print(f"Grades Received: {grades}")      # Tuple: (90, 88, 94)
    print(f"Additional Data: {extra_info}")  # Dict: {'city': 'Dushanbe', 'sport': 'Football'}

student_profile("Anisa", 90, 88, 94, city="Dushanbe", sport="Football")
```
## Lambda Functions (Anonymous)

###  The Concept
* A Lambda is a small, one-line function that doesn't need a name (defined with def). 
* It is perfect for short-term tasks or as an argument to other functions.
* Syntax: lambda arguments: expression

###  Practical Example
```python
# Sorting a list of tuples by the second value (age)
students = [("Sami", 22), ("Ali", 19), ("Zuhra", 20)]

# Using lambda as a key for sorting
students.sort(key=lambda x: x[1])

print(students) 
# Output: [('Ali', 19), ('Zuhra', 20), ('Sami', 22)]
```

## Generators (yield)

###  The Concept
* A Generator is a function that returns an iterator. 
* Unlike normal functions that use return (and stop), a generator uses yield to provide data one piece at a time. 
* This saves RAM because it doesn't store the whole list in memory.

###  Practical Example
```python
def weather_forecast():
    yield "9:00 AM: Sunny, 25°C"
    yield "1:00 PM: Windy, 30°C"
    yield "6:00 PM: Rainy, 22°C"

forecast = weather_forecast()

print(next(forecast)) # 9:00 AM...
print(next(forecast)) # 1:00 PM...
```

## Decorators (@)

###  The Concept
A Decorator is a function that takes another function and extends its behavior without explicitly modifying it. 
Think of it as "wrapping" a gift.

###  Practical Example
```python
def simple_logger(func):
    def wrapper():
        print("[LOG]: The function is starting...")
        func()
        print("[LOG]: The function has finished.")
    return wrapper

@simple_logger
def say_hello():
    print("Hello from Dushanbe!")

say_hello()
```

### 📊 Quick Reference Table

| Feature | Syntax | Analogy | Key Benefit | Real-World Use Case |
| :--- | :--- | :--- | :--- | :--- |
| ***args** | `def f(*args):` | **The Magic Bag** | Accepts any number of items | Summing up all student grades |
| ****kwargs** | `def f(**kw):` | **Labeled Boxes** | Accepts named data (key=val) | Setting weather details (city, wind) |
| **Lambda** | `lambda x: x*2` | **The Paper Cup** | Fast, one-line disposable logic | Sorting names by length |
| **Generators** | `yield` | **The Lazy Cook** | Saves Memory (RAM) | Processing massive lists of users |
| **Decorators** | `@decorator` | **Gift Wrap** | Adds features without changing code | Checking if a user is an "Admin" |