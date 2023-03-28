import pandas as pd
from pandas import DataFrame


def load_df_from__csv_file_by_path(file_path: str):
    return pd.read_csv(file_path)


def save_df_as_parquet_partitioned(result_df: DataFrame, root_dir: str,
                                   cols: list[str]):
    result_df.to_parquet(path=root_dir, partition_cols=cols)


def join_DF_by_orderId(df_items: DataFrame, df_orders: DataFrame) -> DataFrame:
    return pd.merge(df_items, df_orders, on="order_id", how="inner")


def select_columns_required_for_items_price_prediction(df: DataFrame) -> DataFrame:
    return df[["order_id", "order_item_id", "product_id", "order_purchase_timestamp"]]

def receive_mean_of_items_for_specific_timestamp(df: DataFrame) -> DataFrame:
    return df.groupby("product_id", "order_purchase_timestamp").mean()

