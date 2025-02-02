import pandas as pd
from PIL import Image

def crop_and_save_words(image_path, output_folder, labels_csv):
    img = Image.open(image_path)
    
    # Read labels from CSV
    labels_df = pd.read_csv(labels_csv, header=None)
    labels = labels_df[0].tolist()  
    # Dimensions and spacing based on the document's structure
    word_width = 400  # Example width of each word
    line_height = 230  # Example height of each line
    margin_left = 100  # Example left margi
    margin_top = 100   # Example top margin
    spaces_between_words = 5 # Example space width between words
    
    label_index = 0
    for line in range(15):
        # Calculate vertical position of the line
        line_top = margin_top + line * line_height
        line_bottom = line_top + line_height
        
        # Loop through each word (4 words per line)
        for word_index in range(4):
            if label_index < len(labels):
                # Calculate horizontal position of the word
                word_left = margin_left + word_index * (word_width + spaces_between_words)
                word_right = word_left + word_width
                
                # Crop the word using calculated coordinates
                word_img = img.crop((word_left, line_top, word_right, line_bottom))
                
                # Save the cropped word image with the label from CSV
                word_label = labels[label_index]
                word_img.save(f"{output_folder}/{word_label}.png")
                
                label_index += 1

if __name__ == "__main__":
    image_path = r"C:\Users\Hp\Desktop\ml pro\Images\urdu_words_page-0001.jpg"  # Replace with your image path
    output_folder = r"C:\Users\Hp\Desktop\ml pro\output"  # Replace with your desired output folder
    labels_csv = r".\labels.csv"
    crop_and_save_words(image_path, output_folder,labels_csv)


