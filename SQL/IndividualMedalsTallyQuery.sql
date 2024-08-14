select 
	Top 5 name, 
	country_full, 
	count(distinct event) as medals_won
from master_table
where team is null 
group by 
	name, 
	country_full
order by 
	medals_won desc, 
	sum(medal_code);