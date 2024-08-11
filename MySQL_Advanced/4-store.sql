-- Script that create a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER `decrease_order` AFTER INSERT
ON `orders` FOR EACH ROW item
SET quantity = quantity - New.number
WHERE name = New.item_name