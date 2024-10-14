from flask_sqlalchemy import SQLAlchemy

from flask_security import UserMixin, RoleMixin, AsaList, SQLAlchemyUserDatastore

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                    String, ForeignKey


db = SQLAlchemy()

# relationship table
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    permissions = Column(MutableList.as_mutable(AsaList()), nullable=True)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(64), unique=True, nullable=False)
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


# class category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), unique=True)
#     desc = db.Column(db.String(255))

class admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    admin_name = db.Column(db.String)
    admin_email = db.Column(db.String, unique=True)
    admin_pwd = db.Column(db.String, unique=True)
    approval = db.Column(db.String)

class sponsor(db.Model):
    __tablename__ = 'sponsor'
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    s_name = db.Column(db.String)
    s_email = db.Column(db.String)
    s_pwd = db.Column(db.String)
    s_industry = db.Column(db.String)
    org_name = db.Column(db.String)
    org_size = db.Column(db.Integer)
    org_type = db.Column(db.String)
    s_adminflag =db.Column(db.Integer)
    

class influencer(db.Model):
    __tablename__ = 'influencer'
    i_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    i_name = db.Column(db.String)
    i_email = db.Column(db.String)
    i_pwd = db.Column(db.String)
    i_presence = db.Column(db.String)
    i_follow_no = db.Column(db.Integer)
    i_ph_no =db.Column(db.Integer)
    i_link=db.Column(db.String)
    prev_brand_collab =db.Column(db.String)
    i_location=db.Column(db.String)
    i_language =db.Column(db.String)
    i_exp =db.Column(db.Integer)
    i_niche =db.Column(db.String)
    i_adminflag =db.Column(db.Integer)


class campaign(db.Model):
    __tablename__ = 'campaign'
    cam_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cam_name = db.Column(db.String)
    cam_desc = db.Column(db.Text)
    cam_start_date = db.Column(db.String)
    cam_end_date = db.Column(db.String)
    cam_budget = db.Column(db.Float)
    visibility = db.Column(db.String)
    goals = db.Column(db.Text)
    progress = db.Column(db.Integer)
    s_id = db.Column(db.Integer)
    cam_category = db.Column(db.String)
    cname_srch =  db.Column(db.Text)
    cam_adminflag =db.Column(db.Integer)
    s_id=db.Column(db.Integer,db.ForeignKey("sponsor.s_id"),nullable=False)

    def formater(self):
        return {
                "cam_id" : self.cam_id,
                "cam_name" : self.cam_name,
                "cam_desc" : self.cam_desc,
                "cam_start_date" : self.cam_start_date,
                "cam_end_date" : self.cam_end_date,
                "cam_budget" : self.cam_budget,
                "visibility" : self.visibility,
                "goals" : self.goals,
                "progress" : self.progress,
                "s_id" : self.s_id,
                "cam_category" : self.cam_category,
                "cname_srch" :  self.cname_srch,
                "cam_adminflag" : self.cam_adminflag,
            }

class ad_details(db.Model):
    __tablename__ = 'ad_details'
    ad_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    s_id = db.Column(db.Integer)
    cam_id = db.Column(db.Integer) 
    ad_name = db.Column(db.String)
    ad_req = db.Column(db.Text)
    terms = db.Column(db.String)
    status = db.Column(db.String)
    pref_inf_category = db.Column(db.String)
    ad_budget = db.Column(db.Float)
    #i_id = db.Column(db.Integer)
    ad_progress = db.Column(db.Integer) 
    s_id=db.Column(db.Integer,db.ForeignKey("sponsor.s_id"),nullable=False)
    i_id=db.Column(db.Integer,db.ForeignKey("influencer.i_id"),nullable=True)
    cam_id=db.Column(db.Integer,db.ForeignKey("campaign.cam_id"),nullable=False)

    def formater(self):
        return {
            "ad_id" : self.ad_id,
            "cam_id" : self.cam_id,
            "s_id"  : self.s_id,  
            "i_id"  : self.i_id,  
            "ad_name"  : self.ad_name,
            "ad_req"  : self.ad_req,
            "terms" : self.terms, 
            "status"  : self.status, 
            "pref_inf_category"  : self.pref_inf_category, 
            "ad_budget"  : self.ad_budget, 
            "ad_progress" :self.ad_progress
        }

class all_ad_requests(db.Model):
    __tablename__ = 'all_ad_requests'
    r_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cam_id = db.Column(db.Integer) 
    ad_id = db.Column(db.Integer) 
    request_by = db.Column(db.String)
    i_id = db.Column(db.Integer) 
    status = db.Column(db.String)
    ad_id=db.Column(db.Integer,db.ForeignKey("ad_details.ad_id"),nullable=False)
    cam_id=db.Column(db.Integer,db.ForeignKey("campaign.cam_id"),nullable=False)
    i_id=db.Column(db.Integer,db.ForeignKey("influencer.i_id"),nullable=False)


