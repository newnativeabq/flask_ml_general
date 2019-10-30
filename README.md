# flask_ml_general

A deployable flask application tailored for production machine learning.  Contains drop-in model loading, logging pre-configured, and other useful features.  This is not meant to be a REST API and includes no data security or auth.  This is meant to be a lightweight deployable API to drop a model in and get connected to a front-end or dashboard quickly with regular, reliable, JSON responses.

**Features** include:

* Databaes connection manager

* Machine Learning Model loader and factory methods

* Caching

* CORS headers

* Root landing page (rendering this README.md)

## Usage

### Making Requests

*How to make requests*

> Params, Returns

### Updates

*Version Information*

> 2019-10-30 - 1.0 Release

## Notes

### Instance Folder

When committed, this repository is set to ignore the instance/ folder via .gitignore.  In development, Flask app can read from the location, but take care to not commit config.py with any API keys or database URIs.  To get logs, create the instance/logs/debug.log file.  Otherwise, the application will throw an error that debug.log doesn't exist.  See 'logging' for more details.

### Predefined Routes

The root route path is a rendered version of the README.md file unless otherwise specified.  See app.py or the Usage section above for information on accessing functioning endpoints.

### Logging

Logging is enabled by default at the INFO level.  Logs are written to instance/logs/debug.log.  You can configure this or write to external source, console by modifying basic config.

You can change this to DEBUG by modifying the following line:

> logging.basicConfig(filename=app.config['LOGFILE'], level=logging.INFO) **logging.INFO to logging.DEBUG**

> Change default save location by modifying the filename attribute in line referenced above.  **filename=<insert_filename_here>**

#### Special Thanks

It can be hard to get eyes on a project to guide it's feature development.  I want to give special thanks to the data scientists who took a minute to walk through pain points and features they'd like to see.  Got most of it in.

* Harsh Desai
* John Morrison
* Han Lee
