from flask import Flask
import random
import logging
import sys

app = Flask(__name__)

# Setup logging to stdout for Fluent Bit
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s')
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Hello from Flask on Kubernetes!"

@app.route("/healthz")
def healthz():
    app.logger.info("Health check passed")
    return "OK", 200

@app.route("/failcheck")
def failcheck():
    if random.randint(1, 10) > 2:
        app.logger.info("Failcheck route responded OK")
        return "I'm OK", 200
    else:
        app.logger.warning("Failcheck route responded with failure")
        return "Failing", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
