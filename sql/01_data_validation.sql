-- 01. DATA VALIDATION
-- Check total rows in all tables

SELECT 'customers_cleaned' AS table_name, COUNT(*) AS total_rows
FROM customers_cleaned

UNION ALL

SELECT 'orders_cleaned', COUNT(*) FROM orders_cleaned

UNION ALL

SELECT 'order_items_cleaned', COUNT(*) FROM order_items_cleaned

UNION ALL

SELECT 'payments_cleaned', COUNT(*) FROM payments_cleaned

UNION ALL

SELECT 'reviews_cleaned', COUNT(*) FROM reviews_cleaned

UNION ALL

SELECT 'products_cleaned', COUNT(*) FROM products_cleaned

UNION ALL

SELECT 'sellers_cleaned', COUNT(*) FROM sellers_cleaned

UNION ALL

SELECT 'geolocation_cleaned', COUNT(*) FROM geolocation_cleaned

UNION ALL

SELECT 'category_translation_cleaned', COUNT(*) FROM category_translation_cleaned;





