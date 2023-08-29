SELECT g.group_number, AVG(gg.grade) AS average_score
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN student_grades gg ON s.id = gg.student_id
JOIN subjects sj ON gg.subject_id = sj.id
WHERE sj.subject = 'Chemistry'
GROUP BY g.group_number;
