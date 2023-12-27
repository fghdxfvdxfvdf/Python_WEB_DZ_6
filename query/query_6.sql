-- Знайти список студентів у певній групі.

SELECT gr.name AS group_name, s.fullname AS student_name
FROM students s 
JOIN groups gr ON gr.id = s.group_id 
WHERE gr.id = 3;
