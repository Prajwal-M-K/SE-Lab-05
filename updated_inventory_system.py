import json
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    #Add qty of item to stock_data
    if logs is None:
        logs = []
    if not item:
        raise ValueError("Item must be non-empty.")
    if qty < 0:
        raise ValueError("Quantity must be positive.")
    
    stock_data[item] = stock_data.get(item,0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    
def removeItem(item, qty):
    #Remove qty of item from stock_data
    if qty < 0:
        raise ValueError("Quantity must be positive.")
    
    if item not in stock_data:
        raise KeyError(f"Item {item} not found in stock.")

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]

def getQty(item):
    #Return quantity for item, or 0 if not found
    return stock_data.get(item,0)

def loadData(file="inventory.json"):
    #Load inventory from JSON and return as dictionary
    with open(file, "r") as f:
        return json.load(f)

def saveData(file="inventory.json"):
    #Save current stock_data to JSON file
    with open(file, "w") as f:
        json.dump(stock_data, f,indent=2)

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    try:
        loaded = loadData()
        if isinstance(loaded, dict):
            stock_data.clear()
            stock_data.update(loaded)
    except FileNotFoundError:
        print("Inventory file not found, starting fresh.")
    #Removed unsafe eval
    print("eval call removed for safety.")

main()
