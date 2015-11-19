from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          						#This is the main URL
def index():
    return render_template("index.html",name="home",title="Arlene")		#The argument should be in templates folder

@app.route('/index')          						#This is the main URL
def index2():
    return render_template("index.html",name="home",title="Arlene")		#The argument should be in templates folder

@app.route('/story')
def story():
    return render_template("portfolio.html",name="story",title="Arlene")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html",name="gallery",title="Arlene")


@app.route('/contact')
def contact():
    return render_template("contact.html",name="contact",title="Arlene")

@app.route('/resume')
def resume():
    return render_template("resume.html",name="resume",title="Arlene")


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
