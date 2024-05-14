import keras_ocr
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import cv2

from ocr import ImageSelection


def SPOR(image_path):
    # Create an instance of ImageSelection
    selection = ImageSelection(image_path)

    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Create a window to display the image and handle mouse events
    cv2.namedWindow("Select ROI")
    cv2.setMouseCallback("Select ROI", selection.on_mouse_down)

    while not selection.selection_complete:
        # Display the image
        cv2.imshow("Select ROI", image)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    if selection.selection_complete:
        # Load the full image
        full_image = cv2.imread(image_path)

        # Select the region of interest based on the user's selection
        roi = full_image[selection.top_left[1]:selection.bottom_right[1],
              selection.top_left[0]:selection.bottom_right[0]]

        # Preprocess the selected region
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Use Keras OCR to recognize text
        pipeline = keras_ocr.pipeline.Pipeline()
        prediction_groups = pipeline.recognize([processed_image])

        # Extract text predictions
        predictions = prediction_groups[0]

        # Combine the recognized text into a single string
        text = ' '.join([text for text, box in predictions])

        # Clear previous text
        text_box.delete("1.0", tk.END)

        # Insert extracted text into the text box
        text_box.insert(tk.END, text)
