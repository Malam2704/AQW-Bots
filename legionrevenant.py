from pynput.keyboard import Key, Controller
import time
import keyboard

pynputKeyBoard = Controller()
sleepCount = 0.025


def ComboSet():
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
    while True:

        ComboSet()

        if keyboard.is_pressed('p'):
            print('Paused the Bot!')
            break  # finishing the loop


def main():

    # Amount of time needed to click back into AQW
    time.sleep(1)

    ConstantRunning()

    while True:
        if keyboard.is_pressed('`'):
            print("Bot Resumed!")
            ConstantRunning()
        elif keyboard.is_pressed('q'):
            print("Bot Ended!")


main()
