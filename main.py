import logging
from flask import Flask
from common_package.const.local import  config
from webapp.view import attach_views

app = Flask(__name__)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
attach_views(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT, debug =   True)
