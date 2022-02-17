import base64
from Crypto.Cipher import AES



def AES_Encrypt(key, data):
    vi = '7B579877ECB01812'
    pad = lambda s: s + (16 - len(s) % 16) * chr(0)
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    return enctext

key = '7BAB2440978E8950'
data = open('/Users/song.yll/Documents/字典/passwd3.txt','r')
line = data.readlines()
for lines in line:
    AES_Encrypt(key, lines)
    enctext = AES_Encrypt(key, lines)
    #print(enctext)
    AES1 = open('/Users/song.yll/Documents/字典/fuzzDicts-master/userNameDict/AES.txt', 'a')
    AES1.write(enctext+'\n')
    AES1.close()




