item_dic = {"Coffee" : 7, "Pen" : 3, "Paper cup": 2, "Milk" : 1, "Coke" : 4, "Book" : 5}

while True:
    # 1

    # 2
    
    if user_input == "1":
        pro_name = input("Enter the name of the product: ")
        if pro_name in item_dic:
            print(f"Inventory of {pro_name} : {item_dic[pro_name]}")
        else:
            print(f"{pro_name} not found in inventory.")
    elif user_input == "2":
        pro_name, qty = input("Enter name and quantity of the product : ").split()
        qty = int(qty) # convert qty
        if pro_name in item_dic: 
            item_dic[pro_name] += qty # increase user_input product.
            print(qty, 'of', pro_name, '(s) added to the inventory.')
        else:
            print(f"{pro_name} not found in inventory.")
    elif user_input == "3" :
        pro_name, qty = input("Enter name and quantity of the product : ").split()
        qty = int(qty) # convert qty
        if pro_name in item_dic: 
            item_dic[pro_name] -= qty # increase user_input product.
            print(qty, 'of', pro_name, '(s) substracted from the inventory.')
        else:
            print(f"{pro_name} not found in inventory.")
    # 3
   
    # 4