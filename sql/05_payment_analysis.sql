
-- =====================================================
-- 05. PAYMENT ANALYSIS
-- Brazilian E-Commerce Public Dataset by Olist
-- =====================================================


-- 1. Total Payment Transactions
SELECT
    COUNT(*) AS total_payment_transactions
FROM payments_cleaned;


-- 2. Payment Method Distribution
SELECT
    payment_type,
    COUNT(*) AS total_transactions
FROM payments_cleaned
GROUP BY payment_type
ORDER BY total_transactions DESC;


-- 3. Total Payment Value by Payment Method
SELECT
    payment_type,
    ROUND(SUM(payment_value), 2) AS total_payment_value
FROM payments_cleaned
GROUP BY payment_type
ORDER BY total_payment_value DESC;


-- 4. Average Payment Value by Payment Method
SELECT
    payment_type,
    ROUND(AVG(payment_value), 2) AS average_payment_value
FROM payments_cleaned
GROUP BY payment_type
ORDER BY average_payment_value DESC;


-- 5. Payment Installment Distribution
SELECT
    payment_installments,
    COUNT(*) AS total_transactions
FROM payments_cleaned
GROUP BY payment_installments
ORDER BY payment_installments;


-- 6. Average Installments by Payment Method
SELECT
    payment_type,
    ROUND(AVG(payment_installments), 2) AS average_installments,
    COUNT(*) AS total_transactions
FROM payments_cleaned
GROUP BY payment_type
ORDER BY average_installments DESC;


-- 7. Total Payment Value per Order
SELECT
    order_id,
    ROUND(SUM(payment_value), 2) AS total_order_payment
FROM payments_cleaned
GROUP BY order_id
ORDER BY total_order_payment DESC
LIMIT 10;


-- 8. Payment Method Contribution
SELECT
    payment_type,
    ROUND(SUM(payment_value), 2) AS total_payment_value,
    ROUND(
        SUM(payment_value) * 100.0 /
        (SELECT SUM(payment_value) FROM payments_cleaned),
        2
    ) AS payment_contribution_percentage
FROM payments_cleaned
GROUP BY payment_type
ORDER BY payment_contribution_percentage DESC;


-- 9. Payment Summary by Order
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(*) AS total_payment_records,
    ROUND(SUM(payment_value), 2) AS total_payment_value,
    ROUND(AVG(payment_value), 2) AS average_payment_per_record
FROM payments_cleaned;


-- 10. Orders with Multiple Payment Methods
SELECT
    order_id,
    COUNT(DISTINCT payment_type) AS payment_method_count,
    GROUP_CONCAT(DISTINCT payment_type) AS payment_methods,
    ROUND(SUM(payment_value), 2) AS total_payment_value
FROM payments_cleaned
GROUP BY order_id
HAVING COUNT(DISTINCT payment_type) > 1
ORDER BY payment_method_count DESC, total_payment_value DESC
LIMIT 20;
