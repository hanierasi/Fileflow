import function
import FreeSimpleGUI as sg
import os
from pathlib import Path

# -------------------- File Conversion --------------------

label = sg.Text("Convert CSV or TXT to PDF")

input_text = sg.InputText(tooltip="Address file ", key="-CSV-TXT-",enable_events=True)
browser_button = sg.FileBrowse("Browser",target="-CSV-TXT-",file_types=[('CSV file', '*.csv'), ("TXT file", "*.txt")])

CSV_button = sg.Button("CSV to PDF", key="-CSV-PDF-")
TXT_button = sg.Button("TXT to PDF", key="-TXT-PDF-")
open_pdf_button = sg.Button("Open PDF", key="-OPEN-PDF-", disabled=True)
output_text = sg.Text( "Converted file will appear here.",key="-OUTPUT-",size=(50, 2))
conversion_frame = sg.Frame("File Conversion",
                            [
                                [input_text, browser_button],
                                [CSV_button, TXT_button,open_pdf_button],
                                [output_text]
                            ],expand_x=True)
# -------------------- Folder Organization --------------------
input_folder = sg.InputText(tooltip="select a folder to organize", key ="-FOLDER-")
folder_browser_button = sg.FolderBrowse("Browse Folder",target="-FOLDER-")


organize_button = sg.Button("Organize", key="-ORGANIZE-")
open_folder_button = sg.Button("Open Folder",key="-OPEN-FOLDER-",disabled=True)
output_folder = sg.Text("Organization status will appear here.",key="-ORGANIZE-OUTPUT-",size=(50, 2))

organize_frame=sg.Frame("Organize Folder",
                        [
                            [input_folder ,folder_browser_button],
                            [organize_button , open_folder_button],
                            [output_folder]
                        ],expand_x=True)

# -------------------- Main Window --------------------
layout = [[label],
          [conversion_frame],
          [organize_frame],
          [sg.Button("Exit")]]

window = sg.Window("FILEFLOW",
                   layout,
                   font=("Helvetica", 12))
pdf_path = None
organized_folder_path = None
# -------------------- Event Loop --------------------
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "-CSV-TXT-":
        pdf_path = None
        window["-OPEN-PDF-"].update(disabled=True)
        window["-OUTPUT-"].update("New file selected.")

    # Convert CSV to PDF
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

    # Convert TXT to PDF
    elif event == "-TXT-PDF-":
        try:
            file_path = values["-CSV-TXT-"].strip().strip('"')

            if not file_path.lower().endswith(".txt"):
                raise ValueError("Please select a TXT file.")

            pdf_path = function.convert_txt_to_pdf(file_path)

            window["-OUTPUT-"].update("PDF created")
            window["-OPEN-PDF-"].update(disabled=False)

        except(ValueError, FileNotFoundError) as error:
            sg.popup_error(str(error), title="Error")

    # Open the generated PDF
    elif event == "-OPEN-PDF-" and pdf_path:
        if pdf_path.exists():
            os.startfile(pdf_path)

        else:
            sg.popup_error("PDF file not found.")

    # Organize the selected folder
    elif event== "-ORGANIZE-":
        organized_folder_path = None
        window["-OPEN-FOLDER-"].update(disabled=True)
        try:
            folder_path = values["-FOLDER-"].strip().strip('"')

            if not folder_path :
                raise ValueError("Please select a folder.")
            folder = Path(folder_path)

            if not folder.is_dir():
                raise ValueError("The selected folder does not exist.")

            if not any(item.is_file() for item in folder.iterdir()):
                raise ValueError("The selected folder contains no files.")

            organize_count = function.organize_files_by_extension(folder_path)

            window["-ORGANIZE-OUTPUT-"].update(f"Folder organized. {organize_count} files moved.")
            organized_folder_path = Path(folder_path)
            window["-OPEN-FOLDER-"].update(disabled=False)

        except(ValueError, FileNotFoundError) as error:
            sg.popup_error(str(error), title="Error")

    # Open the organized folder
    if event == "-OPEN-FOLDER-" and organized_folder_path:
        if organized_folder_path.exists():
            os.startfile(str(organized_folder_path))
        else:
            sg.popup_error("Folder not found.")


window.close()
