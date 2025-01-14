#!/usr/bin/env python3
""" List all documents in Python """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
