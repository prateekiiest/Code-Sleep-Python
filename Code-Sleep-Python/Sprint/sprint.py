import msvcrt
import time

high_score = 50
name = "no-one"

while(1):

    distance = int(0)
    print("\n--------------------------------------------------------------")
    print('\n\nWelcome to the 100m sprint, tap z and x rapidly to move!')
    print('* = 10m')
    print("\n**Current record: " + str(high_score) + "s, by: " + name)
    print('\nPress enter to start')
    input()
    print('Ready...')
    time.sleep(1)
    print('GO!')

    start_time = time.time()
    while(distance < 100):

        k1 = msvcrt.getch().decode('ASCII')
        if k1 == 'z':
            k2 = msvcrt.getch().decode('ASCII')
            if k2 == 'x':
                distance += 1
                if distance == 50:
                    print("* You're halfway there!")
                elif distance % 10 == 0:
                    print('*')

    fin_time = time.time() - start_time
    fin_time = round(fin_time, 2)
    print('Well done you did it in...')
    print(fin_time)

    if fin_time < high_score:
        print("Well done you've got a new high score ")
        name = input("Please enter your name : ")
        high_score = fin_time
