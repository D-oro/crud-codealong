from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def select_all():
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    users = []
    for row in results:
        user = User(row["first_name"], row["last_name", row["id"]])
        users.append(user)

    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    
    if len(results) > 0: 
      result = results[0]
      user = User(result['first_name'], result['last_name'], result['id'] )
    return user