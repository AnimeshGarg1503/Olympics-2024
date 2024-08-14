select 
	gender, 
	No_of_athletes_2024, 
	case 
		when gender like 'Male' then (
										select count(*) as No_of_athletes_2020
										from athletes_tokyo							
										group by gender
										having gender like 'Male'
										)
				when gender like 'Female' then (
										select count(*) as No_of_athletes_2020
										from athletes_tokyo							
										group by gender
										having gender like 'Female'
										)		
	end as No_of_athletes_2020
from (
		select gender, count(*) as No_of_athletes_2024
		from athletes
		where gender is not null
		group by gender
) as cte   
