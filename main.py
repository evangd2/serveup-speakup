import os
import webapp2
import jinja2
import io

from google.appengine.api import users, images
from models import *
from get_rep_data import *
#from PIL import Image

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    google_user = users.get_current_user()
    template = jinja_env.get_template("templates/login.html")
    if google_user:
      email_address = google_user.nickname()
      ds_user = User.get_by_id(google_user.user_id())
      if ds_user:
          self.redirect("/welcome")
      else:
        self.response.write(template.render({
            "email_address": email_address,
            "signout_link": users.create_logout_url("/")
            }))
    else:
      self.response.write(template.render({
          "signin_link": users.create_login_url("/")
          }))

  def post(self):
    user = users.get_current_user()
    if not user:
      self.error(500)
      return
    user = User(
        name=self.request.get('name'),
        id=user.user_id())
    user.put()
    self.redirect("/welcome")

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        user = User.get_by_id(google_user.user_id()) if google_user else None
        if user:
            welcome_template = jinja_env.get_template("/templates/welcome.html")
            #photo_url = images.get_serving_url(user.photo, secure_url=True) if user.photo else "/media/plant.png"
            self.response.write(welcome_template.render({
                "username": user.name,
                "signout_link": users.create_logout_url("/"),
                "photo_url": "/media/plant.png"
            }))
        else:
            self.redirect("/")
    def post(self):
        pass
        '''google_user = users.get_current_user()
        user = User.get_by_id(google_user.user_id()) if google_user else None
        if user:
            pic_str = self.request.get("upload_photo")
            profile_pic = Image.open(io.BytesIO(pic_str))
            profile_pic = profile_pic.resize((128, 128))

            with io.BytesIO() as output:
                profile_pic.save(output, format="JPEG")
                pic_str = output.getvalue()

            user.photo = pic_str
            user.put()
            self.redirect("/welcome")'''
class NewsHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        user = User.get_by_id(google_user.user_id()) if google_user else None
        if user:
            news_template = jinja_env.get_template("/templates/news.html")
            api_key = ApiKey.query().filter(ApiKey.name == "NEWS").get().value
            category = self.request.get("category")
            news = urlfetch.fetch("https://newsapi.org/v2/top-headlines?q={}&pageSize=20&sortBy=popularity&apikey={}".format(category.lower().replace(" ", ""), api_key))
            dict_news = json.loads(news.content)
            if "totalResults" in dict_news:
                if dict_news['totalResults'] < 3:
                    news = urlfetch.fetch("https://newsapi.org/v2/everything?q={}&pageSize=20&sortBy=popularity&apikey={}".format(category.lower().replace(" ", ""), api_key))
            self.response.write(news_template.render({
                "news": json.loads(news.content.decode('utf-8')),
                "username": user.name,
                "signout_link": users.create_logout_url("/")
            }))
        else:
            self.redirect("/")

class RepHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        user = User.get_by_id(google_user.user_id()) if google_user else None
        if user:
            template_params = {"user_location": "", "rep_data":{}}
            rep_template = jinja_env.get_template("/templates/representatives.html")
            if user.address:
                request_params = {
                    "key":ApiKey.query(ApiKey.name == "CIVIC_INFO").get().value,
                    "address":user.address,
                    "levels":"country",
                    "roles":["legislatorLowerBody", "legislatorUpperBody"]}

                template_params["rep_data"] = get_rep_data(request_params)
                template_params["user_location"] = user.address

            template_params["username"] = user.name
            template_params["signout_link"] = users.create_logout_url("/")
            self.response.write(rep_template.render(template_params))
        else:
            self.redirect("/")
    def post(self):
        user = User.get_by_id(users.get_current_user().user_id())
        address = ""
        for key in addr_keys:
            field = self.request.get(key)
            if field:
                if key == "state":
                    address += field + " "
                elif key == "zip":
                    address += field
                else:
                    address += field + ", "
        user.address = address
        user.put()
        self.redirect("/representatives")

class ServiceHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        user = User.get_by_id(google_user.user_id()) if google_user else None
        if user:
            service_template = jinja_env.get_template("/templates/service.html")
            self.response.write(service_template.render({
                "username": user.name,
                "signout_link": users.create_logout_url("/")
            }))
        else:
            self.redirect("/")

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        google_user = users.get_current_user()
        user = User.get_by_id(google_user.user_id()) if google_user else None
        if user:
            events_template = jinja_env.get_template("/templates/events.html")
            self.response.write(events_template.render({
                "username": user.name,
                "signout_link": users.create_logout_url("/")
            }))
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/welcome', HomeHandler),
    ('/news', NewsHandler),
    ('/representatives', RepHandler),
    ('/service', ServiceHandler),
    ('/events', EventsHandler),


], debug=True)
