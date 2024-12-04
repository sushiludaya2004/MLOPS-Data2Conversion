import sys

def error_message_details(error, error_detail: sys):
    # Capture the exception information
    _, _, exc_tb = sys.exc_info()  # Using sys.exc_info() instead of error_detail.exc_info()
    
    # Get the filename and line number from the traceback
    filename = exc_tb.tb_frame.f_code.co_filename
    linenumber = exc_tb.tb_lineno
    
    # Format the error message
    error_message = f"Error occurred in python script name [{filename}] line number [{linenumber}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the base class constructor
        super().__init__(error_message)
        # Format and store the detailed error message
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        # Return the formatted error message
        return self.error_message