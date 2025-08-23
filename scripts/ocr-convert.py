import ocrmypdf
from pathlib import Path

INPUT_DIR = Path("/workspaces/pdf-tools/data/ocr-in")
OUTPUT_DIR = Path("/workspaces/pdf-tools/data/ocr-out")

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    pdf_files = list(INPUT_DIR.glob("*.pdf"))
    
    for pdf_path in pdf_files:
        output_filename = f"{pdf_path.stem}-converted{pdf_path.suffix}"
        output_path = OUTPUT_DIR / output_filename
        print(f"Converting {pdf_path} -> {output_path}")
        ocrmypdf.ocr(
            pdf_path,
            output_path,
            deskew=True,
            rotate_pages=True,
            clean=True,
            language="eng",      # "eng+spa" etc.
            output_type="pdfa", # PDF/A for archiving and text extraction
        )

if __name__ == "__main__":
    main()