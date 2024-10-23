#!/usr/bin/env python3
"""nginx logs statstics module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    t_logs = client.logs.nginx
    count_logs = t_logs.count_documents({})
    print(f"{count_logs} logs")
    methods = ["GET", "POST", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        logs = t_logs.count_documents({"method": method})
        print(f"\tmethod {method}: {logs}")
    st_logs = t_logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{st_logs} status check")
