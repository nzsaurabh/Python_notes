# error handling within a Python function
# all the code for the function goes within try block
# messages in case of error go into except block
try:
    python_object[row][column] = new_value
# message for known error e.g. index out of range
except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1 or 2."
              " Error type: ", e)
# message for unkown error
except Exception as e:
        print("Something went very wrong."
              " Error type: ", e)
