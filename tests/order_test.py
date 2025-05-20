import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.cust = Customer("Frank")
        self.coffee = Coffee("Macchiato")

    def test_order_initialization(self):
        order = Order(self.cust, self.coffee, 5.0)
        self.assertEqual(order.customer, self.cust)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

        with self.assertRaises(TypeError):
            Order("not customer", self.coffee, 5.0)
        with self.assertRaises(TypeError):
            Order(self.cust, "not coffee", 5.0)
        with self.assertRaises(TypeError):
            Order(self.cust, self.coffee, "not price")

        with self.assertRaises(ValueError):
            Order(self.cust, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.cust, self.coffee, 11.0)

if __name__ == "__main__":
    unittest.main()
