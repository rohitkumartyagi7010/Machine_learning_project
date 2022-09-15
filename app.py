from flask import request,Flask ,jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():

    return "CI CD pipeline has been created"

if __name__=="__main__":
    app.run(debug=True)
