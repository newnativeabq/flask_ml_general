from flask import Flask, request, jsonify
from flask import current_app, g
from ml_module import ml_model
import os

from errors import InvalidUsage

###########
###Setup###
###########

# Initialize Predictor
predictor = ml_model.Predictor()

# Set database name
local_db_name = 'database_name.sqlite3'  # Change this or override with config.py file in instance/


#########################
###Application Factory###
#########################

# Create the application instance by calling create_app()
#     Example: app = create_app()

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # CHANGE THIS!!!!
        DATABASE=os.path.join(app.instance_path, local_db_name),
        LOCALDATABASE=os.path.join(os.getcwd(), local_db_name)  # Attempt to fix pathing issues
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    #  Register database functions.  Will allow db.close() to run on instance teardown.
    import db
    db.init_app(app)


    ############
    ###Routes###
    ############

    @app.route('/')
    def root():
        return "API Main.  Use */api/predict/"

    @app.route('/api/predict/', methods=['GET'])
    def predict():
        # Set Defaults

        # Parse request
        if request.method == 'GET':
            if not 'search' in request.args:
                raise InvalidUsage(message="Search query not provided")

        # Send search request to model
        raw_prediction = predictor.predict(request.args['search'])
        # Query database with those raw model output (if necessary)
        prediction_data = db.query_database(raw_prediction)

        return prediction_data


    # Register error handler
    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app


app = create_app()


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)