SELECT student
FROM students
WHERE group_id = (SELECT id FROM groups WHERE group_number = 4); 
