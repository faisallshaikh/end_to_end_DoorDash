## Data Science Project

### `Project Topic` - Delivery Duration Prediction

### Problem Statement

When a consumer places an order on DoorDash, we show the expected time of delivery. It is very important for DoorDash to get this right, as it has a big impact on consumer experience. In this exercise, we will build a model to predict the `estimated time taken for a delivery`.

Specifically : we will create a model that will predict the total delivery duration in seconds 
i.e. the time taken from 

• Start - the time consumer submits the order to

• End - When the order will be delivered to the consumer 

### `Dataset Description and its Attributes`

The attached file `historical_data.csv` contains a subset of deliveries received at DoorDash in early 2015 in a subset of the cities. Each row in this file corresponds to one unique delivery. 

#### `Note` - 
All Money (dollar) values given in dataset are in cents and all the time duarion values given are in seconds

Each column corresponds to a feature as explained below : 

### Time features 
• `market_id` - A city/region in which DoorDash operates
• `created_at`: when the order was submitted by the consumer to DoorDash
• `actual_delivery_time`: when the order was delivered to the consumer

### Store features

• `store_id`: an id representing the restaurant the order was submitted for 
• `store_primary_category`: cuisine category of the restaurant, e.g., italian, asian
• `order_protocol`: a store can receive orders from DoorDash through many modes. This field represents an id denoting the protocol.

### Order features

• `total_items`: total number of items in the order
• `subtotal`: total value of the order submitted (in cents)
• `num_distinct_items`: number of distinct items included in the order
• `min_item_price`: price of the item with the least cost in the order (in cents)
• `max_item_price`: price of the item with the highest cost in the order (in cents)

### Market features

The following features are values at the time of created_at (order submission time):

• `total_onshift_dashers`: Number of available dashers who are within 10 miles of the store at the time of order creation
• `total_busy_dashers`: Subset of above total_onshift_dashers who are currently working on an order
• `total_outstanding_orders`: Number of orders within 10 miles of this order that are currently being processed.


