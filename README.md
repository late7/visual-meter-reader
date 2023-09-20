## Pressure Meter Pointer Detection
This repository contains a Python script to process and analyze images of pressure meters. The primary goal is to detect the position of the pointer (or needle) and determine its angle relative to the vertical axis. Additionally, the script identifies whether the pointer is on the left or right side of the meter.

#Prerequisites
Python 3.x
OpenCV (opencv-python)
You can install the required packages using:

bash
pip install opencv-python

#Usage
Image Preparation: Ensure you have two images:

A reference image of the meter without the pointer. (Might need to edit with Gimp or similar, Clone Tool is handy :-)
An actual image of the meter with the pointer in position.
Run the Script: Execute the script, providing the paths to the reference and actual images.

python pointer_detection.py --reference path_to_reference_image.png --actual path_to_actual_image.png
Results: The script will display the processed image with the detected pointer and its angle relative to the vertical axis. It will also print whether the pointer is on the left or right side of the meter.
Tuning
If the script isn't detecting the pointer accurately, you may need to adjust parameters related to the Hough Line Transform. This can be done within the detect_line_and_angle function in the script.

Contributions
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions, whether it's refining the code or enhancing documentation, are always welcome!
