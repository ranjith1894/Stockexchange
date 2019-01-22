"""
@author: ranjithctlr@gmail.com
@date:22/01/2018
"""

from Order import Order

class Exchange:
    def __init__(self,orders):
        self.orders = orders

    def execute_order(self, stock_orders):
        """
        This function is used to execute new order with existing stock orders
        :param stock_orders:
        :return stock_orders:
        """
        new_order = stock_orders[-1]
        iteration = 0
        for each_order in stock_orders:
            if each_order.company_name == new_order.company_name and each_order.status != 'closed' and each_order.side != new_order.side:
                if int(new_order.remaining_quantity) > int(each_order.remaining_quantity):
                    Order.reduce_quantity(self,new_order,each_order.remaining_quantity)
                    Order.close_order(self,stock_orders[iteration])
                elif int(each_order.remaining_quantity) > int(new_order.remaining_quantity):
                    Order.reduce_quantity(self, stock_orders[iteration], new_order.remaining_quantity)
                    Order.close_order(self,new_order)
                elif int(each_order.remaining_quantity) == int(new_order.remaining_quantity):
                    Order.close_order(self,new_order)
                    Order.close_order(self,stock_orders[iteration])
            iteration += 1
        return stock_orders


