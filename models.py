from google.appengine.ext import ndb

class ApiKey(ndb.Model):
    name = ndb.StringProperty(required=True)
    value =  ndb.StringProperty(required=True)
