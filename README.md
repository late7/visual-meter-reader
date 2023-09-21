## Needle Meter Pointer Detection
This repository contains a Python script to process and analyze images of pressure meters. The primary goal is to detect the position of the pointer (or needle) and determine its angle relative to the vertical axis. Additionally, the script identifies whether the pointer is on the left or right side of the meter.
Detection process is implemented using substraction of image containin measurement and image without needle, meter backgroud only. Therefore, you need to provide this type of image as reference.

![Reference Image](/../main/reference_image.png) - ![Meterted](/../main/data/metersample1.png) => ![Result](/../main/substracted.png) 


# Prerequisites
Python 3.10 <br>
opencv-python ( OpenCV Python library )  <br>
matplot <br>
numpy , which you most likely have already numpy already installed :-)<br>

You can install the required packages using:

> pip install opencv-python <br>
> pip install matplotlib <br>
> pip install numpy <br>

NOTE: For Linux you might need also:<br>
> sudo apt install libgl1-mesa-glx

# Usage
> git clone https://github.com/late7/visual-meter-reader.git

Image Preparation: Ensure you have two images:

A reference image of the meter without the pointer. (Might need to edit with Gimp or similar, Clone Tool in Gimp is handy :-)
An actual image of the meter with the pointer in position.

Run the Script: Execute the script, providing the paths to the reference and actual images

python pointer_detection.py --reference reference_image.png --actual data/metersample1.png --zeropoint 44 --scale 2.3 --showimage True

Results: The script will display the processed image with the detected pointer and its angle relative to the vertical axis. It will also print whether the pointer is on the left or right side of the meter.

# Tuning
Adjust zero position of the meter by giving '--zeropoint' and '--scale' parameters i.e. ratio in which the units match with needle angle.
If the script isn't detecting the pointer accurately, you may need to adjust parameters related to the Hough Line Transform. This can be done within the detect_line_and_angle function in the script.

# Contributions
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions, whether it's refining the code or enhancing documentation, are always welcome!
