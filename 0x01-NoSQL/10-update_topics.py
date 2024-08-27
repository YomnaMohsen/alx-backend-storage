#!/usr/bin/env python3
"""update module"""


def update_topics(mongo_collection, name, topics):
    """update document by name"""
    updat_top = {"$set": {"topics": topics}}
    mongo_collection.update_many({"name": name}, updat_top)
