from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import insert, select, update, delete

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
    conn.commit()


def get_data():
    with engine.connect() as conn:
        result = conn.execute(select(profile).order_by(profile.c.name))
        for row in result:
            print(row)


def del_data(a: int):
    with engine.connect() as conn:
        stmt = delete(profile).where(profile.c.id == a)
        conn.execute(stmt)
        conn.commit()


def update_data(a,b):
    with engine.connect() as conn:
        stmt = update(profile).where(profile.c.id == a).values(name=b)
        conn.execute(stmt)
        conn.commit()

get_data()
del_data(2)
update_data(1, "Bob")
