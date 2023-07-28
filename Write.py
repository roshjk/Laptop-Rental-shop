import datetime
#Writing a function to update the stocks
def update_stock(stock):
    with open("database.txt", "w") as f:
        for item in stock:
            f.write(", ".join(item) + "\n")


def generate_invoice_number():
    return str(datetime.datetime.now().timestamp()).replace(".", "")