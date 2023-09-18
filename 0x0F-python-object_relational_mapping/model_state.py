import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Replace the placeholders with your actual MySQL credentials
DB_USERNAME = 'mysql_username'
DB_PASSWORD = 'mysql_password'
DB_DATABASE = 'mysql_database'

# Create the database connection string
db_url = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_DATABASE}'

# Create an instance of the declarative base
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Create the database engine
engine = create_engine(db_url)

# Create the table in the database
if __name__ == '__main__':
    Base.metadata.create_all(engine)

