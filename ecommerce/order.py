class Order():
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_items(self, name: str, quantity: int, price: int):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    def pay(self, payment_type: str, security_code: str):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment")
            print(f"Verifying security code: {security_code}")  
            self.status = "paid"      
        else:
            raise Exception(f"Unknown payment type: {payment_type}")
        

abu = Order()
abu.add_items("apples", 2, 20)
abu.add_items("SDD", 2, 50)

print(abu.total_price())
abu.pay("debit", "12334df")