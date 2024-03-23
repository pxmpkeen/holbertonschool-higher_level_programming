#!/usr/bin/python3
"""
List objects
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

# Format is mysql+mysqldb://...
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    s = Session()

    [print(
        "{}: {}".format(state.id, state.name)
        )
        for state in s.query(State).order_by(State.id)]
