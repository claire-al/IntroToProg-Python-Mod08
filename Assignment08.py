# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Claire Lynch,12.8.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CLynch,12.8.2020,Modified code to complete assignment 8
    """
    def __init__(self, product_name: str, product_price: float):
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value:str):
        if str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.__product_price = float(value) #cast to float
        else:
            raise Exception("Prices must be numbers")

    # -- Methods -- #
    def to_string(self):
        """ alias of __str__(), converts product data to string """
        return self.__str__()

    def __str__(self):
        """ Converts product data and price to string """
        return self.product_name + "," + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): Saves products
        and prices to txt file

        read_data_from_file(file_name): Reads products and prices from txt file

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CLynch,12.8.2020,Modified code to complete assignment 8
    """
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Saves products and prices to the txt file

        :param list_of_product_objects: list of products and prices
        :return: True/False if data was successfully written to file
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep="\n")
        return success_status

    def read_data_from_file(file_name):
        """ Reads products and prices from txt file

        :return: list of rows of products/prices from txt file
        """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep="\n")
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Handles user input and output:

    methods:
        print_menu_Tasks(): Prints menu options

        input_menu_choice(): Handles user choice from menu options

        print_current_products_in_list(list_of_rows: list): Shows current
        products/prices in list

        input_new_product_and_price(): Asks user for product/price info
        to input

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CLynch,12.8.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show current data
            2) Add a new product
            3) Save current data
            4) Exit program
            ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_rows: list):
        """ Shows the current products in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products and Prices are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        """ Asks the user for product and price information

        :return: The product/price info the user inputs
        """
        try:
            product = str(input("What is the name of the product? ").strip())
            price = float(input("How much does the product cost? ").strip())
            print()
            input_data = Product(product_name=product, product_price=price)
        except Exception as e:
            print(e)
        return input_data;

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while (True):
        IO.print_menu_Tasks()
        strChoice = IO.input_menu_choice()

        if strChoice.strip() == '1': #show current data
            IO.print_current_products_in_list(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2': #add a new product
            lstOfProductObjects.append(IO.input_new_product_and_price())
            continue
        elif strChoice.strip() == '3': #save data
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue
        elif strChoice.strip() == '4': #exit program
            break
except Exception as e:
    print("There was an error! Check file permissions!")
    print(e, e.__doc__, type(e), sep="\n")

# Main Body of Script  ---------------------------------------------------- #

