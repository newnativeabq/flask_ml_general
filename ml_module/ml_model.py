"""
Machine Learning Model
    This module initializes a given estimator and/or vectorizer and exposes an sklearn-like
    interface to the application.

User must implement the following:

Vectorizer
----------
self.transform

    params
    ------
    raw_input: str-like

    returns
    -------
    vectorized input
    **Note that the predictor instance will vectorized input each pass.  This can be disabled by commenting
        out 'self.vectorized_input = user_input' in method data_available.


Estimator
---------
self.transform

    params
    ------
    raw_input: str-like

    returns
    -------
    vectorized_input: ndarray
    **Invoke vectorizer.transform and store result.  Try to keep vectorizer stateless or states separate.
        If you want to store multiple vectorized inputs, enable logging within the vectorizer.


self.predict
    params
    ------
    user_input: str_like or ndarray
    **Predictor class is input aware for testing purposes.  If numpy.ndarray is passed, will predict. Else,
        will pass through self.vectorizer first.

    returns
    -------
    estimator prediction.
    **Invoke model.predict.  Results not stored, but output response is cached.
        If you want to store multiple model predictions, enable logging within the model.
"""

# Path and File Libraries
import os
import pickle

# Data Transformation Libraries
import pandas as pd
import numpy as np

# Logging
import logging

# Initialize parameters and dependencies from __init__.py
from ml_module import params


###################
##BUILD PREDICTOR##
###################
class Predictor():
    """
    Predictor is comprised of a vectorizer and an estimator.
    """
    def __init__(self, model=None, vectorizer=None):
        self.estimator = Model()
        self.vectorizer = Vectorizer()
        self.logger = logging.getLogger(__name__+'.predictor')
        self.logger.info('Created instance of Predictor(model={}, vectorizer={})'.format(model, vectorizer))

    def transform(self, raw_input, verbose=False):
        self.raw_input = raw_input
        vinput = self.vectorizer.transform(raw_input)
        self.vectorized_input = vinput  # Store vinput for repeat/future predictions
        if verbose:
            print(vinput)

        self.logger.info('Ran transform.  Raw_Input: {} \n Vectorized_Input: {}'.format(raw_input, vinput))
        return vinput

    def predict(self, user_input=None, **kwargs):
        """
        Get model recommendations for given input.

        Parameters
        ----------
        user_input: str or ndarray
            string object (invokes transform) or ndarray (tries directly predicting)
        """
        if self.data_available(user_input):
            if user_input:
                prediction = None
                raise NotImplementedError
            else:
                prediction = None
                raise NotImplementedError
        else:
            prediction = None
            raise Error

        self.logger.info('Predictor.predict executed. user_input:{} \n prediction:{}'.format(user_input, prediction))


    def data_available(self, user_input):
        # Check if data provided or data stored.  If raw_input detected, run transform and return true.
        if user_input is None and self.vectorized_input is None:
            raise NoDataProvided
        else:
            if self.detect_raw_data(user_input):
                try:
                    self.transform(user_input, verbose=False)
                except:
                    print('Could not transform input')
                    return False
            elif user_input:
                self.vectorized_input = user_input
            return True

    def detect_raw_data(self, user_input):
        if type(user_input) == str:
            return True


class Model():
    def __init__(self):
        self.estimator = load_file('estimator')
        self.logger = logging.getLogger(__name__+'.Model')
        self.logger.info('Model instance created with given estimator')

    def predict(self, input_string):
        raise NotImplementedError


class Vectorizer():
    def __init__(self):
        self.vectorizer = load_file('vectorizer')
        self.logger = logging.getLogger(__name__+'.Vectorizer')
        self.logger.info('Vectorizer instance created with given estimator')

    def transform(self, input_string):
        raise NotImplementedError


####################
###Error Handling###
####################
class Error(Exception):
    """Base class for Custom Errors"""
    pass


class NoDataProvided(Error):
    """No Data Provided"""
    pass

######################
###Helper Functions###
######################
def get_abs_path(filename, **kwargs):
    if os.path.isfile(os.path.abspath(filename)):
        return os.path.abspath(filename)
    else:
        # Adjust for directory.  Can replace the '' with necessary path for
        #   system/deployment specifics.
        return os.path.join(
            os.getcwd(), '' + filename,
        )


def load_file(file_key, file_type=None):
    # Load pickle file.
    logger = logging.getLogger(__name__+'.load_file')
    logger.info('Attempting to load file with key: {}'.format(file_key))
    try:
        with open(get_abs_path(params[file_key]), 'rb') as f:
            opened = pickle.load(f)
        return opened
    except KeyError:
        print('Could not load {}.  Parameter not defined'.format(file_key))
        logger.error('Could not load {}.  Parameter not defined'.format(file_key))
        return None