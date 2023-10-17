def get_right_login_data():
    case = {'mail': 'standard_user', 'password': 'secret_sauce'}
    return case


def get_wrong_login_data():
    case = {'mail': '12standard_user12', 'password': '12secret_sauce12'}
    return case
