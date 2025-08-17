def main():
    print("Rainfall Calculator\n" + "-" * 20)
    
    # Input validation for years
    while True:
        try:
            years = int(input("Enter number of years: "))
            if years > 0: break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a number.")

    total_rainfall = 0.0
    months_per_year = 12

    # Outer loop: Years
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        # Inner loop: Months
        for month in range(1, months_per_year + 1):
            month_name = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ][month - 1]
            
            # Input validation for rainfall
            while True:
                try:
                    rainfall = float(input(f"  Rainfall for {month_name} (inches): "))
                    if rainfall >= 0: break
                    print("Rainfall cannot be negative.")
                except ValueError:
                    print("Invalid input. Enter a number.")
            total_rainfall += rainfall

    # Results
    total_months = years * months_per_year
    average = total_rainfall / total_months
    
    print("\nResults:")
    print(f"  Total Months: {total_months}")
    print(f"  Total Rainfall: {total_rainfall:.2f} inches")
    print(f"  Average per Month: {average:.2f} inches")

if __name__ == "__main__":
    main()