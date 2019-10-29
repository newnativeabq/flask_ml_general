# flask_ml_general

A deployable flask application tailored for production machine learning.  Contains drop-in model loading, logging pre-configured, and other useful features.  This is not meant to be a REST API and includes no data security or auth.  This is meant to be a lightweight deployable API to drop a model in and get connected to a front-end or dashboard quickly with regular, reliable, JSON responses.

## Notes

### Instance Folder

When committed, this repository is set to ignore the instance/ folder.  In that folder should be your config.py (if used) file with any sensitive data.  Do not commit config.py with any API keys or database URIs.  Also in the instance/ folder should be a logs folder.  If nothing, create the following in your local root directory: instance/logs/debug.log.  Otherwise, the application will throw an error that debug.log doesn't exist.

### Predefined Routes

The root route path is a landing page for API usage instructions.  Apparently this is a thing and should prbably be built out.

### Logs in the Instance Folder

You really need to manually create the instance folder to get logs in development.  By default, logs are saved to instance/logs/debug.log for safety reasons (don't accidentally want to push sensitive information).  Override the log save path in config.  Note that in heroku, those writes will not persist and you'll need to log to an external service (not currently supported) in production.

### Logging

Logging is enabled by default at the INFO level.  Logs are written to instance/logs/debug.log.  You can configure this or write to external source, console by modifying basic config.

You can change this to DEBUG by modifying the following line:

> logging.basicConfig(filename=app.config['LOGFILE'], level=logging.INFO) **logging.INFO to logging.DEBUG**

## TODO

### Generalize load_file

> Right now, load_file only handled pickled files.  For Keras h5 files, keras.models import load_model needs to be implemented.  For JSON (models can be saved in JSON format as well), the file can be returned as a path (example useage: to keras.models.model_from_json)

### Better Landing Page

> The landing page should have clear instructions as to how the client request should be formed and any subsequent routes they should be aware of.  A nice template would make this update go faster with the renderer already set.


### Add token auth from backend?

> It is likely that backend will be generating user tokens.  As an extension, it might be work considering a kerberos integration for unified authentication to the application server and how that might effect the 'general' architecture.  Though not intended to be implemented here, there may be changes to how things are stored, accessed, that need to be arranged for that level of security in the future. Just a thought.
