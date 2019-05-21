from django.shortcuts import render

# Create your views here.

def unicodeTransfer(request):

    if request.method == "GET":
        return render(request, "onlineTools/unicode.html")

    elif request.method == "POST":

        unicode_content = request.POST.get("unicode_content")

        transfer_content = unicode_content.encode("utf-8").decode("unicode_escape")

        return render(request, "onlineTools/unicode.html",
                      {"transfer_content": transfer_content})

