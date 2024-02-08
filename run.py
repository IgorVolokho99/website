from flask import Flask

from app.main.views import main_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return "Not found"


@app.errorhandler(500)
def internal_error(error):
    return "Server error", 500


if __name__ == '__main__':
    app.run(debug=True)
