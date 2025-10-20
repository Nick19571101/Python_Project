from communicate import get_username, get_password
data_base = []

def create_user():
    username = get_username()
    password = get_password()
    user = username, password
    data_base.append(user)

if __name__ == "__main__":
    test_data_base = []
    data_base = test_data_base
    create_user()
    print(data_base)
# else:
#      create_user()
# import sys
# print(sys.modules.keys())
