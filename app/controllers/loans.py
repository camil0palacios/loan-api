from flask import request
from app.main import app
from ..libs.core.handle_exceptions import handle_exceptions

# Services
from ..services import loans as LoanService

SERVICE_NAME = "loan"

@app.route(f"/{SERVICE_NAME}", methods = ["POST"])
@handle_exceptions
def request_loan():
    body = request.get_json()
    return LoanService.request_loan(body)
