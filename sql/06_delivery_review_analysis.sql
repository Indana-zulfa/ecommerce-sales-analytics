
-- =====================================================
-- 06. DELIVERY & REVIEW ANALYSIS
-- Brazilian E-Commerce Public Dataset by Olist
-- =====================================================


-- 1. Order Distribution by Status
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders_cleaned
GROUP BY order_status
ORDER BY total_orders DESC;


-- 2. Average Delivery Time
SELECT
    ROUND(
        AVG(
            julianday(order_delivered_customer_date) -
            julianday(order_purchase_timestamp)
        ), 2
    ) AS average_delivery_days
FROM orders_cleaned
WHERE order_delivered_customer_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL
  AND julianday(order_delivered_customer_date) >=
      julianday(order_purchase_timestamp);


-- 3. Estimated vs Actual Delivery Time
SELECT
    ROUND(
        AVG(
            julianday(order_estimated_delivery_date) -
            julianday(order_purchase_timestamp)
        ), 2
    ) AS average_estimated_delivery_days,
    ROUND(
        AVG(
            julianday(order_delivered_customer_date) -
            julianday(order_purchase_timestamp)
        ), 2
    ) AS average_actual_delivery_days
FROM orders_cleaned
WHERE order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL
  AND julianday(order_delivered_customer_date) >=
      julianday(order_purchase_timestamp);


-- 4. On-Time vs Late Delivery
SELECT
    CASE
        WHEN julianday(order_delivered_customer_date) <=
             julianday(order_estimated_delivery_date)
        THEN 'On-Time'
        ELSE 'Late'
    END AS delivery_performance,
    COUNT(*) AS total_orders
FROM orders_cleaned
WHERE order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
GROUP BY delivery_performance
ORDER BY total_orders DESC;


-- 5. Average Delivery Delay
SELECT
    ROUND(
        AVG(
            julianday(order_delivered_customer_date) -
            julianday(order_estimated_delivery_date)
        ), 2
    ) AS average_delivery_delay_days
FROM orders_cleaned
WHERE order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
  AND julianday(order_delivered_customer_date) >
      julianday(order_estimated_delivery_date);


-- 6. Delivery Performance by Customer State
SELECT
    c.customer_state,
    COUNT(o.order_id) AS delivered_orders,
    ROUND(
        AVG(
            julianday(o.order_delivered_customer_date) -
            julianday(o.order_purchase_timestamp)
        ), 2
    ) AS average_delivery_days
FROM orders_cleaned o
JOIN customers_cleaned c
    ON o.customer_id = c.customer_id
WHERE o.order_delivered_customer_date IS NOT NULL
  AND o.order_purchase_timestamp IS NOT NULL
  AND julianday(o.order_delivered_customer_date) >=
      julianday(o.order_purchase_timestamp)
GROUP BY c.customer_state
ORDER BY average_delivery_days DESC;


-- 7. Review Score Distribution
SELECT
    review_score,
    COUNT(*) AS total_reviews
FROM reviews_cleaned
GROUP BY review_score
ORDER BY review_score DESC;


-- 8. Average Customer Review Score
SELECT
    ROUND(AVG(review_score), 2) AS average_review_score,
    COUNT(*) AS total_reviews
FROM reviews_cleaned
WHERE review_score IS NOT NULL;


-- 9. Review Score by Delivery Performance
SELECT
    CASE
        WHEN julianday(o.order_delivered_customer_date) <=
             julianday(o.order_estimated_delivery_date)
        THEN 'On-Time'
        ELSE 'Late'
    END AS delivery_performance,
    COUNT(r.review_id) AS total_reviews,
    ROUND(AVG(r.review_score), 2) AS average_review_score
FROM orders_cleaned o
JOIN reviews_cleaned r
    ON o.order_id = r.order_id
WHERE o.order_delivered_customer_date IS NOT NULL
  AND o.order_estimated_delivery_date IS NOT NULL
  AND r.review_score IS NOT NULL
GROUP BY delivery_performance
ORDER BY average_review_score DESC;


-- 10. Review Score by Product Category
SELECT
    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category,
    COUNT(DISTINCT r.review_id) AS total_reviews,
    ROUND(AVG(r.review_score), 2) AS average_review_score
FROM reviews_cleaned r
JOIN order_items_cleaned oi
    ON r.order_id = oi.order_id
JOIN products_cleaned p
    ON oi.product_id = p.product_id
LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name
WHERE r.review_score IS NOT NULL
GROUP BY product_category
ORDER BY average_review_score DESC;
