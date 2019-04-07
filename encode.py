import base64

def pic2base64(fname):
    f=open(fname,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    print(ls_f)
    return ls_f

def base642pic(bs,fname):
# bs='iVBORw0KGgoAAAANSUhEUg....' # 太长了省略
    imgdata=base64.b64decode(bs)
    file=open(fname,'wb')
    file.write(imgdata)
    file.close()

pic2base64('./photo/个人网站组织图.png')