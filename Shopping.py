class Product:
    def __init__(self,P_name,quantity,P_id):
        self.P_name = P_name
        self.quantity = quantity
        self.P_id = P_id
        
class Shop:
    
    def __init__(self):   
        self.add = []  
    def add_product(self,product):
        self.add.append(product)    
        # print('product successfully added')
    def buy_product(self,name):
        flag = False
        for items in self.add:
            if items.P_name == name:
                if  items.quantity > 0:
                    items.quantity -= 1
                    print(items.quantity)
                    print(f'Your {name} purchase has been successful.')
                    return
                else:
                    print(f'Sorry, {name} is out of stock.')
                    # flag = True
            # print(items.quantity)
        print(f'{name} are not available.')
        # if flag:
        #     print(f'Your {name} purchase has been successful.')
        # else:
        #     print(f'{name} are not available.')
p1 = Product('Mango',3,'M45')
p2 = Product('Orange',7,'O85')
p3 = Product('Apple',1,'A55')
            
Rajin = Shop()

Rajin.add_product(p1)
Rajin.add_product(p2)
Rajin.add_product(p3)

Rajin.buy_product('Mango')
Rajin.buy_product('Apple')
Rajin.buy_product('Apple')