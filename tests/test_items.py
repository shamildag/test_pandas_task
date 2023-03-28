import unittest
import pandas as pd

from main import join_DF_by_orderId


class MyTestCase(unittest.TestCase):
    def test_joining(self):
        data = {"order_id": [3, 2, 10000], "fruit": ["apple", "banana", "avocado"]}
        data2 = {"order_id": [3, 2, 10000], "phones": ["Motorola", "LG", "Sagem"]}
        df_temp = pd.DataFrame.from_dict(data)
        df_temp2 = pd.DataFrame.from_dict(data2)
        print(join_DF_by_orderId(df_temp, df_temp2))

if __name__ == '__main__':
    unittest.main()
