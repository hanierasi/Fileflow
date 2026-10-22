# FileFlow

A Python-based file management and conversion application that converts CSV and TXT files into PDF documents and organizes files by extension. The project started as a command-line interface (CLI) application and was later expanded with a desktop graphical user interface (GUI) built using FreeSimpleGUI.

## Features

- **CSV to PDF Conversion:** Convert CSV files into formatted PDF documents.
- **TXT to PDF Conversion:** Convert text files into PDF documents.
- **File Organization:** Organize files into subfolders based on their extensions.
- **File Selection:** Browse and select input files and folders through the graphical interface.
- **Open Generated PDFs:** Open converted PDF documents directly from the application.
- **Open Organized Folders:** Quickly access folders after organizing their contents.
- **Input Validation:** Validate file types, file paths, folders, and user inputs.
- **Error Handling:** Handle common file-related errors and invalid inputs.
- **Command-Line Interface (CLI):** Run file conversion and organization tasks through the terminal.
- **Graphical User Interface (GUI):** Use a desktop interface built with FreeSimpleGUI to interact with the application's features.

## Technologies

- Python 3
- FreeSimpleGUI
- ReportLab
- pathlib
- csv
- shutil
- os
- Exception Handling
- File Handling and Path Validation

## Requirements

- Python 3
- FreeSimpleGUI
- ReportLab

## Getting Started

### 1. Clone or Download the Repository

Clone or download the project repository to your computer.

### 2. Open the Project Directory

Open a terminal in the project directory.

### 3. Install the Required Libraries

```bash
pip install FreeSimpleGUI reportlab
```

### 4. Run the Application

To run the command-line version:

```bash
python main.py
```

To run the desktop graphical interface:

```bash
python GUI.py
```

If necessary, use `python3` instead of `python`.

## Project Structure

```text
FileFlow/
├── main.py
├── GUI.py
├── function.py
└── README.md
```

- **`main.py`:** Contains the command-line interface (CLI) for interacting with the application's file conversion and organization functions.
- **`GUI.py`:** Contains the desktop graphical user interface (GUI), allowing users to convert files and organize folders through a visual interface.
- **`function.py`:** Originally developed to support the CLI version, this module was later adapted to support the GUI as well. It contains reusable functions for file conversion and organization that can be called from both interfaces.
- **`README.md`:** Provides project documentation, including features, requirements, installation instructions, and usage.

## How It Works

1. Choose the command-line version or launch the desktop GUI.
2. Select a CSV or TXT file to convert it into a PDF document.
3. Open the generated PDF directly from the GUI.
4. Select a folder to organize its files into subfolders based on their extensions.
5. Open the organized folder directly from the GUI.

## Learning Objectives

This project demonstrates practical Python programming skills, including modular programming, reusable functions, file handling, path management, exception handling, input validation, GUI development, and PDF generation. It also demonstrates the process of expanding a command-line application into a desktop graphical interface.

## Future Improvements

- Enhance the graphical interface and improve the user experience.
- Detect and remove duplicate files during file organization.
- Add automated unit tests.
- Support additional file formats.
- Improve file organization options.
- Package the application as a standalone desktop executable.
