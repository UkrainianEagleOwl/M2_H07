SELECT DISTINCT s.subject
FROM students AS st
JOIN student_grades AS g ON st.id = g.student_id
JOIN subjects AS s ON g.subject_id = s.id
JOIN teachers AS t ON g.subject_id = t.subject_id
WHERE st.student = 'Brittany Diaz' 
  AND t.teacher = 'Mary Mora';  
