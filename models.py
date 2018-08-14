from google.appengine.ext import ndb

class ApiKey(ndb.Model):
    name = ndb.StringProperty(required=True)
    value =  ndb.StringProperty(required=True)

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    address = ndb.StringProperty()
    representatives = ndb.KeyProperty(repeated=True)

'''class Address(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty()
    line2 = ndb.StringProperty()
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    zip = ndb.StringProperty(required=True)

class Representative(ndb.Model):
    name = ndb.StringProperty(required=True)
    party = ndb.StringProperty()
    address = ndb.KeyProperty()'''
