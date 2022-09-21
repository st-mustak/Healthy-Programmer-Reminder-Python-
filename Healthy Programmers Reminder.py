# This Programme is made By : Mustak Ahmed, Pursuing B.Tech in CSE(Roll-CSE194028) From Aliah University.
# Datetime : 15 April 2021 at 7.00 Pm
# Project Name : Healthy Programmer's Reminder.
# Water : Every 30 mins  ||   Eyes-rest :  every 20 mins   ||   Exercise : every 60 mins.

# ________________________________Modules_______________________________________________
import os
from pygame import mixer
from datetime import datetime, timedelta, date
from time import time

# ___________________________________Functions______________________________________________


def music(file, stop_button):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        user_input = input(f"\nEnter '{stop_button}' when done : ")
        print()
        user_input.lower()
        if user_input == stop_button:
            mixer.music.stop()
            break
        else:
            print("Invalid Enter.Please try agian.")
            continue


def record(file, statement):
    if not os.path.exists('Records'):
        os.makedirs('Records')
    with open(f"Records\{file}_{date.today()}.txt", 'a') as f:
        f.write(
            f"__________________{datetime.now()}_____________________\n\n{statement}\n\n")


# ___________________________Main Programme Starts From Here_________________________________

if __name__ == '__main__':

    print("\n\n<<<________Healthy Programmer's Reminder_________>>>\n\n")
    print("Enter the Time Period.\n")
    start = str(input("Start at (HH:MM) : "))
    end = str(input("Ends at (HH:MM) : "))

    # __________________Variables______________________

    water_sound = "Sounds\Water.mp3"
    eyes_sound = "Sounds\Eyes.mp3"
    exercise_sound = "Sounds\Exercise.mp3"

    water_stop_butt = 'water'
    eyes_stop_butt = 'eyes'
    exercise_stop_butt = 'exercise'

    print()
    water_inp = float(
        input("Enter the cycle period for Water (in mins) : "))  # 30*60
    print()
    water_duration = water_inp*60
    eyes_inp = float(
        input("Enter the cycle period for Eyes (in mins) : "))    # 20*60
    print()
    eyes_duration = eyes_inp*60
    exercise_inp = float(
        input("Enter the cycle period for Exercise (in mins) : "))  # 60*60
    print()
    exercise_duration = exercise_inp*60

    water_initial = time()
    eyes_initial = time()
    exercise_initial = time()

    volume = 0
    phase1 = 0
    phase2 = 0
    point1 = 0
    point2 = 0
    water_point = 0

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Program has Started Successfully.\n")

        while current_time > start and current_time < end:

            if time() - water_initial > water_duration:  # _____For Water
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                future = now + timedelta(seconds=water_duration)
                next_time = future.strftime("%H:%M:%S")
                statement1 = f"\n>>>>  Drink One Glass Of Water.   ( Required Volume = 200 ml )\n     | Current Time = {current_time}  |  Next Reminder = {next_time}   |  Your Current Point: {water_point}"

                print(
                    statement1, end="\n")
                music(water_sound, water_stop_butt)
                water_initial = time()
                volume = volume+200
                water_point = water_point + 20
                status1 = f"Total Volume done = {volume} ml    |     Your Point : {water_point} \n"
                print(status1)
                print("\n\n\n")
                record('water_record', f"{statement1} \n {status1}")

            if time() - eyes_initial > eyes_duration:                   # ______For eyes

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                future = now + timedelta(seconds=eyes_duration)
                next_time = future.strftime("%H:%M:%S")
                statement2 = f"\n>>>>  Take 5 minutes rest For Your Eyes and look at the Nature.\n     | Current Time : {current_time}  |  Next Reminder : {next_time}   |  Your Current points = {point1} pt."

                print(
                    statement2, end="\n")
                music(eyes_sound, eyes_stop_butt)
                eyes_initial = time()
                phase1 = phase1+1
                point1 = point1+5
                status2 = f"     Phase {phase1} Done     |     Your Points = {point1} pt.\n"
                print(status2)
                print("\n\n\n")
                record('Eyes_record', f"{statement2} \n {status2}")

            if time() - exercise_initial > exercise_duration:          # ______For exercise

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                future = now + timedelta(seconds=exercise_duration)
                next_time = future.strftime("%H:%M:%S")
                statement3 = f"\n>>>>  It's time to Exercise for 5 minutes.\n     | Current Time = {current_time}  |  Next Reminder = {next_time}   |  Your Current points = {point2} pt."

                print(
                    statement3, end="\n")
                music(exercise_sound, exercise_stop_butt)
                exercise_initial = time()
                phase2 = phase2+1
                point2 = point2+10
                status3 = f"     Phase {phase2} Done     |     Your Points = {point2} pt."
                print(status3)
                print("\n\n\n")
                record('Exercise_record', f"{statement3} \n {status3}")
