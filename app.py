from flask import Flask, request, jsonify
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from application.models import *

def create_celery(app):
    from celery import Celery
    celery = Celery(app.import_name)
    import celery_config
    celery.config_from_object(celery_config)
    return celery

def create_app():
    app = Flask(__name__)

    from application.config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    security = Security(app, user_datastore)

    from flask_restful import Api
    api = Api(app, prefix='/api')

    from flask_cors import CORS
    CORS(app)

    from caching import cache
    cache.init_app(app)
    
    celery = create_celery(app)
    from mailer import mail
    mail.init_app(app)

    return app, api, celery

app, api_handler, celery_app = create_app()
import tasks

from celery.schedules import crontab
celery_app.conf.beat_schedule = {
    'daily-email-test':{
        'task': 'tasks.daily_mail',
        'schedule': crontab(hour=17, minute=14)
    },
    'monthly-email-test':{
        'task': 'tasks.monthly_mail',
        'schedule': crontab(day_of_month=20,hour=16, minute=30)
    }    
}


from routes.auth import signup, login
api_handler.add_resource(signup, '/signup')
api_handler.add_resource(login, '/login')

from routes.campaign import CampaignResource
api_handler.add_resource(CampaignResource, '/CampaignResource')

from routes.campaign import CampaignSpecific
api_handler.add_resource(CampaignSpecific, '/CampaignSpecific/<int:id>')

from routes.campaign import CampaignInfluencerSpecific
api_handler.add_resource(CampaignInfluencerSpecific, '/CampaignInfluencerSpecific/<int:id>')

from routes.ad import AdResource,AdSpecific
api_handler.add_resource(AdResource, '/AdResource/<int:id>','/AdResource')
api_handler.add_resource(AdSpecific, '/AdSpecific/<int:id>')

from routes.sponsor import SponsorResource
api_handler.add_resource(SponsorResource, '/SponsorResource','/SponsorResource/<int:id>')

from routes.influencer import InfluencerResource, InfluencerSpecific, InfluencerStat
api_handler.add_resource(InfluencerResource, '/InfluencerResource')
api_handler.add_resource(InfluencerSpecific, '/InfluencerSpecific/<int:id>')
api_handler.add_resource(InfluencerStat, '/InfluencerStat')



from routes.ad_requests import Ad_request,Inf_ad_req_decision
api_handler.add_resource(Ad_request, '/Ad_request')
api_handler.add_resource(Inf_ad_req_decision,'/Inf_ad_req_decision')

from routes.admin import activateManager
api_handler.add_resource(activateManager,'/activateManager')

from routes.admin import AdminFind
api_handler.add_resource(AdminFind,'/AdminFind')

from routes.admin import AdminFlagUser
api_handler.add_resource(AdminFlagUser,'/AdminFlagUser')

from routes.admin import AdminUnFlagUser
api_handler.add_resource(AdminUnFlagUser,'/AdminUnFlagUser')

from routes.admin import AdminHomeDetails
api_handler.add_resource(AdminHomeDetails,'/AdminHomeDetails')

from routes.admin import AdminStat
api_handler.add_resource(AdminStat,'/AdminStat')

from routes.sponsor import SponsorStat
api_handler.add_resource(SponsorStat,'/SponsorStat')




@app.route('/api/test', methods=['POST'])
@auth_token_required
@roles_accepted('sponsor')
def test():
    return jsonify({"message":"Test successful", "id": current_user.id})
    
@app.route('/hello_world', methods=['GET'])
def hello_world():
    result = tasks.daily_mail.delay()
    while not result.ready(): 
        pass
    return jsonify({"message":"Hello World"})


if __name__ == "__main__":
    app.run(debug=True, port = 5000 )