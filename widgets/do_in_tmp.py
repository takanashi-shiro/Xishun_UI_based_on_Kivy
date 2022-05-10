
def write_in_tmp(username):
    with open('./tmp/tmp','w') as f:
        f.write(username)
        f.close()

def read_tmp():
    with open('./tmp/tmp','r') as f:
        s = f.read()
        f.close()
    return s
