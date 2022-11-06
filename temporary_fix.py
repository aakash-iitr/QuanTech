import random
sample_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&1234567890'


def generate(n):
    st = ''
    for i in range(n):
        st += random.choice(sample_str)
    
    return st
