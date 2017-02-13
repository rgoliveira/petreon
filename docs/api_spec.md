#API Specification
The part of the Petreon API root URL will be played graciously
by `petreon.org/api/`. 

## CampaignsAPI
'petreon.org/api/campaigns/<string:rescuee_id>'

### GET
List all of the Campaigns attached to the `rescuee_id`. Currently, `rescuee_id` is the database-generated uuid value.

## CampaignAPI
'petreon.org/api/campaign/<string:rescuee_id>/<string:campaign_type>'
### GET
### POST
### DELETE

## DonationAPI
'petreon.org/api/donation/<string:donor_id>/<string:campaign_id>'
### GET
### POST
### DELETE

## DonorAPI
'petreon.org/api/donor/<string:donor_name>'
### GET
### POST
### DELETE

## RescueesAPI
'petreon.org/api/rescuees'
### GET
List all of the rescuees in the database.

## RescueeAPI
'petreon.org/api/rescuee/<string:rescuee_id>'
### GET
### POST
### PUT
### DELETE

## OrganizationAPI
'petreon.org/api/org/<string:org_name>'
### GET
### POST
### DELETE

## Test
'petreon.org/api/tests`

###GET
If the API is configured for TESTING, this will fill the database with some dummy data.
