SELECT first_name, last_name, city, state
FROM person p
left join address a
on p.person_id=a.person_id
