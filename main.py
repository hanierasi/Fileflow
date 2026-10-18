import function as file_read
while True:
    choice =int( input("1-Convert CSV to PDF\n"
                   "2-Organize files by extension\n"
                   "3-Exit\n"
                   "Choose an option: "))
    if 1 <= choice <= 3 :
        if choice == 1:
            file_read.convert_csv_to_pdf()
        elif choice == 2:
            pass
        elif choice == 3:
            print("Goodbye")
            break
    else :
        print("Please choose an option between 1 and 3")



