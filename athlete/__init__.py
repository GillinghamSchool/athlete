from flask import Flask

app = Flask(__name__,
            static_url_path=""
            )

app.config["SECRET_KEY"] = "totally_secret"

from athlete.app_routes import *
from athlete.asset_manager import *
from athlete.error_handlers import *
