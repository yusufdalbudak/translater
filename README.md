# PDF Translator

This Python project is a GUI-based application that allows users to select a PDF file, extract its text, translate the text into another language (Turkish by default), and save the translated text as a new PDF file. The project uses `tkinter` for the GUI, `PyPDF2` for PDF text extraction, `deep_translator` for translation, and `FPDF` for generating the translated PDF file.

## Features

- **PDF Text Extraction:** Extracts text from a user-selected PDF file.
- **Translation:** Translates the extracted text into Turkish (default).
- **Save as PDF:** Saves the translated text as a new PDF file.
- **Graphical User Interface (GUI):** User-friendly interface to select files and display results.

## Installation

### Requirements

Before running the project, you will need to install the following dependencies:

1. **Python 3.x**
2. Install the required Python libraries:
    - `tkinter`: Standard Python library for building GUIs.
    - `PyPDF2`: A library for reading and extracting text from PDF files.
    - `deep_translator`: A library for translating text using Google Translate.
    - `FPDF`: A library for generating PDF files.

To install the required packages, run the following command:

```bash
pip install PyPDF2 deep-translator fpdf



If tkinter is not included in your Python installation, you may need to install it separately:

On Windows, tkinter should come pre-installed with Python.
On Linux, you can install tkinter using your package manager:

sudo apt-get install python3-tk


### Downloading the Font

This project uses the **DejaVuSans** font, which supports Unicode characters for displaying text in multiple languages.

1. You can download the DejaVuSans font from [FontSquirrel](https://www.fontsquirrel.com/fonts/dejavu-sans).
2. Once downloaded, place the `DejaVuSans.ttf` file in a folder named `dejavu-sans` inside the project directory.
3. Ensure that the relative path to the font in the script is correct:
   ```python
   pdf.add_font('DejaVu', '', './dejavu-sans/DejaVuSans.ttf', uni=True)


This addition provides a direct link for users to download the necessary font files from FontSquirrel.

Translation:

The application will extract text from the selected PDF and translate it into Turkish.
The translated text will then be saved as a new PDF file in the same directory as the original, with _translated appended to the filename.

# File Structure
.
├── dejavu-sans/
│   ├── DejaVuSans.ttf
│   ├── DejaVuSans-Bold.ttf
│   └── (other font variations, optional)
├── translater_main.py    # Main Python script for the project
├── README.md             # This README file


# Dependencies
Python 3.x
tkinter: GUI library.
PyPDF2: PDF reading and text extraction.
deep_translator: Translation API for translating text.
FPDF: PDF generation and text insertion.




# USAGE
python translater_main.py


