from flask import Flask
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# Swagger configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"  # Location of our swagger file
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Python Flask RESTful API"}
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

class HealthCheck(Resource):
    def get(self):
        """
        Get method for Healthy Check
        ---
        responses:
          200:
            description: Returns a Healthy Message
        """
        return {'Message': 'Healthy'}

api.add_resource(HealthCheck, '/healthcheck')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')