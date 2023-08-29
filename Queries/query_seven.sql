SELECT s.student, g.grade
FROM students s
JOIN student_grades g ON s.id = g.student_id
JOIN subjects sj ON g.subject_id = sj.id
WHERE s.group_id = (SELECT id FROM groups WHERE group_number = 7) 
  AND sj.subject = 'History'; 
