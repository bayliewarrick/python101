stores = []

def create_store():
    store_name = input("Enter the store name: ")
    store = {"name": store_name, "items": []}
    stores.append(store)

def display_stores():
    for index in range(0,len(stores)):
        store = stores[index]
        print(f"{index + 1} - {store['name']}")
        items = store["items"]

def display_lists():
    for index in range(0,len(stores)):
        store = stores[index]
        items = store["items"]
        for item in items:
            print(f"{item['name']} - {item['price']}")


   
def add_item_to_store():
    display_stores()
    store_number = int(input("enter store number: ")) - 1
    store = stores[store_number]
    grocery_item_name = input("Enter the name of grocery item: ")
    grocery_item_price = input("Enter price: ")
    
    grocery_item = {"name": grocery_item_name, "price": grocery_item_price}

    store_items = store["items"]
    store_items.append(grocery_item)


while True:
    print("Press 1 to create store")
    print("Press 2 to add item to the store")
    print("Press 3 to view all stores")
    print("Press 4 to view all lists")
    print("Press q to quit")

    choice = input("Enter choice: ")

    if(choice == "1"):
        create_store()
    elif(choice == "3"):
        display_stores()
    elif(choice == "2"):
        add_item_to_store()
    elif(choice == "4"):
        display_lists()
