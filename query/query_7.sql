--Знайти оцінки студентів у окремій групі з певного предмета.

SELECT g.grade AS grade, s.fullname AS student_name, gr.name AS group_name, d.name AS discipline_name
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN disciplines d ON g.discipline_id = d.id
JOIN groups gr ON s.group_id = gr.id
WHERE d.name = 'Історія' AND gr.name = 'Є331';
