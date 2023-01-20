# The Wanda Magic teapot virtual version. Just like the original it has 5 options that will guide your future. Just think of a question and see.
import random
import time

(print(" ⠀⠀           ⢀⣘⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"))
(print("⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⢀⣀⠘⠛⠛⠛⠛⠛⠛⠁⣀⠀"))
(print("⠀⢠⡿⠋⠉⠛⠃⣠⣤⣈⣉⡛⠛⠛⠛⠛⠛⠛⢛⣉⣁⣤⣄⠀⠀⣾⣿⡿⠗"))
(print("⠀⢸⡇⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣿⣿"))
(print("⠀⢸⣇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣉⣠⣿⣿⡀"))
(print("⠀⠀⠙⠷⡆⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢰⣿⣿⣿⣿⣿⡇⠀"))
(print("⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠸⣿⣿⣿⣿⠟⠀"))
(print("⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠈⠉⠁⠀⠀"))
(print("⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠙⠻⠿⠿⠿⠿⠿⠿⠛⠋"))

(print("Welcome to the magical teapot!"))
time.sleep(2)
(print("Think of a question..."))
time.sleep(3)

while True:
    answer = random.randint(1, 5)
    (print("Hmmm, the answer to your question is..."))
    time.sleep(2)
    if answer == 1:
        print("The Teapot says... Yes✅")
    elif answer == 2:
        print("The Teapot says... No❌")
    elif answer == 3:
        print("The Teapot says... Maybe❔")
    elif answer == 4:
        print("The Teapot says... Not today🕙")
    else:
        print("The Teapot says... Who knows🤔")

    again = input("Do you have another question for the teapot?  Yes/No ")

    if 'yes' in again:
            continue
    else:
            print("See you next time!")
            break
