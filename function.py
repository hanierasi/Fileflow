from pathlib import Path
import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Spacer
from reportlab.lib.units import cm
import shutil


def get_valid_file_path():
    while True:
        file_path = input("Please enter the file path: ")
        path = Path(file_path)
        if path.exists():
            return path
        else:
            print("Please enter a valid file path")


def convert_csv_to_pdf(csv_path):
    """Convert a CSV file into a formatted PDF document."""
    csv_path = Path(csv_path)

    if not csv_path.is_file():
        raise FileNotFoundError("CSV file not found.")

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Please select a CSV file.")

    with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        data = list(reader)

    if not data or not any(
            value.strip()
            for row in data
            for value in row
    ):
        raise ValueError("The CSV file is empty.")

    # Make sure all rows have the same number of columns.
    max_columns = max(len(row) for row in data)

    for row in data:
        row.extend([""] * (max_columns - len(row)))

    styles = getSampleStyleSheet()

    # Use smaller text so more data fits on each page.
    cell_style = styles["BodyText"]
    cell_style.fontName = "Helvetica"
    cell_style.fontSize = 7
    cell_style.leading = 8.5
    cell_style.wordWrap = "LTR"

    header_style = styles["BodyText"]
    header_style.fontName = "Helvetica-Bold"
    header_style.fontSize = 7
    header_style.leading = 8.5

    table_data = []

    for row_index, row in enumerate(data):
        style = header_style if row_index == 0 else cell_style

        table_data.append([
            Paragraph(
                str(value).replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\n", "<br/>"),
                style
            )
            for value in row
        ])

    # Use landscape orientation for wide tables.
    pdf_path = csv_path.with_suffix(".pdf")

    pdf = SimpleDocTemplate(
        str(pdf_path),
        pagesize=landscape(A4),
        leftMargin=20,
        rightMargin=20,
        topMargin=25,
        bottomMargin=25
    )

    available_width = (
            landscape(A4)[0] - pdf.leftMargin - pdf.rightMargin)

    # Give more space to columns containing longer text.
    weights = [
        1,  # Order_Id
        1,  # Date
        1.7,  # Customer
        1.2,  # Region
        1.5,  # Product
        1.0,  # Category
        0.4,  # Quantity
        0.8,  # Unit_Price
        0.9,  # Total
        0.9,  # Status
        2.5  # Notes
    ]

    # Adapt the widths if the CSV has a different number of columns.
    if max_columns != len(weights):
        weights = [1.0] * max_columns

    total_weight = sum(weights)

    column_widths = [
        available_width * weight / total_weight
        for weight in weights
    ]

    table = Table(
        table_data,
        colWidths=column_widths,
        repeatRows=1,
        hAlign="LEFT"
    )

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))

    pdf.build(
        [table],
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    return pdf_path


def convert_txt_to_pdf(txt_path):
    """Convert a text file into a PDF document."""

    txt_path = Path(txt_path)

    if not txt_path.is_file():
        raise FileNotFoundError("TXT file not found.")

    if txt_path.suffix.lower() != ".txt":
        raise ValueError("Please select a TXT file.")

    with open(txt_path, "r", encoding="utf-8-sig") as file:
        lines = [line.rstrip("\r\n") for line in file]

    if not any(line.strip() for line in lines):
        raise ValueError("The TXT file is empty.")

    styles = getSampleStyleSheet()
    body_style = styles["BodyText"]
    body_style.fontSize = 11
    body_style.leading = 16

    story = []

    for line in lines:
        if line.strip():
            paragraph = Paragraph(
                line.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"),
                body_style
            )
            story.append(paragraph)
            story.append(Spacer(1, 8))
        else:
            story.append(Spacer(1, 8))

    pdf_path = txt_path.with_suffix(".pdf")

    pdf = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    pdf.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    return pdf_path

def add_page_number(canvas, doc):
    """Add a page number to each PDF page."""
    canvas.saveState()

    page_width, page_height = doc.pagesize

    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(
        page_width / 2,
        12,
        f"Page {doc.page}"
    )

    canvas.restoreState()

def organize_files_by_extension(folder_path):
    """Move files into subfolders based on their file extensions."""

    folder_path = Path(folder_path)

    if not folder_path.exists() or not folder_path.is_dir():
        raise ValueError("Please enter a valid folder path.")

    files = list(folder_path.iterdir())
    organized_count = 0

    for file_path in files:
        if not file_path.is_file() or not file_path.suffix:
            continue

        folder_name = file_path.suffix[1:].upper()
        destination_folder = folder_path / folder_name
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / file_path.name

        if destination_file.exists():
            print(f"Skipped duplicate file: {file_path.name}")
            continue

        shutil.move(str(file_path), str(destination_file))
        organized_count += 1

    return organized_count



