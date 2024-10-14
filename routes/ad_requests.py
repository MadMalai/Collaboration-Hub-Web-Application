from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from application.models import *
from sqlalchemy import and_


class Ad_request(Resource):
    # from caching import cache
    @auth_token_required
    @roles_accepted('sponsor','influencer')
    # @cache.cached(timeout=20)
    def post(self):
        role_id = current_user.roles[0].id if current_user.roles else None
        print(role_id)
        if role_id == 3:
            data = request.get_json()
            cam_id = data['cam_id']
            i_id = data['i_id']
            ad_id = data['ad_id']
            new_request = all_ad_requests(cam_id=cam_id,ad_id=ad_id,request_by='influencer',i_id=i_id,status='request sent') 
            db.session.add(new_request)
            db.session.commit()

        if role_id == 2:
            data = request.get_json()
            cam_id = data['cam_id']
            i_id = data['i_id']
            req_msg = data['req_msg']
            ad_id = data['ad_id']


            existing_request = all_ad_requests.query.filter(and_(all_ad_requests.cam_id == cam_id, 
                                                             all_ad_requests.i_id == i_id,
                                                             all_ad_requests.ad_id == ad_id,
                                                             all_ad_requests.request_by== 'sponsor',
                                                             all_ad_requests.status!='Rejected')).first()
            
            if existing_request:
                return make_response(jsonify({"message": "Duplicate request found"}), 200)
            else:
                new_request = all_ad_requests(cam_id=cam_id,ad_id=ad_id,request_by='sponsor',i_id=i_id,status='request sent') 
                db.session.add(new_request)
                db.session.commit()
                return make_response(jsonify({"message": "Influencer Request submitted successfully"}), 201)

    @auth_token_required
    @roles_accepted('sponsor','influencer')
    # @cache.cached(timeout=20)
    def get(self):
        user_id=current_user.id
        role_id = current_user.roles[0].id if current_user.roles else None
        if role_id == 3:
            # cam_requests_recevied = db.session.query(all_ad_requests)\
            #     .outerjoin(campaign,all_ad_requests.cam_id==campaign.cam_id)\
            #         .outerjoin(sponsor,campaign.s_id==sponsor.s_id)\
            #             .filter(all_ad_requests.i_id==user_id, all_ad_requests.status!="Accepted", all_ad_requests.status!="Rejected", all_ad_requests.request_by=='sponsor')\
            #                 .with_entities(campaign.cam_id,campaign.cam_name,campaign.cam_desc,campaign.goals,sponsor.org_name,all_ad_requests.status,all_ad_requests.r_id)

            cam_requests_recevied = db.session.query(all_ad_requests)\
                    .outerjoin(ad_details,all_ad_requests.ad_id==ad_details.ad_id)\
                        .outerjoin(campaign,all_ad_requests.cam_id==campaign.cam_id)\
                            .outerjoin(sponsor,campaign.s_id==sponsor.s_id)\
                                .filter(all_ad_requests.i_id==user_id, all_ad_requests.status!="Accepted", all_ad_requests.status!="Rejected", all_ad_requests.request_by=='sponsor')\
                                    .with_entities(campaign.cam_id, campaign.cam_name,campaign.cam_desc,campaign.goals,\
                                                   ad_details.ad_name,ad_details.ad_req,ad_details.terms,ad_details.ad_budget,ad_details.ad_id,sponsor.org_name,all_ad_requests.status,all_ad_requests.r_id)


            data = []
            for cam in cam_requests_recevied:
                cam_details = {
                    'cam_id' : cam.cam_id,
                    'cam_name': cam.cam_name,
                    'cam_desc': cam.cam_desc,
                    'ad_name':cam.ad_name,
                    'ad_req':cam.ad_req,
                    'goals': cam.goals,
                    'org_name': cam.org_name,
                    'ad_status': cam.status,
                    'r_id': cam.r_id,
                    }
                data.append(cam_details)
            if not data:
                return make_response(jsonify({"message": "No campaign details listed"}), 404)
            return make_response(jsonify({"message": "all campaign requests received", "data": data}), 200)
        
        if role_id == 2:
            cam_requests_recevied = db.session.query(all_ad_requests)\
                .outerjoin(campaign,all_ad_requests.cam_id==campaign.cam_id)\
                    .outerjoin(influencer,all_ad_requests.i_id==influencer.i_id)\
                    .outerjoin(sponsor,campaign.s_id == sponsor.s_id).filter(campaign.s_id==user_id, all_ad_requests.request_by=='sponsor')\
                            .with_entities(campaign.cam_id,campaign.cam_name,all_ad_requests.status,all_ad_requests.r_id, all_ad_requests.i_id,influencer.i_name,influencer.i_link)
            data = []
            for cam in cam_requests_recevied:
                cam_details = {
                    'cam_id' : cam.cam_id,
                    'cam_name': cam.cam_name,
                    'i_id': cam.i_id,
                    'i_name': cam.i_name,
                    'i_link': cam.i_link,
                    'ad_status': cam.status,
                    'r_id': cam.r_id,
                    }
                data.append(cam_details)
            if not data:
                return make_response(jsonify({"message": "No campaign details listed"}), 404)
            return make_response(jsonify({"message": "all campaign requests sent", "data": data}), 200)
        


class Spon_ad_req_decision(Resource):
    @auth_token_required
    @roles_accepted('sponsor')
    def put(self):
        data = request.get_json()
        reqaction = data['reaction']
        reqid = data['reqid']

        s_id = current_user.id
        
        if reqaction == 'Accept':
            req = db.session.query(all_ad_requests).filter(all_ad_requests.r_id == reqid).first()
            req.status = 'Accepted'
            ad_details = db.session.query(ad_details).filter(ad_details.s_id == s_id,ad_details.ad_id ==req.ad_id).first()
            ad_details.i_id = req.i_id
            ad_details.status = "Assigned"
            db.session.commit()
        
        else:
            req = db.session.query(all_ad_requests).filter(all_ad_requests.r_id == reqid).first()
            req.status = 'Rejected'
            ad_details = db.session.query(ad_details).filter(ad_details.s_id == s_id,ad_details.ad_id ==req.ad_id).first()
            ad_details.i_id = req.i_id
            ad_details.status = "Pending"
            db.session.commit()
        return make_response(jsonify({"message": "updated ad request"}) )

class Inf_ad_req_decision(Resource):
    @auth_token_required
    @roles_accepted('influencer')
    def put(self):
        data = request.get_json()
        reaction = data['reaction']
        r_id = data['r_id']
        print(data)
        s_id = current_user.id
        
        if reaction == 1:
            req = db.session.query(all_ad_requests).filter(all_ad_requests.r_id == r_id).first()
            req.status = 'Accepted'
            print(req.ad_id)
            ad = db.session.query(ad_details).filter(ad_details.ad_id ==req.ad_id).first()
            ad.i_id = req.i_id
            ad.status = "Assigned"
            db.session.commit()
            return make_response(jsonify({"message": "updated ad request"}),201)


        if reaction == 2:
            req= db.session.query(all_ad_requests).filter(all_ad_requests.r_id == r_id).first()
            req.status = 'Negotiate'
            db.session.commit()
            return make_response(jsonify({"message": "updated ad request"}),201)

        
        else:
            req = db.session.query(all_ad_requests).filter(all_ad_requests.r_id == r_id).first()
            req.status = 'Rejected'
            db.session.commit()
            return make_response(jsonify({"message": "updated ad request"}),201)



                

           
