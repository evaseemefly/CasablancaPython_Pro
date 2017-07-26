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
def test(s):
    # temp=''.join(c for in s.lower() if c in keep)
    temp=''.join(c for c in s.lower() if c in keep)
    return temp
def normalize_min(s):
    """标准化——简写形式
    """
    return ''.join(c for c in s.lower() if c in keep)
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
    num_lines=s.count('\n')
    #返回一个词频的字典
    d=make_freq_dict(s)
    #计算s包含多少个单词
    # all_words= d[w] for w in d   
    num_words=sum(d[w] for w in d)#此处没太看懂
    # 等价于
    # lst_temp=[]
    # for w in d
    #     if True:
    #         d[w]
    #         将d[w]加入到list_temp中
    #   return list_temp
    # 创建一个列表，其中的元素由出现次数和单词组成的元组
    lst=[(d[w],w) for w in d]
    # 按照出现次数从高到低排序
    lst.sort()
    lst.reverse()
    print("文件共有'%s':"%fname)
    print(" %s characters"%num_chars)
    print(" %s lines"%num_lines)
    print(" %s words"%num_words)
    print("\n十个出现频率最高的词组为:")
    i=1
    for count,word in lst[:10]:
        print('%2s.%4s %s'%(i,count,word))
        i+=1

def main():
    print_file_stats('D:\\02编程\\2016年\\01协同开发\\Python\\CasablancaPython_Pro\\demo-文本统计\\readdemo.txt')
if __name__=='__main__':
    main()