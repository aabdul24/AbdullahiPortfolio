-- AbdulRahman Abdullahi Assignment 3 --

USE my_guitar_shop;

/*Answer 1*/

SELECT COALESCE(product_name, NULL) AS product_name, COUNT(*) AS num_orders, SUM(quantity) AS num_products, CONCAT('$', FORMAT(AVG(discount_amount), 2)) AS avg_discount

FROM Products P, orders O, order_items OI

WHERE O.order_id = OI.order_id AND OI.product_id = P.product_id

GROUP BY product_name WITH ROLLUP;


/*Answer 2*/

SELECT CONCAT('$', list_price) AS 'Product List Price', product_name AS 'Product', description AS 'Description'

FROM products

WHERE list_price <= 
			(SELECT AVG(list_price)
			 FROM products, categories
			 WHERE category_name = 'Guitars')

ORDER BY list_price, product_name;

/*Answer 3*/

SELECT CONCAT(last_name, ', ', first_name) AS 'Customer Name', COUNT(DISTINCT O.order_id) AS num_orders, COUNT(OI.item_id) AS num_items, CONCAT('$', FORMAT(SUM((item_price - discount_amount) + ship_amount + tax_amount), 2)) AS order_total

FROM Customers C, orders O, order_items OI

WHERE O.order_id = OI.order_id AND O.customer_id = C.customer_id AND ship_date IS NOT NULL

GROUP BY C.customer_id, last_name, first_name

ORDER BY order_total  




