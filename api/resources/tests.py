from flask import jsonify, url_for
from models import db
from models.rescuee import Rescuee
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict

class TestsAPI(Resource):
    def get(self):
        try:
            objs =  [
                    Rescuee(id="diddy", name="Diddy", kind="dog"),
                    Rescuee(id="dixie", name="Dixie", kind="dog")
                    ]
            for o in objs:
                db.session.add(o)
            db.session.commit()
        except:
            # rescuee already there with that name
            db.session.rollback()
            pass

        return "Ok!", 200

