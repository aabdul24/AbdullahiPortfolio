/* Question 1 */

USE my_guitar_shop;
SELECT * FROM order_items;

drop table if exists order_items_copy;
drop table if exists products_copy;

create table order_items_copy as select * from order_items;
create table products_copy as select * from products;

/* Question 2 */

USE my_guitar_shop;

insert into products (category_id, product_code, product_name,
description, list_price, discount_percent, date_added)
values(4, 'PP5B', 'Yamaha P45B',
	'The P45B is an 88-note weighted-keyboard digital piano', 519.99, 10.00, '2019-06-26');

/* Question 3 */

USE my_guitar_shop;

insert into orders (order_id, product_id, item_price, discount_amount, quantity)
values(9, 4, 519.99, 51.99, 2);

/* Question 4 */

USE my_guitar_shop;

UPDATE products
SET list_price =598.00, discount_percent = 15.0
WHERE category_id = 4 AND product_code = 'PP5B' AND product_name = 'Yamaha P45B';

/* Question 5 */

USE my_guitar_shop;

UPDATE order_items
SET item_price = 349.50
WHERE product_id = 5;

/* Question 6 */

SET sql_safe_updates = 0;

USE my_guitar_shop;

DELETE FROM orders WHERE 

--- DELETE FROM customers WHERE ship_address_id = 






    
    
    
    
    
    