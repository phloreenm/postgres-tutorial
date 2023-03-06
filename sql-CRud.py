import sql_creds
from sqlalchemy import create_engine, Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine(
    sql_creds.DATABASE
    + "://"
    + sql_creds.DB_USERNAME
    + ":"
    + sql_creds.DB_PASSWORD
    + "@"
    + sql_creds.HOST
    + ":"
    + str(sql_creds.PORT)
    + "/"
    + sql_creds.DB_NAME
)
base = declarative_base()


class Programmer(base):
    __tablename__ = "programmers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

# CREATing records on Programmer table

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="Bristish",
    famous_for="First programmer",
)
adam_turing = Programmer(
    first_name="Adam",
    last_name="Turing",
    gender="M",
    nationality="Bristish",
    famous_for="Modern Computer",
)
grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="M",
    nationality="American",
    famous_for="COBOL language",
)
margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apolo 11",
)
bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="F",
    nationality="American",
    famous_for="Microsoft",
)
tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="Bristish",
    famous_for="World Wide Web",
)

# session.add(ada_lovelace)
session.add(adam_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
session.commit()


# READ records from Programmer table
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | ",
    )
