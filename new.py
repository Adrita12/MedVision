import cv2
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from PIL import Image, ImageTk
import pytesseract as tess
import sys


def listen_to_me():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        say("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=7)
        try:
            text = recognizer.recognize_google(audio)
            print("USER:", text)
            return text
        except sr.UnknownValueError:
            say("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def ocr_image(image_path):
    img = Image.open(image_path)
    tet = tess.image_to_string(img)
    return tet


def capture_image():
    while True:  # Loop until the scanned medicine matches the expected one
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            say("Error: Could not open camera.")
            return None

        ret, frame = cap.read()
        if not ret:
            say("Error: Could not read frame.")
            return None

        cv2.imwrite('captured_image.jpg', frame)
        cap.release()

        image = Image.open('captured_image.jpg')
        image = ImageTk.PhotoImage(image)

        image_label.config(image=image)
        image_label.image = image

        say("Picture captured")
        ocr_result = ocr_image('captured_image.jpg')
        say(ocr_result)
        text_label.config(text="Extracted Text: " + ocr_result)

        if ocr_result:
            if sys.argv[1].lower() in ocr_result.lower():  # Check if medicine name is present in OCR result
                say("Scanned medicine matches the triggered alarm.")
                return ocr_result
            else:
                say("Scanned medicine does not match the triggered alarm. Scanning again.")
                continue  # Restart the loop to capture another image
        # else:
        #     say("Could not extract text from the image. Scanning again.")
        #     continue  # Restart the loop to capture another image


def start_listening():
    text = listen_to_me()
    if text and "camera" in text:
        say(text)
        capture_image()


root = tk.Tk()
root.title("OCR Application")
root.configure(background='#FAF9F6')

top_frame = tk.Frame(root, background='#F0F0F0')
top_frame.pack(side=tk.TOP)
bottom_frame = tk.Frame(root, background='#F0F0F0')
bottom_frame.pack(side=tk.BOTTOM)

title_label = tk.Label(top_frame, text="⚕️MedVision⚕️", font=("Helvetica", 24), background='#F0F0F0')
title_label.pack()

text_label = tk.Label(bottom_frame, text="Extracted Text: ", font=("Helvetica", 14), background='#F0F0F0')
text_label.pack()

image_label = tk.Label(bottom_frame, background='#FFFFFF')
image_label.pack()

listen_button = tk.Button(bottom_frame, text="     🎙️", font=("Helvetica", 362), command=start_listening, background='#4CAF50', foreground='#FFFFFF', width=200, height=30)
listen_button.pack(pady=(50, 100))

root.mainloop()
