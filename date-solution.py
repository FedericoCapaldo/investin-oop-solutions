# DIFFICULTY LEVEL: Easy (compared to the other exerices, but it's still challenging!)
# SUMMARY: Create a DateStamp class which takes day, month, and year as properties.
#  Then create an object with a date of your choice and print it back with a fucntion.


# 1.0 create DateStamp class
# 1.1 the class should should be initialized with the following properties (all received at object creation)
#   day
#   month
#   year
# 1.2 create a function called get_date(self) in the DateStamp class that return the date in the format dd/mm/yyyy
#   hint: str(number) converts a number to string, you may need this to convert the day, month, year from numbers to string in order to print correctly.
# 1.3 create a function called set_date(self, day, month, year) in the DateStamp class to set a new day, month, year in its respective properties
class DateStamp:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self,):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

    def set_date(self, new_day, new_month, new_year):
        self.day = new_day
        self.month = new_month
        self.year = new_year

if __name__ == "__main__":
    print("hello, world!")

    # 2. create a DateStamp object called dateOne
    #  (initialize the object with day, month, year of your choice)
    dateOne = DateStamp(18, 7, 1980)

    # 3. print the date of dateOne
    print(dateOne.get_date())

    # 4. give dateOne a new day, month, year
    dateOne.set_date(25, 12, 2022)

    # 5. print again the date of dateOne
    print(dateOne.get_date())
