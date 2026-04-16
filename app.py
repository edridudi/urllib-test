import urllib3
import requests
from flask import Flask

app = Flask(__name__)

http = urllib3.PoolManager()


@app.route("/")
def index():
    response = http.request("GET", "http://example.com")
    return response.data.decode("utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
