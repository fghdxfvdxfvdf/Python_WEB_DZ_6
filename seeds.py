from datetime import date, datetime, timedelta
from random import randint

import faker

fake = faker.Faker()

disciplines = [
    "Вища математика",
    "Історія",
    "Лінійна алгебра",
    "Креслення",
    "Теорія ймовірності",
    "Історія України",
    "Англійська мова",
    "Програмування",
    "Фізика",
    "Хімія",
]
groups = ["Є331", "ТПК-155", "ЄС-97л", "КН-51", "ПЦБ-13з"]
NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
STUDENT_FROM_ONE_DAY = 5


def seed_teachers(cur):
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    # sql = "INSERT OR IGNORE INTO teachers(fullname) VALUES(?);"

    cur.executemany(
        sql,
        zip(
            teachers,
        ),
    )


def seed_discipline(cur):
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);"
    # sql = "INSERT OR IGNORE INTO disciplines(name, teacher_id) VALUES(?, ?);"

    cur.executemany(
        sql,
        zip(
            disciplines,
            iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines))),
        ),
    )


def seed_groups(cur):
    sql = "INSERT INTO groups(name) VALUES(?);"
    # sql = "INSERT OR IGNORE INTO groups(name) VALUES(?);"

    cur.executemany(
        sql,
        zip(
            groups,
        ),
    )


def seed_students(cur):
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    # sql = "INSERT OR IGNORE INTO students(fullname, group_id) VALUES(?, ?);"

    cur.executemany(
        sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students))))
    )


def seed_grades(cur):
    start_date = datetime.strptime("2020-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);"
    # sql = "INSERT OR IGNORE INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);"


    def get_list_data(start: date, end: date) -> list[date]:
        result = []
        current_data = start
        while current_data <= end:
            if current_data.isoweekday() < 6:
                result.append(current_data)
            current_data += timedelta(1)
        return result

    list_data = get_list_data(start_date, end_date)

    grades = []
    for day in list_data:
        random_discipline = randint(1, len(disciplines))
        random_students = [
            randint(1, NUMBER_STUDENTS) for _ in range(STUDENT_FROM_ONE_DAY)
        ]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))

    cur.executemany(sql, grades)
