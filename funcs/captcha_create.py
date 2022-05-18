import random


def Captcha_Create():
    content = ''
    for i in range(1, 5):
        random_str = random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
        content += random_str
    return content
