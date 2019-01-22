"""
@author: ranjithctlr@gmail.com
@date:22/01/2018
"""


class Order:
    def __init__(self, stock_id, side, company_name, total_quantity, remaining_quantity, status):
        self.stock_id = stock_id
        self.side = side
        self.company_name = company_name
        self.total_quantity = total_quantity
        self.remaining_quantity = remaining_quantity
        self.status = status

    def close_order(self,order):
        """
        This function is used to change the status of an order to closed and
        remaining quantity to zero
        :param order:
        :return:order
        """
        if hasattr(order, 'remaining_quantity'):
            order.remaining_quantity = 0
            order.status = 'closed'
            return order
        else:
            return False

    def reduce_quantity(self,order,quantity):
        """
        This is method is used to reduce a specific quantity from an order
        :param order:
        :param quantity:
        """
        order.remaining_quantity = int(order.remaining_quantity) - int(quantity)
        return order




