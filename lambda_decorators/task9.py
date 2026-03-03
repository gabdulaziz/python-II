def to_fahrenheit(func):
    def wrapper(*args, **kwargs):
        celsius = func(*args, **kwargs)
        return (celsius * 9/5) + 32
    return wrapper

@to_fahrenheit
def today_temp():
    return 30

print(today_temp())