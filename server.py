from snpapi import app
from werkzeug.contrib.fixers import ProxyFix

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(environ["PORT"]))