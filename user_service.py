def get_user_name(user):
    return user["name"]

def process_user(user):
    name = get_user_name(user)
    return name.upper()
