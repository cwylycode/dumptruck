"""
A grocery store linked list challenge that I found on some website. It was supposed to be homework for some college guy apparently, but I decided to do it on my own. LOL.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self,nodes:list):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for obj in nodes:
                node.next_node = Node(data=obj)
                node = node.next_node

    def __str__(self):
        node = self.head
        nodes = []
        i = 0
        while node is not None:
            i += 1
            nodes.append(str(i)+". "+str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def add_start(self,node:Node):
        node.next_node = self.head
        self.head = node

    def add_before(self,node:Node,target_data):
        if not self.head: raise Exception("List is empty")
        if self.head.data == target_data: return self.add_start(node)
        prev_node = self.head
        for this_node in self:
            if this_node.data == target_data:
                prev_node.next_node = node
                node.next_node = this_node
                return
            prev_node = this_node
        raise Exception(f"Node {node.data} not found")

    def add_after(self,node:Node,target_data):
        if not self.head: raise Exception("List is empty")
        for this_node in self:
            if this_node.data == target_data:
                node.next_node = this_node.next_node
                this_node.next_node = node
                return
        raise Exception(f"Node {node.data} not found")

    def add_end(self,node:Node):
        if not self.head:
            self.head = node
            return
        for this_node in self: pass
        this_node.next_node = node

    def remove_node(self, target_data):
        if not self.head: raise Exception("List is empty")
        if self.head.data == target_data:
            self.head = self.head.next_node
            return
        prev_node = self.head
        for node in self:
            if node.data == target_data:
                prev_node.next_node = node.next_node
                return
            prev_node = node
        raise Exception(f"Node {target_data} not found")

def main():
    import os

    current = [
        {"name":"Bubba Farts O'Laught Canned Chili","price":3.99,"stock":8},
        {"name":"Swine Squeal Tasty Bacon","price":7.95,"stock":19},
        {"name":"Lettuce","price":24.99,"stock":341},
        {"name":"Tomato","price":2.99,"stock":427},
        {"name":"Onion","price":1.99,"stock":98},
        {"name":"Potato Chips - Skin Flavor","price":4.99,"stock":277},
        {"name":"Frozen Pizza - Unknown Flavor","price":10.99,"stock":139},
        {"name":"Slap That Bass! Frozen Fishsticks","price":12.95,"stock":295},
        {"name":"Generic Cereal","price":3.99,"stock":69},
        {"name":"Less-Generic Cereal","price":4.99,"stock":43},
        {"name":"Greasy Pete's Premium Deer Semen XL","price":499.99,"stock":1},
        {"name":"It's-a Good-a Past-a - Penne","price":1.69,"stock":94},
        {"name":"It's-a Good-a Past-a - Spaghetti","price":1.69,"stock":87},
        {"name":"Beans","price":0.79,"stock":420}
    ]
    products = LinkedList(current)

    def prompt():
        i = input("\n>")
        return i
    
    def clear_screen():
        os.system("cls") if os.name == "nt" else os.system("clear")

    def pause():
        print("\nPress 'Enter' to continue")
        i = prompt()
    
    def isfloat(string:str):
        try: float(string)
        except ValueError: return False
        return True

    def products_add():
        entries = ["Name","Price","Stock"]
        new_product = {"name":None,"price":None,"stock":None}
        # Product setup
        while True:
            # Entries
            i = 0
            while True:
                clear_screen()
                print(f"\nPlease type in the '{entries[i]}' of the new product:\n")
                usr = prompt()
                if i == 0 and usr:
                    if usr in [p.data["name"] for p in products]:
                        print("\nError: A product with that name already exists.")
                        pause()
                        continue
                    new_product["name"] = str(usr)
                    i += 1
                    continue
                if i == 1 and isfloat(usr):
                    new_product["price"] = round(abs(float(usr)),2)
                    i += 1
                    continue
                if i == 2 and usr.isdigit():
                    new_product["stock"] = int(usr)
                    break
                print(f"\nInvalid entry. Must be a {'whole ' if i == 2 else ''}{'word' if i == 0 else 'number'}.")
                pause()
            # Finalize
            redo = False
            while True:
                clear_screen()
                print(f"\nNew product is:\n\nName: {new_product['name']}\nPrice: ${new_product['price']:,.2f}\nStock: {new_product['stock']}")
                print("\nIs this correct? (Y/N)")
                usr = prompt()
                if usr in ["y","Y","yes","YES","Yes"]:
                    redo = False
                    break
                elif usr in ["n","N","no","NO","No"]:
                    redo = True
                    break
                else:
                    print(f"\nInvalid entry. Must be a something resembling a 'yes' or a 'no'.")
                    pause()
            # Do over or not
            if redo: continue
            else: break
        # Adding to list
        while True:
            clear_screen()
            print("\nWhere should this product be inserted?\n")
            print("1. Beginning of list")
            print("2. End of list")
            print("3. Before other product")
            print("4. After other product")
            print("5. Exit and discard product")
            usr = prompt()
            # Beginning
            if usr == "1":
                products.add_start(Node(new_product))
                break
            # End
            elif usr == "2":
                products.add_end(Node(new_product))
                break
            # Before or After
            elif usr == "3" or usr == "4":
                bfr = True if usr == "3" else False
                while True:
                    plist = products_all(pause_screen=False,data_return=True)
                    print(f"\nPlease select a product to place the new product {'BEFORE' if bfr else 'AFTER'} it.")
                    usr = prompt()
                    if usr.isdigit() and int(usr) in range(1,len(plist)+1):
                        i = int(usr)-1
                        if bfr: products.add_before(Node(new_product),plist[i])
                        else: products.add_after(Node(new_product),plist[i])
                        break
                    else:
                        print(f"\nInvalid entry. Must be a number in range.")
                        pause()
                        continue
                break
            # Exit
            elif usr == "5":
                return
            # Error
            else:
                print("\nInvalid entry!")
                pause()
        # Finished
        clear_screen()
        print("\nThe product has been added.")
        pause()

    def products_all(pause_screen=True,data_return=False):
        clear_screen()
        print(f"\nAll current products:\n")
        l = [p.data for p in products]
        dl = l.copy()
        for i,d in enumerate(l):
            l[i] = f"{str(i+1)+'. '+str(d)}"
        print(*l,sep="\n")
        if pause_screen: pause()
        if data_return: return dl
    
    def products_price():
        clear_screen()
        print("\nPlease enter a price:")
        while True:
            usr = prompt()
            if isfloat(usr) or usr.isdigit(): break
            print("\nInvalid. Must be a number.")
        clear_screen()
        price = abs(float(usr))
        print(f"\nProducts with a price higher than ${price:,.2f}\n")
        l = sorted([p.data for p in products if p.data["price"] > price],key=lambda d: d["price"])
        for i,d in enumerate(l):
            l[i] = f"{str(i+1)+'. '+str(d)}"
        print(*l,sep="\n")
        pause()

    def products_stock():
        clear_screen()
        print(f"\nProducts that are low in stock:\n")
        low = 20
        l = sorted([p.data for p in products if p.data["stock"] < low],key=lambda d: d["stock"])
        for i,d in enumerate(l):
            l[i] = f"{str(i+1)+'. '+str(d)}"
        print(*l,sep="\n")
        pause()

    while True:
        clear_screen()
        print("\nGrocery Inventory\nPlease select an option:\n")
        print("1. Add product")
        print("2. Print all products")
        print("3. Print products above price")
        print("4. Print products low in stock")
        print("5. Exit")
        usr = prompt()
        if usr == "1": products_add()
        elif usr == "2": products_all()
        elif usr == "3": products_price()
        elif usr == "4": products_stock()
        elif usr == "5": break
        else:
            print("\nInvalid entry!")
            pause()
            continue

if __name__ == '__main__':
    main()