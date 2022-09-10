from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Travel" table
class Travel(base):
    __tablename__ = "Travel"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    city_name = Column(String)
    population = Column(Integer)
    famous_for = Column(String)
   

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Travel table
tianjin = Travel(
    country_name="China",
    city_name="Tianjin",
    population=int(14000000),
    famous_for="Tianjin Eye"
)

paris = Travel(
    country_name="France",
    city_name="Paris",
    population=int(65000000),
    famous_for="The Eiffel Tower"
)

athens = Travel(
    country_name="Greece",
    city_name="Athens",
    population=int(10000000),
    famous_for="The Acropolis"
)

# add each instance of our programmers to our session
# session.add(tianjin)
# session.add(paris)
# session.add(athens)


# updating a single record
# travel = session.query(Travel).filter_by(id=1).first()
# travel.famous_for = "The Haihe River"

# commit our session to the database
session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# delete multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find all Travel Destinations
destinations = session.query(Travel)
for destination in destinations:
    print(
        destination.id,
        destination.country_name,
        destination.city_name,
        destination.population,
        destination.famous_for,
        sep=" | "
    )