import function
import FreeSimpleGUI as sg
import os

label = sg.Text("Convert CSV to PDF")
input_text = sg.InputText(tooltip="Address CSV file ", key = "-CSV-")
browser_button = sg.FileBrowse("Browser",target= "-CSV-",file_types= [('CSV file', '*.csv')])

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
open_pdf_button = sg.Button("Open PDF", key="-OPEN-PDF-", disabled=True)

output_text = sg.Text(
    "Converted file will appear here.",
    key="-OUTPUT-",
    size=(50, 2)
)

layout = [[label],
          [input_text ,browser_button],
          [convert_button , exit_button, open_pdf_button],
          [output_text]]

window = sg.Window("FILEFLOW",
                    layout ,
                    font=("Helvetica", 12))
pdf_path = None
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Convert":
        try:
            pdf_path = function.convert_csv_to_pdf(values["-CSV-"])
            window["-OUTPUT-"].update("PDF created")

            window["-OPEN-PDF-"].update(disabled=False)

        except (ValueError, FileNotFoundError) as error:
            sg.popup_error(str(error))

    if event == "-OPEN-PDF-" and pdf_path:
        if pdf_path.exists():
            os.startfile(pdf_path)
        else:
            sg.popup_error("PDF file not found.")
window.close()
