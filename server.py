from snpapi import app
from werkzeug.contrib.fixers import ProxyFix

if __name__ == "__main__":
  app.run(port=process.env.PORT)