import xlwings as xw


def connect():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


@xw.func
def connect_to_daphne(username, password):
    print('--> USERNAME:', username)
    print('--> PASSWORD:', password)

    # --> 1. Connect to daphne here

    # --> 2. Return login results to VBA
    return_status = ['Success', 'Invalid Credentials']
    return return_status[1]



@xw.func
def hello(name):
    return f"Hello {name}!"


@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 8 * (x + y)


if __name__ == "__main__":
    xw.Book("tutorial.xlsm").set_mock_caller()