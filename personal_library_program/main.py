# this is for myself so i can easily run it in the web browser version of vs code python3 /workspaces/CP2-PROJECTS/PersonalLibraryProgram/main.py
# these are all the lists used in all the functions
types = ()
names = ()
authors = ()
lengths = ()
genres = ()

# this function is for adding items to the library
def add_item_func(types, names, authors, lengths, genres):
    # converting tuple to list
    types = list(types)
    names = list(names)
    authors = list(authors)
    lengths = list(lengths)
    genres = list(genres)

    # main part of function
    for i in range(int(input("How many items do you want to add to your library? "))):
        types.append(input(f"Is item {i+1} a book, or a movie? ").strip().lower())
        names.append(input(f"What is the name of your {types[i]}? ").strip().lower())
        authors.append(input("What is the name of the author? ").strip().lower())
        lengths.append(input(f"How long is the {types[i]}? (enter only as a number) ").strip())
        genres.append(input(f"What genres does the {types[i]} fit into? (format: horror, fiction, historic, etc.) ").strip().lower())

    # converting list back into tuple
    types = tuple(types)
    names = tuple(names)
    authors = tuple(authors)
    lengths = tuple(lengths)
    genres = tuple(genres)

    # Display the updated library
    for i in range(len(names)):
        print(f"\n{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")

    return types, names, authors, lengths, genres

# Function for searching items in the library
def searcher_func(types, names, authors, lengths, genres):
    search_term = input("Enter the name of the item you are searching for: ").strip().lower()
    found = False

    for i in range(len(names)):
        if search_term in names[i]:  # Compare using lowercase (data is stored in lowercase)
            print(f"\n{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")
            found = True

    if not found:
        print("\nNo items found with that name.")

# Function for modifying an item in the library
def modify_func(types, names, authors, lengths, genres):

    types = list(types)
    names = list(names)
    authors = list(authors)
    lengths = list(lengths)
    genres = list(genres)


    search_term = input("Enter the name of the item you want to modify: ").strip().lower()
    found_indexes = []

    for i in range(len(names)):
        if search_term in names[i]:
            print(f"\n{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")
            found_indexes.append(i)

    if not found_indexes:
        print("\nNo items found with that name.")
        return types, names, authors, lengths, genres

    if len(found_indexes) > 1:
        selection = int(input("\nMultiple matches found. Enter the number corresponding to the item you want to modify: ")) - 1
    else:
        selection = found_indexes[0]

    while True:
        print("\nWhat would you like to modify?")
        print("1. Type\n2. Name\n3. Author\n4. Length\n5. Genres\n6. Go back to main menu")
        choice = int(input("Enter the number corresponding to your choice: "))

        if choice == 1:
            types[selection] = input("Enter the new type (book/movie): ").strip().lower()
        elif choice == 2:
            names[selection] = input("Enter the new name: ").strip().lower()
        elif choice == 3:
            authors[selection] = input("Enter the new author: ").strip().lower()
        elif choice == 4:
            lengths[selection] = input("Enter the new length: ").strip()
        elif choice == 5:
            genres[selection] = input("Enter the new genres (format: horror, fiction, etc.): ").strip().lower()
        elif choice == 6:

            print("\nReturning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

        print("\nItem modified successfully!")
        print(f"\n{selection+1}. {names[selection].title()} - {types[selection].title()} by {authors[selection].title()}, Length: {lengths[selection]}, Genres: {genres[selection].title()}")

  
    types = tuple(types)
    names = tuple(names)
    authors = tuple(authors)
    lengths = tuple(lengths)
    genres = tuple(genres)

    return types, names, authors, lengths, genres

# Main function
def main():
    global types, names, authors, lengths, genres
    list_made = 0

    while True:
        print("Where would you like to go? \n(1) Library Maker\n(2) Library Modifier\n(3) Library Searcher\n(4) Library Viewer")
        lib_selection = int(input("\nEnter the number corresponding to your choice: "))

        if lib_selection == 1:
            types, names, authors, lengths, genres = add_item_func(types, names, authors, lengths, genres)
            list_made = 1
        elif lib_selection == 2:
            if list_made != 1:
                print("You need to start a bookshelf before you can modify it. Go to Library Maker to start your library!")
            else:
                types, names, authors, lengths, genres = modify_func(types, names, authors, lengths, genres)
        elif lib_selection == 3:
            if list_made != 1:
                print("You need to start a bookshelf before you can search it. Go to Library Maker to start your library!")
            else:
                searcher_func(types, names, authors, lengths, genres)
        elif lib_selection == 4:
            if list_made !=1:
                print("You need to start a bookshelf before you can view it. Go to Library Maker to start your library!")
            else:
                for i in range(len(names)):
                    print(f"\n{i+1}. {names[i].title()} - {types[i].title()} by {authors[i].title()}, Length: {lengths[i]}, Genres: {genres[i].title()}")

        if int(input("\nWould you like to continue to manage your library?\n\n1. Yes\n\n2. No\n\nEnter the number corresponding to your choice: ")) == 2:
            print("Goodbye! Come again soon")
            break

if __name__ == "__main__":
    main()
