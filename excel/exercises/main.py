import xlwings as xw

from connection.Request import RequestClient


"""
        ___  ___      _       
        |  \/  |     (_)      
        | .  . | __ _ _ _ __  
        | |\/| |/ _` | | '_ \ 
        | |  | | (_| | | | | |
        \_|  |_/\__,_|_|_| |_|                  
"""


if __name__ == "__main__":
    xw.Book("tutorial.xlsm").set_mock_caller()
    xw.serve()


"""
         _   _____________   
        | | | |  _  \  ___|  
        | | | | | | | |_ ___ 
        | | | | | | |  _/ __|
        | |_| | |/ /| | \__ \
         \___/|___/ \_| |___/        
"""


@xw.func
def request_chat_history():
    client = RequestClient()
    # result = client.execute('ca/dialogue/command_history', {})
    # if 'response' in result:
    #     return result['response']
    return ""


@xw.func
def request_ask_question(question, workbook, worksheet, cell):
    print('--> QUESTION:', question, workbook, worksheet, cell)
    client = RequestClient()
    result = client.execute('ca/dialogue/command', {'command': question, 'workbook': workbook, 'worksheet': worksheet, 'cell': cell})
    if 'response' in result:
        return result['response']
    return "no response"


@xw.func
def request_new_user(username, email, password_1, password_2):
    client = RequestClient()
    result = client.execute('auth/register', {'username': username, 'email': email, 'password1': password_1, 'password2': password_2})
    print('--> NEW USER RESULT', result)
    if 'status' in result:
        if 'registration_error' in result:
            return result['registration_error']
        return result['status']
    return 'local error'


@xw.func
def request_login(username, password):
    client = RequestClient()
    result = client.execute('auth/login', {'username': username, 'password': password})
    print('--> LOGIN RESULT', result)
    if 'status' in result:
        return result['status']
    return 'local error'


@xw.func
def request_logout():
    client = RequestClient()
    result = client.execute('auth/logout', {})
    print('--> LOGOUT RESULT', result)
    if 'message' in result:
        return result['message']
    return 'local error'


@xw.func
def request_new_session():
    client = RequestClient()
    client.delete_session()
    return 'session removed'


@xw.func
def request_event(cell_row, cell_col, cell_value):
    print('--> SENDING EVENT:', cell_row, cell_col, cell_value)
    client = RequestClient()
    result = client.execute('ca/dialogue/event', {'row': cell_row, 'col': cell_col, 'value': cell_value})
    if 'response' in result:
        return result['response']
    return "no response"
