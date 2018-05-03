from flask import Flask
from redis import Redis, RedisError
import os
import socket
from  helloWorld import app

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
