from pathlib import Path
from pypdf import PdfReader

pdf_path=Path("cvriri.pdf")

reader = PdfReader(pdf_path)

print(f"Nombre de pages : {len(reader.pages)}")

text = ""

for page in reader.pages:
    text += page.extract_text() or ""

print("\n--- DÉBUT DU TEXTE ---\n")
print(text[:3000])