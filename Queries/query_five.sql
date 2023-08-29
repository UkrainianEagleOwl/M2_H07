SELECT t.teacher, sj.subject
FROM teachers t
JOIN subjects sj ON t.subject_id = sj.id
WHERE t.teacher = 'Mrs. Denise Wilson'; 