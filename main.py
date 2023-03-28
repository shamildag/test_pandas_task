from pandas import DataFrame

from items.item_utils import load_df_from__csv_file_by_path, join_DF_by_orderId, save_df_as_parquet_partitioned, \
    select_columns_required_for_items_price_prediction, add_additional_date_column

dataset_list = ["olist_order_items_dataset", "olist_customers_dataset", "olist_geolocation_dataset",
                "olist_order_payments_dataset", "olist_order_reviews_dataset",
                "olist_orders_dataset", "olist_products_dataset", "olist_sellers_dataset",
                "product_category_name_translation"]

# main method plays role of ETL
if __name__ == '__main__':
    storage_place: str = "C:/tmp/"
    df_items = load_df_from__csv_file_by_path("archive/olist_order_items_dataset.csv")
    df_orders = load_df_from__csv_file_by_path("archive/olist_orders_dataset.csv")
    result: DataFrame = join_DF_by_orderId(df_items, df_orders)
    selected_result = select_columns_required_for_items_price_prediction(result)

    #add additional date column
    # with_data_col = add_additional_date_column(selected_result)
    # print(with_data_col)
    # save as parquet indexed by product_id and timestamp
    columns: list[str] = ["product_id", "order_purchase_timestamp"]
    save_df_as_parquet_partitioned(result, storage_place, columns)
