import os
import webapp2
import jinja2

from google.appengine.api import users
from models import *
from get_rep_data import *



jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      email_address = user.nickname()
      user = User.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      if user:
        self.response.write('''
            Welcome %s (%s)! <br> %s <br>''' % (
              user.name,
              email_address,
              signout_link_html))
      else:
        self.response.write('''
            Welcome to our site, %s!  Please sign up! <br>
            <form method="post" action="/">
            <input type="text" name="name">
            <input type="submit">
            </form><br> %s <br>
            ''' % (email_address, signout_link_html))
    else:
      self.response.write('''
        Please log in! <br>
        <a href="%s">Sign in</a>''' % (
          users.create_login_url('/')))

  def post(self):
    user = users.get_current_user()
    if not user:
      self.error(500)
      return
    user = User(
        name=self.request.get('name'),
        id=user.user_id())
    user.put()
    self.response.write('Thanks for signing up, %s!' %
        user.name)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_env.get_template("/templates/welcome.html")
        self.response.write(welcome_template.render())

class NewsHandler(webapp2.RequestHandler):
    def get(self):
        news_template = jinja_env.get_template("/templates/news.html")
        api_key = ApiKey.query().filter(ApiKey.name == "NEWS").get().value
        category = self.request.get("category")
        news = urlfetch.fetch("https://newsapi.org/v2/top-headlines?q={}&pageSize=20&apikey={}".format(category.lower(), api_key))
        self.response.write(news_template.render({ "news": json.loads(news.content.decode('utf-8')) }))

class RepHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {"user_location": "", "rep_data":{}}
        user = User.get_by_id(users.get_current_user().user_id())
        rep_template = jinja_env.get_template("/templates/representatives.html")
        if user.location:
            request_params = {
                "key":ApiKey.query(ApiKey.name == "CIVIC_INFO").get().value,
                "address":user.location,
                "levels":"country",
                "roles":["legislatorLowerBody", "legislatorUpperBody"]}

            template_params["rep_data"] = get_rep_data(request_params)
            template_params["user_location"] = user.location
        self.response.write(rep_template.render(template_params))
    def post(self):
        user = User.get_by_id(users.get_current_user().user_id())
        location = self.request.get("location_input")
        user.location = location
        user.put()
        self.redirect("/representatives")

class ServiceHandler(webapp2.RequestHandler):
    def get(self):
        service_template = jinja_env.get_template("/templates/service.html")
        self.response.write(service_template.render())

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        events_template = jinja_env.get_template("/templates/events.html")
        self.response.write(events_template.render())


app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/welcome', WelcomeHandler),
    ('/news', NewsHandler),
    ('/representatives', RepHandler),
    ('/service', ServiceHandler),
    ('/events', EventsHandler),


], debug=True)
