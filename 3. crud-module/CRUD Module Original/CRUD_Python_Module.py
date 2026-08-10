from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        """ Database connection """
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create a method to return the next available record number for use in the create method

    def create(self, data):
        """ Insert new record into database """
        if data is not None:
            self.database.animals.insert_one(data) #insert document
            return True
        else:
            return False

    def read(self, query):
        """ Find record(s) in database """
        if query is not None:
            cursor = self.database.animals.find(query) #query database
            results = []
            for document in cursor:
                results.append(document) #load returned records into list
            return results
        else:
            return []

    def update(self, query, update):
        """ Update record(s) in database """
        if query is not None and update is not None:
            result = self.database.animals.update_many(query, update) #update records
            return result.modified_count
        else:
            return False

    def delete(self, query):
        """ Delete record(s) in database """
        if query is not None:
            result = self.database.animals.delete_many(query) #delete records
            return result.deleted_count
        else:
            return False