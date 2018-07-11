from flask import Flask, render_template
# import Flask class from flask framework
# Flask is a class of flask library
# render_template method of the flask library accesses html file from python files and displays it on the request of url.

app = Flask(__name__)     # think of it as the main website
#app is the Flask object
#(__name__) helps Flask determine the route path

# @ signifies a decorator - its a way you can wrap up an existing function and modify its behaviour.
@app.route('/')      # request this ('/') url
def home():
    return render_template("home.html")  # here is the response of the above request
# connecting the different pages of the website is called Routing.
#'/' is the route directory that is the home page of the website
# if we want to do something with the profile page then we write ('/profile')

@app.route('/about/')                    # connects the home page of the website
def about():                             # usually name the function same with the page you are working with
    return "This is the About page!"     # it defines what your webpage will do.
# # the last 3 lines of codes is called routing or mapping
# # Its basicaly tying a url on your website to a python function.

@app.route('/profile/<username>')
def profile(username):
    return "Hi there %s" %username


if __name__ == "__main__":   # its a quick check to make sure that we only run the app whenever this file is called directly
    app.run(debug=True)      # means start this file on our server
# # CASE I : Script Executed -  __name__ = "__main__"
# # CASE II : Script Imported -  __name__ = "RealWorldApp-WebApp"
#
# #to make our website actually run whenever we run this program
#




