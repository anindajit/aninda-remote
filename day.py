import datetime

def get_day_of_week():
    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))

        # Create a date object
        date_obj = datetime.date(year, month, day)
        
        # Get the day name (e.g., Monday, Tuesday)
        day_name = date_obj.strftime("%A")
        
        print(f"The day on {date_obj} is {day_name}.")
        
    except ValueError:
        print("Invalid date. Please enter numeric values for year, month, and day.")

if __name__ == "__main__":
    get_day_of_week()
