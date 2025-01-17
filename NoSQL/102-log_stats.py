#!/usr/bin/env python3
"""
Log stats in Python
"""
from pymongo import MongoClient


def log_stats():
    """
    Test
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    total_logs = collection.count_documents({})
    methods = collection.aggregate([
        {
            '$group': {
                '_id': '$method',
                'count': {'$sum': 1}
            }
        }
    ])
    status_check = collection.count_documents({'status': '200'})
    ip_counts = collection.aggregate([
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1}
        },
        {
            '$limit': 10
        }
    ])
    print(f"{total_logs} logs")
    for method in methods:
        print(f"Method {method['_id']}: {method['count']}")
    print(f"{status_check} status check")

    print("IPs:")
    for ip in ip_counts:
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
