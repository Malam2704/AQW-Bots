from pynput.keyboard import Key, Controller
import time
import keyboard

# Constants: the pynputlibrary and the constant wait
# time between each move/keyboard press
pynputKeyBoard = Controller()
sleepCount = 0.025


def ComboSet():
    # The combo for each class, change for
    # other classes

    time.sleep(sleepCount)
    pynputKeyBoard.press("4")
    pynputKeyBoard.release("4")

    time.sleep(sleepCount)
    pynputKeyBoard.press("5")
    pynputKeyBoard.release("5")

    time.sleep(sleepCount)
    pynputKeyBoard.press("2")
    pynputKeyBoard.release("2")

    time.sleep(sleepCount)
    pynputKeyBoard.press("3")
    pynputKeyBoard.release("3")


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
