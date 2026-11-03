select seller_name 
from seller s
where s.seller_id not in ( select seller_id 
from orders o
where EXTRACT(year from sale_date)=2020)
order by 1