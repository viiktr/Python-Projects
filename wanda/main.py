# The Wanda Magic teapot virtual version. Just like the original it has 5 options that will guide your future. Just think of a question and see.
import random
import time
(print("Hmmm, the answer to your question is... • Хммм, отговорът на твоя въпрос е:"))
time.sleep(2)
print ("
#                     ____( )_____
#     ___            |            |     ____
#     \  \         _---__________---_  / __ \
#      \  \       /                  \/ /  \ \
#_______|  |_____/                    \/____\ \_________________________________
       |  |    /                      \     | |
        \  \__|                        |    | |      _____________
         \    |                        |    | |      |           |/\
          \   |                        |   / /       |___________|  \
           \__\                        /__/ /        \-----------/  /
               \                      /____/          |---------|__/
                \____________________/               / \ _____ / \
Vicky Wilks      |__________________|                \___________/")
answer=random.randint(1,5)
if answer==1:
    print("Yes • Да")
elif answer==2:
    print("No • Не")
elif answer == 3:
        print("Maybe • Може би")
elif answer == 4:
        print("Not today • Не и днес")
else:
        print("Who knows • Кой знае")
