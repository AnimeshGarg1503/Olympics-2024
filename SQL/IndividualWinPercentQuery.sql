select 
	Top 5 country_code, 
	round(100.0*count(*)/max(total),2) as individual_win_percent, 
	max(total) as total_medals
from (
		select 
			distinct country_code, 
			name, 
			event, 
			total 
		from master_table 
		where team is null
	) as cte
group by country_code
order by total_medals desc
