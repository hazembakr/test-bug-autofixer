def get_user_name(user):
    return user["name"]

def process_user(user):
    if user is None:
        return None
    name = get_user_name(user)
    return name.upper()
