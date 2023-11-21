# Write a class that meets these requirements.
#
# Name:       Receipt
#
# Required state:
#    * tax rate, the percentage tax that should be applied to the total
#
# Behavior:
#    * add_item(item)   # Add a ReceiptItem to the Receipt
#    * get_subtotal()   # Returns the total of all of the receipt items
#    * get_total()      # Multiplies the subtotal by the 1 + tax rate
#
# Example:
#    item = Receipt(.1)
#    item.add_item(ReceiptItem(4, 2.50))
#    item.add_item(ReceiptItem(2, 5.00))
#
#    print(item.get_subtotal())     # Prints 20
#    print(item.get_total())        # Prints 22
class ReceiptItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def get_total(self):
        total = self.price*self.quantity
        return total


class Receipt:
    def __init__(self, tax_rate):
        self.tax_rate = float(tax_rate)
        self.reciept = []

    def add_item(self, item):
        self.reciept.append(item)

    def get_subtotal(self):
        subtotal = 0
        for item in self.reciept:
            subtotal += item.quantity*item.price
        return subtotal

    def get_total(self):
        total = self.get_subtotal() * self.tax_rate + self.get_subtotal()
        return total


item = Receipt(.1)
item.add_item(ReceiptItem(4, 2.50))
item.add_item(ReceiptItem(2, 5.00))

print(item.get_subtotal())     # Prints 20.0
print(item.get_total())        # Prints 22.0
