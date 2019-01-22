from unittest import TestCase
from Stock import Stock

class TestStock(TestCase):
    def test_negative_load_file(self):
        #non csv file
        self.assertEquals(Stock.load_file('test.txt'), False)

    def test_positive_load_file(self):
        self.assertEquals(Stock.load_file('input.csv'), True)

    def test_write_file(self):
        s_obj = Stock()
        s_obj.stock_id ='3'
        s_obj.company_name ='ABC'
        s_obj.side ='buy'
        s_obj.total_quantity ='12'

        objList=[]


        s_obj1 = Stock()
        s_obj1.stock_id = '3'
        s_obj1.company_name = 'XYZ'
        s_obj1.side = 'buy'
        s_obj1.total_quantity = '12'
        objList.append(s_obj1)


        s_obj2 = Stock()
        s_obj2.stock_id = '3'
        s_obj2.company_name = 'ABC'
        s_obj2.side = 'sell'
        s_obj2.total_quantity = '15'
        objList.append(s_obj2)
        self.assertEqual(Stock.execute_order(s_obj,objList))
    #     self.fail()
    #
    # def test_execute_order(self):
    #     self.fail()
    #
    # def test_load_file(self):
    #     self.fail()
