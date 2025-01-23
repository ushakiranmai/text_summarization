# Text Summarization with Advanced Output Formats

This repository contains a Python-based text summarization project that uses the transformers library and a pre-trained distilbart-cnn-12-6 model to summarize long texts into concise outputs. The project supports various output formats, including plain text, JSON, HTML, CSV, Markdown, PDF, and Excel. The user interface is built using Gradio, enabling a seamless and interactive experience.

# Features

Summarizes large input texts by splitting them into manageable chunks.

Supports adjustable summary length (min and max length sliders).

Provides output in multiple formats:

Plain Text

JSON

HTML

CSV

Markdown

PDF

Excel

Simple and intuitive user interface built with Gradio.

# Requirements

To run this project, ensure you have the following dependencies installed:

Python 3.8 or higher

# Required libraries (specified in requirements.txt):

torch==2.0.1 -f https://download.pytorch.org/whl/torch_stable.html
transformers>=4.36.2,<5.0.0
diffusers>=0.25.0,<1.0.0
ctransformers>=0.2.27
pillow>=9.3.0,<10.0.0
gradio>=3.37.0,<4.0.0
streamlit<1.29.0
accelerate>=0.25.0,<1.0.0
pypdf>=3.0.0,<4.0.0
peft>=0.6.0,<1.0.0

# Installation

Clone this repository:

git clone https://github.com/yourusername/text-summarization-advanced.git
cd text-summarization-advanced

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies:

pip install -r requirements.txt

Usage

# Running the Application

Start the Gradio interface:

python app.py

Open your browser and navigate to the provided URL (usually http://127.0.0.1:7860).

Enter text in the input field, adjust summary length, and select the desired output format.

View or download the summarized content in the selected format.

Output Formats

Plain Text: Displays the summarized text directly.

JSON: Returns a JSON object with details about the summary.

HTML: Generates an HTML snippet containing the summary.

CSV: Produces a CSV format output with original and summarized text.

Markdown: Provides a Markdown-formatted summary.

PDF: Saves the summary as a PDF file.

Excel: Creates an Excel file with the original and summarized text.

# Project Structure

text-summarization-advanced/
├── app.py                 # Main application file
├── requirements.txt       # Dependency requirements
├── README.md              # Project documentation
├── summary.pdf            # Example output (if any)
├── summary.xlsx           # Example output (if any)
└── .gitignore             # Git ignore file

# Model Information

The summarization model used is sshleifer/distilbart-cnn-12-6, a lightweight version of BART fine-tuned on CNN/DailyMail dataset for abstractive summarization. The model is optimized with torch and integrated with transformers.

# Acknowledgments

Hugging Face for the Transformers library.

Gradio for providing an easy-to-use interface framework.

FPDF for PDF generation.

Pandas for data manipulation and Excel export.

# Contact

For any questions or feedback, please reach out to [pamuusha1974@gmail.com].
