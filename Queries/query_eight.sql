SELECT t.teacher, AVG(g.grade) AS average_score
FROM teachers t
JOIN subjects sj ON t.subject_id = sj.id
JOIN student_grades g ON sj.id = g.subject_id
WHERE t.teacher = 'Teresa Bennett' 
GROUP BY t.teacher;
