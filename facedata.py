import cv2
import os
import tkinter as tk
from tkinter import Entry, Button
import winsound

click_sound_path = "click.wav"

def play_click_sound():
    winsound.PlaySound(click_sound_path, winsound.SND_FILENAME)

def capture_images(name):
    # Create a VideoCapture object to access the camera
    cap = cv2.VideoCapture(0)
    os.mkdir(f"./faces/{name}")
    # Initialize the font and text parameters
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 0, 255)  # Red color
    font_thickness = 2

    facial_dim = ["Front", "Side-Left", "Side-Right", "Down", "Up"]
    for face in facial_dim:
        countdown_duration = 5
        while countdown_duration > 0:
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read a frame from the camera.")
                break

            # Display the countdown on the image
            countdown_text = f"Capturing {face} in {countdown_duration}"
            text_size, _ = cv2.getTextSize(countdown_text, font, font_scale, font_thickness)
            text_x = (frame.shape[1] - text_size[0]) // 2
            text_y = (frame.shape[0] + text_size[1]) // 2
            cv2.putText(frame, countdown_text, (text_x, text_y), font, font_scale, font_color, font_thickness)

            cv2.imshow("Countdown Timer", frame)
            cv2.waitKey(1000)  # Delay for 1 second
            countdown_duration -= 1
        play_click_sound()
        # Capture an image after the countdown
        ret, image = cap.read()

        if ret:
            cv2.imwrite(f"./faces/{name}/{name}_{face}.png", image)
            print(f"Image captured and saved as {name}_{face}.png")
        else:
            print("Error: Could not capture an image.")

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def submit_name():
    name = name_entry.get()
    capture_images(name)
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("Face Image Capture")
window.geometry(800,800)
# Create and place GUI elements
name_label = tk.Label(window, text="Enter your name:")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()
submit_button = Button(window, text="Submit", command=submit_name)
submit_button.pack()

# Start the GUI main loop
window.mainloop()
