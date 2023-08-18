from flask import Flask
import requests


r = requests.put('http://169.254.169.254/latest/api/token', headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'})
token = r.content

PORT = 8080

app = Flask(__name__)

@app.route("/")
def root():
  return token

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
