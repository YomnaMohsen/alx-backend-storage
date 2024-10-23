#!/usr/bin/env python3
"""nginx logs statstics module"""
from pymongo import MongoClient


if __name__ == "__main__":
    """provides some statstics about nginx logs"""
    
    client = MongoClient()
    databs = client.logs
    tlogs = databs.nginx
    logs = tlogs.count_documents({})
    print(f"{logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        logs = tlogs.count_documents({"method": method})
        print(f"\tmethod {method}: {logs}")
    stlogs = tlogs.count_documents({"method": "GET", "path": "/status"})
    print(f"{stlogs} status check")
