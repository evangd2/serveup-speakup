from google.appengine.ext import ndb

class ApiKey(ndb.Model):
    name = ndb.StringProperty(required=True)
    value =  ndb.StringProperty(required=True)

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    location = ndb.StringProperty()
    representatives = ndb.KeyProperty(repeated=True)
