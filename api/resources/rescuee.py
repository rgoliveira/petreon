from flask import jsonify, url_for
from models import db
from models.rescuee import Rescuee
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict

class RescueesAPI(Resource):
    def get(self):
        return jsonify({"rescuees": to_dict(Rescuee.query.all())})

class RescueeAPI(Resource):
    
    # Setup parser
    _parser = reqparse.RequestParser()
    _parser.add_argument('name', type=str, default="Bigly", help="Name of the rescuee")
    _parser.add_argument('kind', type=str, default="Doggo", help="Species of the rescuee")

    def get(self, rescuee_id):
        rescuee = Rescuee.query.filter_by(id=rescuee_id).first()
        if rescuee is None:
            abort(404, message="Rescuee {} doesn't exist".format(rescuee_id))
        else:
            return jsonify({"rescuee": to_dict(rescuee)})

    def post(self, rescuee_id):
        args = self._parser.parse_args()

        if Rescuee.query.filter_by(id=rescuee_id).first() is not None:
            # A rescuee with the same ID exists
            # TODO: Maybe make a new unique id?
            abort(400, message="Rescuee {} already exists".format(rescuee_id))

        rescuee = Rescuee(id=rescuee_id, name=args["name"], kind=args["kind"])
        db.session.add(rescuee)
        db.session.commit()
        return jsonify({"rescuee": to_dict(rescuee)})

    def put(self, rescuee_id):
        args = self._parser.parse_args()

        rescuee = Rescuee.query.filter_by(id=rescuee_id).first()

        if rescuee is None:
            abort(404, message="Rescuee {} does not exist".format(rescuee_id))

        # TODO: Check if defaults were set by arg-parser and if so, don't update field
        # TODO: More elegant way to do this?
        rescuee.name, rescuee.kind = args["name"], args["kind"]
        db.session.commit()
        return jsonify({"rescuee": to_dict(rescuee)})

    def delete(self, rescuee_id):
        rescuee = Rescuee.query.filter_by(id=rescuee_id).first()
        if rescuee is None:
            abort(404, message="Rescuee {} does not exist".format(rescuee_id))

        db.session.delete(rescuee)
        db.session.commit()

        return "Deleted {}!".format(rescuee_id)