from flask import jsonify, url_for
from models import db
from models.donation import Donation
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict
from datetime import date

class DonationAPI(Resource):
    def get(self, donor_id, campaign_id):
        donation = Donation.query.filter_by(donor_uuid=donor_id, campaign_uuid=campaign_id).first()
        if donation is None:
            abort(404, message="Donor {} has no donations to Campaign {}!".format(donor_id, campaign_id))

        return jsonify({"donation": to_dict(donation)})

    def post(self, donor_id, campaign_id):
        if Donation.query.filter_by(donor_uuid=donor_id, campaign_uuid=campaign_id).first() is not None:
            abort(409, message="Donor {} already has a donation to Campaign {}".format(donor_id, campaign_id))

        donation = Donation(donor_uuid=donor_id, campaign_uuid=campaign_id, date=date.today())
        db.session.add(donation)
        db.session.commit()

        return jsonify({"donation": to_dict(donation)})

    def delete(self, donor_id, campaign_id):
        donation = Donation.query.filter_by(donor_uuid=donor_id, campaign_uuid=campaign_id).first()
        if donation is None:
            abort(404, message="Donor {} has no donation to Campaign {}!".format(donor_id, campaign_id))

        db.session.delete(donation)
        db.session.commit()

        return "Deleted donation {}!".format(donation)
