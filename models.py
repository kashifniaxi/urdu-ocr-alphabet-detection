import cv2
import os

def apply_morphological_operations(image_folder):
    # Define the 3x3 kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Iterate over each image in the folder
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load the image
            img_path = os.path.join(image_folder, filename)
            img = cv2.imread(img_path)

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply morphological operations to enhance text regions
            morph_img = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

            # Apply erosion and dilation
            morph_img_eroded = cv2.erode(morph_img, kernel, iterations=1)
            morph_img_dilated = cv2.dilate(morph_img, kernel, iterations=1)

            # Save or display results as needed
            # Example: Save eroded and dilated images
            output_folder = "output_folder"
            os.makedirs(output_folder, exist_ok=True)

            cv2.imwrite(os.path.join(output_folder, f"{filename}_eroded.jpg"), morph_img_eroded)
            cv2.imwrite(os.path.join(output_folder, f"{filename}_dilated.jpg"), morph_img_dilated)

            # Alternatively, display images (optional)
            # cv2.imshow("Eroded Image", morph_img_eroded)
            # cv2.imshow("Dilated Image", morph_img_dilated)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

if __name__ == "__main__":
    image_folder =  r"C:\Users\Hp\Desktop\ml pro\output"
    apply_morphological_operations(image_folder)
