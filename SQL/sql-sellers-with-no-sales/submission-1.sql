select seller_name 
from seller s
where s.seller_id not in ( select seller_id from (select EXTRACT(year from sale_date) y, seller_id
from orders o
)where y=2020)
order by 1