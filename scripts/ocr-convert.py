import ocrmypdf

ocrmypdf.ocr(
    "input_scanned.pdf",
    "output_searchable.pdf",
    deskew=True,
    rotate_pages=True,
    clean=True,
    language="eng",      # "eng+spa" etc.
    output_type="pdf",   # or "pdfa"
)