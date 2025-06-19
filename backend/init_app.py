from app import create_app

app,_ = create_app()

with app.app_context():
    from application.models import db, user_datastore

    db.drop_all()

    db.create_all()
    
    #create roles in DB
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='sponsor', description='sponsor')
    user_datastore.find_or_create_role(name='influencer', description='influencer')

    db.session.commit()

    #find for admin user in the DB
    admin_user = user_datastore.find_user(email="admin@a.com")
    from application.models import User
    admin__user = User.query.filter_by(email="admin@a.com").first()

    #if no admin found, create admin, grant all 3 access roles in DB
    if not admin_user:
        User_admin = user_datastore.create_user(email="admin@a.com", password="admin")
        user_datastore.add_role_to_user(User_admin, 'admin')
        user_datastore.add_role_to_user(User_admin, 'sponsor')
        user_datastore.add_role_to_user(User_admin, 'influencer')

    db.session.commit()