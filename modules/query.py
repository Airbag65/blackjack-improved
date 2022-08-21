
fetch = {
    "get_username": "select * from users where username is '{prompt}';",
    "get_email": "select * from users where email is '{prompt}';"
}

add = {
    "new_user": """insert into users(
        username,
        email,
        firstName,
        lastName,
        password)
        values('{username}',
        '{email}',
        '{firstname}',
        '{lastname}',
        '{password}'
        );    
    """
}