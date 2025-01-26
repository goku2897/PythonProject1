#Python program to convert the month name to a number of days.

month_name = input("Please enter a month name: ").capitalize()

def convert_month_to_days(month_name):

    if month_name in ["Jan","March","May","July","August","October","December"]:
        return 31
    elif month_name in ["April","June","September","November"]:
        return 30
    elif month_name == "Feb":
        return 28
    else:
        print("Please enter a valid month name")


print(convert_month_to_days(month_name))



