#!/usr/bin/python3
"""Start link class to table in database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    state_searched = sys.argv[4]
    query = select(State).where(State.name == state_searched)
    with engine.connect() as connection:
        states = connection.execute(query).first()
        if states:
            print(states.id)
        else:
            print("Not found")

    engine.dispose()
