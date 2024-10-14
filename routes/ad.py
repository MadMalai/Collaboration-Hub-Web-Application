from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from application.models import *

class AdResource(Resource):
    @auth_token_required
    # from caching import cache
    @roles_accepted('admin','sponsor','influencer')
    # @cache.cached(timeout=20)
    def get(self,id):
        print(request)

        cam_id = id
        ad_list = db.session.query(ad_details).filter(ad_details.cam_id==cam_id).with_entities(ad_details.ad_id,ad_details.ad_name,ad_details.ad_req,ad_details.terms,ad_details.status,\
                    ad_details.pref_inf_category,ad_details.ad_budget,ad_details.i_id,ad_details.ad_progress).all()
        data=[]
        for ad in ad_list:
            addetails = {
                'ad_id': ad[0],
                'ad_name': ad[1],
                'ad_req': ad[2],
                'terms': ad[3],
                'status': ad[4],
                'pref_inf_category': ad[5],
                'ad_budget': ad[6],
                'i_id': ad[7],
                'ad_progress':ad[8]
                }
            data.append(addetails)
        if not data:
            return make_response(jsonify({"message": "No ad details listed"}), 404)
        return make_response(jsonify({"message": "get all ad details", "data": data}), 200)


    @auth_token_required
    @roles_accepted('sponsor')
    def post(self): 
        print(request.get_json())
        data = request.get_json()

        cam_id = data['cam_id']
        ad_name = data['ad_name']
        ad_req = data['ad_req']
        terms = data['terms']
        status = data['status']
        pref_inf_category = data['pref_inf_category']
        ad_budget = data['ad_budget']
        ad_progress = 0

        s_id = current_user.id

        addetails = ad_details(ad_name=ad_name,cam_id=cam_id, ad_req=ad_req,terms=terms, status=status\
                                ,pref_inf_category=pref_inf_category,ad_budget=ad_budget, i_id=None,ad_progress=ad_progress,s_id=s_id)

        db.session.add(addetails)
        db.session.commit() 

        return make_response(jsonify({"message": "Ad created successfully", "id": addetails.ad_id, "name": addetails.ad_name}), 201)

class AdSpecific(Resource): 
    @auth_token_required
    @roles_accepted('admin', 'sponsor')
    def get(self, id):
        ad_list = ad_details.query.filter_by(ad_id=id).first()
        ad_list = ad_list.formater()
        if not ad_list:
            return make_response(jsonify({"message": "No ads listed for the given id"}), 404)
        return jsonify({"message": "get specific ad", "data": ad_list} )   

    @auth_token_required
    @roles_accepted('admin', 'sponsor')
    def put(self, id):
        ad_list = ad_details.query.filter_by(ad_id=id,s_id=current_user.id).first()
        if not ad_list:
            return make_response(jsonify({"message": "No ads listed for the given id"}), 404)
        data = request.get_json()
        ad_name = data['ad_name']
        if not ad_name:
            return jsonify({"message": "ad name is required"})
        ad_req = data['ad_req']
        if not ad_req:
            return jsonify({"message": "ad description is required"})
        terms = data['terms']
        if not terms:
            return jsonify({"message": "terms is required"})         
        ad_budget = data['ad_budget']
        if not ad_budget:
            return jsonify({"message": "ad budget is required"})                    
        pref_inf_category = data['pref_inf_category']
        if not pref_inf_category:
            return jsonify({"message": "pref_inf_category is required"})

        ad_list.ad_name = ad_name 
        ad_list.ad_req = ad_req         
        ad_list.terms = terms
        ad_list.ad_budget = ad_budget
        ad_list.pref_inf_category = pref_inf_category  
                
        # if current_user.has_role('admin,sponsor'):
        #     campaigns.status = True
        # else:
        #     campaigns.status = False
        db.session.commit()
        return make_response(jsonify({"message": "update specific ad", 'id': id}) ,201)

    @auth_token_required
    @roles_accepted('sponsor')
    def delete(self, id):
        ad_list = ad_details.query.filter_by(ad_id=id,s_id=current_user.id).first()
        if not ad_list:
            return make_response(jsonify({"message":"No ads listed for the given id"}), 404)
        else:
            db.session.delete(ad_list)
            db.session.commit()
        
        ad_req_list = db.session.query(all_ad_requests).join(campaign.cam_id==all_ad_requests.cam_id).join(sponsor.s_id==campaign.s_id).filter_by(all_ad_requests.ad_id==id,sponsor.s_id==current_user.id).first()
        if not ad_req_list:
            return make_response(jsonify({"message":"No ads listed for the given id"}), 404)
        else:
            db.session.delete(ad_req_list)
            db.session.commit()
        
        return make_response(jsonify({"message": "delete specific ad operation compelted", 'id': id}), 201)  




        

