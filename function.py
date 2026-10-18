from pathlib import Path
import csv
from reportlab.platypus import SimpleDocTemplate , Table

def get_valid_file_path ():
    while True:
        file_path = input("Please enter the file path: ")
        path = Path(file_path)
        if path.exists():
            return path
        else:
            print("Please enter a valid file path")


def convert_csv_to_pdf () :
    while True:
        csv_path = get_valid_file_path()
        if csv_path.suffix.lower()!=".csv":
            print("Please select a csv file")
            continue

        else :
            with open (csv_path , "r",newline="",encoding="utf-8") as file :
                reader = csv.reader(file)
                data = list(reader)

                if not data :
                    print("he csv file is empty")
                    return
                max_colums = max(len(row) for row in data)
                for row in data :
                    while len(row) < max_colums :
                        row.append("")
                pdf_path = csv_path.with_suffix(".pdf")

                pdf = SimpleDocTemplate(str(pdf_path))
                table = Table(data)

                pdf.build([table])
                print(f"PDF saved to {pdf_path}")
