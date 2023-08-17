from flask import Flask
import subprocess
import os

PORT = 8080

cmd = "TOKEN=`curl -X PUT \"http://169.254.169.254/latest/api/token\" -H \"X-aws-ec2-metadata-token-ttl-seconds: 21600\"` && curl -H \"X-aws-ec2-metadata-token: $TOKEN\" -v http://169.254.169.254/latest/meta-data/"

os.system(cmd);
try:
    message = os.environ['$TOKEN']
except Exception as e:
    message = e;

app = Flask(__name__)

@app.route("/")
def root():
  result = message.encode("utf-8")
  return result


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)



