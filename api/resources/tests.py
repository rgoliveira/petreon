from flask import jsonify, url_for
from models import db
from models.campaign import Campaign
from models.donation import Donation
from models.donor import Donor
from models.rescuee import Rescuee
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict
from datetime import date

class TestsAPI(Resource):
    def get(self):
        try:
	    #Rescuees
            rescuees = [
                    Rescuee(id="diddy", name="Diddy", kind="dog"),
                    Rescuee(id="dixie", name="Dixie", kind="dog")
                    ]

            for rescuee in rescuees:
                db.session.add(rescuee)

            diddy = Rescuee.query.filter_by(id=rescuees[0].id).first()

	    #Donors
            donors = [
                    Donor(name="ShigeruMiyamoto", email="creator@donkey.com", verified=True)
                    ]
	    
            for donor in donors:
                db.session.add(donor)

            miyamoto = Donor.query.filter_by(name=donors[0].name).first()

	    #Campaigns
            campaigns = [
                    Campaign(rescuee_uuid=diddy.uuid, type='DiddyKongRacing', goal="10000", current_amount="500")
                    ]

            for campaign in campaigns:
                db.session.add(campaign)
            
            diddykongracing = Campaign.query.filter_by(type='DiddyKongRacing').first()

	    #Donations
            donations = [
                    Donation(campaign_uuid=diddykongracing.uuid, donor_uuid=miyamoto.uuid, amount="500", date=date.today())
                    ]

            for donation in donations:
                db.session.add(donation)

	    #Commit the objects
            db.session.commit()

        except:
            # any of these objects already there with its name
            db.session.rollback()
            return "One of the test entities already existed!", 409

        return "Ok!", 200

