import os
import numpy as np
from PIL import Image, ImageFilter

def apply_erosion_and_dilation(image_path, output_folder, kernel_size=(4, 4)):
    # Read the grayscale image
    img = Image.open(image_path).convert('L')
    
    # Define the kernel for erosion and dilation
    kernel = np.ones(kernel_size, dtype=np.uint8)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Define the erosion function
    def erode(image, kernel):
        return Image.fromarray(image).filter(ImageFilter.MinFilter(kernel_size[0]))
    
    # Define the dilation function
    def dilate(image, kernel):
        return Image.fromarray(image).filter(ImageFilter.MaxFilter(kernel_size[0]))
    
    # Apply erosion
    eroded_img = erode(img_array, kernel)
    
    # Apply dilation
    dilated_img = dilate(img_array, kernel)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Save the processed images
    base_filename = os.path.basename(image_path)
    filename, ext = os.path.splitext(base_filename)
    
    eroded_output_path = os.path.join(output_folder, f"{filename}_eroded{ext}")
    dilated_output_path = os.path.join(output_folder, f"{filename}_dilated{ext}")
    
    eroded_img.save(eroded_output_path)
    dilated_img.save(dilated_output_path)

# Example usage
if __name__ == "__main__":
    image_folder = r"C:\Users\Hp\Desktop\ml pro\output_folder"  # Replace with your image folder path
    output_folder = r"C:\Users\Hp\Desktop\ml pro\processed_images"  # Replace with your desired output folder
    
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            apply_erosion_and_dilation(image_path, output_folder)
