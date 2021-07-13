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
    double = db.execute(
      "SELECT double FROM users WHERE value = ?", (value)
    )
    if not double:
      double = "Value not in database"
    else:
      double = double.fetchone()[0] 
    return double
