CREATE DATABASE food_order_system;
USE food_order_system;

CREATE TABLE users(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
email VARCHAR(100)
);

CREATE TABLE food_items(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
price FLOAT
);

CREATE TABLE orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT,
food_id INT,
quantity INT,
order_date DATE
);