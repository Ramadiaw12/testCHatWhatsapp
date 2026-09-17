from pathlib import Path
from pypdf import PdfReader
import psycopg
from dotenv import load_dotenv
import os

load_dotenv("/.env")
pdf_path=Path("cvriri.pdf")

reader = PdfReader(pdf_path)

print(f"Nombre de pages : {len(reader.pages)}")

text = ""

for page in reader.pages:
    text += page.extract_text() or ""

print("\n--- DÉBUT DU TEXTE ---\n")
print(text[:3000])

# CONNEXION DATABASE

with psycopg.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)as count:
    print("connection postgre reussit !")