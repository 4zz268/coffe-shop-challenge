import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):

    def test_name_validation(self):
        coffee = Coffee("Americano")
        self.assertEqual(coffee.name, "Americano")
        with self.assertRaises(TypeError):
            Coffee(123)
        with self.assertRaises(ValueError):
            Coffee("aa")

    def test_orders_and_customers(self):
        coffee = Coffee("Flat White")
        cust1 = Customer("Chris")
        cust2 = Customer("Dana")

        order1 = cust1.create_order(coffee, 3.5)
        order2 = cust2.create_order(coffee, 4.0)

        self.assertIn(order1, coffee.orders())
        self.assertIn(order2, coffee.orders())
        self.assertIn(cust1, coffee.customers())
        self.assertIn(cust2, coffee.customers())

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Cappuccino")
        cust = Customer("Eve")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0)

        cust.create_order(coffee, 4.0)
        cust.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 5.0)

if __name__ == "__main__":
    unittest.main()
