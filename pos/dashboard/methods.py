from dashboard.models import Products, Customers, Orders
from login.models import Users


class methods:
    # Class variable
    species = "Canis familiaris"

    # Constructor method (initializer)
    def __init__(self):
        # Instance variables
        name = "Just"
        age = 12
        pass

    # Insert products
    @staticmethod
    def insert_product(db, name, price, date, distributor):
        # Create a new Product instance
        new_product = Products(Name=name, Price=price, DateAdded=date, Distributor=distributor)

        # Save the new product to the database
        new_product.save()
        # print("Product name = "+name+" Price :"+price+" Date:"+ str(date)+" Distro:"+distributor)
        return 1

    # add customer
    @staticmethod
    def insert_customer( db, name, lName, phone, email, street, town, city, PCode):
        # Create a new Product instance
        new_product = Customers(Name=name, LastName=lName, Phone=phone, Email=email, Street=street, Town=town, City=city, PostalCode=PCode)

        # Save the new product to the database
        new_product.save()
        return 1

    # insert order
    @staticmethod
    def createOrder(customer_id, product_id, order_date, status, qty):
        # Create a new Product instance
        new_order = Orders(CustomerId=customer_id, ProductId=product_id, OrderDate=order_date, Status=status, Qty=qty)

        # Save the new product to the database
        new_order.save()

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Another instance method
    def get_human_years(self):
        return self.age * 7


# Creating instances of the Dog class
method = methods()
