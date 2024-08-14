select 
	code, 
	name,
	birth_date,
	country_code, 
	discipline, 
	event
from 
	master_table 
where 
	birth_date in (
					select max(birth_date) from master_table
				   );