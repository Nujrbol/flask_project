from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"


@app.route("/about_me")
def about_me():
    return "About me information"


@app.route("/contact")
def contact():
    return "Nurbol email = nurbolkachkynbekov47@gmail.com"



if __name__ == "__main__":
    app.run(debug=True)
