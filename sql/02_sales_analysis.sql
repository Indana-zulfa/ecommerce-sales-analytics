-- ==========================================
-- 02. SALES PERFORMANCE ANALYSIS
-- ==========================================

-- 1. Total Orders

SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM orders_cleaned;

-- 2. Total Items Sold

SELECT
    COUNT(*) AS total_items_sold
FROM order_items_cleaned;


-- 3. Total Sales Value

SELECT
    ROUND(SUM(price), 2) AS total_sales_value
FROM order_items_cleaned;



-- 4. Average Order Value (AOV)

SELECT
    ROUND(SUM(oi.price) / COUNT(DISTINCT o.order_id), 2) AS average_order_value
FROM order_items_cleaned oi
JOIN orders_cleaned o
    ON oi.order_id = o.order_id;



-- 5. Monthly Sales Performance

SELECT
    strftime('%Y-%m', o.order_purchase_timestamp) AS sales_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.price) AS total_sales_value
FROM orders_cleaned o
JOIN order_items_cleaned oi
    ON o.order_id = oi.order_id
WHERE o.order_purchase_timestamp >= '2016-10-01'
  AND o.order_purchase_timestamp < '2018-09-01'
GROUP BY strftime('%Y-%m', o.order_purchase_timestamp)
ORDER BY sales_month;



-- 6. Sales Performance by Product Category

SELECT
    COALESCE(
        ct.product_category_name_english,
        p.product_category_name,
        'Unknown'
    ) AS product_category,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS total_items_sold,
    ROUND(SUM(oi.price), 2) AS total_sales_value
FROM order_items_cleaned oi
JOIN products_cleaned p
    ON oi.product_id = p.product_id
LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name
GROUP BY product_category
ORDER BY total_sales_value DESC
LIMIT 10;



-- 7. Sales Performance by Customer State

SELECT
    c.customer_state,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(oi.price), 2) AS total_sales_value
FROM orders_cleaned o
JOIN customers_cleaned c
    ON o.customer_id = c.customer_id
JOIN order_items_cleaned oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_state
ORDER BY total_sales_value DESC;


-- 8. Sales Performance by Order Status

SELECT
    o.order_status,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(oi.order_item_id) AS total_items,
    ROUND(SUM(oi.price), 2) AS total_sales_value
FROM orders_cleaned o
LEFT JOIN order_items_cleaned oi
    ON o.order_id = oi.order_id
GROUP BY o.order_status
ORDER BY total_sales_value DESC;


