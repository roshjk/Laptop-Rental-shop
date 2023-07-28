import time#importing different necessary modules
import datetime
from Read import *
from Write import *
from Main import *

def find_laptop_for_order(stock, laptop_name, brand, processor, graphics):
    for item in stock:
        if item[0] == laptop_name and item[1] == brand and item[4] == processor and item[5] == graphics:
            return item
    return None #finding laptops to order

def order_laptops(stock, laptop_name, brand, price, quantity,  processor, graphics, distributor):
    laptop = find_laptop_for_order(stock, laptop_name, brand, processor, graphics)
    if laptop is None:
        laptop = [laptop_name, brand, str(price), "0", processor, graphics]
        stock.append(laptop)

    laptop_quantity = int(laptop[3])
    laptop[3] = str(laptop_quantity + quantity)
    laptop[2] = str(price)
    update_stock(stock)#updating stock after ordering laptops

    net_amount = price * quantity
    vat_amount = net_amount * 0.13
    gross_amount = net_amount + vat_amount
    invoice_number = generate_invoice_number()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")#getting date and time

    print("\n\n------------------------Purchase details------------------------\n\n")
    print(f"Invoice Number: {invoice_number}") #Bill generation process
    print(f"Date/Time: {timestamp}")
    print(f"Distributor: {distributor}\n")

    print("{:<25} {:<25} {:<25}\n".format("Laptop", "Quantity", "Unit Price"))
    print("{:<25} {:<25} {:<25}\n".format(laptop[0]+"("+laptop[1]+")", quantity, "$"+str(price)))

    print(f"Net Amount: ${net_amount}")
    print(f"VAT Amount: ${vat_amount}")
    print(f"Gross Amount: ${gross_amount}\n")
    print("----------------------------------------------------------------")  

    with open(f"invoice_{invoice_number}.txt", "w") as f:
        f.write("\n\n------------------------Purchase details------------------------\n\n")
        f.write(f"Invoice Number: {invoice_number}\n") #making a txt file for bill generation and adding the details
        f.write(f"Date/Time: {timestamp}\n")
        f.write(f"Distributor: {distributor}\n\n")

        f.write("{:<25} {:<25} {:<25}\n".format("Laptop", "Quantity", "Unit Price"))
        f.write("{:<25} {:<25} {:<25}\n".format(laptop[0]+"("+laptop[1]+")", quantity, "$"+str(price)))

        f.write(f"\nNet Amount: ${net_amount}\n")
        f.write(f"VAT Amount: ${vat_amount}\n")
        f.write(f"Gross Amount: ${gross_amount}\n")
        f.write("----------------------------------------------------------------")
        f.close()

    input("Press enter to continue: ")

def generate_invoice_number():
    return str(datetime.datetime.now().timestamp()).replace(".", "")

def display_stock(stock):
    i = 0
    print("Laptops in stock: \n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("SN", "Laptop-Name", "Brand", "Price", "Quantity", "Processor", "Graphics"))
    print("-----------------------------------------------------------------------------------------------------------------------------")
    for item in stock:
        i+=1
        print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(i, item[0], item[1], item[2]+"$", item[3], item[4], item[5]))
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("\n")


def sell_laptop(stock, sn, customer_name, shipping_cost, amount,address):
    if sn > len(stock):
        print("Invalid choice")
        time.sleep(3)
        return

    laptop = stock[sn-1]

    laptop_quantity = int(laptop[3])
    if laptop_quantity <= 0:
        print("Laptop out of stock.")
        return
    if laptop_quantity < amount:
        print("We're sorry! You want to Purchase more than we have in Stock.")
        return

    laptop[3] = str(laptop_quantity - amount)
    update_stock(stock)

    price = int(laptop[2])*amount
    total_cost = int(laptop[2])*amount + shipping_cost
    invoice_number = generate_invoice_number()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n\n------------------------Sales details-----------------------------------------\n\n")
    print(f"\t Invoice Number: {invoice_number}")#bill generation process
    print(f"\t Date/Time: {timestamp}")
    print(f"\n")
    print(f"\t Customer Name: {customer_name}\n")
    print(f"\t Address:{address}\n")

    print("\t {:<25} {:<25} {:<25}\n".format("Laptop", "Quantity", "Unit Price"))
    print("\t {:<25} {:<25} {:<25}\n".format(laptop[0]+"("+laptop[1]+")", amount, "$"+laptop[2]))

    print(f"\t Total Price: ${price}")
    print(f"\t Shipping: ${shipping_cost}")
    print(f"\t Total Cost: ${total_cost}\n")
    print("--------------------------------------------------------------------------------")


    with open(f"invoice_{invoice_number}.txt", "w") as f: # making a txt file for bill generation and adding the details
        f.write("\n\n------------------------Sales details-----------------------------------\n\n")
        f.write(f"\t Invoice Number: {invoice_number}\n")
        f.write(f"\t Date/Time: {timestamp}\n")
        f.write(f"\n")
        f.write(f"\t Customer Name: {customer_name}\n\n")
        f.write(f"\t Address: {address}\n\n")

        f.write("\t {:<25} {:<25} {:<25}\n".format("Laptop", "Quantity", "Unit Price"))
        f.write("\t {:<25} {:<25} {:<25}\n".format(laptop[0]+"("+laptop[1]+")", amount, "$"+laptop[2]))

        f.write(f"\tTotal Price: ${price}\n")
        f.write(f"\t Shipping: ${shipping_cost}\n")
        f.write(f"\t Total Cost: ${total_cost}\n")
        f.write("-----------------------------------------------------------------------------")
        f.close()

    input("Do you want to continue?(y/n): ").lower()
 