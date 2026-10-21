import function
import FreeSimpleGUI as sg
import os

label = sg.Text("Convert CSV or TXT to PDF")
input_text = sg.InputText(tooltip="Address file ", key="-CSV-TXT-")
browser_button = sg.FileBrowse("Browser",
                               target="-CSV-TXT-",
                               file_types=[('CSV file', '*.csv'), ("TXT file", "*.txt")])

CSV_button = sg.Button("CSV to PDF", key="-CSV-PDF-")
TXT_button = sg.Button("TXT to PDF", key="-TXT-PDF-")
exit_button = sg.Button("Exit")
open_pdf_button = sg.Button("Open PDF", key="-OPEN-PDF-", disabled=True)

output_text = sg.Text(
    "Converted file will appear here.",
    key="-OUTPUT-",
    size=(50, 2)
)

layout = [[label],
          [input_text, browser_button],
          [CSV_button, TXT_button],
          [output_text],
          [open_pdf_button],
          [exit_button]]

window = sg.Window("FILEFLOW",
                   layout,
                   font=("Helvetica", 12))
pdf_path = None
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "-CSV-PDF-":
        try:
            file_path = values["-CSV-TXT-"].strip().strip('"')

            if not file_path.lower().endswith(".csv"):
                raise ValueError("Please select a CSV file.")
            pdf_path = function.convert_csv_to_pdf(file_path)

            window["-OUTPUT-"].update("PDF created")
            window["-OPEN-PDF-"].update(disabled=False)

        except (ValueError, FileNotFoundError) as error:
            sg.popup_error(str(error), title="Error")
    if event == "-TXT-PDF-":
        try:
            file_path = values["-CSV-TXT-"].strip().strip('"')

            if not file_path.lower().endswith(".txt"):
                raise ValueError("Please select a TXT file.")

            pdf_path = function.convert_txt_to_pdf(file_path)

            window["-OUTPUT-"].update("PDF created")
            window["-OPEN-PDF-"].update(disabled=False)
        except(ValueError, FileNotFoundError) as error:
            sg.popup_error(str(error), title="Error")

    if event == "-OPEN-PDF-" and pdf_path:
        if pdf_path.exists():
            os.startfile(pdf_path)
        else:
            sg.popup_error("PDF file not found.")
window.close()
