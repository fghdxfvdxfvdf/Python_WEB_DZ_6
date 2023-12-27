-- Список курсів, які певному студенту читає певний викладач.

SELECT DISTINCT d.name AS discipline_name, s.fullname AS student_name, t.fullname AS teacher_name
FROM grades g
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE s.id = 3 AND t.id = 3;
