from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "Hello world"


@app.route("/about")
def about_me():
    return "About me information"


@app.route("/contact")
def contact():
    return "Nurbol email = nurbolkachkynbekov47@gmail.com"


@app.route("/profile")
def profile():
    return "My profile"


@app.route("/catalog")
def catalog():
    return "Catalog"


@app.route("/support")
def support():
    return "Support"


if __name__ == "__main__":
    app.run(debug=True)
