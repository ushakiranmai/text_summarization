import gradio as gr
from transformers import pipeline
import torch
from fpdf import FPDF
import pandas as pd
import json
import csv

# Load the summarization pipeline
text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.float32)

def chunk_text(input_text, max_chunk_size=1024):
    """
    Splits the input text into smaller chunks of size `max_chunk_size` or smaller.
    """
    words = input_text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(" ".join(current_chunk + [word])) <= max_chunk_size:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

def summary(input_text, max_length=130, min_length=30, output_format="Plain Text"):
    """
    Summarizes the input text, handling cases where the text exceeds the model's maximum sequence length.
    Supports different output formats (Plain Text, JSON, HTML, CSV, Markdown, PDF, Excel).
    """
    chunks = chunk_text(input_text)
    summarized_chunks = []

    for chunk in chunks:
        output = text_summary(chunk, max_length=max_length, min_length=min_length)
        summarized_chunks.append(output[0]['summary_text'])

    summary_text = " ".join(summarized_chunks)
    
    # Return the output in the selected format
    if output_format == "Plain Text":
        return summary_text
    
    elif output_format == "JSON":
        result = {
            "summary": summary_text,
            "chunk_count": len(chunks),
            "original_length": len(input_text.split()),
            "summary_length": len(summary_text.split())
        }
        return json.dumps(result, indent=4)
    
    elif output_format == "HTML":
        html_output = f"<html><body><h2>Summary</h2><p>{summary_text}</p></body></html>"
        return html_output
    
    elif output_format == "CSV":
        csv_output = "Original Text, Summary\n"
        for chunk, summary in zip(chunks, summarized_chunks):
            csv_output += f'"{chunk}", "{summary}"\n'
        return csv_output
    
    elif output_format == "Markdown":
        markdown_output = f"## Summary\n\n{summary_text}"
        return markdown_output

    elif output_format == "PDF":
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, summary_text)
        pdf_output = "summary.pdf"
        pdf.output(pdf_output)
        return f"PDF generated: {pdf_output}"

    elif output_format == "Excel":
        data = {
            "Original Text": chunks,
            "Summary": summarized_chunks
        }
        df = pd.DataFrame(data)
        excel_output = "summary.xlsx"
        df.to_excel(excel_output, index=False)
        return f"Excel file generated: {excel_output}"

# Create a Gradio interface with an additional output format selection
iface = gr.Interface(
    fn=summary,
    inputs=[
        gr.Textbox(label="Input Text", lines=10),
        gr.Slider(label="Max Length", minimum=30, maximum=300, step=10, value=130),
        gr.Slider(label="Min Length", minimum=20, maximum=100, step=10, value=30),
        gr.Dropdown(label="Output Format", choices=["Plain Text", "JSON", "HTML", "CSV", "Markdown", "PDF", "Excel"], value="Plain Text")
    ],
    outputs=gr.Textbox(label="Summarized Output"),
    title="Text Summarization with Advanced Output Formats"
)

iface.launch()
