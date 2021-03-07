from db import db
import users
from flask import make_response, flash

def get_list():
   
   
    sql = """SELECT A.id, A.item, A.ad_text, C.cat_name, A.img, A.user_id FROM ad A, category C 
    WHERE A.cat_id = C.id AND A.ad_type != 5 AND A.sent_at > current_date - A.valid ORDER BY A.sent_at DESC"""
    result = db.session.execute(sql)
   
    list = result.fetchall()
    return list


def get_my_list():
    
    user_id = users.user_id()
    if user_id == 0:
        return False
    
    sql = """SELECT A.id, A.item, A.ad_text, C.cat_name, A.img, A.user_id FROM ad A, category C 
    WHERE A.cat_id = C.id AND A.user_id=:user_id AND A.ad_type != 5 AND A.sent_at > current_date - A.valid ORDER BY A.sent_at DESC"""
    result = db.session.execute(sql, {"user_id":user_id})
    list = result.fetchall()
   
    return list

def search(cat_id, ad_type, item, ad_text):
    s = "%"
    item = s+item
    item +=s
    ad_text = s+ad_text
    ad_text +=s
    sql = """SELECT A.id, A.item, A.ad_text, C.cat_name, A.img, A.user_id FROM ad A, category C 
        WHERE A.cat_id = C.id AND A.ad_type != 5 AND A.cat_id=:cat_id and A.ad_type=:ad_type AND A.sent_at > current_date - A.valid"""
    if(item != "%%"):
        print("item")
        if(ad_text != "%%"):
            sql += " AND (A.item ILIKE :item"
        else:
            sql += " AND A.item ILIKE :item"

    if(ad_text != "%%"):
        print("ad_text")
        if(item != "%%"):
            sql += " OR A.ad_text ILIKE :ad_text)"
        else:
            sql += " AND A.ad_text ILIKE :ad_text"
    sql += " ORDER BY A.sent_at DESC"
    result = db.session.execute(sql, {"cat_id":cat_id, "ad_type":ad_type, "item":item, "ad_text":ad_text})
    list = result.fetchall()
    return list

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

    sql = """INSERT INTO ad (user_id, cat_id, ad_type, sent_at, valid, item, ad_text, img)
             VALUES (:user_id, :cat_id, :ad_type, NOW(), :valid, :item, :ad_text, :img)"""
    db.session.execute(sql, {"user_id":user_id, "cat_id":cat_id, "ad_type":ad_type, "valid":valid, "item":item, "ad_text":ad_text, "img":img})
    db.session.commit()
    return True

def new_cat(cat_name):
    sql = "INSERT INTO category(parent_id, dep, cat_name) VALUES (0,0,:cat_name)"
    result = db.session.execute(sql, {"cat_name":cat_name})
    db.session.commit()
    return True

def delete_ad(id):
    sql = "UPDATE ad SET ad_type=5 WHERE id=:id"
    db.session.execute(sql, {"id":id})
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
