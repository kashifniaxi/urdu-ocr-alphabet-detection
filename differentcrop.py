# import cv2
# import pandas as pd
# from PIL import Image
# import os

# def crop_and_save_words_with_contours(image_path, output_folder, labels_csv):
#     # Load the main image
#     img = cv2.imread(image_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Use adaptive thresholding
#     thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

#     # Find contours
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Debug: Check number of contours found
#     print(f"Number of contours found: {len(contours)}")

#     # Read labels from CSV
#     labels_df = pd.read_csv(labels_csv, header=None)
#     labels = labels_df[0].tolist()

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     label_index = 0

#     # Sort contours from top to bottom and left to right
#     contours = sorted(contours, key=lambda ctr: (cv2.boundingRect(ctr)[1], cv2.boundingRect(ctr)[0]))

#     for contour in contours:
#         if label_index >= len(labels):
#             break

#         # Get bounding box for each contour
#         x, y, w, h = cv2.boundingRect(contour)
        
#         # Filter out small contours that might be noise
#         if w < 50 or h < 50:
#             continue

#         # Add padding to the bounding box
#         padding = 10
#         x = max(x - padding, 0)
#         y = max(y - padding, 0)
#         w = min(w + 2 * padding, img.shape[1] - x)
#         h = min(h + 2 * padding, img.shape[0] - y)
        
#         # Debug: Print coordinates and size of bounding box
#         print(f"Contour {label_index + 1}: x={x}, y={y}, w={w}, h={h}")

#         # Crop the word from the image
#         word_img = img[y:y+h, x:x+w]
#         word_img_pil = Image.fromarray(cv2.cvtColor(word_img, cv2.COLOR_BGR2RGB))

#         # Save the cropped word image with the label from CSV
#         word_label = labels[label_index]
#         output_path = os.path.join(output_folder, f"{word_label}.png")
#         word_img_pil.save(output_path)
        
#         # Debug: Confirm the file was saved
#         if os.path.exists(output_path):
#             print(f"Saved: {output_path}")
#         else:
#             print(f"Failed to save: {output_path}")
        
#         label_index += 1

# if __name__ == "__main__":
#     image_path = r"C:\Users\Hp\Downloads\ML_sample_project\output\page_1.png"  # Replace with your image path
#     output_folder = r"C:\Users\Hp\Downloads\ML_sample_project\output"  # Replace with your desired output folder
#     labels_csv = r"C:\Users\Hp\Downloads\ML_sample_project\labels.csv"
#     crop_and_save_words_with_contours(image_path, output_folder, labels_csv)





import cv2
import pandas as pd
from PIL import Image
import os

def crop_and_save_words_with_contours(image_path, output_folder, labels_csv, page_number):
    # Load the main image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply morphological operations to enhance text regions
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph_img = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(morph_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Read labels from CSV
    labels_df = pd.read_csv(labels_csv, header=None)
    labels = labels_df[0].tolist()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    label_index = 0

    # Sort contours from top to bottom and left to right
    contours = sorted(contours, key=lambda ctr: (cv2.boundingRect(ctr)[1], cv2.boundingRect(ctr)[0]))

    for contour in contours:
        if label_index >= len(labels):
            break

        # Get bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)

        # Filter out contours that are too small or too large
        if w < 30 or h < 30 or w > img.shape[1] // 2:
            continue

        # Add padding to the bounding box
        padding = 10
        x = max(x - padding, 0)
        y = max(y - padding, 0)
        w = min(w + 2 * padding, img.shape[1] - x)
        h = min(h + 2 * padding, img.shape[0] - y)

        # Debug: Print coordinates and size of bounding box
        print(f"Page {page_number}, Contour {label_index + 1}: x={x}, y={y}, w={w}, h={h}")

        # Crop the word from the image
        word_img = img[y:y+h, x:x+w]
        word_img_pil = Image.fromarray(cv2.cvtColor(word_img, cv2.COLOR_BGR2RGB))

        # Save the cropped word image with a unique filename using page number and label
        word_label = labels[label_index]
        output_path = os.path.join(output_folder, f"page_{page_number}_word_{label_index + 1}.png")
        word_img_pil.save(output_path)

        # Debug: Confirm the file was saved
        if os.path.exists(output_path):
            print(f"Saved: {output_path}")
        else:
            print(f"Failed to save: {output_path}")

        label_index += 1

if __name__ == "__main__":
    for i in range(1, 5):
        image_path = r"C:\Users\Hp\Desktop\ml pro\output\page_{i}.png"  # Replace with your image path using f-string
        output_folder = r"C:\Users\Hp\Desktop\ml pro\output"  # Replace with your desired output folder
        labels_csv = r"C:\Users\Hp\Desktop\ml pro\labels.csv"
        crop_and_save_words_with_contours(image_path, output_folder, labels_csv, i)
