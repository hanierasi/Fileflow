import function as file_read

while True:
    try:
        choice = int(
            input(
                "1-Convert CSV to PDF\n"
                "2-Convert Text to PDF\n"
                "3-Organize files by extension\n"
                "4-Exit\n"
                "Choose an option: "
            )
        )
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        file_read.convert_csv_to_pdf()
    elif choice == 2:
        file_read.convert_txt_to_pdf()
    elif choice == 3:
        file_read.organize_files_by_extension()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Please choose an option between 1 and 4.")
