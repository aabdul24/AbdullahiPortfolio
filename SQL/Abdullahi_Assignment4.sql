-- Assignment_4_Abdullahi --

/* Question 1 */

USE ForestGlenInn;

CREATE VIEW guest_who_have_weekend_reservations AS 

	SELECT guest_id, first_name, last_name, check_in_date, check_out_date
    
	FROM guests, reservations
    
	WHERE reservation.check_in_date = "Friday to Sunday only"; 

/* Question 2 */

USE ForestGlenInn;

CREATE VIEW guest_who_have_weekend_reservations AS 

	SELECT guest_id, first_name, last_name, check_in_date, check_out_date
    
	FROM guests, reservations
    
	WHERE reservation.check_in_date = "More than three days";

