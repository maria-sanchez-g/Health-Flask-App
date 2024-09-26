from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Simple health check API endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'OK'}), 200

# Swagger UI configuration
SWAGGER_URL = '/docs'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # Path to the Swagger file

# Create Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)

# Register Swagger UI blueprint in Flask app
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)