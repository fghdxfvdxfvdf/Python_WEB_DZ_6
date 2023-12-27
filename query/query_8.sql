-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT d.name AS lesson, t.fullname AS teacher_name, 
ROUND(AVG(g.grade), 2) AS average_grade 
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON d.teacher_id = t.id 
WHERE d.name = 'Історія'
GROUP BY d.name, t.fullname
