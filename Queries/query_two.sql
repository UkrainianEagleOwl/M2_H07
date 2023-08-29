SELECT s.student, AVG(g.grade) AS average_gpa
FROM students s
JOIN student_grades g ON s.id = g.student_id
JOIN subjects sj ON g.subject_id = sj.id
WHERE sj.subject = 'Mathematics'
GROUP BY s.student
ORDER BY average_gpa DESC
LIMIT 1;
