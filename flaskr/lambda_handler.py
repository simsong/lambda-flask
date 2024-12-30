"""
Handle the AWS Lambda function

The AWS runtime looks for a function lambda_handler inside a file called
lambda_handler.py (this file)
"""

import os
import logging

from apig_wsgi import make_lambda_handler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

def dump_files(path="."):
    """For debugging."""
    for (root, dirs, files) in os.walk(path): # pylint: disable=unused-variable
        for fn in files:
            logging.error("%s/%s",root,fn)

try:
    dump_files(os.environ['DEBUG_DUMP_FILES_ROOT'])
except KeyError:
    pass

from flaskr.flaskr import app
lambda_handler = make_lambda_handler(app)
