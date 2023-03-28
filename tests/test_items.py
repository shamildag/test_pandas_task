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

    def test_something2(self):
        # creating the first DataFrame
        df1 = pd.DataFrame({"fruit": ["apple", "banana", "avocado"],
                            "market_price": [21, 14, 35]})
        print("The first DataFrame")
        print(df1)

        # creating the second DataFrame
        df2 = pd.DataFrame({"fruit": ["banana", "apple", "avocado"],
                            "wholesaler_price": [65, 68, 75]})
        print("The second DataFrame")
        print(df2)

        # joining the DataFrames
        print("The merged DataFrame")
        print(pd.merge(df1, df2, on="fruit", how="inner"))


if __name__ == '__main__':
    unittest.main()
