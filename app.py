from flask import Flask,render_template,jsonify,request
from database import load_clubs_from_db,load_club_from_db,add_application_to_db

app=Flask(__name__)



@app.route('/')
def hello():
    clubs=load_clubs_from_db()
    return render_template('home.html',clubs=clubs)

@app.route('/api/clubs')
def list_clubs():
    clubs=load_clubs_from_db()
    return jsonify(clubs)

@app.route("/club/<id>")
def show_club(id):
    club=load_club_from_db(id)
    if not club:
        return "Not Found",404
    return render_template('clubpage.html',club=club)
    
@app.route("/club/<id>/apply", methods=['Post'])
def apply_to_club(id):
    club=load_club_from_db(id)
    data=request.form

    add_application_to_db(id,data)
    return render_template("submitted.html", application=data,club=club)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

