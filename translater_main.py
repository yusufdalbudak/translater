import tkinter as tk 
from tkinter import filedialog
import PyPDF2
from deep_translator import GoogleTranslator
from fpdf import FPDF

# Function to split text into smaller chunks (under 5000 characters)
def split_text(text, max_length=5000):
    chunks = []
    while len(text) > max_length:
        split_point = text.rfind(' ', 0, max_length)  
        if split_point == -1:
            split_point = max_length
        chunks.append(text[:split_point])
        text = text[split_point:]
    chunks.append(text)  
    return chunks

# Function to extract text from PDF
def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to translate the extracted text in smaller chunks
def translate_text(text, dest_lang='tr'):
    translator = GoogleTranslator(target=dest_lang)
    text_chunks = split_text(text)
    translated_chunks = [translator.translate(chunk) for chunk in text_chunks]
    return ' '.join(translated_chunks)

# Function to save the translated text as a new PDF
def save_text_as_pdf(translated_text, output_pdf_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Add a Unicode-supported font (for this project ; DejaVuSans.ttf)
    pdf.add_font('DejaVu', '', './dejavu-sans/DejaVuSans.ttf', uni=True) 
    pdf.set_font('DejaVu', '', 12)
    
    pdf.multi_cell(0, 10, translated_text)
    pdf.output(output_pdf_path)

# Function to handle file selection and translation (Translates to Turkish)
def select_file_and_translate():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        text = pdf_to_text(pdf_path)
        translated_text = translate_text(text, 'tr')  
        output_pdf_path = pdf_path.replace(".pdf", "_translated.pdf")
        save_text_as_pdf(translated_text, output_pdf_path)
        result_label.config(text=f"Translation completed and saved as {output_pdf_path}")

# Create the GUI
root = tk.Tk()
root.title("PDF Translator")

# Button to select and translate PDF
select_button = tk.Button(root, text="Select PDF and Translate", command=select_file_and_translate)
select_button.pack(pady=20)

# Label to display the result message
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Set window size
root.geometry("400x200")
root.mainloop()
