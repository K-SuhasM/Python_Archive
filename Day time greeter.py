import time
timestamp = time.strftime('%H:%M:%S')
print("The time is", timestamp)
hour = time.strftime('%H')
if 00<int(hour)<12:
    print("Good morning")
if hour==00:
    print("Good night")
elif 12<=int(hour)<18:
    print("Good afternoon")
elif 18<=int(hour)<20:
    print("Good evening")
elif 20==int(hour):
    print("Good night")
elif 20<=int(hour)<00:
    print("Good night")
