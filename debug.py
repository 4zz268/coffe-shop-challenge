from customer import Customer
from coffee import Coffee

def main():
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")

    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    order1 = cust1.create_order(coffee1, 3.5)
    order2 = cust1.create_order(coffee2, 4.0)
    order3 = cust2.create_order(coffee1, 5.0)

    print(f"{cust1.name} ordered coffees: {[c.name for c in cust1.coffees()]}")
    print(f"{coffee1.name} has {coffee1.num_orders()} orders, average price: {coffee1.average_price():.2f}")

    top = Customer.most_aficionado(coffee1)
    if top:
        print(f"Top spender on {coffee1.name} is {top.name}")
    else:
        print(f"No top spender on {coffee1.name}")

if __name__ == "__main__":
    main()
