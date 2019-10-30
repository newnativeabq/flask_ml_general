# flask_ml_general

A deployable flask application tailored for production machine learning.  Contains drop-in model loading, logging pre-configured, and other useful features.  This is not meant to be a REST API and includes no data security or auth.  This is meant to be a lightweight deployable API to drop a model in and get connected to a front-end or dashboard quickly with regular, reliable, JSON responses.

## Usage

### Making Requests

*How to make requests*

> Params, Returns

### Updates

*Version Information*

> 2019-10-30 - 1.0 Release

## Notes

### Instance Folder

When committed, this repository is set to ignore the instance/ folder.  In that folder should be your config.py (if used) file with any sensitive data.  Do not commit config.py with any API keys or database URIs.  Also in the instance/ folder should be a logs folder.  If nothing, create the following in your local root directory: instance/logs/debug.log.  Otherwise, the application will throw an error that debug.log doesn't exist.

### Predefined Routes

The root route path is a landing page for API usage instructions.  Apparently this is a thing and should prbably be built out.

### Logging

Logging is enabled by default at the INFO level.  Logs are written to instance/logs/debug.log.  You can configure this or write to external source, console by modifying basic config.

You can change this to DEBUG by modifying the following line:

> logging.basicConfig(filename=app.config['LOGFILE'], level=logging.INFO) **logging.INFO to logging.DEBUG**
