-- -- Fill Roles table
-- INSERT INTO Roles (roleId, roleName) VALUES
-- (1, 'customer'),
-- (2, 'manager'),
-- (3, 'admin');

-- -- Fill User table
-- INSERT INTO User (id, username, password, email, name, company) VALUES
-- (1, 'customer1', 'password1', 'customer1@example.com', 'Customer One', 'Company A'),
-- (2, 'customer2', 'password2', 'customer2@example.com', 'Customer Two', 'Company B'),
-- (3, 'customer3', 'password3', 'customer3@example.com', 'Customer Three', 'Company C'),
-- (4, 'manager1', 'password4', 'manager1@example.com', 'Manager One', 'storageSystems'),
-- (5, 'admin1', 'password5', 'admin1@example.com', 'Admin One', 'storageSystems');

-- -- Fill UserRoles table
-- INSERT INTO UserRoles (userId, roleId) VALUES
-- (1, 1),  -- Customer One (customer role)
-- (2, 1),  -- Customer Two (customer role)
-- (3, 1),  -- Customer Three (customer role)
-- (4, 2),  -- Manager One (manager role)
-- (5, 3);  -- Admin One (admin role)

-- -- Fill Product table
-- INSERT INTO Product (id, name, category, price, quantityInStock, unitOfMeasure, description) VALUES
-- (1, 'Product A', 'Category 1', 20.99, 50, 'pcs', 'Description for Product A'),
-- (2, 'Product B', 'Category 2', 15.50, 30, 'pcs', 'Description for Product B'),
-- (3, 'Product C', 'Category 1', 10.75, 25, 'pcs', 'Description for Product C'),
-- (4, 'Product D', 'Category 3', 30.25, 40, 'pcs', 'Description for Product D'),
-- (5, 'Product E', 'Category 4', 18.99, 20, 'pcs', 'Description for Product E'),
-- (6, 'Product F', 'Category 2', 25.00, 15, 'pcs', 'Description for Product F'),
-- (7, 'Product G', 'Category 1', 22.50, 60, 'pcs', 'Description for Product G'),
-- (8, 'Product H', 'Category 3', 17.99, 10, 'pcs', 'Description for Product H'),
-- (9, 'Product I', 'Category 4', 12.75, 30, 'pcs', 'Description for Product I'),
-- (10, 'Product J', 'Category 1', 28.50, 45, 'pcs', 'Description for Product J'),
-- (11, 'Product K', 'Category 2', 14.99, 55, 'pcs', 'Description for Product K'),
-- (12, 'Product L', 'Category 3', 19.25, 5, 'pcs', 'Description for Product L'),
-- (13, 'Product M', 'Category 4', 23.00, 35, 'pcs', 'Description for Product M'),
-- (14, 'Product N', 'Category 1', 16.75, 25, 'pcs', 'Description for Product N'),
-- (15, 'Product O', 'Category 2', 32.50, 0, 'pcs', 'Description for Product O');


-- -- Fill Warehouse table
-- INSERT INTO Warehouse (id, location, name, managerId, maxCapacity, currentCapacity, storageCost) VALUES
-- (1, 'Location A', 'Warehouse 1', 4, 1000.00, 500.00, 2.50),
-- (2, 'Location B', 'Warehouse 2', 4, 1500.00, 800.00, 3.00);

-- -- Fill Orders table
-- INSERT INTO Orders (id, userId, orderedProducts, totalAmount, orderStatus, warehouseId, orderDate) VALUES
-- (1, 1, '[{"productId": 1, "quantity": 2}, {"productId": 3, "quantity": 1}]', 52.73, 'Delivered', 1, '2023-01-10 08:30:00'),
-- (2, 2, '[{"productId": 2, "quantity": 3}, {"productId": 5, "quantity": 2}]', 77.00, 'Pending', 2, '2023-01-11 10:15:00'),
-- (3, 3, '[{"productId": 4, "quantity": 1}, {"productId": 6, "quantity": 4}]', 160.50, 'Canceled', 1, '2023-01-12 12:45:00'),
-- (4, 1, '[{"productId": 8, "quantity": 2}, {"productId": 10, "quantity": 3}]', 122.25, 'Shipped', 2, '2023-01-13 14:30:00'),
-- (5, 2, '[{"productId": 11, "quantity": 1}, {"productId": 13, "quantity": 2}]', 45.48, 'Ready to pick up', 1, '2023-01-14 16:00:00'),
-- (6, 3, '[{"productId": 14, "quantity": 3}, {"productId": 15, "quantity": 1}]', 60.25, 'Delivered', 2, '2023-01-15 18:30:00');

-- -- Fill PaymentTransaction table
-- INSERT INTO PaymentTransaction (id, orderId, status, paymentMethod, paymentDate) VALUES
-- (1, 1, 'Success', 'Credit Card', '2023-01-10 09:00:00'),
-- (2, 2, 'Success', 'PayPal', '2023-01-11 11:00:00'),
-- (3, 3, 'Success', 'Bank Transfer', '2023-01-12 13:00:00'),
-- (4, 4, 'Success', 'Credit Card', '2023-01-13 15:00:00'),
-- (5, 5, 'Success', 'PayPal', '2023-01-14 17:00:00'),
-- (6, 6, 'Success', 'Cash', '2023-01-15 19:00:00');


-- -- Fill Notification table for order statuses
-- -- User 1 notifications
-- INSERT INTO Notification (id, userId, message, timestamp) VALUES
-- (1, 1, 'Your order with id 1 is Delivered', '2023-01-10 09:30:00'),
-- (2, 1, 'Your order with id 4 is Shipped', '2023-01-13 15:30:00');

-- -- User 2 notifications
-- INSERT INTO Notification (id, userId, message, timestamp) VALUES
-- (3, 2, 'Your order with id 2 is Pending', '2023-01-11 11:30:00'),
-- (4, 2, 'Your order with id 5 is Ready to pick up', '2023-01-14 17:30:00');


-- -- Fill Report table with a report on current inventory
-- INSERT INTO Report (id, reportType, content, creationDate) VALUES
-- (1, 'Inventory Report', '{"Product A": 50, "Product B": 30, "Product C": 25, "Product D": 40, "Product E": 20, "Product F": 15, "Product G": 60, "Product H": 10, "Product I": 30, "Product J": 45, "Product K": 55, "Product L": 5, "Product M": 35, "Product N": 25, "Product O": 0}', '2023-01-16 10:00:00');
