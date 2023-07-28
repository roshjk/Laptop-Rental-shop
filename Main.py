from Read import *#importing different modules
from Write import *
from Operation import *


def read_stock():
    stock = []#inatilizes an empty list
    with open("database.txt", "r") as f:
        for line in f:
            stock.append(line.strip().split(", "))
    return stock




def main():
    stock = read_stock()

    while True: #printing the format for table generation
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("\t\t\t\t\t_________________________________")
        print("\t\t\t\t\t|\tHorwin Electronics\t|")
        print("\t\t\t\t\t_________________________________")
        #print("\n")
        print("\t\t\t\t\t|\t California,USA\t\t|")
        print("\t\t\t\t\t_________________________________")
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("-------------------------------------------------------------------------------------------------------------------------")
        print("\t \t \t\t Welcome to Horwin Electronics ! How can i Help you?")
        print("-------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        #display_stock(stock)
        print("*************************************************************************************************************************")
        print("*\t Menu:\t\t\t\t\t\t\t\t\t\t\t\t\t\t*")
        print("*\t 1. Sell to Customer\t\t\t\t\t\t\t\t\t\t\t\t*")
        print("*\t 2. Purchase from Wholesaler\t\t\t\t\t\t\t\t\t\t\t*")
        print("*\t 3. Quit \t\t\t\t\t\t\t\t\t\t\t\t\t*" )
        print("*************************************************************************************************************************")


        while True:
            try:
                option = int(input("Choose an option: "))
                break
            except ValueError:#It displays an error message if the user gives invalid input
                print("Invalid input. Please enter a valid option number.")

        if option == 1:#This option 
            display_stock(stock)#Display function to display the stock
            while True:
                try:
                    laptop_name = int(input("Enter laptop SN.: "))
                    validate_id = True
                    break
                except ValueError:#It disolays an error message if the user gives invalid input
                    print("Invalid input. Please enter a valid laptop serial number.")

            customer_name = input("Enter customer name: ")

            while True:
                try:
                    shipping_cost = int(input("Enter shipping cost: "))
                    break
                except ValueError:#It disolays an error message if the user gives invalid input
                    print("Invalid input. Please enter a valid shipping cost.")

            while True:
                try:
                    amount = int(input("Enter how many laptops are being sold: "))
                    break
                except ValueError:#It disolays an error message if the user gives invalid input
                    print("Invalid input. Please enter a valid quantity.")

            while True:
                try:
                    address =input("Enter the address of the costomer: ")
                    break
                except ValueError:#It displays an error message if the user gives invalid input
                    print("Invalid input. Please enter a valid address.")       

            sell_laptop(stock, laptop_name, customer_name, shipping_cost, amount, address)
        elif option == 2:
            display_stock(stock)
            laptop_name = input("Enter laptop name: ")
            brand = input("Enter brand: ")

            while True:
                try:
                    price = int(input("Enter price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")

            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")

            distributor = input("Enter distributor: ")
            processor = input("Enter processor: ")
            graphics = input("Enter graphics card: ")
            order_laptops(stock, laptop_name, brand, price, quantity, processor, graphics, distributor)
        elif option == 3:
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main() 