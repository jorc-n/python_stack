
class store:
    def __init__ (self, name):
        self.name =name
        self.list =[]
        self.producto=product("",50000,"")


    def add_product (self, new_product):
        self.list.append(new_product)
        return self

    def sell_product (self, id):
        print("Productos vendidos: " ,self.list[id])
        self.list.pop(id)
        return self

    def inflation(self, percent_increase):
        self.producto.update_price(percent_increase,True)


class product:

    def __init__(self ,name, price, category):
        self.name =name
        self.price =price
        self.category =category


    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price= self.price + self.price * percent_change/100
            print("nuevo valor ",self.price)
        elif not is_increased:
            self.price = self.price - self.price * percent_change/100
            print("nuevo valor ", self.price)
        return self

    def print_info (self):
        print("Producto: " ,self.name, "Categoria: " ,self.category, "Precio: " ,self.price)
        return self

paris=store("paris")
paris.add_product("camisa").add_product("pantalon").add_product("reloj").add_product("polera").sell_product \
    (2).sell_product(0).inflation(30)

prod =product("reloj",30000,"relojes")
prod.update_price(30,True).print_info()

