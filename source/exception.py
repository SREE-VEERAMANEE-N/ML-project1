import sys
import logging

def error_message(error, error_details):
    _, _, exc_info = error_details
    exc_tb = exc_info.tb_next
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in Python script name [{0}] at line number [{1}] with error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message

