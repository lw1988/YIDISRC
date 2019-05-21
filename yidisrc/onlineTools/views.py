from django.shortcuts import render
import hashlib

# Create your views here.

def unicodeTransfer(request):

    if request.method == "GET":
        return render(request, "onlineTools/unicode.html")

    elif request.method == "POST":

        unicode_content = request.POST.get("unicode_content")

        transfer_content = unicode_content.encode("utf-8").decode("unicode_escape")

        return render(request, "onlineTools/unicode.html",
                      {"transfer_content": transfer_content})

def md5Transfer(request):
    if request.method == "GET":
        return render(request, "onlineTools/md5.html")

    elif request.method == "POST":
        md5_content = request.POST.get("md5_content")
        m = hashlib.md5()
        '''
        # Tips
            # 此处必须encode
            # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
            # 因为python3里默认的str是unicode
            # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
            b = str.encode(encoding='utf-8')
            m.update(b)
            str_md5 = m.hexdigest()
        '''

        b = md5_content.encode(encoding='utf-8')
        m.update(b)

        str_md5 = m.hexdigest()

        return render(request, "onlineTools/md5.html",
                      {"md5_content": str_md5})


