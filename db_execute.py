from flask_login import UserMixin

from db import get_db

class Value():
  @staticmethod
  def create(value, double):
    db = get_db()
    db.execute(
      "INSERT INTO users (value, double) "
      "VALUES (?, ?)", (value, double)
    )
    db.commit()

  @staticmethod
  def get(value):
    db = get_db()
    db.execute(
      "SELECT double FROM users WHERE value = ?", (value)
    ).fetchone()
    if not double:
      return None 
    return double
