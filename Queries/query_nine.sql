SELECT sj.subject
FROM students s
JOIN student_grades g ON s.id = g.student_id
JOIN subjects sj ON g.subject_id = sj.id
WHERE s.student = 'Melanie Lara'
GROUP BY sj.subject;
