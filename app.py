from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template ("home.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/contact")
def contact():
    return render_template ("contact.html")

@app.route("/base")
def base():
    return render_template ("base.html")

@app.route("/wallpaper")
def wallpaper():
    return render_template ("wallpaper.html")

@app.route("/wallpaper2")
def wallpaper2():
    return render_template ("wallpaper2.html")

@app.route("/wallpaper3")
def wallpaper3():
    return render_template ("wallpaper3.html")






if __name__ == "__main__":
    app.run(debug=True)
    