from pypdf import PdfMerger
import os

pdfs = [file for file in os.listdir() if file.endswith(".pdf")]

merger = PdfMerger()

for pdf in pdfs:
    with open(pdf, "rb") as f:
        merger.append(f)

merger.write("result.pdf")
merger.close()
