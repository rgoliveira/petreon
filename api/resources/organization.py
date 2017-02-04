from flask import jsonify, url_for
from models import db
from models.organization import Organization
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict

class OrganizationAPI(Resource):
    def get(self, org_name):
        org = Organization.query.filter_by(name=org_name).first()
        if org is None:
            abort(404, message="Organization {} does not exist!".format(org_name))
        return jsonify({"organization": to_dict(org)})

    def post(self, org_name):
        if Organization.query.filter_by(name=org_name).first() is not None:
            # TODO: Warn the user properly? Maybe make a unique name?
            abort(409, message="Organization {} already exists!".format(org_name))
        org = Organization(name=org_name)
        db.session.add(org)
        db.session.commit()

        return jsonify({"organization": to_dict(org)})

    def delete(self, org_name):
        org = Organization.query.filter_by(name=org_name).first()
        if org is None:
            abort(404, message="Organization {} does not exist!".format(org_name))

        db.session.delete(org)
        db.session.commit()

        return "Deleted organization {}!".format(org_name)
