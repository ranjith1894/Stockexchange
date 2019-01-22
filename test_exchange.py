from unittest import TestCase
from Exchange import Exchange


class TestExchange(TestCase):
    def test_negative_execute_order(self):
        self.assertEquals(Exchange.execute_order(self,{"test":"test"}), False)

    def test_positive_execute_order(self):
        obj = Order('1', 'BUY','EFG',  '18', 5, 'open')
        obj2 = Order('1', 'BUY', 'EFG', '18', 0, 'closed')
        self.assertEquals(Exchange.execute_order(self,obj), obj2)
