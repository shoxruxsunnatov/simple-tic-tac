import os
import time 

print('Starting game...')
time.sleep(0.4)
print('Building project...')
time.sleep(0.4)
print('Running...')
os.system('cls')

def start():
    cmd = str(input(" \033[0;32;1mQayta boshlash uchun istalgan tugmani bosing...\033[0m"))
    game()

def game():

    lis = ['\033[0;34;1m1\033[0m', '\033[0;34;1m2\033[0m','\033[0;34;1m3\033[0m',
            '\033[0;34;1m4\033[0m','\033[0;34;1m5\033[0m','\033[0;34;1m6\033[0m',
            '\033[0;34;1m7\033[0m','\033[0;34;1m8\033[0m','\033[0;34;1m9\033[0m']

    lis_ = [0,0,0,0,0,0,0,0,0]
    n = 1
    print(" \nDastur yaratuvchisi:\033[0;32;1m Shoxrux Sunnatov.\033[0m\n               \033[0;34;1mTelegram: @Alexander_King\033[0m\n")
    while True:
        print("[{}] [{}] [{}]\n[{}] [{}] [{}]\n[{}] [{}] [{}]".
            format(lis[0], lis[1], lis[2], lis[3], lis[4], lis[5], lis[6], lis[7], lis[8]))
        if n % 2 == 1:
            try:
                point = int(input("A: "))
            except:
                print("\033[0;31;1m Xatolik!!!\033[0m")
                game()

            if point < 1 or point > 9:
                print("\033[0;31;1m Xatolik!!!\033[0m")
                game()
            point -= 1
            if lis[point] == 'A' or lis[point] == 'B':
                os.system('cls')
                print("***Navbatingizni o'tqizib yubordingiz \033[0;31;1m A\033[0m!")
            else:
                lis[point] = 'A'
                lis_[point] = 1
                
                os.system('cls')

        else:
            try:
                point = int(input("B: "))
            except:
                print("\033[0;31;1m Xatolik!!!\033[0m")
                game()

            if point < 1 or point > 9:
                print("\033[0;31;1m Xatolik!!!\033[0m")
                game()
            point -= 1
            if lis[point] == 'A' or lis[point] == 'B':
                os.system('cls')
                print("***Navbatingizni o'tqizib yubordingiz \033[0;31;1m B\033[0m!")
            else:
                lis[point] = 'B'
                lis_[point] = 1
                
                os.system('cls')
        # check
        if lis_[0] == 1 and lis_[1] == 1 and lis_[2] == 1:
            if lis[0] == 'A' and lis[1] == 'A' and lis[2] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[0] == 'B' and lis[1] == 'B' and lis[2] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()

        if lis_[3] == 1 and lis_[4] == 1 and lis_[5] == 1:
            if lis[3] == 'A' and lis[4] == 'A' and lis[5] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[3] == 'B' and lis[4] == 'B' and lis[5] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()
        
        elif lis_[6] == 1 and lis_[7] == 1 and lis_[8] == 1:
            if lis[6] == 'A' and lis[7] == 'A' and lis[8] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[6] == 'B' and lis[7] == 'B' and lis[8] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()

        if lis_[2] == 1 and lis_[5] == 1 and lis_[8] == 1:
            if lis[2] == 'A' and lis[5] == 'A' and lis[8] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[2] == 'B' and lis[5] == 'B' and lis[8] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()

        if lis_[1] == 1 and lis_[4] == 1 and lis_[7] == 1:
            if lis[1] == 'A' and lis[4] == 'A' and lis[7] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[1] == 'B' and lis[4] == 'B' and lis[7] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()

        if lis_[0] == 1 and lis_[3] == 1 and lis_[6] == 1:
            if lis[0] == 'A' and lis[3] == 'A' and lis[6] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[0] == 'B' and lis[3] == 'B' and lis[6] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()

        if lis_[6] == 1 and lis_[4] == 1 and lis_[2] == 1:
            if lis[6] == 'A' and lis[4] == 'A' and lis[2] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[6] == 'B' and lis[4] == 'B' and lis[2] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()

        if lis_[0] == 1 and lis_[4] == 1 and lis_[8] == 1:
            if lis[0] == 'A' and lis[4] == 'A' and lis[8] == 'A':
                print("\033[0;34;1m *** O'yinda yutdingiz A!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz B!\033[0m!")
                start()
            elif lis[0] == 'B' and lis[4] == 'B' and lis[8] == 'B':
                print("\033[0;34;1m *** O'yinda yutdingiz B!\033[0m!")
                print("\033[0;31;1m *** O'yinda yutqazdingiz A!\033[0m!")
                start()


        n += 1
game()
start()  