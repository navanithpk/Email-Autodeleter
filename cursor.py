import pyautogui
import time
import keyboard
import threading  # Import the threading module


# Example usage:

# Run the script, alt+tab into the browser window.
# Place the cursor on the 'Select all' button and press'n' key to capture its coordinates.
# Place the cursor on the 'Delete' button and press 'n' to capture its coordinates.
# Now alt-tab back into the IDE, and replace the point1 and point2 variables with the select and delete coordinates.
# Re-run the script, and alt-tab back into the browser window and press 'p' to start the deletion.

# Change the duration parameter in move_between_points() in order to make the cursor move slower or fatser.
# Use the mouse to take the cursor to the top right corner to break out of the script.


def print_coordinates():
    while True:
        if keyboard.is_pressed('n'):
            x, y = pyautogui.position()
            print(f"Current Mouse Position - X: {x}, Y: {y}")
            time.sleep(0.2)


def move_between_points(point1, point2, clicks=1):
    for _n in range(clicks):
        pyautogui.moveTo(point1[0], point1[1], duration=1)
        pyautogui.click()
        pyautogui.moveTo(point2[0], point2[1], duration=1)
        pyautogui.click()


# Example usage

point1 = (437, 287)
point2 = (628, 293)

print_coordinates_thread = threading.Thread(target=print_coordinates)
print_coordinates_thread.start()

while True:
    if keyboard.is_pressed('p'):
        for m in range(500):
            move_between_points(point1, point2)
            m += 1
