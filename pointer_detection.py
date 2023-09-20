import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def subtract_images(image1_path, image2_path):
    # Load the images
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    # Ensure both images are of the same size
    if img1.shape != img2.shape:
        raise ValueError("Both images should have the same dimensions.")
    
    # Subtract the images
    diff = cv2.absdiff(img1, img2)
    
    # Apply a threshold to enhance the needle
    _, threshed = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    return threshed

def detect_line_and_angle(image, zeropoint, showimage):
    # Use Probabilistic Hough Line Transform to detect the needle
    lines = cv2.HoughLinesP(image, 1, np.pi / 180, threshold=10, minLineLength=30, maxLineGap=5)
    
    if lines is not None:
        # For simplicity, we'll just take the first detected line. You can iterate over all if needed.
        x1, y1, x2, y2 = lines[0][0]
        
        # Draw the detected line on the image
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        # Calculate the angle with respect to the vertical axis
        angle_rad = np.arctan2(y2 - y1, x2 - x1)
        angle_deg = np.degrees(angle_rad) + float(zeropoint)

        # Calculate the midpoint of the detected line
        midpoint_x = (x1 + x2) / 2

        # Determine if the needle is on the left or right side
        image_midpoint_x = image.shape[1] / 2
        if midpoint_x < image_midpoint_x:
            position = "left"
        else:
            position = "right"
            angle_deg += 180  # For regular SouthWest starting meters this is needed.

        if showimage == "True":
            plt.imshow(image, cmap='gray')
            plt.title(f'Detected Needle with Angle: {angle_deg:.2f} degrees on {position} of image')
            plt.show()

        return angle_deg
    else:
        print("No line detected!")
        return None

def main(reference_image_path, actual_image_path, zeropoint, scale, showimage):
    result = subtract_images(reference_image_path, actual_image_path)
    value = detect_line_and_angle(result, zeropoint, showimage) / float(scale)

    if value is not None:
        print(f"Meter value: {value:.2f} ")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect the position and angle of a meter's pointer.")
    parser.add_argument('--reference', required=True, help='Path to the reference image (meter without the pointer).')
    parser.add_argument('--actual', required=True, help='Path to the actual image (meter with the pointer).')
    parser.add_argument('--zeropoint', required=True, help='Correction value for calibrating meter zero point. (basic SW meters try: 45)')
    parser.add_argument('--scale', required=True, help='Scaling value to match scale of the meter. (start with: 2.3)')
    parser.add_argument('--showimage', required=True, help='Show processed images. (True/False)')

    args = parser.parse_args()

    main(args.reference, args.actual, args.zeropoint, args.scale, args.showimage)
