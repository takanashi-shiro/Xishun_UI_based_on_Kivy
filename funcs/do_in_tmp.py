def write_in_tmp(username, pwd):
    with open('./tmp/tmp', 'w') as f:
        f.write(username + ' ' + pwd)
        f.close()


def read_tmp():
    with open('./tmp/tmp', 'r') as f:
        s = f.read()
        f.close()
    return s

def clean_tmp():
    with open('./tmp/tmp', 'w') as f:
        f.write('')
        f.close()