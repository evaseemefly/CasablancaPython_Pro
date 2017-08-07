import hashlib
import hmac

m=hashlib.md5()
m.update(b"hello")
m.update(b"It's me")
# digest为二进制数据字符串值
print(m.digest())
# hexdigest为十六进制数据字符串值
print(m.hexdigest())

h=hmac.new(b'1234',"宝塔镇河妖".encode(encoding="utf-8"))
print("使用编码:%s，输出结果为:%s"%("hmac",h.hexdigest()))