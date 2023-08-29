SELECT AVG(g.grade) AS average_score
FROM student_grades AS g
JOIN students AS st ON g.student_id = st.id
JOIN subjects AS s ON g.subject_id = s.id
JOIN teachers AS t ON s.id = t.subject_id
WHERE st.student = 'Michael Valdez' 
  AND t.teacher = 'Teresa Bennett'; 
