

def validate_username(text: str):
    prompt = ""
    status = False
    if len(text) == 0 or text.isspace():
        prompt = "Ім'я не може бути порожним рядком"
    elif not text.isidentifier():
        prompt = "Ім'я має починатись з літери..."
    else:
        status = True
    return prompt, status

def validate_password(text):
    prompt = ""
    status = False
    if len(text) < 8 or text.isspace():
        prompt = "Пароль не може бути меньше 8 символів"
    elif text.isalpha():
        prompt = "Пароль повинен мати також ще і цифри."
    else:
        status = True
    return prompt, status
