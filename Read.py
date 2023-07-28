def find_laptop(stock, laptop_name): #finds laptop
    for item in stock:
        if item[0] == laptop_name:
            return item
    return None


def read_stock():
    stock = []
    with open("database.txt", "r") as f: #open to read mode
        for line in f:
            stock.append(line.strip().split(", "))
    return stock