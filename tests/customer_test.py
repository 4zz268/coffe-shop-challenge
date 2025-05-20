import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):

    def test_name_setter_getter(self):
        cust = Customer("Owen")
        self.assertEqual(cust.name, "Owen")
        with self.assertRaises(TypeError):
            cust.name = 123
        with self.assertRaises(ValueError):
            cust.name = ""

    def test_orders_and_coffees(self):
        cust = Customer("Anna")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Latte")
        order1 = cust.create_order(coffee1, 4.5)
        order2 = cust.create_order(coffee2, 5.0)

        self.assertIn(order1, cust.orders())
        self.assertIn(order2, cust.orders())
        self.assertIn(coffee1, cust.coffees())
        self.assertIn(coffee2, cust.coffees())

    def test_most_aficionado(self):
        cust1 = Customer("Amy")
        cust2 = Customer("Ben")
        coffee = Coffee("Espresso")

        cust1.create_order(coffee, 3.0)
        cust1.create_order(coffee, 2.0)
        cust2.create_order(coffee, 6.0)

        top = Customer.most_aficionado(coffee)
        self.assertEqual(top, cust2)

        # No orders case
        coffee2 = Coffee("Latte")
        self.assertIsNone(Customer.most_aficionado(coffee2))

if __name__ == "__main__":
    unittest.main()
