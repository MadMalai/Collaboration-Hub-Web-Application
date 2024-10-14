from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user
from application.models import *
# from caching import cache

class SponsorResource(Resource):
    # from caching import cache
    @auth_token_required
    @roles_accepted('admin','sponsor','influencer')
    # @cache.cached(timeout=20)
    def get(self,id):

        sponsor_list = db.session.query(sponsor).filter(sponsor.s_id==id).with_entities(sponsor.s_name,sponsor.s_email,sponsor.s_industry,sponsor.org_name,\
                    sponsor.org_size,sponsor.org_type).all()
        data = []
        for spon in sponsor_list:
            s_details = {
                's_name': spon[0],
                's_industry': spon[2],
                'org_name': spon[3],
                'org_size': spon[4],
                'org_type': spon[5],
                }
            data.append(s_details)
        if not data:
            return make_response(jsonify({"message": "No sponsor details listed"}), 404)
        return make_response(jsonify({"message": "get all sponsor details", "data": data}), 200)


    def post(self): 
        data = request.get_json()
        print(data)
        s_name = data['s_name']
        s_industry = data['s_industry']
        org_name = data['org_name']
        org_size = data['org_size']
        org_type = data['org_type']
        s_id = data['s_id']

        s_details = sponsor(s_name=s_name,s_email=None,s_pwd=None,s_industry=s_industry,\
                            org_name=org_name,org_size=org_size, org_type=org_type,s_adminflag=None,s_id=s_id)

        db.session.add(s_details)
        db.session.commit() 

        return make_response(jsonify({"message": "sponsor created/updated successfully", "id": s_details.s_id, "name": s_details.s_name}), 201)

 

  



class SponsorStat(Resource):
    @auth_token_required
    @roles_accepted('sponsor')
    def get(self): 
        campaign_by_months=db.session.query(func.strftime('%Y-%m', campaign.cam_start_date).label('month_year'),
                                func.count(campaign.cam_id).label('campaign_count')
                                ).filter(campaign.s_id == userid).group_by(func.strftime('%Y-%m', campaign.cam_start_date)).all()

        campaign_status_summary={
            'Status_label':['Ongoing','Completed'],
            's_values' : [db.session.query(campaign).filter(campaign.progress < 100,campaign.s_id == userid).count(),db.session.query(campaign).filter(campaign.progress== 100,campaign.s_id == userid).count()],
            'months_label': [mon[0] for mon in campaign_by_months],
            'm_values':[mon[1] for mon in campaign_by_months]
        }

        print(campaign_status_summary)
        cam_cnt = db.session.query(campaign).join(sponsor).filter(campaign.s_id == userid,campaign.s_id == sponsor.s_id).count()
        ad_cnt = db.session.query(ad_details).filter(ad_details.s_id == userid).count()

        kpi_data = {
        'cam_count': cam_cnt,
        'ad_count': ad_cnt
        }
        return jsonify({
        "kpi_data": kpi_data,
        "campaign_by_months": campaign_by_months,
        "campaign_status_summary": campaign_status_summary
    })    



  

