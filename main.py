import pyautogui as p
import time
import math


VIDEO_URL = "https://app.ofppt-langues.ma/platform/#/discover/VOCABULARY/HOUSE_HOME/lesson/FR_FR_B1_VOCABULARY_ACHETER_UNE_MAISON_AVEC_UNE_AGENCE_IMMOBILIERE/activity/FR_FR_B1_VOCABULARY_ACHETER_UNE_MAISON_AVEC_UNE_AGENCE_IMMOBILIERE_VIDEO_PARTIE_1_ANIMATION/video"

SCREEN_SIZE = p.size()


def main():
    # Script Start.
    print(
        "Make sure you have PYAUTOGUI installed, and running this script as recommended."
    )
    print(
        "Make sure you are already logged in with your account, this script does not handle authentication for security reasons."
    )
    print(
        "You have 10 sec before the script start executing, from now on don't touch your mouse and keyboard."
    )

    for i in range(10, 0, -1):
        time.sleep(1)
        print(f"Script starts in: {i}")

    # Open Firefox.
    print("Opening Firefox.")
    p.hotkey("win")
    p.typewrite(("firefox"))
    p.press("enter")

    time.sleep(10)

    # Open Video URL.
    print("Opening Video URL.")
    p.hotkey("ctrl", "t")
    p.typewrite(VIDEO_URL)
    p.press("enter")

    time.sleep(10)

    # Play the Video.
    print("Playing the Video.")
    p.moveTo(math.floor(SCREEN_SIZE[0] / 2), math.floor(SCREEN_SIZE[1] / 2))
    p.click()

    iter = 0
    while True:

        time.sleep(10)
        p.press("left")

        print(f"Iteration number: {iter}")
        iter += 1


if __name__ == "__main__":
    main()
