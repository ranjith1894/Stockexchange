from unittest import TestCase
from Order import Order


class TestOrder(TestCase):
    def test_negative_close_order(self):
        self.assertEquals(Order.close_order(self,{"test":"test"}), False)

    def test_positive_close_order(self):
        obj = Order('1', 'BUY','EFG',  '18', 5, 'open')
        obj2 = Order('1', 'BUY', 'EFG', '18', 0, 'closed')
        self.assertEquals(Order.close_order(self,obj), obj2)

    def test_negative_reduce_quantity(self):
        obj = Order('1', 'BUY', 'EFG', '18', 5, 'open')
        quantity = 3
        obj2 = Order('1', 'BUY', 'EFG', '18', 5, 'open')
        self.assertEquals(Order.reduce_quantity(self,obj,quantity), obj2)

    def test_positive_reduce_quantity(self):
        obj = Order('1', 'BUY', 'EFG', '18', 5, 'open')
        quantity = 3
        obj2 = Order('1', 'BUY', 'EFG', '18', 2, 'open')
        self.assertEquals(Order.reduce_quantity(self, obj, quantity), obj2)
        self.assertEquals(Order.load_file('input.csv'), True)
