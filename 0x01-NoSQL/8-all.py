#!/usr/bin/env python3
"""list doc module"""


def list_all(mongo_collection):
    """list doc in given collection passed
    as arg"""
    docs = mongo_collection.find()
    if not docs:
        return []
    return docs
