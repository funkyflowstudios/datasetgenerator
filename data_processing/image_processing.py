from PIL import Image
import numpy as np

def process_image(image_path: str, size: tuple = (224, 224)) -> np.ndarray:
    """
    Process an image by resizing it and converting it to a numpy array.

    Args:
        image_path (str): Path to the image file.
        size (tuple): Desired size for the output image. Defaults to (224, 224).

    Returns:
        np.ndarray: Processed image as a numpy array.

    Raises:
        FileNotFoundError: If the specified image file does not exist.
        ValueError: If the image cannot be opened or processed.
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)
            img_array = np.array(img) / 255.0  # Normalize pixel values
            return img_array
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {image_path}")
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")

# Example usage
if __name__ == "__main__":
    try:
        sample_image_path = "path/to/your/image.jpg"  # Replace with an actual image path
        processed_image = process_image(sample_image_path)
        print(f"Processed image shape: {processed_image.shape}")
        print(f"Pixel value range: {processed_image.min()} to {processed_image.max()}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")