"""
created by Daiji Kuriakose
Date:19/11/2024
program to create a list in a market and find higest stock value and item name
"""
inventory=[
    ("laptop",5,30000.00),
    ("Headphone",15,500.00),
    ("Mouse",50,150.00),
    ("Keyboard",20,150.00),
    ("Monitor",10,3000)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(f"Item name:{item_name},The stock value is:{stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"Higest stock value is {highest_stock_value}")
print(f"Item with higest stock value is: {item_with_highest_stock_value}")