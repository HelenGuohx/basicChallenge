"""
encode AES
https://www.cnblogs.com/xiao-apple36/p/8744408.html
"""
# pip install pycryptodome
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

def solution():
    #秘钥,此处需要将字符串转为字节
    key = 'abcdefgh'
    #加密内容需要长达16位字符，所以进行空格拼接
    def pad(text):
        while len(text) % 16 != 0:
            text += ' '
        return text
    #加密秘钥需要长达16位字符，所以进行空格拼接
    def pad_key(key):
        while len(key) % 16 != 0:
            key += ' '
        return key
    #进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
    aes = AES.new(pad_key(key).encode(), AES.MODE_ECB)
    #加密内容,此处需要将字符串转为字节
    text = 'hello'
    #进行内容拼接16位字符后传入加密类中，结果为字节类型
    encrypted_text = aes.encrypt(pad(text).encode())
    print(encrypted_text)
    encrypted_text_hex = b2a_hex(encrypted_text)
    print(encrypted_text_hex)


    # #此处是为了验证是否能将字节转为字符串后，进行解密成功
    # #实际上a 就是 encrypted_text ，也就是加密后的内容
    # #用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
    de = str(aes.decrypt(a2b_hex(encrypted_text_hex)), encoding='utf-8',errors="ignore")
    # #获取str从0开始到文本内容的字符串长度。
    print(de[:len(text)])


#coding: utf8
class Aescrypt():
    def __init__(self, key):
        self.key = self.pad(key).encode()
        self.mode = AES.MODE_ECB

    def pad(self,text):
        try:
            return text + (16 - len(text))*"0"
        except Exception as e:
            print("pad error",str(e))

    def encrypt(self,text):

        # 加密内容需要长达16位字符，所以进行空格拼接
        aes = AES.new(self.key, self.mode)
        # 进行内容拼接16位字符后传入加密类中，结果为字节类型
        encrypted_text = aes.encrypt(self.pad(text).encode())
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        print(b2a_hex(encrypted_text))
        return b2a_hex(encrypted_text)

    def decrypt(self, text):
        aes = AES.new(self.key, self.mode)
        plain_text = aes.decrypt(a2b_hex(text)).decode()
        # #获取str从0开始到文本内容的字符串长度。
        print(plain_text.strip())
        return plain_text.strip()


#初始化秘钥
acrypt = Aescrypt("encrypt")
e = acrypt.encrypt("tedhelen")
d = acrypt.decrypt('a897ea66176ffd2016684221534ec553')
