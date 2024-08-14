select  
	a.code, 
	a.name, 
	a.gender,
	a.country_code, 
	a.country_full,
	a.birth_date, 
	m.medal_date,
	m.medal_type,
	m.medal_code,
	m.discipline,
	m.event,
	m.team, 
	mt.Gold,
	mtt.gold_21,
	mt.Silver,
	mtt.silver_21,
	mt.Bronze,
	mtt.bronze_21,
	mt.total,
	mtt.total_21
into master_table
from athletes a 
join medallists m on a.code = m.code
join medals_total mt on a.country_code = mt.country_code
left join medals_total_tokyo mtt on a.country_code = mtt.country_code
 
