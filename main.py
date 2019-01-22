"""
@author: ranjithctlr@gmail.com
@date:15/01/2018
"""
import csv
from Order import Order
from Exchange import Exchange

def load_file(file_name):
    """
    This is the main function  used to read input csv file and execute stock order
    :param file_name:
    """
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        stock_orders = []
        if csv_reader:
            for row in csv_reader:
                if line_count != 0:
                    new_order_obj = Order(row[0], row[1], row[2], row[3], row[3], 'open')
                    stock_orders.append(new_order_obj)
                    if stock_orders:
                        stock_orders = Exchange.execute_order(new_order_obj, stock_orders)

                line_count += 1
            if stock_orders:
                for row in stock_orders:
                    print(row.stock_id,row.company_name,row.side,row.total_quantity,row.remaining_quantity,row.status)
                return True
            else:
                return False
        else:
            return False
load_file('input.csv')