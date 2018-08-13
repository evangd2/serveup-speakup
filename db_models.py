from google.appengine.ext import ndb
class User(ndb.Model):
    name = ndb.StringProperty()
    location = ndb.StringProperty()
    interests = ndb.StringProperty(repeated=True)
    representatives = ndb.KeyProperty(repeated=True)
