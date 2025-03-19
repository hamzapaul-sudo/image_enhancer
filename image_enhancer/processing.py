from rembg import remove
import cv2


def remove_background(input_path: str, output_path: str):
    """Removes the background from an image."""
    with open(input_path, "rb") as file:
        input_image = file.read()

    result = remove(input_image)

    with open(output_path, "wb") as out_file:
        out_file.write(result)

    return output_path


def enhance_image(input_path: str, output_path: str):
    """Enhances brightness and contrast of an image."""
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError("Invalid image file.")

    # Apply contrast and brightness adjustments
    alpha = 1.2  # Contrast
    beta = 30  # Brightness
    enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    cv2.imwrite(output_path, enhanced)
    return output_path
