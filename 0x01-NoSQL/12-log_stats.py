#!/usr/bin/env python3
"""nginx logs statstics module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    t_logs = client.logs.nginx
    count_logs = t_logs.count_documents({})
    print(f"{count_logs} logs")
    print("Methods")
    get_logs = t_logs.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get_logs}")
    post_logs = t_logs.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post_logs}")
    put_logs = t_logs.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put_logs}")
    patch_logs = t_logs.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch_logs}")
    delete_logs = t_logs.count_documents({"method": "DELETE"})
    print(f"\tmethod DELTE: {delete_logs}")
    st_logs = t_logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{st_logs} status check")
