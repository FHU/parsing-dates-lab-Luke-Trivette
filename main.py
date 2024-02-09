#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)

def parse_month(month):
    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    return month_dict.get(month, "Invalid Month")

def parse_date(user_string):
    x = user_string.split(" ")
    month = parse_month(x[0])
    day = x[1][:-1].zfill(2) 
    year = x[2]
    return f"{month}/{day}/{year}"

# REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_input = input("Enter a date (e.g., January 18, 2024): ")
    formatted_date = parse_date(user_input)
    print("Formatted date:", formatted_date)

