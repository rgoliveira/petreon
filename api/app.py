import sys
import logging
import time
import psycopg2

from flask import Flask, jsonify, redirect, url_for
from flask_migrate import Migrate, MigrateCommand, upgrade
from flask_restful import reqparse, abort, Api, Resource

import config
from models import db
from models import Rescuee

from resources.campaign import CampaignAPI, CampaignsAPI
from resources.donor import DonorAPI
from resources.rescuee import RescueeAPI, RescueesAPI
from resources.organization import OrganizationAPI
from resources.tests import TestsAPI

def create_app(config_obj = None):
    app = Flask(__name__)
    app.config.from_object(config_obj or config.DevelopmentConfig)

    # extensions
    api = Api(app)
    migrate = Migrate(app, db)
    db.init_app(app)

    # setup resources
    api.add_resource(CampaignsAPI, '/campaigns/<string:rescuee_id>')
    api.add_resource(CampaignAPI, '/campaign/<string:rescuee_id>/<string:campaign_type>')
    api.add_resource(DonorAPI, '/donor/<string:donor_name>')
    api.add_resource(RescueesAPI, '/rescuees')
    api.add_resource(RescueeAPI, '/rescuee/<string:rescuee_id>')
    api.add_resource(OrganizationAPI, '/org/<string:org_name>')

    if app.config["TESTING"]:
        api.add_resource(TestsAPI, '/tests')

    return app

if __name__ == "__main__":

    # todo: use proper logging instead or printing to stderr!

    app = create_app()

    #
    # ensure db is ready
    #
    db_ok = False
    while not db_ok:
        try:
            conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
            db_ok = True
            print("Database ready!", file=sys.stderr)
        except Exception as e:
            print("Database NOT ready: " + str(e), file=sys.stderr)
            print("Waiting 3 seconds to try again...", file=sys.stderr)
            time.sleep(3)

    #
    # run migrations
    #
    print("Running migrations...", file=sys.stderr)
    with app.app_context():
        upgrade()
        db.session.commit()

    #
    # run app
    #
    # set host so it works with docker
    # set debug so it'll reload on code change and be more verbose
    print("Starting app...", file=sys.stderr)
    app.run(host='0.0.0.0', debug=True)
