#seed.py
from werkzeug.security import generate_password_hash, check_password_hash
from main2 import app
from model import db, User

data = [
{
  "username": "sbeeching0",
  "email": "dgoulstone0@about.me",
  "password": "mY2<f2*(~u5lp",
  "type":"superadmin"
}, {
  "username": "tbesantie1",
  "email": "pdenney1@boston.com",
  "password": "aI7>.9e!eo1zE10v",
  "type":"admin"
}, {
  "username": "jduddy2",
  "email": "ekilloran2@salon.com",
  "password": "sN9{pcNlk",
  "type":"driver"
}, {
  "username": "okemson3",
  "email": "ahotchkin3@washington.edu",
  "password": "cU4+K?3(25",
  "type":"employee"
}, {
  "username": "jwilbor4",
  "email": "spalmar4@blinklist.com",
  "password": "qS4*f\"E+3/}!E",
  "type":"customer"
}, {
  "username": "jcattlemull5",
  "email": "iashurst5@gmpg.org",
  "password": "xR0<v26oJ1ON\\g",
  "type":"customer"
}, {
  "username": "gfilgate6",
  "email": "mbecerro6@dyndns.org",
  "password": "bJ6=hIk05DwLi.T",
  "type":"customer"
}, {
  "username": "msergeant7",
  "email": "lcampa7@yahoo.co.jp",
  "password": "sN9'ZDnOr/Ik",
  "type":"customer"
}, {
  "username": "bpreble8",
  "email": "awhorlow8@themeforest.net",
  "password": "zE2)00/iL*#}A2_",
  "type":"customer"
}, {
  "username": "edenisovich9",
  "email": "zmallion9@independent.co.uk",
  "password": "cQ4(/#f~wFMsH7|",
  "type":"customer"
}]

type = ['superadmin', 'admin', 'customer', 'driver','restaurant_owner']

with app.app_context():
    users = []
    for i in range(len(data)):
        data[i]['password'] = generate_password_hash(data[i]['password'])
        user = User(**data[i])
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    print("Seeded Successfully")
