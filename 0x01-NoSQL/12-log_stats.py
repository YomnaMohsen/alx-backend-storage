#!/usr/bin/env python3
"""nginx logs statstics module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    t_logs= client.logs.nginx
    count_logs = t_logs.count_documents({})
    get_logs = t_logs.count_documents({"method": "GET"})
    post_logs = t_logs.count_documents({"method": "POST"})
    put_logs = t_logs.count_documents({"method": "PUT"})
    patch_logs = t_logs.count_documents({"method": "PATCH"})
    delete_logs = t_logs.count_documents({"method": "DELETE"})
    st_logs = t_logs.count_documents({"method": "GET", "path": "/status"})
    print("{} logs\n Methods:\n \t method GET: {}\n \t method POST: {}\n \t method"
           "PUT: {}\n \t method PATCH: {}\n \t method DELETE: {}"
          "\n {} status check".format(count_logs, get_logs, post_logs, put_logs, patch_logs, 
                                      delete_logs, st_logs))
