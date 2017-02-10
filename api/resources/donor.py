from flask import jsonify, url_for
from models import db
from models.donor import Donor
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict

class DonorAPI(Resource):
    def get(self, donor_name):
        donor = Donor.query.filter_by(name=donor_name).first()
        if donor is None:
            abort(404, message="Donor {} does not exist!".format(donor_name))
        return jsonify({"donor": to_dict(donor)})

    def post(self, donor_name):
        if Donor.query.filter_by(name=donor_name).first() is not None:
            # TODO: Warn the user properly? Maybe make a unique name?
            abort(409, message="Donor {} already exists!".format(donor_name))
        donor = Donor(name=donor_name)
        db.session.add(donor)
        db.session.commit()

        return jsonify({"donor": to_dict(donor)})

    def delete(self, donor_name):
        donor = Donor.query.filter_by(name=donor_name).first()
        if donor is None:
            abort(404, message="Donor {} does not exist!".format(donor_name))

        db.session.delete(donor)
        db.session.commit()

        return "Deleted donor {}!".format(donor_name)
