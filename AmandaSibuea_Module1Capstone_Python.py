# Book Haven Library Management System

### dictionary for book list
book_list = {}

# sample data for the library added to book_list dictionary
book_list[0] = {
    "title": "Harry Potter",
    "author": "J. K Rowling",
    "year": 1997,
    "genre": "Kids",
    "no_of_copies": 3,
    "next_available_date": "today"
}

book_list[1] = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1931,
    "genre": "Fiction",
    "no_of_copies": 0,
    "next_available_date": "19 March 2025"
}

book_list[2] = {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "year": 1913,
    "genre": "Romance",
    "no_of_copies": 1,
    "next_available_date": "today"
}

book_list[3] = {
    "title": "Sense and Sensibility",
    "author": "Jane Austen",
    "year": 1811,
    "genre": "Romance",
    "no_of_copies": 0,
    "next_available_date": "15 March 2025"
}

book_list[4] = {
    "title": "Fahrenheit 451",
    "author": "Ray Bradbury",
    "year": 1953,
    "genre": "Fiction",
    "no_of_copies": 2,
    "next_available_date": "today"
}

book_list[5] = {
    "title": "Animal Farm",
    "author": "George Orwell",
    "year": 1945,
    "genre": "Fiction",
    "no_of_copies": 1,
    "next_available_date": "today"
}

book_list[6] = {
    "title": "The Notebook",
    "author": "Nicholas Sparks",
    "year": 1996,
    "genre": "Romance",
    "no_of_copies": 1,
    "next_available_date": "today"
}

book_list[7] = {
    "title": "The Giving Tree",
    "author": "Shel Silverstein",
    "year": 1964,
    "genre": "Kids",
    "no_of_copies": 0,
    "next_available_date": "20 March 2025"
}

book_list[8] = {
    "title": "Charlotte's Web",
    "author": "E. B White",
    "year": 1952,
    "genre": "Kids",
    "no_of_copies": 3,
    "next_available_date": "today"
}

book_list[9] = {
    "title": "Pachinko",
    "author": "Min Jin Lee",
    "year": 2017,
    "genre": "Fiction",
    "no_of_copies": 1,
    "next_available_date": "today"
}

### OPTION 0 - WELCOMING, MENU, SUB MENU
# welcoming and inputing name & date
def welcoming_user():
    print("Welcome to Book Haven Library")

    # input the name and current date
    name = input("Please enter your name here: ").title()
    date = input("Please enter the date here: ").title()

    # display name and date
    print(f"Hi {name}, welcome to Book Haven")
    print(f"The date is {date} \n")

    return

# main menu with user input for menu choice
def main_menu():
    # prompt for user
    print("Please choose a number from the menu below \n")
    menu_design()

    # user input - choice of menu
    choice = input("Please enter your choice: ")

    # conditionals
    if choice in ("1", "2", "3", "4", "5", "6","7"):
        return choice
    
    else:
        print(f"{choice} is an invalid input")
        main_menu()

    return choice

# menu design content - list of menus
def menu_design():
    print("Book Haven Library Main Menu")
    print("-" * 35)
    print("1. View all books")
    print("2. Add a book to the system")
    print("3. Search and borrow a book")
    print("4. Edit book details")
    print("5. Delete a book to the system")
    print("6. Sort books")
    print("7. Exit \n")

# sub menu with user input for menu choice
def sub_menu():
    # prompt for user
    print("Please choose a letter from the menu below \n")
    sub_menu_design()

    while True:
        # user input - choice of sub menu
        choice = input("Please enter your choice: ").lower()

        # conditionals
        if choice in ("a", "b", "c", "d"):
            return choice
        
        elif choice == "e":
            print("Back to main menu")
            return "e"
            
        else:
            print(f"'{choice}' is an invalid input. Please try again.")

# sub menu design content - list of sub menus
def sub_menu_design():
    print("Book Haven Library Sub Menu")
    print("-" * 35)
    print("A. Title")
    print("B. Author")
    print("C. Year")
    print("D. Genre")
    print("E. Back to Main Menu \n")

### helper function for all the conditionals
def conditionals():
    while True:
        choice = input("Please enter yes or no: ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print(f"'{choice}' is an invalid input. Please try again.")

### OPTION 1 - DISPLAY DATA
# display both header and data
def display_library(book_list):
    data_header()
    data_content(book_list)

# display library header
def data_header():
    print("{:<6} {:<30} {:<30} {:<10} {:<15} {:<15} {:<30}".format("Index", "Title", "Author", "Year", "Genre", "No. of Copies", "Next Available Date"))
    print("-" * 135)

# display only the data
def data_content(book_list):
    for key, value in book_list.items():
        title = value["title"]
        author = value["author"]
        year = value["year"]
        genre = value["genre"]
        no_of_copies = value["no_of_copies"]
        next_available_date = value["next_available_date"]
        print("{:<6}".format(key), "{:<30} {:<30} {:<10} {:<15} {:<15} {:<30}".format(title, author, year, genre, no_of_copies, next_available_date))
    print("\n")

### OPTION 2 - ADD A BOOK TO THE SYSTEM
# add a book to the system
def add_book():
    # prompts for users
    print("You've chosen to add a new book to the system")
    print("Please enter the book title you would like to add")
    new_title = input("Please enter book title: ").title()
    print(f"Title: {new_title}")

    # check to see if the is already in the system
    book_found = False

    # iterate over the titles
    for key, value in book_list.items():
        title = value["title"]

        # if book is already in the system - just add one more copy
        if new_title == title:
            book_list[key]["no_of_copies"] += 1

            # let user know that it is already in the system and no of copies are added
            print(f"{new_title} is already in Book Haven's system")
            print("Number of copies successfully updated \n")

            # option to see updated data - only one row
            view_updated_row(new_title)

            # set book_found to true once
            book_found = True
            break

    # if book is not in the system
    # add all other details
    if not book_found:
        print(f"'{new_title}' is not in the system")
        print(f"Please enter details of '{new_title}' to be added to the system")
        
        # new author input
        new_author = input("Please enter the author: ").title()
        print("Author: " + new_author)

        # new year input (with validation)
        while True:
            try:
                new_year = int(input("Please enter the year: "))
                print("Year: " + str(new_year))
                break
            except ValueError:
                print("Invalid year. Please enter a valid number.")

        # new genre input
        new_genre = input("Please enter the genre of the book: ").title()
        print("Genre: " + new_genre)

        # automatically adds 1 copy
        new_copies = 1
        print("No. of Copies: " + str(new_copies))

        # automatically makes next available date to be today
        new_next_available_date = "today"
        print("Next available date: " + new_next_available_date)

        # creating the new key and value pairs for the new book
        new_key = max(book_list.keys()) + 1 if book_list else 0 
        book_list[new_key] = {
            "title": new_title,
            "author": new_author,
            "year": new_year,
            "genre": new_genre,
            "no_of_copies": new_copies,
            "next_available_date": new_next_available_date
        }

        # let user know that the new book is in the system
        print(f"'{new_title}' and other details successfully added to the system.")

        # option to see updated data - only one row
        view_updated_row(new_title)

# conditionals - view updated data after adding one book only the one row 
def view_updated_row(new_title):
    # ensure that function keeps asking until the user inputs yes or no
    while True:
        # prompt to user
        print(f"Would you like to view the updated data for {new_title}? \n")
        choice = input("Please enter yes or no").lower()

        # conditionals
        if choice == "yes":
            print(f"Here is the updated data for {new_title}:")
            data_header()
            for key, value in book_list.items():
                title = value["title"]
                if title == new_title:
                    print("{:<6}".format(key), "{:<30} {:<30} {:<10} {:<15} {:<15} {:<30}".format(title, value["author"], value["year"], value["genre"], value["no_of_copies"], value["next_available_date"]))
            # exit the loop after displaying the row
            break
            
        elif choice == "no":
            add_another_book()
            break

        else:
            print(f"'{choice}' is an invalid input. Please try again.")

# conditionals - add another book option
def add_another_book():
    # prompt
    print("Would you like to add another book? \n")
    if conditionals():
        add_book()
    else:
        print("Back to main menu")
        return

### OPTION 3 - SEARCH AND BORROW BOOK FROM THE SYSTEM    
# function to search book
def search_book():
    print("You've chosen to search a book in the system")
    print("Please choose how you would like to search a book \n")

    # display sub menu to prompt user how to search
    choice = sub_menu()

    # if user chooses to go back to main menu. return control to main programme
    if choice == "e":
        return

    # dictionary to call based on choice
    if choice in ("a", "b", "d"):
        prompts = {
            "a": "title",
            "b": "author",
            "d": "genre",
        }

        # let user know of their choice title author genre. prompt them to search the book
        print(f"You've chosen to search {choice.capitalize()}: {prompts[choice].capitalize()} \n")
        print(f"Which book {prompts[choice]} would you like to search?")
        search = input(f"Please enter book {prompts[choice]}: ").title()
        print(f"{prompts[choice].capitalize()}: {search} \n")

        # display the filtered books title author genre
        filtered_book(search)

        # option to borrow book
        borrow_book()

    elif choice == "c":
        print("From which years would you like to search?")
        min_year = int(input("Please enter the lower range value: "))
        max_year = int(input("Please enter the higher range value: "))
        print(f"Year: '{min_year}' to '{max_year}'")

        # initialise the book_found flag to false
        book_found = False
        
        # display the filtered books year
        for key, value in book_list.items():
            year = value["year"]

            # checking if book is in the system
            if min_year <= year <= max_year:
                if not book_found: # check if this is the first time the value is found within the range
                    print(f"We found books from '{min_year}' to '{max_year}' in the system")
                    print("\n")
                    data_header()
                    book_found = True # set flag to True only once
            
                print("{:<6} {:<30} {:<30} {:<10} {:<15} {:<15} {:<30}".format(key, value["title"], value["author"], year, value["genre"], value["no_of_copies"], value["next_available_date"]))
                    
        # option to borrow book
        borrow_book()

        # if the book is not fouund within the years provided
        if not book_found:
            print(f"Books from the years '{min_year}' to '{max_year}' are not in the system")
            search_another_book()

# filtered book data after searching
def filtered_book(search):
    # list to store matching books as a new dictionary
    search_match = []

    # check to see if the title is found in the search
    book_found = False

    # iterate over title author year genre (year here is only used for book detail edit)
    for key, value in book_list.items():
        title = value["title"]
        author = value["author"]
        year = value["year"]
        genre = value["genre"]

        # checking if book based on search is in the system:
        if search == title or search == author or search == year or search == genre:
            # check if this is the first time the book is found
            if not book_found:
                print(f"We found '{search}' in the Book Haven system \n")
                data_header()
                # set book_found to true once
                book_found = True
            
            print("{:<6}".format(key), "{:<30} {:<30} {:<10} {:<15} {:<15} {:<30}".format(title, author, year, genre, value["no_of_copies"], value["next_available_date"]))
            
            # append the results to the search_match
            search_match.append(value)

    # book not found in the system
    if not book_found:
        print(f"'{search}' is not in the Book Haven system")

        # search another book option
        search_another_book()

    return search_match

# option to borrow a book from list displayed after search - includes conditionals
def borrow_book():
    # ensure that function keeps asking until the user inputs yes or no
    while True:
        print("Would you like to borrow a book from the list above? \n")
        choice = input("Please enter yes or no: ").lower()

        # conditionals - if yes
        if choice == "yes":
            print("Please enter the book title you would like to borrow")
            title_borrow = input("Please enter the title: ").title()

            # flag to check if the book is found
            book_found = False

            # iterations over titles, no of copies, next available date
            for key, value in book_list.items():
                title = value["title"]
                no_of_copies = value["no_of_copies"]
                next_available_date = value["next_available_date"]

                # if book is in the system (if the user spelling is correct)
                if title_borrow == title:

                    # conditionals for number of copies
                    ### if copies are available
                    if no_of_copies > 0:
                        book_list[key]["no_of_copies"] -= 1
                        print(f"You've successfullly borrowed '{title_borrow}'")

                        ### if there are no copies left, set next available date
                        if no_of_copies == 1:
                            book_list[key]["next_available_date"] = "30 March 2025"

                    else:
                        print(f"'{title_borrow}' is not currently availble")
                        view_availability(title_borrow, next_available_date)

                    ### exit loop after finding book
                    book_found = True
                    break

            if not book_found:
                print(f"'{title_borrow}' is not in the system")
                search_another_book()
            
            ### exit the borrow_book() function
            return

        # if user choice is no
        elif choice == "no":
            search_another_book()

            return

        else:
            print(f"'{choice}' is an invalid input. Please try again.")


# conditionals - option to see book availability
def view_availability(title_borrow, next_available_date):
    # prompt user
    print(f"Would you like to see the next available date for '{title_borrow}'? \n")
    if conditionals():
        print("The next available date for '{}' is {}".format(title_borrow, next_available_date))
    else:
        search_another_book()

# conditionals -  search another book option
def search_another_book():
    # prompt user
    print("Would you like to search for another book? \n")
    if conditionals():
        search_book()
    else:
        print("Back to main menu")
        return
    
### OPTION 4 - EDIT BOOK DETAILS
# conditionals - function to change another book (last step in option 4)
def edit_another_book_option():
    # prompt user
    print("\n")
    print("Would you like to edit another book? \n")
    if conditionals():
        edit_book()
    else:
        print("Back to main menu")
        return

# conditionals - function to change another info (within the same book)
def edit_another_detail_option(book_index):
    # prompt user
    print("Would you like to edit another detail? \n")
    if conditionals():
        edit_detail(book_index)
    else:
        edit_another_book_option()

# conditionals - function to view updated book_list
def display_update_option(book_index):
    # prompt user
    print("Would you like to view the updated list of books? \n")
    if conditionals():
        display_library(book_list)

    else:
        edit_another_book_option()

# conditionals - function to assure the user of the change they are making
def change_confirmation():
    # ensure that function keeps asking until the user inputs yes or no
    while True:
        # prompt user
        print("Are you sure you would like to save the changes made to the book details above? \n")
        confirmation = input("Please enter yes or no: ").lower()

        # conditionals
        if confirmation == "yes":
            ### display success of change
            print("You've successfully made an edit to the book")
            return True
        
        elif confirmation == "no":
            ### no changes has been made
            print("Changes cancelled")
            return False
        
        else:
            print(f"'{confirmation}' is an invalid input. Please try again.")

# edit_detail() function to edit specific details. starts with sub_menu
def edit_detail(book_index):
    # prompt user to choose from the sub menu
    print("What would you like to edit?")
    choice = sub_menu()

    # if user chooses to go back to main menu. return control back to main programme
    if choice == "e":
        return

    # prompts for easier access
    prompts = {
        "a": "title",
        "b": "author",
        "c": "year",
        "d": "genre"
    }

    # display user's choice
    print(f"You've chosen to change the {prompts[choice]} \n")
    
    # input and display change
    print("Please enter the new information")
    new_info = input("Please enter the new information here: ").title()
    print(f"New {prompts[choice]}: {new_info}")

    confirmed = change_confirmation()

    # if user confirmed the changes, save and update the detail
    if confirmed:
        ### save the edit to the system
        save_edit(choice, new_info, book_index)
        ### option to view the whole book_list
        display_update_option(book_index)
        edit_another_detail_option(book_index)
    
    # if user does not confirm changes, prompt them to change another detail instead
    elif not confirmed:
        edit_another_detail_option(book_index)


# the whole option 4 edit_book() function which includes the search for the book
def edit_book():
    print("You've chosen to edit a book in the system\n")
    # display all books then prompt user to search based on index (key) so that we can always refer to the same row after changes
    display_library(book_list)
    print("\n")
    
    while True:
        try:
            print("Please choose the index of the book you would like to edit")
            book_index = int(input("Please enter the index number here: "))
            if book_index in book_list:
                break
            else:
                print(f"'{book_index}' is not a valid book index. Please try again.")
        
        # this is when the user inputs a non int
        except ValueError:
            print("Invalid input. Please enter an index number")
    
    print("You've decided to change the details on the book {}".format(book_list[book_index]["title"]))
    edit_detail(book_index)
   
# saving the edits made after confirmation is made (if confirmation == yes)
def save_edit(choice, new_info, book_index):
    # iterate over the book_list to access old information
    for key, value in book_list.items():
        # compare key with book_index
        if key == book_index:

            if choice == "a":
                book_list[key]["title"] = new_info
                break

            elif choice == "b":
                book_list[key]["author"] = new_info
                break

            elif choice == "c":
                book_list[key]["year"] = new_info
                break

            elif choice == "d":
                book_list[key]["genre"] = new_info
                break

### OPTION 5 - DELETE BOOK FROM SYSTEM
def delete_book():
    # prompt user to search the book they want to delete based on the title
    print("You've chosen to delete a book from the Book Haven library system")
    print("What book would you like to delete? \n")
    search = input("Please enter the book title: ").title()
    print(f"Title: {search}")

    # find the book to delete and store the key
    book_to_delete_key = None

    for key, value in book_list.items():
        if value["title"] == search:
            book_to_delete_key = key
            break

    if book_to_delete_key is None:
        print(f"'{search}' is not in the Book Haven library system")
        # option to search and delete another book
        return search_del_another_book()

    # reason to delete
    print(f"What is the reason to delete {search}?")
    reason = input("Please enter your reason here: ")
    
    # confirm deletion with the user
    confirmed = delete_confirmation(search, reason)

    # delete the row of book based on the key above
    if confirmed:
        del book_list[book_to_delete_key]

    # update the index numbers
    update_book_index()

    return search_del_another_book()

# update the index number
def update_book_index():
    # refer to the global book_list
    global book_list

    # create new dictionary to reset the indeces
    new_book_list = {}
    new_index = 0

    for old_key in book_list:
        new_book_list[new_index] = book_list[old_key]
        new_index += 1

    # modify the global book_list
    book_list = new_book_list

# conditionals - deletion confirmation
def delete_confirmation(search, reason):
    # ensure that function keeps asking until the user inputs yes or no
    while True:
        # promt user
        print(f"Are you sure you would like to delete '{search}' from the system due to {reason}? \n")
        confirmation = input("Please enter yes or no: ").lower()

        # conditionals
        if confirmation == "yes":
            ### display success of deletion
            print(f"You've successfully deleted '{search}'")
            return True
        
        elif confirmation == "no":
            ### no changes has been made
            print("Deletion cancelled")
            return False
        
        else:
            print(f"{confirmation} is an invalid input. Please try again.")

# conditionals - option to search and delete another book
def search_del_another_book():
    # prompt user
    print("Would you like to search for another book to delete? \n")
    if conditionals():
        delete_book()
    else:
        print("Back to main menu")
        return

### OPTION 6 - SORT BOOKS
# function to sort books - option 6
def sort_book():
    # new dictionary to store the sorted book list
    sorted_book_list = {}

    # prompt user
    print("You've chosen to sort the books in Book Haven library")
    print("Which category would you like to sort? \n")

    choice = sub_menu()

    # if user chooses to go back to main menu. return control to main programme
    if choice == "e":
        return
    
    prompts = {
        "a": "title",
        "b": "author",
        "c": "year",
        "d": "genre"
    }

    # display user's choice
    print(f"You've chosen to sort the books by {prompts[choice]}\n")
    
    # get sorting order
    sorting_order = sorting_order_options(prompts, choice)

    books_for_sorting = []
    for key, value in book_list.items():
        books_for_sorting.append((key, value))

    sort_key = prompts[choice]

    if sorting_order == "a":
        books_for_sorting.sort(key = lambda x: x[1][sort_key]) #asc
    elif sorting_order == "b":
        books_for_sorting.sort(key = lambda x: x[1][sort_key], reverse = True) #desc

    # convert back to dictionary
    sorted_book_list = {key: value for key, value in books_for_sorting}
    
    display_library(sorted_book_list)

# function for the asc desc option
def sorting_order_options(prompts, choice):
    # prompt user
    print(f"How would you like to sort the {prompts[choice]}?")

    # if choice is title author genre
    while True:
        ### alphabetically
        if choice in ("a", "b", "d"):
            print("A. From A to Z")
            print("B. From Z to A\n")

        ### numerical
        elif choice == "c":
            print("A. Oldest to Newest")
            print("B. Newest to Oldest\n")

        sub_choice = input("Please enter 'A' or 'B' here: ").lower()

        if sub_choice in ("a", "b"):
            return sub_choice
        
        else:
            print(f"'{sub_choice}' is an invalid input. Please try again.")

### MAIN PROGRAMME ###'
def main_programme():
    # welcoming the user
    welcoming_user()

    # loop to keep showing the menu until exit option is chosen
    while True:
        # displaying the menu and prompting user to choose menu
        menu_option = main_menu()
    
        # conditionals for user's menu options
        ### option 1 - view all books
        if menu_option == "1":
            display_library(book_list)
        
        ### option 2 - add a book to the system
        elif menu_option == "2":
            print("You chose option 2")
            add_book()
    
        ### option 3 - search and borrow book
        elif menu_option == "3":
            search_book()
    
        ### option 4 - edit book details
        elif menu_option == "4":
            edit_book()
    
        ### option 5 - delete a book from the system
        elif menu_option == "5":
            delete_book()
    
        ### option 6 - sort books
        elif menu_option == "6":
            sort_book()
    
        ### option 7 - exit programme
        elif menu_option == "7":
            print("You've chosen to close the programme")
            print("Exit Successful")
            break