from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from application.models import *
from sqlalchemy import func

class InfluencerResource(Resource):
    # from caching import cache
    @auth_token_required
    @roles_accepted('admin','sponsor')
    # @cache.cached(timeout=20)
    def get(self):
        inf_list = db.session.query(influencer).with_entities(influencer.i_name,influencer.i_email,influencer.i_presence,influencer.i_follow_no,\
                    influencer.i_niche,influencer.i_exp,influencer.i_ph_no,influencer.i_link,influencer.prev_brand_collab,influencer.i_location,\
                    influencer.i_language,influencer.i_id).all()
        data = []
        for inf in inf_list:
            i_details = {
                'i_name': inf[0],
                'i_email': inf[1],
                'i_presence': inf[2],
                'i_follow_no': inf[3],
                'i_niche': inf[4],
                'i_exp': inf[5],
                'i_ph_no': inf[6],
                'i_link': inf[7],
                'prev_brand_collab': inf[8],
                'i_location': inf[9],
                'i_language': inf[10],    
                'i_id': inf[11]             
         
                }
            data.append(i_details)
        if not data:
            return make_response(jsonify({"message": "No influencer details listed"}), 404)
        return make_response(jsonify({"message": "get all influencer details", "data": data}), 200)



    def post(self): 
        data = request.get_json()
        i_name= data['i_name']
        i_presence= data['i_presence']
        i_follow_no= data['i_follow_no']
        i_niche= data['i_niche']
        i_exp= data['i_exp']
        i_link= data['i_link']
        prev_brand_collab= data['prev_brand_collab']
        i_location=data['i_location']
        i_language= data['i_language'] 
        i_id = data['i_id']

        i_details = influencer(i_name=i_name,i_email=None,i_pwd=None,i_presence=i_presence, i_follow_no=i_follow_no\
                                ,i_niche=i_niche,i_exp=i_exp,i_ph_no=None,i_link=i_link,prev_brand_collab=prev_brand_collab,\
                                i_location=i_location,i_language=i_language,i_adminflag=None,i_id=i_id)

        db.session.add(i_details)
        db.session.commit() 

        return make_response(jsonify({"message": "influencer created/updated successfully", "id": i_details.i_id, "name": i_details.i_name}), 201)


class InfluencerSpecific(Resource):
    # from caching import cache
    @auth_token_required
    @roles_accepted('admin','influencer','sponsor')
    # @cache.cached(timeout=20)
    def get(self,id):
        inf_list = db.session.query(influencer).filter(influencer.i_id==id).with_entities(influencer.i_name,influencer.i_email,influencer.i_presence,influencer.i_follow_no,\
                    influencer.i_niche,influencer.i_exp,influencer.i_ph_no,influencer.i_link,influencer.prev_brand_collab,influencer.i_location,\
                    influencer.i_language,influencer.i_id).all()
        data = []
        for inf in inf_list:
            i_details = {
                'i_name': inf[0],
                'i_email': inf[1],
                'i_presence': inf[2],
                'i_follow_no': inf[3],
                'i_niche': inf[4],
                'i_exp': inf[5],
                'i_ph_no': inf[6],
                'i_link': inf[7],
                'prev_brand_collab': inf[8],
                'i_location': inf[9],
                'i_language': inf[10],    
                'i_id': inf[11]             
         
                }
            data.append(i_details)
        if not data:
            return make_response(jsonify({"message": "No influencer details listed"}), 404)
        return make_response(jsonify({"message": "get all influencer details", "data": data}), 200) 



class InfluencerStat(Resource):
    # from caching import cache
    @auth_token_required
    @roles_accepted('influencer')
    # @cache.cached(timeout=20)
    def get(self):
        userid=current_user.id
        industry_focus = db.session.query(ad_details).join(sponsor,ad_details.s_id==sponsor.s_id).filter(ad_details.i_id == userid).with_entities(sponsor.s_industry, func.count(sponsor.s_industry)).group_by(sponsor.s_industry)
        total_ads = db.session.query(ad_details).filter(ad_details.i_id == userid).count()
        total_campaigns = db.session.query(campaign).join(ad_details,campaign.cam_id ==ad_details.cam_id).filter(ad_details.i_id == userid).count()

        kpi_data = {
        'total_ads': total_ads,
        'total_campaigns': total_campaigns,
        }
        print(kpi_data)

        sponsor_profile={
            "Industries" :[ind[0] for ind in industry_focus ],
            "count":[ind[1] for ind in industry_focus ]
        }
        print(sponsor_profile)
        campaign_by_months=db.session.query(ad_details).join(sponsor,ad_details.s_id==sponsor.s_id).join(campaign,ad_details.cam_id==campaign.cam_id).filter(ad_details.i_id == userid).with_entities(
                                func.strftime('%Y-%m', campaign.cam_start_date).label('month_year'),
                                func.count(campaign.cam_id).label('campaign_count')
                                ).group_by(func.strftime('%Y-%m', campaign.cam_start_date)).all()

        campaign_status_summary={
            'Status_label':['Ongoing','Completed'],
            's_values' : [db.session.query(campaign.progress < 100).count(),db.session.query(campaign.progress == 100).count()],
            'months_label': [mon[0] for mon in campaign_by_months],
            'm_values':[mon[1] for mon in campaign_by_months]
        }
        print(campaign_status_summary)
        data={
            "kpi_data": kpi_data,
            # "sponsor_profile": sponsor_profile,
            # "campaign_by_months": campaign_by_months,
            # "campaign_status_summary": campaign_status_summary
            }

        if not data:
            return make_response(jsonify({"message": "No influencer Stats"}), 404)
        return make_response(jsonify({"message": "all influencer stats", "data":data}), 200)  