#!/usr/bin/env python3
"""nginx logs statstics module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    tlogs = client.logs.nginx
    countlogs = tlogs.count_documents({})
    print(f"{countlogs} logs")
    methods = ["GET", "POST", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        logs = tlogs.count_documents({"method": method})
        print(f"\tmethod {method}: {logs}")
    stlogs = tlogs.count_documents({"method": "GET", "path": "/status"})
    print(f"{stlogs} status check")
