import pandas as pd
from pandas import DataFrame

dataset_list = ["olist_order_items_dataset", "olist_customers_dataset", "olist_geolocation_dataset",
                "olist_order_payments_dataset", "olist_order_reviews_dataset",
                "olist_orders_dataset", "olist_products_dataset", "olist_sellers_dataset",
                "product_category_name_translation"]


def join_DF_by_orderId(df_items: DataFrame, df_orders: DataFrame) -> DataFrame:
    # df = pd.read_csv(file_items)
    # df_order = pd.read_csv(file_orders).astype(str)
    # res_df = df[["product_id", "order_item_id", "order_id"]].astype(str)
    # print(df.dtypes)3
    # print(df_order.dtypes)
    # pd.merge(df_temp2, df_temp, left_on="order_id", right_index=True,
    #          how='left', sort=False)
    # result: DataFrame = res_df.groupby("product_id").sum("order_item_id")
    return df_items.join(df_orders, on="order_id")
    # print(result)
    # return df_temp
    # res3.join(file_orders, on="order_id")
    # Press the green button in the gutter to run the script.


def load_df_from__csv_file_by_path(file_path: str):
    return pd.read_csv(file_path)


def save_df_as_parquet_partitioned(result_df: DataFrame, root_dir: str,
                                   cols: list[str]):
    result_df.to_parquet(path=root_dir, partition_cols=cols)


if __name__ == '__main__':
    storage_place: str = "./"
    df_items = load_df_from__csv_file_by_path("archive/olist_order_items_dataset.csv")
    df_orders = load_df_from__csv_file_by_path("archive/olist_orders_dataset.csv")
    result: DataFrame = join_DF_by_orderId(df_items, df_orders)
    columns: list[str] = ["product_id"]
    # save_df_as_parquet_partitioned(result,storage_place, columns)
    print(result)
