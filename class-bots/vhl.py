from pynput.keyboard import Key, Controller
import time
import keyboard

# Constants: the pynputlibrary and the constant wait
# time between each move/keyboard press
pynputKeyBoard = Controller()
sleepCount = 0.025

# combo as a string here:
comboString = "543343"


def ComboSet():
    # The combo for each class, change for
    # other classes

    for i in comboString:
        time.sleep(sleepCount)
        pynputKeyBoard.press(i)
        pynputKeyBoard.release(i)


def ConstantRunning():
    # Loop running combo function abvoe and waiting
    # pause

    while True:
        ComboSet()

        if keyboard.is_pressed('p'):
            print('Paused the Bot!')
            break  # finishing the loop


def main():

    # Amount of time needed to click back into AQW
    time.sleep(1)

    # The function to loop a combo and pause the loop
    ConstantRunning()

    # If a user paused this loop pops up waiting for a player
    # to resume to continue
    while True:
        if keyboard.is_pressed('`'):
            print("Bot Resumed!")
            ConstantRunning()
        elif keyboard.is_pressed('q'):
            print("Bot Ended!")


if __name__ == '__main__':
    main()
