#Importing the required libraries
from flask import Flask , g , request , jsonify
from flask_restful import Api , Resource 
from database import get_db , connect_db

app = Flask(__name__) # create the Flask app
api = Api(app) # wrap the app in the api

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        
class getUser(Resource):
    def get(self,user_id):
        db = get_db()
        try:
            cur = db.execute('select * from users where id = ?', [user_id])
            results = cur.fetchone()
        except:
            return {"data":"No data found!"}
        return {"User_data": {
            "Username" : results['username'],
            "Mail" : results['email'],
            "Password" : results['password']
        }}
    
class CreateUser(Resource):
    def post(self):
        try:
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
        except:
            return {"Status":"Error","Message":"Something went wrong!"}
        db = get_db()
        db.execute('insert into users (username,email,password) values (?,?,?)', [username,email,password])
        db.commit()
        return jsonify({"Status":"Successfully created!"})
    
class getUsers(Resource):
    def get(self):
        db = get_db()
        try:
            cur = db.execute('select * from users')
            results = cur.fetchall()
            list_data = []
            for i in results:
                user = {
                    "Username" : i['username'],
                    "Mail" : i['email'],
                    "Password" : i['password']
                }
                list_data.append(user)
        except:
            return {"data":"No data found!"}
        return jsonify({"Users":list_data})


    
api.add_resource(getUser, "/user/<int:user_id>") # add the resource to the api
api.add_resource(CreateUser, "/create_user") # add the resource to the api
api.add_resource(getUsers, "/user") # add the resource to the api

if __name__ == "__main__":
    app.run(debug=True) # run the app in debug mode