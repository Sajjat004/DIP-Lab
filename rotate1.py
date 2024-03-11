import cv2

def rotate_image(image_path, angle):
  """
  Rotates an image by a specified angle in degrees clockwise.

  Args:
      image_path: Path to the image file.
      angle: Rotation angle in degrees (clockwise).

  Returns:
      The rotated image as a NumPy array.
  """

  # Read the image
  image = cv2.imread(image_path)

  # Get image dimensions (height and width)
  (h, w) = image.shape[:2]

  # Calculate the center of the image
  center = (w // 2, h // 2)

  # Create the rotation matrix for the specified angle
  rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

  # Rotate the image using affine transformation
  rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

  return rotated_image

# Example usage
image_path = "path/to/your/image.jpg"  # Replace with your image path
angle = 33  # Rotation angle in degrees (clockwise)

rotated_image = rotate_image(image_path, angle)

# Display the original and rotated images (optional)
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the rotated image (optional)
cv2.imwrite("rotated_image.jpg", rotated_image)
