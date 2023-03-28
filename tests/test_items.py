import unittest
import pandas as pd

from main import join_DF_by_orderId


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = {"order_id": [3, 2, 10000]}
        data2 = {"order_id": [3, 2, 10000]}
        df_temp = pd.DataFrame.from_dict(data)
        df_temp2 = pd.DataFrame.from_dict(data2)
        join_DF_by_orderId(df_temp, df_temp2)

        if __name__ == '__main__':
            unittest.main()
