from flask import Flask
import requests


r = requests.put('http://169.254.169.254/latest/api/token', headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'})
token = r.content

PORT = 8080

app = Flask(__name__)

@app.route("/")
def root():
  return token

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
