from flask import Flask,render_template 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", titolo=home)

@app.route("/")
def details():
    prodotti=(("siero alla caffeina" , "bellezza", "20")("korean tone", "bellezza", "15")("gua sha", "bellezza", "11"))
    

app.run()
