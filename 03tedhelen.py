"""
trans
"""
import string
def translate_chr(str):
    intab = ''.join([chr(x) for x in range(ord('a'), ord('z') + 1)])
    outtab = ''.join([chr(x) for x in range(ord('c'), ord('z') + 1)] + ['a','b'])
    trantab = str.maketrans(intab, outtab)
    return str.translate(trantab)

def translate_string(s):
    table = s.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    return s.translate(table)


def re_translate_str(str):
    table = str.maketrans(string.ascii_lowercase[2:] + string.ascii_lowercase[:2],string.ascii_lowercase)
    return str.translate(table)
answer = "to solve the riddle you have to answer the question which city did we meet"
print(translate_string(answer))

tt = 'vq uqnxg vjg tkffng aqw jcxg vq cpuygt vjg swguvkqp yjkej ekva fkf yg oggv'
print(re_translate_str(tt))
