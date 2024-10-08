#!/usr/bin/env python3
"""insert module"""


def insert_school(mongo_collection, **kwargs):
    """insert doc in given collection and
    return id"""

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
