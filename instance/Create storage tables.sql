CREATE TABLE User (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255),
    name VARCHAR(255),
    company VARCHAR(255)
);

CREATE TABLE Roles (
    roleId INT PRIMARY KEY,
    roleName VARCHAR(255)
);

CREATE TABLE UserRoles (
    userId INT,
    roleId INT,
    PRIMARY KEY (userId, roleId),
    FOREIGN KEY (userId) REFERENCES User(id),
    FOREIGN KEY (roleId) REFERENCES Roles(roleId)
);

CREATE TABLE Warehouse (
    id INT PRIMARY KEY,
    location VARCHAR(255),
    name VARCHAR(255),
    managerId INT,
    maxCapacity DOUBLE, -- m^2
    currentCapacity DOUBLE, -- m^2
    storageCost DOUBLE, -- per m^2
    FOREIGN KEY (managerId) REFERENCES User(id)
);

CREATE TABLE Orders (
    id INT PRIMARY KEY,
    userId INT,
    orderedProducts JSON,
    totalAmount DOUBLE,
    orderStatus BOOLEAN,
    warehouseId INT,
    orderDate DATETIME,
    FOREIGN KEY (userId) REFERENCES User(id),
    FOREIGN KEY (warehouseId) REFERENCES Warehouse(warehouseId)
);

CREATE TABLE Product (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    price DOUBLE,
    quantityInStock INT,
    unitOfMeasure VARCHAR(50),
    description TEXT
);

CREATE TABLE PaymentTransaction (
    id INT PRIMARY KEY,
    orderId INT,
    status VARCHAR(50),
    paymentMethod VARCHAR(50),
    paymentDate DATETIME,
    FOREIGN KEY (orderId) REFERENCES Orders(id)
);

CREATE TABLE Notification (
    id INT PRIMARY KEY,
    userId INT,
    message VARCHAR(255),
    timestamp DATETIME,
    FOREIGN KEY (userId) REFERENCES User(id)
);

CREATE TABLE Report (
    id INT PRIMARY KEY,
    reportType VARCHAR(50),
    content JSON,
    creationDate DATETIME
);
