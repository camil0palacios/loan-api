from flask import jsonify
from functools import wraps

def handle_exceptions(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            response = jsonify(func(*args, **kwargs))
        except Exception as e:
            message = "There was an error: " + str(e)
            response = jsonify(error=message)
            response.status_code = 500
        
        return response
    
    return wrapper
