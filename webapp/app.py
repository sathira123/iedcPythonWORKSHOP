from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def disp():
    return render_template("disp.html")
@app.route("/about")
def abt():
    return"Welcome to my about page"
if(__name__=="__main__"):
    app.run(debug=True)