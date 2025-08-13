try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You summarize and compare two documents."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    summary = response.choices[0].message.content
    return summary
except Exception as e:
    return f"❌ Error from GPT: {e}"

import fitz  # PyMuPDF
from openai import OpenAI
from docx import Document
import os

# Initialize the OpenAI client
client = OpenAI(api_key = os.environ["OPENAI_API_KEY"])


def extract_text(file_path):
    ext = file_path.split('.')[-1].lower()

    if ext == "pdf":
        with open(file_path, "rb") as f:
            with fitz.open(stream=f.read(), filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
    elif ext == "docx":
        doc = Document(file_path)
        text = "\n".join(para.text for para in doc.paragraphs)
    elif ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")

    return text

def compare_docs(file1_path, file2_path):
    try:
        text1 = extract_text(file1_path)
        text2 = extract_text(file2_path)

        # Create a representation of the difference for GPT
        # A simple concatenation for now; can be improved with diffing libraries
        diff_text = f"Document A:\n\n{text1}\n\n---\n\nDocument B:\n\n{text2}"

        # Ask GPT to summarize the diff
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4o"
            messages=[
                {"role": "system", "content": "You are an assistant that explains differences between two text documents in simple terms."},
                {"role": "user", "content": f"Please summarize the following differences between two documents:\n\n{diff_text}"}
            ],
            temperature=0.7
        )

        summary = response.choices[0].message.content
        return summary

    except Exception as e:
        return f"❌ Error during comparison or summarization: {e}"

from openai import OpenAI
from dotenv import load_dotenv
import os

os.environ["OPENAI_API_KEY"] = #Insert your API KEY

# Initialize the OpenAI client
client = OpenAI(api_key = os.environ["OPENAI_API_KEY"])

# Ask GPT to summarize the diff
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o"
    messages=[
        {"role": "system", "content": "You are an assistant that explains differences between two text documents in simple terms."},
        {"role": "user", "content": f"Please summarize the following differences between two documents:\n\n{diff_text}"}
    ],
    temperature=0.7
)

# Print summary
summary = response.choices[0].message.content
print(summary)

import gradio as gr

# Gradio UI
iface = gr.Interface(
    fn=compare_docs,
    inputs=[
        gr.File(label="Upload Document A", type="filepath"),
        gr.File(label="Upload Document B", type="filepath")
    ],
    outputs="text",
    title="📄 Document Comparator",
    description="Upload two documents (PDF, DOCX, or TXT) to get a section-wise and overall difference comparison."
)

iface.launch()
