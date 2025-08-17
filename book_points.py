def book_points_calculator():
    print("\nCSU Global Book Club Points Calculator")
    print("-----------------------------------")
    
    # Get number of books with validation
    while True:
        try:
            books = int(input("Enter number of books purchased this month: "))
            if books >= 0:
                break
            print("Number of books cannot be negative.")
        except ValueError:
            print("Please enter a valid integer.")

    # Calculate points
    if books == 0:
        points = 0
    elif books == 2:
        points = 5
    elif books == 4:
        points = 15
    elif books == 6:
        points = 30
    elif books >= 8:
        points = 60
    else:
        points = 0  # For 1,3,5,7 books (not specified in requirements)

    # Display results
    print(f"\nYou have earned {points} points this month!")
    
    # Additional feedback
    if points == 0 and books > 0:
        print("Note: No points awarded for purchasing", books, 
              "book(s). Consider purchasing 2, 4, 6 or 8+ books to earn points.")

if __name__ == "__main__":
    book_points_calculator()