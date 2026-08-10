"""
Module Name: Module.py
Description: This program is a CRUD module that accesses a MongoDB
database of US national parks that I created.
Author: Sebastian Stohn
Date: 2026-08-03
"""

from pymongo import MongoClient

class NationalParkDatabase(object):
    """ CRUD operations for parks collection in MongoDB """
    
    def __init__(self, new_user, new_pass):
        """ Database connection """
        username = new_user
        password = new_pass
        host = 'localhost'
        port = 27017
        db = 'national_parks'
        col = 'parks'
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=%s'
                                  % (username, password, host, port, db))
        self.database = self.client['%s' % db]
        self.collection = self.database['%s' % col]

    def create(self, data):
        """ Insert new record into database """
        if data is not None:
            self.database.parks.insert_one(data) # Insert document
            return True
        else:
            return False

    def read(self, query):
        """ Find record(s) in database """
        if query is not None:
            cursor = self.database.parks.find(query) # Query database
            results = []
            for document in cursor:
                results.append(document) # Load returned records into list
            return results
        else:
            return []

    def update(self, query, update):
        """ Update record(s) in database """
        if query is not None and update is not None:
            result = self.database.parks.update_many(query, update) # Update records
            return result.modified_count
        else:
            return False

    def delete(self, query):
        """ Delete record(s) in database """
        if query is not None:
            result = self.database.parks.delete_many(query) # Delete records
            return result.deleted_count
        else:
            return False