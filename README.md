# Urdu OCR Alphabet Detection

This project focuses on the classification of Urdu text using Optical Character Recognition (OCR) techniques. The aim is to detect Urdu alphabets and classify words starting, containing, or ending with specific characters.

## Table of Contents
- [Project Description](#project-description)
- [Learning Outcomes](#learning-outcomes)
- [Data Generation](#data-generation)
- [Augmentation Techniques](#augmentation-techniques)
- [Classifier](#classifier)
- [Results and Analysis](#results-and-analysis)
- [Running the Project from GitHub](#running-the-project-from-github)
- [Dependencies](#dependencies)
- [Project Worth](#project-worth)
- [Conclusion](#conclusion)
- [Future Enhancements](#future-enhancements)

## Project Description
Data generation and architecture design for the classification of Urdu text. Words are created with 1 to 5 characters. For example, a 5-character word uses a start character, 3 mid characters, and an end character. The project addresses challenges in Urdu OCR, including ligature complexity and noise robustness.

## Learning Outcomes
- Understanding data generation for OCR tasks.
- Designing and modifying machine learning architectures for improved performance.

## Data Generation
### 1. Datasets
- Downloaded existing Urdu OCR datasets.
- Generated custom datasets using Python scripts and MS Word.

### 2. Character Selection
- Focused on primary ligatures to reduce classes.
- Selected 1 of 14 characters from the 'Start' column.

### 3. Word Generation
- Words consist of 1 to 5 characters.
- For 5-character words: `Start character + 3 mid characters + End character`.

### 4. Formatting
- Page size: A4
- Margins: Narrow (0.5” on all sides)
- Columns: 4
- Line spacing: Single

### 5. File Naming Convention
- Format: `index_start_index_mid1_index_mid2_index_mid3_index_end_augmentation`
- Example: `03_27_31_14_none` for the word **قمر**.

## Augmentation Techniques
Enhanced the dataset using image processing techniques:
1. **Erosion and Dilation**:
   - Applied via `AugmentedScript.py` and `models.py` using PIL and OpenCV.
   - **Erosion**: Shrinks text regions.
   - **Dilation**: Expands text regions.
2. **Other Techniques**:
   - Rotation
   - Shearing

## Classifier
1. **State-of-the-Art Method**:
   - Implemented latest Urdu OCR methodology from recent literature.
2. **Proposed Modifications**:
   - Enhanced morphological operations.
   - Added noise to test datasets for robustness evaluation.
3. **Code**:
   - Model implementation in `models.py`.

## Results and Analysis
1. **Noise Testing**:
   - Introduced varying noise levels to test data.
   - Analyzed performance degradation and proposed solutions.
2. **Findings**:
   - Performance impacted by noisy data.
   - Suggested advanced denoising techniques and robust architectures.

## Running the Project from GitHub

### Clone the Repository
```bash
git clone https://github.com/yourusername/urdu-ocr-alphabet-detection.git
cd urdu-ocr-alphabet-detection
```



## Install Dependencies
pip install -r requirements.txt
## How to Run
#### 1. Data Generation:
python ImageGeneratingScript.py
#### 2.Data Augmentation:
python AugmentedScript.py
#### 3.Model Training and Testing:
python models.py
## Dependencies
Python 3.x

numpy

Pillow

opencv-python

python-docx
## Project Worth

This project addresses the complexities of Urdu text recognition, a language with intricate ligatures. By generating robust datasets and applying state-of-the-art OCR techniques, it advances multilingual text recognition. The methodologies can be adapted to other complex scripts, broadening OCR research impact.
## Conclusion

The project demonstrates practical ML applications for Urdu OCR. Through data generation, augmentation, and classifier optimization, we achieved reliable character detection. Challenges from noisy data were addressed with proposed solutions, paving the way for future enhancements
## Future Enhancements

Multilingual Support: Extend to Persian, Arabic, etc.

Real-Time OCR: Develop for mobile/web apps.

Deep Learning Models: Integrate CNNs and Transformers.

Dataset Expansion: Include diverse handwriting/printed samples.

Noise Robustness: Implement advanced noise reduction techniques
