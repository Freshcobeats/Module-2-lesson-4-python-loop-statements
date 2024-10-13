import random

weekday = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
mood = ['Happy', 'Sad', 'Energetic','Calm']

for day in weekday:
    chosen_mood = random.choice(mood)
    print(f"on {day}, you were feeling {chosen_mood}.")