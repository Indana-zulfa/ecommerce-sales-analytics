SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers_cleaned c
JOIN orders_cleaned o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
HAVING COUNT(DISTINCT o.order_id) > 2
ORDER BY total_orders DESC;


-- 1. Total Unique Customers

SELECT
    COUNT(DISTINCT customer_unique_id) AS total_unique_customers
FROM customers_cleaned;

-- 2. Customer Distribution by State

SELECT
    customer_state,
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM customers_cleaned
GROUP BY customer_state
ORDER BY total_customers DESC;

-- 3. One-Time vs Repeat Customers

WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers_cleaned c
    JOIN orders_cleaned o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)

SELECT
    CASE
        WHEN total_orders = 1 THEN 'One-Time Customer'
        ELSE 'Repeat Customer'
    END AS customer_type,
    COUNT(*) AS total_customers
FROM customer_orders
GROUP BY customer_type;



-- 4. Repeat Purchase Rate

WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers_cleaned c
    JOIN orders_cleaned o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)

SELECT
    COUNT(*) AS total_customers,

    SUM(
        CASE
            WHEN total_orders > 1 THEN 1
            ELSE 0
        END
    ) AS repeat_customers,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN total_orders > 1 THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS repeat_purchase_rate_pct

FROM customer_orders;



-- 5. Top Customers by Order Count

SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers_cleaned c
JOIN orders_cleaned o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
ORDER BY total_orders DESC
LIMIT 10;


-- 6. Customer Order Frequency

WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers_cleaned c
    JOIN orders_cleaned o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)

SELECT
    total_orders,
    COUNT(*) AS total_customers
FROM customer_orders
GROUP BY total_orders
ORDER BY total_orders;

-- 7. Customers with More Than Two Orders

SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers_cleaned c
JOIN orders_cleaned o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
HAVING COUNT(DISTINCT o.order_id) > 2
ORDER BY total_orders DESC;


-- 8. Monthly Active Customers

SELECT
    strftime('%Y-%m', o.order_purchase_timestamp) AS sales_month,
    COUNT(DISTINCT c.customer_unique_id) AS active_customers
FROM orders_cleaned o
JOIN customers_cleaned c
    ON o.customer_id = c.customer_id
WHERE o.order_purchase_timestamp >= '2016-10-01'
  AND o.order_purchase_timestamp < '2018-09-01'
GROUP BY strftime('%Y-%m', o.order_purchase_timestamp)
ORDER BY sales_month;