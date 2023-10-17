from flask import jsonify
from functools import wraps

from ..core.logger import Logger

def handle_exceptions(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            response = jsonify(func(*args, **kwargs))
        except Exception as e:
            message = "There was an error: " + str(e)
            Logger.log("ERROR", f"Error: {e}")
            response = jsonify(error=message)
            response.status_code = 500
        
        return response
    
    return wrapper
