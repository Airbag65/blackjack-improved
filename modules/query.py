
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

update = {
    "update_username": "update users set username = '{prompt1}' where email is '{prompt2}';",
    "update_email": "update users set email = '{prompt1}' where username is '{prompt2}';",
    "update_password": "update users set password = '{prompt1}' where username is '{prompt2}';",
    "update_balance": "update users set balance = {prompt1} where username is '{prompt2}';"
}