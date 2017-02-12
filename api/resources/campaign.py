from flask import jsonify, url_for
from models import db
from models.campaign import Campaign
from flask_restful import reqparse, abort, Api, Resource
from petreon_utils import to_dict

class CampaignAPI(Resource):
    def get(self, rescuee_id, campaign_type):
        campaign = Campaign.query.filter_by(rescuee_uuid=rescuee_id,type=campaign_type).first()
        if campaign is None:
            abort(404, message="Rescuee {} has no {} campaign!".format(rescuee_id, campaign_type))

        return jsonify({"campaign": to_dict(campaign)})

    def post(self, rescuee_id, campaign_type):
        if Campaign.query.filter_by(rescuee_uuid=rescuee_id, type=campaign_type).first() is not None:
            # TODO: Warn the user properly? Maybe make a unique name?
            abort(409, message="Rescuee {} already has a {} campaign!".format(campaign_type))
        campaign = Campaign(rescuee_uuid=rescuee_id, type=campaign_type)
        db.session.add(campaign)
        db.session.commit()

        return jsonify({"campaign": to_dict(campaign)})

    def delete(self, rescuee_id, campaign_type):
        campaign = Campaign.query.filter_by(rescuee_uuid=rescuee_id, type=campaign_type).first()
        if campaign is None:
            abort(404, message="Rescuee {} has no {} campaign!".format(rescuee_id, campaign_type))

        db.session.delete(campaign)
        db.session.commit()

        return "Deleted campaign {}!".format(campaign_type)

class CampaignsAPI(Resource):
    def get(self, rescuee_id):
        '''
	Rescuee to campaigns is a one-to-many relationship. Returns all the campaigns in JSON.
	'''
        campaigns = Campaign.query.filter_by(rescuee_uuid=rescuee_id).all()
        if not campaigns:
            abort(404, message="Rescuee {} has no campaigns!".format(rescuee_id))
        campaigns = [to_dict(campaign) for campaign in campaigns]

        return jsonify({"campaigns": campaigns})

