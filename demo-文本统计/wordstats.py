
# 包含所有要保留的字符的集合
keep={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','','-',"'"}

def normalize(s):
    """标准化——获取最小化的且满足a-z的形式的字符
    """
    result=''
    for c in s.lower():
        if c in keep:
            result+=c
        return result
def normalize_min(s):
    """标准化——简写形式
    """
    return ''.join(c for in s.lower() if c in keep)

def make_freq_dict(s):
    """返回一个词频的字典dict
    """
    #获取标准化后的字符串
    s=normalize_min(s)
    #对字符串进行切片
    words=s.split()
    d={}
    for w in words:
        if w in d:#若w 出现过，则将其出现次数加1
            d[w]+=1
        else:   #若w第一次出现，将其次数设置为1
            d[w]=1
    return d

def print_file_stats(fname):
    s=open(fname,'r').read()

    num_chars=len(s)
    num_lines=s.count('\n'))
    #返回一个词频的字典
    d=make_freq_dict(s)
    #计算s包含多少个单词
    num_words=sum(d[w] for w in d)#此处没太看懂
    # 等价于
    # lst_temp=[]
    # for w in d
    #     if True:
    #         d[w]
    #         将d[w]加入到list_temp中
    #   return list_temp
    lst=[(d[w],w) for w in d]
    lst.sort()
    lst.reverse()