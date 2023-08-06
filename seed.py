#seed.py
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from model import db, User

data = [
{
  "id": 1,
  "username": "sbeeching0",
  "email": "dgoulstone0@about.me",
  "password": "mY2<f2*(~u5lp",
  "user_role":"superadmin"
}, {
  "id": 2,
  "username": "tbesantie1",
  "email": "pdenney1@boston.com",
  "password": "aI7>.9e!eo1zE10v",
  "user_role":"admin"
}, {
  "id": 3,
  "username": "jduddy2",
  "email": "ekilloran2@salon.com",
  "password": "sN9{pcNlk",
  "user_role":"driver"
}, {
  "id": 4,
  "username": "okemson3",
  "email": "ahotchkin3@washington.edu",
  "password": "cU4+K?3(25",
  "user_role":"employee"
}, {
  "id": 5,
  "username": "jwilbor4",
  "email": "spalmar4@blinklist.com",
  "password": "qS4*f\"E+3/}!E",
  "user_role":"customer"
}, {
  "id": 6,
  "username": "jcattlemull5",
  "email": "iashurst5@gmpg.org",
  "password": "xR0<v26oJ1ON\\g",
  "user_role":"customer"
}, {
  "id": 7,
  "username": "gfilgate6",
  "email": "mbecerro6@dyndns.org",
  "password": "bJ6=hIk05DwLi.T",
  "user_role":"customer"
}, {
  "id": 8,
  "username": "msergeant7",
  "email": "lcampa7@yahoo.co.jp",
  "password": "sN9'ZDnOr/Ik",
  "user_role":"customer"
}, {
  "id": 9,
  "username": "bpreble8",
  "email": "awhorlow8@themeforest.net",
  "password": "zE2)00/iL*#}A2_",
  "user_role":"customer"
}, {
  "id": 10,
  "username": "edenisovich9",
  "email": "zmallion9@independent.co.uk",
  "password": "cQ4(/#f~wFMsH7|",
  "user_role":"customer"
}]

roles = ['superadmin', 'admin', 'customer', 'driver','restaurant_owner']

with app.app_context():
    users = []
    for i in range(len(data)):
        data[i]['password'] = generate_password_hash(data[i]['password'])
        user = User(**data[i], user_role=roles[i])
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    print("Seeded Successfully")
