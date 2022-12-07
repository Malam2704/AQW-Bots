from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
sleepCount = 1


def main():

    while True:
        time.sleep(sleepCount)
        keyboard.press("4")
        keyboard.release("4")

        time.sleep(sleepCount)
        keyboard.press("5")
        keyboard.release("5")

        time.sleep(sleepCount)
        keyboard.press("2")
        keyboard.release("2")

        time.sleep(sleepCount)
        keyboard.press("3")
        keyboard.release("3")


main()
