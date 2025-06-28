import fitz  # PyMuPDF

def parse_document(uploaded_file):
    """
    Extracts and returns text from an uploaded PDF or TXT file.
    """
    if uploaded_file.type == "application/pdf":
        # Read PDF
        pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf_doc:
            text += page.get_text()
        return text

    elif uploaded_file.type == "text/plain":
        # Read TXT
        return uploaded_file.read().decode("utf-8")

    else:
        return "Unsupported file type."