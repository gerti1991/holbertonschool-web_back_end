#!/usr/bin/env python3
""" List all documents in Python """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ updates a document based on name """
    if mongo_collection is None:
        return None
    return mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
