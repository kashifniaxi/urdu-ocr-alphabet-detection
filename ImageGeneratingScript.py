import itertools
import docx
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn  # Correctly importing the namespace qualifier
import csv

# Single start character
start_char = 'ع'
mid_chars = ['ب', 'ج', 'س', 'ص', 'ط', 'ع', 'ف', 'ق', 'ک', 'ل', 'م', 'ن', 'ہ', 'ی']
end_chars = ['ا', 'ب', 'ج', 'د', 'ر', 'س', 'ص', 'ط', 'ع', 'ف', 'ق', 'ک', 'ل', 'م', 'ن', 'و', 'ہ', 'ی', 'ے']
urdu_alphabets = [
    'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ہ', 'ء', 'ی', 'ے'
]

# Creating a character-to-index mapping
character_to_index = {char: i + 1 for i, char in enumerate(urdu_alphabets)}

def generate_urdu_words():
    indexed_words = []
    length = 5  # Fixed length of the words to generate

    for e in end_chars:
        for combination in itertools.product(mid_chars, repeat=length-2):
            word = start_char + ''.join(combination) + e
            indexes = [character_to_index[start_char]] + [character_to_index[c] for c in combination] + [character_to_index[e]]
            indexed_name = "_".join(f"{idx:02}" for idx in indexes)
            indexed_words.append((word, indexed_name))
    
    return indexed_words

def create_word_document(filename, indexed_words):
    print("Creating Word document...")
    doc = docx.Document()
    section = doc.sections[0]
    section.page_height = Inches(18.7)  # A4 height
    section.page_width = Inches(8.3)  # A4 width
    section.top_margin = Inches(1.5)
    section.bottom_margin = Inches(1.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.orientation = WD_ORIENT.PORTRAIT
    
    cols = section._sectPr.xpath('./w:cols')[0]
    cols.set(qn('w:num'), '4')  # Setting 4 columns
    
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Noori Nastaleeq'
    font.size = Pt(36)  # Updated font size to 36
    style.paragraph_format.line_spacing = Pt(36)  # Updated line spacing to match font size

    for word, _ in indexed_words:
        doc.add_paragraph(word, style='Normal').alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
    
    doc.save(filename)
    print(f"Word document '{filename}' created.")

def create_csv_file(filename, indexed_words):
    print("Creating CSV file...")
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for _, name in indexed_words:
            csvwriter.writerow([name])
    print(f"CSV file '{filename}' created.")

# Generate words and save them
indexed_words = generate_urdu_words()
create_word_document('urdu_words.docx', indexed_words)
create_csv_file('labels.csv', indexed_words)
