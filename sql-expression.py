from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" database
db = create_engine("postgres:///chinook")
meta = MetaData(db)

# making the connection
with db.connect() as connection: