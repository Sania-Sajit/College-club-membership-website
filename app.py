from flask import Flask,render_template,jsonify

app=Flask(__name__)

Clubs = [{'id':1,
          'name':"Robotics Club",
          'domain':"Technical",
          'Description':"Designing the future, one robot at a time.",
          "head":"Amy",
          'logo':"robo.jpg"},
         
         {'id':2,
          'name':"Music Club",
          'domain':"Cultural",
          'Description':"Where melodies come alive and voices unite.",
          "head":"Brian",
          'logo':"music.jpg"},

         {'id':3,
          'name':"Reading Club",
          'domain':"Literary",
          'Description':"Journey through stories, one page at a time.",
          "head":"Charles",
          'logo':"read.jpg"}
         
        ]
@app.route('/')
def hello():
    return render_template('home.html',clubs=Clubs)

@app.route('/api/clubs')
def list_clubs():
    return jsonify(Clubs)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

