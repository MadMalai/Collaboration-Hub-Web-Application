from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from application.models import *

class CampaignResource(Resource):
    # from caching import cache
    @auth_token_required
    @roles_accepted('admin','sponsor','influencer')
    # @cache.cached(timeout=20)
    def get(self):
        print(current_user.roles)
        role = current_user.roles[0].id if current_user.roles else None
        if role==3:
            cam_list = db.session.query(campaign).filter(campaign.visibility=='Public').with_entities(campaign.cam_id,campaign.cam_name,campaign.cam_desc,campaign.cam_start_date,campaign.cam_end_date,\
                        campaign.cam_budget,campaign.goals,campaign.progress,campaign.visibility).all()
            data = []
            for cam in cam_list:
                cam_details = {
                    'cam_id': cam[0],
                    'cam_name': cam[1],
                    'cam_desc': cam[2],
                    'cam_start_date': cam[3],
                    'cam_end_date': cam[4],
                    'cam_budget': cam[5],
                    'goals': cam[6],
                    'progress': cam[7],
                    'visibility':cam[8]
                    }
                data.append(cam_details)
            if not data:
                return make_response(jsonify({"message": "No campaign details listed"}), 404)
            return make_response(jsonify({"message": "get all public campaign details", "data": data}), 200)
        
        elif role==2:
            print(current_user.id)

            cam_list = db.session.query(campaign).filter(campaign.s_id==current_user.id)\
                .with_entities(campaign.cam_id,campaign.cam_name,campaign.cam_desc,campaign.cam_start_date,campaign.cam_end_date,\
                                campaign.cam_budget,campaign.goals,campaign.progress,campaign.visibility).all()
            data = []
            for cam in cam_list:
                cam_details = {
                    'cam_id': cam[0],
                    'cam_name': cam[1],
                    'cam_desc': cam[2],
                    'cam_start_date': cam[3],
                    'cam_end_date': cam[4],
                    'cam_budget': cam[5],
                    'goals': cam[6],
                    'progress': cam[7],
                    'visibility':cam[8]
                    }
                data.append(cam_details)
            if not data:
                return make_response(jsonify({"message": "No campaign details listed"}), 404)
            return make_response(jsonify({"message": "get all campaign details", "data": data}), 200)


    @auth_token_required
    @roles_accepted('sponsor')
    def post(self): 
        data = request.get_json()
        cam_name = data['cam_name']
        cam_desc = data['cam_desc']
        cam_start_date = data['cam_start_date']
        cam_end_date = data['cam_end_date']
        cam_budget = data['cam_budget']
        visibility = data['visibility']
        goals = data['goals']
        progress = 0
        cam_category = data['cam_category']
        cam_adminflag = 0

        s_id = current_user.id
        cname_search = data['cam_name']

        cam_details = campaign(cam_name=cam_name, cam_desc=cam_desc,cam_category=cam_category, cam_start_date=cam_start_date\
                                ,cam_end_date=cam_end_date,cam_budget=cam_budget, visibility=visibility,goals=goals,progress=None,s_id=s_id,cname_srch = cname_search)

        db.session.add(cam_details)
        db.session.commit() 

        return make_response(jsonify({"message": "Campaign created successfully", "id": cam_details.cam_id, "name": cam_details.cam_name}), 201)

class CampaignSpecific(Resource): 
    @auth_token_required
    @roles_accepted('admin','influencer' ,'sponsor')
    def get(self, id):
        if current_user.roles =='sponsor':

            cam_list = campaign.query.filter_by(cam_id=id, s_id=current_user.id).first()
            cam_list = [cam_list.formater()]
            print(type(cam_list))
            if not cam_list:
                return make_response(jsonify({"message": "No campaigns listed for the given id"}), 404)
            return jsonify({"message": "View Sponsor specific campaign", "data": cam_list} )   
        elif current_user.roles == 'influencer':
            cam_list = campaign.query.filter_by(cam_id=id, visibility="public").first()
            cam_list = [cam_list.formater()]
            print(type(cam_list))
            if not cam_list:
                return make_response(jsonify({"message": "No campaigns listed for the given id"}), 404)
            return jsonify({"message": "View specific public campaign for infleuncer", "data": cam_list} ) 
        else:
            cam_list = campaign.query.filter_by(cam_id=id).first()
            cam_list = [cam_list.formater()]
            print(type(cam_list))
            if not cam_list:
                return make_response(jsonify({"message": "No campaigns listed for the given id"}), 404)
            return jsonify({"message": "View specific campaign for admin", "data": cam_list} )   

    @auth_token_required
    @roles_accepted('admin', 'sponsor')
    def put(self, id):
        cam_list = campaign.query.filter_by(cam_id=id,s_id=current_user.id).first()
        print(cam_list)
        if not cam_list:
            return make_response(jsonify({"message": "No campaigns listed for the given id"}), 404)
        data = request.get_json()
        cam_name = data['cam_name']
        if not cam_name:
            return jsonify({"message": "campaign name is required"})
        cam_desc = data['cam_desc']
        if not cam_desc:
            return jsonify({"message": "campaign description is required"})
        cam_start_date = data['cam_start_date']
        if not cam_start_date:
            return jsonify({"message": "campaign start date is required"})  
        cam_end_date = data['cam_end_date']
        if not cam_end_date:
            return jsonify({"message": "campaign end date is required"})        
        cam_budget = data['cam_budget']
        if not cam_budget:
            return jsonify({"message": "campaign budget is required"})                    
        visibility = data['visibility']
        if not visibility:
            return jsonify({"message": "public or private should be mentioned"})
        goals = data['goals']
        if not goals:
            return jsonify({"message": "campaign goals is required"}) 
        cam_category = data['cam_category']
        if not cam_category:
            return jsonify({"message": "campaign category is required"})  

        cam_list.cam_name = cam_name 
        cam_list.cam_desc = cam_desc         
        cam_list.cam_start_date = cam_start_date
        cam_list.cam_end_date = cam_end_date
        cam_list.cam_budget = cam_budget
        cam_list.visibility = visibility
        cam_list.goals = goals
        cam_list.cam_category = cam_category

        # if current_user.has_role('admin,sponsor'):
        #     campaigns.status = True
        # else:
        #     campaigns.status = False
        db.session.commit()
        return make_response(jsonify({"message": "update specific campaign", 'id': id}),201 )

    @auth_token_required
    @roles_accepted('sponsor')
    def delete(self, id):
        cam_list = campaign.query.filter_by(cam_id=id,s_id=current_user.id).first()
        if not cam_list:
            return make_response(jsonify({"message":"No campaigns listed for the given id"}), 404)
        db.session.delete(cam_list)
        db.session.commit()

        ad_list = ad_details.query.filter_by(cam_id=id,s_id=current_user.id).first()
        if not ad_list:
            return jsonify({"message":"No ads listed for the given id"})
        else:
            db.session.delete(ad_list)
            db.session.commit()

        ad_req_list = all_ad_requests.query.filter_by(cam_id=id).first()
        if not ad_req_list:
            return jsonify({"message":"No ads listed for the given id"})
        else:
            db.session.delete(ad_list)
            db.session.commit()

        return make_response(jsonify({"message": "delete specific campaign & Ads", 'id': id}), 201)  


class CampaignInfluencerSpecific(Resource): 
    @auth_token_required
    @roles_accepted('influencer')
    def get(self, id):
        #cam_list = campaign.query.all()
        cam_list = db.session.query(ad_details).join(sponsor,ad_details.s_id==sponsor.s_id).join(campaign,ad_details.cam_id==campaign.cam_id)\
                            .filter(ad_details.i_id == current_user.id,ad_details.status =='Assigned')\
                                .with_entities(campaign.cam_name,ad_details.ad_name,sponsor.org_name, campaign.progress,campaign.cam_id).all()
    
        data = []
        for cam in cam_list:
            cam_details = {
                'cam_id': cam.cam_id,
                'cam_name': cam.cam_name,
                'ad_name': cam.ad_name,
                'org_name': cam.org_name,
                'progress': cam.progress,
                }
            data.append(cam_details)

        print(type(cam_list))
        if not cam_list:
            return make_response(jsonify({"message": "No campaigns listed for the given id"}), 404)
        return jsonify({"message": "get all campaigns for influencer", "data": data} )   



