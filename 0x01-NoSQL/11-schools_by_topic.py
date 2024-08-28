#!/usr/bin/env python3
"""search by topic module"""

def schools_by_topic(mongo_collection, topic):
    """args:
        collection to search in,
        topic name to search by,
        return list of topics
        """
    results = mongo_collection.find({"topics":topic})
    return list(results)    
    