CREATE TABLE order_test_cases(
    id INT PRIMARY KEY,
    product_id VARCHAR(10)
    quantity INT,
    expected_total DECIMAL(10,2)

)
INSERT INTO order_test_cases VALUES
(1, 'FI-SW-01', 2, 36.00),
(2, 'K9-DL-01', 1, 18.50);
print(order_test_cases)