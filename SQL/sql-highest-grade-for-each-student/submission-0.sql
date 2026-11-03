select e.student_id, min(exam_id) as exam_id, score
from exam_results e
inner join 
(select student_id, max(score) as sc from exam_results
group by student_id) em
on e.student_id=em.student_id and e.score=em.sc
group by e.student_id, score