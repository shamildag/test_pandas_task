# Test task for pandas
Dataset can be pulled from here, data schema available as well: Brazilian E-Commerce Public Dataset by Olist

Task: We want to forecast for each item, what are the sales going to be next week.

Expected output is repository that has the following:

Code to load relevant tables for the task (minimum tables needed), and prepare efficient ETL that builds a dataset on which Data Scientist can continue the work (use pandas)
The output should be in parquet, well partitioned by product
The format of output is a single table that can be used for modelling (no need to extract features).
python script to run code, that you can pass arguments to
A couple of simple pytest tests, and run them in github.com actions at every PR.
Configuration files in yml
Think about the following:
Which features would you extract and how from the tables? How would you use the remaining tables?
How would you turn it into an application in production?
How would you design an application if you knew that you would have to build a similar solution for a couple other countries, and the data schema might be different for them, however, you can get the same underlying data?
If the task takes too long time, prepare pseudocode how you would do these. Simplifications are fine.

The dataset consist of 9 tables

olist_order_items_dataset ("order_id","order_item_id","product_id","seller_id","shipping_limit_date","price","freight_value")
olist_customers_dataset("customer_id","customer_unique_id","customer_zip_code_prefix","customer_city","customer_state")
olist_geolocation_dataset("geolocation_zip_code_prefix","geolocation_lat","geolocation_lng","geolocation_city","geolocation_state")
olist_order_payments_dataset("order_id","payment_sequential","payment_type","payment_installments","payment_value")
olist_order_reviews_dataset("review_id","order_id","review_score","review_comment_title","review_comment_message","review_creation_date","review_answer_timestamp")
olist_orders_dataset("order_id","customer_id","order_status","order_purchase_timestamp","order_approved_at","order_delivered_carrier_date","order_delivered_customer_date","order_estimated_delivery_date")
olist_products_dataset ("product_id","product_category_name","product_name_lenght","product_description_lenght","product_photos_qty","product_weight_g","product_length_cm","product_height_cm","product_width_cm")
olist_sellers_dataset("seller_id","seller_zip_code_prefix","seller_city","seller_state")
product_category_name_translation (product_category_name,product_category_name_english)
Some difficulty was to understand what does the term item mean. After looking through the olist_order_items_dataset and the response from the team , the answer is that item means unit of product inside the order from specific seller. The order can have the same items from different sellers. So the table has composite key ("order_id", "product_id","seller_id","order_item_id"). The aim of tasks can be reformulated as ***how many units of product are expected to be sold in the next week".

There are several approaches to forecast selling of item (Opportunity Stage Forecasting, Length of Sales Cycle Forecasting, Historical Forecasting, Lead Pipeline Forecasting,
Test Market Analysis Forecasting(A/B testing), Multivariable Analysis) It seems that Historical Forecasting will be used.

I. Which features would you extract and how from the tables? How would you use the remaining tables?

The minimal DATA required for this contains product , items, time of order.
This can be achieved by joining tables olist_order_items_dataset, olist_orders_dataset. Unfortunately olist_products_dataset contains only params of product and the category in which product belongs to. It helps us to predict how many items will be solved based of previous year's result and depends on season factor.

But there are also another scenarios for analysis data: what is the top seller for specific product ? what is its shipment cost (freight_value)? for every product find a location where it is the most popular product?

II. How would you turn it into an application in production?

Not sure that streaming approach is required here. It seems the batching mode with appending for processing incoming data will be enough. The no reason for using Deltahouse approach with ACID under cloud object storage. The common Data Lake approach where new data in CSV format will be added in timeline manner in object storage and scheduled ETL will be invoked to process them and add to existing data in parquet format for future using.

III. How would you design an application if you knew that you would have to build a similar solution for a couple other countries, and the data schema might be different for them, however, you can get the same underlying data?

Here I am in doubt as the statement of this question is not clear. How can be data be the same for different countries? At least geolocation and customers datasets will be different.

For distributed processing environment like Spark the best way is to collocate all tables, omit unused columns. Also instead of joining at first stage, broadcasting of lookup table like olist_sellers_dataset, olist_products_dataset and product_category_name_translation to simplifying joining operation shall be used. But not sure for situation with pure Python with pandas library. So any ETL will be done from the scratch without any semi-processed result from another ETL. For experimenting manually with data the collab jupiter notebook was used.