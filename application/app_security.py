
from flask_security import Security, SQLAlchemyUserDatastore
from database.models import db,User,Role

#The SQLAlchemyUserDatastore is used to connect SQLAlchemy models (such as User and Role) with Flask-Security.
user_datastore = SQLAlchemyUserDatastore(db,User,Role)

# Initialise Flask Security
security = Security()