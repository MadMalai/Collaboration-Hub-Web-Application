from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import roles_accepted, auth_token_required
from sqlalchemy import func
from caching import cache
from application.models import *

class activateManager(Resource):
    @auth_token_required
    @roles_accepted('admin')
    def post(self):
        data = request.get_json()
        id = data.get('id')
        user = user_datastore.find_user(id=id)
        if user and user.has_role('sponsor'):
            user_datastore.activate_user(user)
            db.session.commit()
            return jsonify({"message":"User activated successfully"})
        return jsonify({"message":"User not found"})
    
    @auth_token_required
    @roles_accepted('admin')

    def get(self):
        deactivated_users = User.query.filter_by(active=False).all()
        data=[]
        for user in deactivated_users:
            usrlist={
                "id":user.id,
                "email":user.email
            }
            data.append(usrlist)
            if data:
                return make_response(jsonify({"message": "deactivated user list", "data": data}), 200)

class AdminFlagUser(Resource):
    @auth_token_required
    @roles_accepted('admin')
    def put(self):
            data = request.get_json()
            objecttype = data['objecttype']
            objectid = data['objectid']

            if objecttype=="1":
                usr= db.session.query(campaign).filter(campaign.cam_id == objectid).first()
                usr.cam_adminflag = 1
                db.session.commit()

            elif objecttype=="2":
                usr= db.session.query(sponsor).filter(sponsor.s_id == objectid).first()
                usr.s_adminflag = 1
                db.session.commit()
           
            elif objecttype=="3":
                usr= db.session.query(influencer).filter(influencer.i_id == objectid).first()
                usr.i_adminflag = 1
                db.session.commit()
            return make_response(jsonify({"message": "updated flag request"}))
             

class AdminUnFlagUser(Resource):
    @auth_token_required
    @roles_accepted('admin')
    def put(self):
            data = request.get_json()
            objecttype = data['objecttype']
            objectid = data['objectid']

            if objecttype=="1":
                usr= db.session.query(campaign).filter(campaign.cam_id == objectid).first()
                usr.cam_adminflag = 0
                db.session.commit()

            elif objecttype=="2":
                usr= db.session.query(sponsor).filter(sponsor.s_id == objectid).first()
                usr.s_adminflag = 0
                db.session.commit()
         
            elif objecttype=="3":
                usr= db.session.query(influencer).filter(influencer.i_id == objectid).first()
                usr.i_adminflag = 0
                db.session.commit()
            return make_response(jsonify({"message": "updated unflag request"}))

class AdminStat(Resource):
    @auth_token_required
    @roles_accepted('admin')

    @cache.cached(timeout=10)
    def get(self):
        sponsor_by_industry = db.session.query(sponsor.s_industry, func.count(sponsor.s_industry)).group_by(sponsor.s_industry).all()
        sponsor_profile={
            "Industries" :[ind[0] for ind in sponsor_by_industry ],
            "count":[ind[1] for ind in sponsor_by_industry ]
        }
      
        campaign_by_months=db.session.query(
                                func.strftime('%Y-%m', campaign.cam_start_date).label('month_year'),
                                func.count(campaign.cam_id).label('campaign_count')
                                ).group_by(func.strftime('%Y-%m', campaign.cam_start_date)).all()

        campaign_status_summary={
            'Status_label':['Ongoing','Completed'],
            's_values' : [db.session.query(campaign.progress < 100).count(),db.session.query(campaign.progress == 100).count()],
            'months_label': [mon[0] for mon in campaign_by_months],
            'm_values':[mon[1] for mon in campaign_by_months]
        }

        influencer_by_niche = db.session.query(influencer.i_niche, func.count(influencer.i_niche)).group_by(influencer.i_niche).all()
        influencer_by_platform = db.session.query(influencer.i_presence, func.count(influencer.i_presence)).group_by(influencer.i_presence).all()
        influencer_profile={
            "Niches" :[ind[0] for ind in influencer_by_niche ],
            "n_count":[ind[1] for ind in influencer_by_niche ],
            "Platforms" :[ind[0] for ind in influencer_by_platform ],
            "p_count":[ind[1] for ind in influencer_by_platform ]
        }
        
        cam_list = db.session.query(campaign).join(sponsor).filter(campaign.s_id == sponsor.s_id,campaign.progress < 100).count()
        spon_list = db.session.query(sponsor).count()
        inf_list = db.session.query(influencer).count()
        ad_count = db.session.query(ad_details).count()

        kpi_data = {
        'spon_count': spon_list,
        'inf_count': inf_list,
        'cam_count': cam_list,
        'ad_count': ad_count
        }
        return jsonify({
            "kpi_data": kpi_data,
            "sponsor_profile": sponsor_profile,
            "campaign_status_summary": campaign_status_summary,
            "influencer_profile": influencer_profile
        })

class AdminFind(Resource):
    @auth_token_required
    @roles_accepted('admin')
    def get(self):       
        cam_list = db.session.query(campaign).join(sponsor).filter(campaign.s_id == sponsor.s_id).with_entities(campaign.cam_id,campaign.cam_name,campaign.cam_desc,\
                                                                                                                                       sponsor.org_name, campaign.progress).all()
        print(cam_list)
        cam_list_data = []
        for cam in cam_list:
            cam_details = {
                'cam_id': cam[0],
                'cam_name': cam[1],
                'cam_desc': cam[2],
                'org_name': cam[3],
                'progress': cam[4]
                }
            cam_list_data.append(cam_details)                                                                                                                                

        spon_list = db.session.query(sponsor).with_entities(sponsor.s_id, sponsor.s_name, sponsor.s_industry, sponsor.org_name).all()
        spon_list_data = []
        for spon in spon_list:
            spon_details = {
                's_id': spon[0],
                's_name': spon[1],
                's_industry': spon[2],
                'org_name': spon[3]
                }
            spon_list_data.append(spon_details) 

        inf_list = db.session.query(influencer).with_entities(influencer.i_id,influencer.i_name,influencer.i_link,influencer.i_niche).all()
        inf_list_data = []
        for inf in inf_list:
            inf_details = {
                'i_id': inf[0],
                'i_name': inf[1],
                'i_link': inf[2],
                'i_niche': inf[3]
                }
            inf_list_data.append(inf_details) 

        return jsonify({
            "cam_list": cam_list_data,
            "spon_list": spon_list_data,
            "inf_list": inf_list_data
        })


class AdminHomeDetails(Resource):
    @auth_token_required
    @roles_accepted('admin')
    def get(self):  
        cam_list = db.session.query(campaign).join(sponsor).filter(campaign.s_id == sponsor.s_id).with_entities(campaign.cam_id,campaign.cam_name,campaign.progress,sponsor.org_name).all()
        print(cam_list)
        cam_list_data = []
        for cam in cam_list:
            cam_details = {
                'cam_id': cam[0],
                'cam_name': cam[1],
                'progress': cam[2],
                'org_name': cam[3]
                }
            cam_list_data.append(cam_details)  

        flagged_inf = db.session.query(influencer).filter(influencer.i_adminflag==1).with_entities(influencer.i_id,influencer.i_name,influencer.i_link).all()
        flagged_inf_data = []
        for inf in flagged_inf:
            inf_details = {
                'i_id': inf[0],
                'i_name': inf[1],
                'i_link': inf[2]
                }
            flagged_inf_data.append(inf_details)

        flagged_spon=db.session.query(sponsor).filter(sponsor.s_adminflag==1).with_entities(sponsor.s_id,sponsor.s_name,sponsor.org_name).all()
        flagged_spon_data = []
        for spon in flagged_spon:
            spon_details = {
                's_id': spon[0],
                's_name': spon[1],
                'org_name': spon[2]
                }
            flagged_spon_data.append(spon_details)

        flagged_cam=db.session.query(campaign).filter(campaign.cam_adminflag==1).with_entities(campaign.cam_id,campaign.cam_name,campaign.cam_category).all()
        flagged_cam_data = []
        for cam in flagged_cam:
            cam_details = {
                'cam_id': cam[0],
                'cam_name': cam[1],
                'cam_category': cam[2]
                }
            flagged_cam_data.append(cam_details)

        return jsonify({
            "cam_list": cam_list_data,
            "flagged_inf": flagged_inf_data,
            "flagged_spon": flagged_spon_data,
            "flagged_cam": flagged_cam_data
        })
        
        

  