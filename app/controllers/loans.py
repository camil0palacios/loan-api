from app.main import app
from flask import request, jsonify

# Services
from ..services import loans as LoanService

SERVICE_NAME = "loan"

@app.route(f"/{SERVICE_NAME}", methods = ["POST"])
def request_loan():
    body = request.get_json()
    return jsonify(LoanService.request_loan(body))
