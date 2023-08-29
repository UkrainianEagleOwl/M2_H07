SELECT st.student, g.grade
FROM student_grades AS g
JOIN students AS st ON g.student_id = st.id
JOIN subjects AS s ON g.subject_id = s.id
JOIN groups AS gr ON st.group_id = gr.id
WHERE gr.group_number = '3'      
  AND s.subject = 'Ukrainian'   
  AND g.date_of = (SELECT MAX(date_of) FROM student_grades WHERE subject_id = s.id);
