from typing import List
import re
from klpt.preprocess import Preprocess
from klpt.tokenize import Tokenize
import docx
import os
def read_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)
def read_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
def read_input_file(file_path: str) -> str:
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.docx':
        return read_docx(file_path)
    elif file_extension == '.txt':
        return read_txt(file_path)
    else:
        raise ValueError("Unsupported file format. Use .txt or .docx")
def convert_numbers_to_kurdish(text: str) -> str:
    number_map = {
        '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
        '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
    }
    for eng, kurd in number_map.items():
        text = text.replace(eng, kurd)
    return text
def remove_english(text: str) -> str:
    text = re.sub(r'[a-zA-Z]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
def process_text(text: str) -> str:
    preprocessor = Preprocess()
    tokenizer = Tokenize()

    text = convert_numbers_to_kurdish(text)
    text = remove_english(text)
    text = preprocessor.preprocess(text)
    sentences = tokenizer.tokenize_sentences(text)

    output_lines = []
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            output_lines.append(f"{word} O")
        output_lines.append(". O")  # Add end of sentence marker
        output_lines.append("")  # Empty line between sentences

    return "\n".join(output_lines)
def main():
    # Input and output file paths
    input_file = "input.txt"  # or "input.docx"
    output_file = "output.txt"

    # Read input file
    try:
        input_text = read_input_file(input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Process text
    processed_text = process_text(input_text)

    # Save output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_text)
        print(f"Successfully processed and saved to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")
if name == "main":
    main()