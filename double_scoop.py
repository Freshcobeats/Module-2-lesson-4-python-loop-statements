import random

weekday = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
time_of_day = ['morning', 'afternoon', 'evening']
mood = ['Happy', 'Sad', 'Energetic','Calm']

for day in weekday:
    for time in time_of_day:
        current_mood = random.choice(mood)
        print(f"in the {time} on {day} you were feeling {current_mood}")