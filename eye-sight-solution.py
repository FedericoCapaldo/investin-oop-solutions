# DIFFICULTY LEVEL: Medium
# SUMMARY: Create a Customer class and EyesightTest class, so that each customer
#  can keep track of their eyesight appointment history.
# IMPORTANT: Follow the correct order of the instructions to create you program successfully!


# 1.0 Create a Customer class
# 1.1 the class should be initialized with the following properties (only name is received during object creation)
#   name
#   eye_sight_visits (just an empty list)
# 1.2 create a function called say_hello(self) in the Customer class that prints "Hi, my name is" + the name of customer
# 6. create a function in the Customer class called 'save_eyesight_test(self, new_test)' that stores a new test in the eye_sight_visits property
# 8. create a function that returns all the eyesight tests (i.e. eye_sight_visits)
class Customer:

    def __init__(self, name):
        self.name = name
        self.eye_sight_visits = []

    def say_hello(self):
        print("Hi, my name is", self.name)

    def save_eyesight_test(self, new_test):
        self.eye_sight_visits.append(new_test)

    def get_all_tests(self):
        return self.eye_sight_visits


# 3.0 Create class EyesightTest
# 3.1 the class should be initialized with the following properties (all received at object creation)
#   short_sightedness (it is measured from 0 - perfert eye - until -10.00)
#   astigmatism (it is measured from 0 - perfect eye - until 20.00)
#   test_date (e.g. '15/04/2020')
# 3.2 create a function in the EyesightTest class that returns a summary of the test with all it's info
class EyesightTest:

    def __init__(self, short_sightedness, astigmatism, test_date):
        self.short_sightedness = short_sightedness
        self.astigmatism = astigmatism
        self.test_date = test_date

    def get_results(self):
        return "Test Date: " + str(self.test_date) + " \n" \
            "Short Sightedness value: " + str(self.short_sightedness) + " \n" + \
            "Astigmatism value: " + str(self.astigmatism)


if __name__ == "__main__":
    print("hello, world")

    # 2.0 create a customer object jenny
    #  initialize this object with name 'jenny'
    jenny = Customer('Jenny')

    # 2.1 make jenny say hello (verify that this prints out on the screen)
    jenny.say_hello()

    # 4. create and EyeTest object test1
    # initialize this object with the desired values (hopefully our customer has good sight!),
    # the date of the test should be sometime in 2020
    test1 = EyesightTest(0, 0.5, '15/04/2020')

    # 5. create and EyeTest object test2
    # initialize this object with the desired values (perhaps our customer sight worsened a bit!),
    # the date of the test should be sometime in 2022
    test2 = EyesightTest(-1, 0.5, '15/04/2022')

    # 7. add both tests to the current customer
    jenny.save_eyesight_test(test1)
    jenny.save_eyesight_test(test2)

    # 9. print a summary of each test for the customer jenny
    jenny_eyesight_test = jenny.get_all_tests()

    for single_test in jenny_eyesight_test:
        print(single_test.get_results())
