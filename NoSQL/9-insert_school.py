#!/usr/bin/env python3
"""Insert a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    inserted_document = mongo_collection.insert_one(kwargs)
    return inserted_document.inserted_id
