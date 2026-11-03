-- Write your query below
select name from sales_person where sales_id not in (
select distinct sales_id from orders
where com_id=(select com_id from company
where name like 'CRIMSON'))