-- 1. Total Products

SELECT
    COUNT(DISTINCT product_id) AS total_products
FROM products_cleaned;

-- 2. Products by Category

SELECT
    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category,

    COUNT(DISTINCT p.product_id) AS total_products

FROM products_cleaned p

LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name

GROUP BY product_category
ORDER BY total_products DESC;


-- 3. Top Selling Products

SELECT
    oi.product_id,

    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category,

    COUNT(*) AS total_items_sold

FROM order_items_cleaned oi

JOIN products_cleaned p
    ON oi.product_id = p.product_id

LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name

GROUP BY
    oi.product_id,
    product_category

ORDER BY total_items_sold DESC
LIMIT 10;



-- 4. Top Products by Revenue

SELECT
    oi.product_id,

    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category,

    COUNT(*) AS total_items_sold,

    ROUND(
        SUM(CAST(oi.price AS REAL)),
        2
    ) AS total_sales_value

FROM order_items_cleaned oi

JOIN products_cleaned p
    ON oi.product_id = p.product_id

LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name

GROUP BY
    oi.product_id,
    product_category

ORDER BY total_sales_value DESC
LIMIT 10;



-- 5. Category Performance

SELECT
    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category,

    COUNT(DISTINCT p.product_id) AS total_products,

    COUNT(DISTINCT oi.order_id) AS total_orders,

    COUNT(*) AS total_items_sold,

    ROUND(
        SUM(CAST(oi.price AS REAL)),
        2
    ) AS total_sales_value

FROM order_items_cleaned oi

JOIN products_cleaned p
    ON oi.product_id = p.product_id

LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name

GROUP BY product_category

ORDER BY total_sales_value DESC;


-- 6. Average Product Selling Price

SELECT
    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category,

    COUNT(*) AS total_items_sold,

    ROUND(
        AVG(CAST(oi.price AS REAL)),
        2
    ) AS average_selling_price

FROM order_items_cleaned oi

JOIN products_cleaned p
    ON oi.product_id = p.product_id

LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name

GROUP BY product_category

ORDER BY average_selling_price DESC;


-- 7. Product Price Distribution

SELECT
    CASE
        WHEN CAST(price AS REAL) < 50 THEN 'Below R$50'
        WHEN CAST(price AS REAL) < 100 THEN 'R$50 - R$99.99'
        WHEN CAST(price AS REAL) < 200 THEN 'R$100 - R$199.99'
        WHEN CAST(price AS REAL) < 500 THEN 'R$200 - R$499.99'
        ELSE 'R$500 and Above'
    END AS price_range,

    COUNT(*) AS total_items,

    ROUND(
        AVG(CAST(price AS REAL)),
        2
    ) AS average_price

FROM order_items_cleaned

GROUP BY price_range

ORDER BY
    CASE price_range
        WHEN 'Below R$50' THEN 1
        WHEN 'R$50 - R$99.99' THEN 2
        WHEN 'R$100 - R$199.99' THEN 3
        WHEN 'R$200 - R$499.99' THEN 4
        ELSE 5
    END;



    -- 8. Category Contribution to Revenue

WITH category_sales AS (
    SELECT
        COALESCE(
            NULLIF(ct.product_category_name_english, ''),
            p.product_category_name,
            'Unknown'
        ) AS product_category,

        SUM(CAST(oi.price AS REAL)) AS total_sales_value

    FROM order_items_cleaned oi

    JOIN products_cleaned p
        ON oi.product_id = p.product_id

    LEFT JOIN category_translation_cleaned ct
        ON p.product_category_name = ct.product_category_name

    GROUP BY product_category
)

SELECT
    product_category,

    ROUND(total_sales_value, 2) AS total_sales_value,

    ROUND(
        100.0 * total_sales_value /
        SUM(total_sales_value) OVER (),
        2
    ) AS revenue_contribution_pct

FROM category_sales

ORDER BY total_sales_value DESC;



-- 9. Products with No Sales

SELECT
    p.product_id,

    COALESCE(
        NULLIF(ct.product_category_name_english, ''),
        p.product_category_name,
        'Unknown'
    ) AS product_category

FROM products_cleaned p

LEFT JOIN order_items_cleaned oi
    ON p.product_id = oi.product_id

LEFT JOIN category_translation_cleaned ct
    ON p.product_category_name = ct.product_category_name

WHERE oi.product_id IS NULL

ORDER BY product_category;