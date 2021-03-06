from db import db
import users
from flask import make_response, flash


def send(content, to_id):
    from_id = users.user_id()
    if from_id == 0:
        return False
    sql = "INSERT INTO messages (content, from_id, to_id, sent_at) VALUES (:content, :from_id, :to_id, NOW())"
    db.session.execute(sql, {"content":content, "from_id":from_id, "to_id":to_id})
    db.session.commit()
    return True

def get_messages():
    user_id = users.user_id()
    if user_id == 0:
        flash('Kirjaudu jotta voit valita omat viestisi', 'danger')
        return False
    to_id = user_id

    sql = "SELECT M.content, M.from_id, M.to_id, M.sent_at, F.username, T.username FROM messages M LEFT JOIN users F ON M.from_id = F.id LEFT JOIN users T ON M.to_id = T.id WHERE M.from_id=:to_id OR M.to_id=:to_id ORDER BY sent_at DESC"
    result = db.session.execute(sql, {"from_id":to_id, "to_id":to_id})
    message_list = result.fetchall()
    return message_list