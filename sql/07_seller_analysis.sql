
-- =====================================================
-- 07. SELLER ANALYSIS
-- Brazilian E-Commerce Public Dataset by Olist
-- =====================================================


-- 1. Total Sellers
SELECT
    COUNT(DISTINCT seller_id) AS total_sellers
FROM sellers_cleaned;


-- 2. Seller Distribution by State
SELECT
    seller_state,
    COUNT(DISTINCT seller_id) AS total_sellers
FROM sellers_cleaned
GROUP BY seller_state
ORDER BY total_sellers DESC;


-- 3. Top 10 Sellers by Total Orders
SELECT
    s.seller_id,
    s.seller_state,
    COUNT(DISTINCT oi.order_id) AS total_orders
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_id, s.seller_state
ORDER BY total_orders DESC
LIMIT 10;


-- 4. Top 10 Sellers by Items Sold
SELECT
    s.seller_id,
    s.seller_state,
    COUNT(*) AS total_items_sold
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_id, s.seller_state
ORDER BY total_items_sold DESC
LIMIT 10;


-- 5. Top 10 Sellers by Sales Value
SELECT
    s.seller_id,
    s.seller_state,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS total_items_sold,
    ROUND(SUM(oi.price), 2) AS total_sales_value
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_id, s.seller_state
ORDER BY total_sales_value DESC
LIMIT 10;


-- 6. Average Item Price by Seller
SELECT
    s.seller_id,
    s.seller_state,
    ROUND(AVG(oi.price), 2) AS average_item_price,
    COUNT(*) AS total_items_sold
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_id, s.seller_state
ORDER BY average_item_price DESC
LIMIT 10;


-- 7. Seller Sales Performance by State
SELECT
    s.seller_state,
    COUNT(DISTINCT s.seller_id) AS total_sellers,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS total_items_sold,
    ROUND(SUM(oi.price), 2) AS total_sales_value
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_state
ORDER BY total_sales_value DESC;


-- 8. Average Freight Value by Seller State
SELECT
    s.seller_state,
    COUNT(*) AS total_items_sold,
    ROUND(AVG(oi.freight_value), 2) AS average_freight_value,
    ROUND(SUM(oi.freight_value), 2) AS total_freight_value
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_state
ORDER BY average_freight_value DESC;






-- 9. Product Category Diversity by Seller
SELECT
    s.seller_id,
    s.seller_state,
    COUNT(DISTINCT p.product_category_name)
        AS total_product_categories,
    COUNT(DISTINCT oi.product_id) AS total_products_sold,
    COUNT(*) AS total_items_sold
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
JOIN products_cleaned p
    ON oi.product_id = p.product_id
GROUP BY s.seller_id, s.seller_state
ORDER BY total_product_categories DESC,
         total_products_sold DESC
LIMIT 10;


-- 10. Sellers with No Sales
SELECT
    s.seller_id,
    s.seller_state
FROM sellers_cleaned s
LEFT JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
WHERE oi.seller_id IS NULL
ORDER BY s.seller_id;


SELECT
    s.seller_state,
    COUNT(*) AS total_order_items,
    COUNT(oi.price) AS non_null_prices,
    SUM(oi.price) AS total_sales_value
FROM sellers_cleaned s
JOIN order_items_cleaned oi
    ON s.seller_id = oi.seller_id
WHERE s.seller_state = 'AC'
GROUP BY s.seller_state;