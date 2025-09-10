import sys
import logging

def error_message_detail(error: Exception,error_details:sys)->str:
    """
    EXtracts detailed error information including file name ,line number and the error  message.

    :param error :The exception that occured.
    : param error_detail :The sys module to access tracjback details.
    : return :A formatted error message string.
    """

    #Exxtract trackbook details(Exceotion information)
    _,_,exc_tb=error_details.exc_info()

    #Get the file name where the exception occurred
    file_name=exc_tb.tb_frame.f_code.co_filename

    #Create a formatted error message string with file name ,line number and the actuak errir 
    line_number=exc_tb.tb_lineno
    error_message =f"Error occured in oython script: [{file_name}] at line number [{line_number}]: {str(error)}"

    #log the error for better tracking 
    logging.error(error_message)

    return error_message

class MyException(Exception): #coming from the above 
    """
    Custom exception class for handling errors in the US visa application.
    """
    def __init__(self,error_messages:str,error_details:sys):
        '''
        Initializes the USvisa Exception with a details error messsage.
        :parma error message :A string descrbing the error 
        : param error details : The sus modules to acces trackeback details
        
        '''
        #Call the base class constructor wiht the error message
        super().__init__(error_messages)

        #Format the deatiled error_message using the error_message_details function
        self.error_message =error_message_detail(error_messages,error_details)

    def __str__(self) -> str:
        """
        Return the strinf representation of the error message.
        """
        return self.error_message