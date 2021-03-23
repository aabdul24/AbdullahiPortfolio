/* Question 1 */

USE om;

SELECT 
	CONCAT(customer_first_name,', ',customer_last_name) AS 'Customer Name',
	CONCAT('Contact #: ', customer_phone) AS 'Customer Contact Number',
	CONCAT(customer_address,', ', customer_city,', ', customer_state,', ', customer_zip) AS 'Customer Address'
FROM customers
WHERE customer_first_name  < 'f' and customer_last_name > 'b'
ORDER BY customer_last_name;

/* Question 2 */

USE om;

SELECT order_id AS 'Order ID',
	CONCAT(customer_first_name,', ',customer_last_name) AS 'Customer Name',
	order_date, CONCAT(IFNULL (shipped_date, "Not Yet Shipped.")) AS 'Shipped Date'
FROM orders
	JOIN customers
    USING (customer_id)
WHERE order_id >= 773
ORDER BY order_id;

/* Question 3 */

USE ap;

SELECT CONCAT(vendors.vendor_name) AS 'Vendor Name',
	CONCAT(veendor_contacts.first_name,', ', vendor_contacts.last_name) AS 'Contact Full Name',
    CONCAT(invoices.invoice_id) AS 'Invoice ID',
    CONCAT(invoices.invoice_total - invoices.payment_total) AS 'Balance Due'
FROM vendor_contacts
LEFT JOIN vendors
	USING (vendor_id)
LEFT JOIN invoices
	USING(vendor_id)
ORDER BY vendor_name, (invoices.invoice_total - invoices.payment_total - invoices.credit_total);

/* Question 4 */

USE ap;

SELECT terms.term_description, vendors.vendor_state, vendors.vendor_name, vendors.vendor_id
FROM vendors
INNER JOIN terms
	ON vendors.default_terms_id = terms.terms_id
WHERE vendor_state > 'N' and vendor_state < 'R'
ORDER By terms_description, vendor_state, vendor_id, vendor_name






    
    
    
    
    
    