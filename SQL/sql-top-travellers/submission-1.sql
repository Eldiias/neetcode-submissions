-- Write your query below
select u.name, coalesce(d.dd,0) as travelled_distance
from users u
left join (select user_id, sum(distance) as dd
from rides
group by user_id) d
on u.id=d.user_id
order by 2 desc,1