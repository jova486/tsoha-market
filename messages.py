from db import db
import users
from flask import make_response

def get_list():
    sql = "SELECT A.id, A.item, A.ad_text, C.cat_name, A.img, A.user_id FROM ad A, category C WHERE A.cat_id = C.id ORDER BY A.sent_at"
    result = db.session.execute(sql)
    list = result.fetchall()
    return list

def send(content, to_id):
    from_id = users.user_id()
    if from_id == 0:
        flash('Et voi lähettää viestiä ellet ole kirjautunut', 'danger')
        return False
    sql = "INSERT INTO messages (content, from_id, to_id, sent_at) VALUES (:content, :from_id, :to_id, NOW())"
    db.session.execute(sql, {"content":content, "from_id":from_id, "to_id":to_id})
    db.session.commit()
    return True

def get_messages():
    user_id = users.user_id()
    if user_id == 0:
        return False
    to_id = user_id
    sql = "SELECT content, from_id, to_id, sent_at FROM messages WHERE to_id=:to_id ORDER BY sent_at DESC"
    result = db.session.execute(sql, {"to_id":to_id})
    message_list = result.fetchall()
    return message_list

def new_ad(cat_id, ad_type, valid, item, ad_text, image):
    user_id = users.user_id()
    if user_id == 0:
        return False

    name = image.filename
    if not name.endswith(".jpg"):
        return "Invalid filename"
    data = image.read()
    sql = "INSERT INTO images (data) VALUES (:data)"
    result = db.session.execute(sql, {"data":data})
    sql = "SELECT COUNT(id) FROM images"
    result = db.session.execute(sql)
    db.session.commit()
    img=result.fetchall()[0][0]
    valid = 30

    
    sql = """INSERT INTO ad (user_id, cat_id, ad_type, sent_at, valid, item, ad_text, img)
             VALUES (:user_id, :cat_id, :ad_type, NOW(), :valid, :item, :ad_text, :img)"""
    db.session.execute(sql, {"user_id":user_id, "cat_id":cat_id, "ad_type":ad_type, "valid":valid, "item":item, "ad_text":ad_text, "img":img})
    db.session.commit()
    return True

def get_cat():
    sql = "SELECT * FROM category ORDER BY cat_name"
    result = db.session.execute(sql)
    return result

def get_ad(id):
    sql = """SELECT A.id, A.item, A.ad_text, C.cat_name, I.id FROM ad A, category C, images I 
    WHERE A.id=:id AND A.cat_id = C.id AND A.img = I.id"""
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()[0]

def get_image(id):
    sql = "SELECT data FROM images WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    data = result.fetchone()[0]
    response = make_response(bytes(data))
    response.headers.set("Content-Type","image/jpeg")
    return response
