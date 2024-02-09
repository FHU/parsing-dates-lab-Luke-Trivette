#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)

def parse_month(month):
    if month == "January":
        return "1"
    if month == "Feburary":
        return "2"
    if month == "March":
        return "3"
    if month == "April":
        return "4"
    if month == "May":
        return "5"
    if month == "June":
        return "6"
    if month == "July":
        return "7"
    if month == "August":
        return "8"
    if month == "September":
        return "9"
    if month == "October":
        return "10"
    if month == "November":
        return "11"
    if month == "December":
        return "12"


def parse_date(user_string):
    x = user_string.split(" ")
    month = x[1]
    return (parse_month(month),"/",x[2],"/",x[3])

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    print(parse_date(input()))