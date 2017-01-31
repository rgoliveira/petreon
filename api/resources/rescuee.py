from flask import jsonify, url_for
from models.rescuee import Rescuee
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict

class RescueesAPI(Resource):
    def get(self):
        return jsonify({"rescuees": to_dict(Rescuee.query.all())})

class RescueeAPI(Resource):
    def get(self, rescuee_id):
        rescuee = Rescuee.query.filter_by(id=rescuee_id).first()
        if rescuee is None:
            abort(404, message="Rescuee {} doesn't exist".format(rescuee_id))
        else:
            return jsonify({"rescuee": to_dict(rescuee)})

