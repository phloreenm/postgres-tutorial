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

# UPDATE a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World president"

# UPDATE multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined!")

# DELETE a single record
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# programmer = (
#     session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# )
# # defensiuve programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation == "y":
#         session.delete(programmer)
#         print("Programmer" + fname + " " + lname + " deleted!")
#     else:
#         print("Programmer not deleted!")
# else:
#     print("No records found for: ", fname + " " + lname)
#DELETE ALL records (DO NOT DO THIS )
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)

# commit session
session.commit()


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
