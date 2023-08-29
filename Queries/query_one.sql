SELECT s.student, AVG(g.grade) AS average_gpa
FROM students s
JOIN student_grades g ON s.id = g.student_id
GROUP BY s.student
ORDER BY average_gpa DESC
LIMIT 5;
