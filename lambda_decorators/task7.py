def weather_tracker(start_temp):
    temp = start_temp
    while True:
        yield temp
        temp += 1

tracker = weather_tracker(25)
print(next(tracker))
print(next(tracker))
print(next(tracker))