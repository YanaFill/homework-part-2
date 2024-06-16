from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, func
from sqlalchemy import insert, select, update, delete, ForeignKey

engine = create_engine("sqlite:///users.db", echo=True)

metadata = MetaData()
profile = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), nullable=False),
    Column("surname", String(30), nullable=False),
    Column("b-day", String(30), nullable=False)
)

profile1 = Table(
    "grade",
    metadata,
    Column("subject", String(30), nullable=False),
    Column("score", Integer, nullable=False),
    Column("student_id", Integer, ForeignKey("students.id"), nullable=False)
)

metadata.drop_all(engine)
metadata.create_all(engine)
with engine.connect() as conn:
    stmt = insert(profile)
    conn.execute(stmt, [{"name": "John", "surname": "Boyd", "b-day": "25.01.1987"},
                        {"name": "Seeley", "surname": "Booth", "b-day": "10.07.2003"},
                        {"name": "Angela", "surname": "Montenegro", "b-day": "02.07.2004"},
                        {"name": "Jack", "surname": "Hoodgins", "b-day": "09.05.2003"},
                        {"name": "Camille", "surname": "Saroyan", "b-day": "23.11.2001"},
                        {"name": "Lance", "surname": "Sweets", "b-day": "19.10.2002"}])
    stmt1 = insert(profile1)
    conn.execute(stmt1, [{"subject": "Math", "score": 85, "student_id": 1},
                         {"subject": "Math", "score": 51, "student_id": 2},
                         {"subject": "Math", "score": 73, "student_id": 3},
                         {"subject": "Math", "score": 67, "student_id": 4},
                         {"subject": "Math", "score": 94, "student_id": 5},
                         {"subject": "Math", "score": 59, "student_id": 6}])
    conn.commit()


def get_data():
    with engine.connect() as conn:
        result = conn.execute(select(profile.c.name, profile.c.surname, profile1.c.subject, profile1.c.score)
                              .select_from(profile.join(profile1))
                              .order_by(profile.c.surname))
        for row in result:
            print(row)


def get_score(surname: str):
    with engine.connect() as conn:
        result = conn.execute(select(profile.c.surname, profile1.c.score)
                              .select_from(profile.join(profile1))
                              .where(profile.c.surname == surname))
        for row in result:
            print(row)


def del_data(id: int):
    with engine.connect() as conn:
        stmt = delete(profile).where(profile.c.id == id)
        conn.execute(stmt)
        conn.commit()


def update_data(id: int,b):
    with engine.connect() as conn:
        stmt = update(profile).where(profile.c.id == id).values(name=b)
        conn.execute(stmt)
        conn.commit()

def get_avg_subjects_scores():
    with engine.connect() as conn:
        stmt = select(profile1.c.subject, func.avg(profile1.c.score).label('average_score')
                      ).group_by(profile1.c.subject)
        result = conn.execute(stmt)
        for row in result:
            print(f"Subject: {row.subject}, Average Score: {row.average_score:.2f}")



get_data()
del_data(2)
update_data(1, "Bob")
get_score("Boyd")
get_avg_subjects_scores()