# # from app import celery_app

# # @celery_app.task()
# # def helloWorld():
# #     print("first task")
#     # return "Hello World"
# from app import celery_app
# from celery_context import ContextTask
# from mailer import mail
# from flask_mail import Message
# from application.models import *
# from sqlalchemy import distinct,case, func

# @celery_app.task(base=ContextTask)
# def daily_mail():
#     request_received = (
#         db.session.query(all_ad_requests).outerjoin(User, all_ad_requests.i_id == User.id).filter(all_ad_requests.status == 'request sent').with_entities(User.email,all_ad_requests.i_id).all()
#     )

#     email_sub = "Daily email"
#     email_body = "Please accept the ad requests you received or check the public ads"

#     for req in request_received:
#         html_body = "<html><body>"
#         html_body += "<h1>Hi"
#         html_body += f"{req.i_id}</h1>"
#         html_body += f"<p>{req.email}</p>"
#         html_body += "</body></html>"
#         msg = Message(subject=email_sub, recipients=[req.email])
#         msg.body = email_body
#         msg.html = html_body
#         # msg.sender = "admin@a.com"
#         mail.send(msg)
#     return "Mail sent"       

# @celery_app.task(base=ContextTask)
# def monthly_mail():
#     ads_status = (db.session.query(campaign.cam_name,func.count(case([(ad_details.status == 100, 1)])).label('completed_ads_count')).join(ad_details, campaign.cam_id == ad_details.cam_id).group_by(campaign.cam_id).all())

#     email_sub = "Monthly email"
#     email_body = "Campaign name:{campaign.cam_name} ,No. of completed ads:{completed_ads_count} "

#     for ad_det in ads_status:
#         html_body = "<html><body>"
#         html_body += "<h1>Hi"
#         html_body += f"{ad_det.id}</h1>"
#         html_body += f"<p>{ad_det.email}</p>"
#         html_body += "</body></html>"
#         msg = Message(subject=email_sub, recipients=[ad_det.email])
#         msg.body = email_body
#         msg.html = html_body
#         mail.send(msg)
#     return "Mail sent"       