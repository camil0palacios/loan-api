from ..libs.core.logger import Logger

# Utils
from ..libs.utils.constants import LoanStatus, BASE_AMOUNT

def request_loan(data):
    
    amount = data["amount"]

    Logger.log("INFO", f"Check amount: {amount}")

    loan_status = LoanStatus.APPROVED
    if amount < BASE_AMOUNT:
        loan_status = LoanStatus.DECLINED

    elif amount == BASE_AMOUNT:
        loan_status = LoanStatus.UNDECIDED

    response = {
        "status": loan_status
    }
    
    Logger.log("INFO", f"Response {response}")

    return response
