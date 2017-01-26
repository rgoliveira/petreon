from flask import Flask, jsonify, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DBConfig
from models.rescuee import Rescuee
from petreon_utils import toDict

app = Flask(__name__)
engine = create_engine(DBConfig.DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.route("/init-tests")
def initTests():
    session = Session()
    try:
        objs =  [
                Rescuee(id="diddy", name="Diddy", kind="dog"),
                Rescuee(id="dixie", name="Dixie", kind="dog")
                ]
        for o in objs:
            session.add(o)
        session.commit()
    except:
        # rescuee already there with that name
        session.rollback()
        pass

    # session must be open to get model columns
    res = toDict(objs)
    session.close()
    return redirect(url_for("getRescuees"))

@app.route("/rescuees")
def getRescuees():
    session = Session()

    rescuees = session.query(Rescuee).all()
    session.close()

    return jsonify({"rescuees": toDict(rescuees)})

if __name__ == "__main__":
    # todo: wait for db to be ready

    # todo: deal with migrations


    # set host so it works with docker
    # set debug so it'll reload on code change
    app.run(host='0.0.0.0', debug=True)

