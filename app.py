from flask import Flask,render_template,jsonify
from database import load_clubs_from_db

app=Flask(__name__)



@app.route('/')
def hello():
    clubs=load_clubs_from_db()
    return render_template('home.html',clubs=clubs)

@app.route('/api/clubs')
def list_clubs():
    clubs=load_clubs_from_db()
    return jsonify(clubs)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

