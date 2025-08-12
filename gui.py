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