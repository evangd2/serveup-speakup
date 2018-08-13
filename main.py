import os
import webapp2
import jinja2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_env.get_template("templates/welcome.html")
        self.response.write(welcome_template.render())

class NewsHandler(webapp2.RequestHandler):
    def get(self):
        news_template = jinja_env.get_template("templates/news.html")
        self.response.write(news_template.render())

class RepHandler(webapp2.RequestHandler):
    def get(self):
        rep_template = jinja_env.get_template("templates/news.html")
        self.response.write(rep_template.render())

class ServiceHandler(webapp2.RequestHandler):
    def get(self):
        service_template = jinja_env.get_template("templates/service.html")
        self.response.write(service_template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/news', NewsHandler),
    ('/representatives', RepHandler),
    ('/service', ServiceHandler),
], debug=True)
