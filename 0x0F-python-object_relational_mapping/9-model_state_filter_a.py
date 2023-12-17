#!/usr/bin/python3
'''model state filter'''


if __name__ == "__main__":
    """ Start link class to table in database"""
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, select

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    query = select(State).filter(State.name.like('%a%'))\
        .order_by(State.id.asc())
    with engine.connect() as connection:
        states = connection.execute(query)
        for state in states:
            print(f"{state.id}: {state.name}")

    engine.dispose()
