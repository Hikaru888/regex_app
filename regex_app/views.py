import re
from django.shortcuts import render


def index(request):
    return render(request, "regex_app/index.html")


def confirm(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        age = request.POST.get("age", "")
        zip_code = request.POST.get("zip_code", "")
        cell_phone = request.POST.get("cell_phone", "")

        name = name.replace(" ", "")

        if re.match("^\d{1,3}$", age):
            print("マッチしました！")
        else:
            print("マッチしませんでした！")
            return render(request, "regex_app/index.html", {"age":""})

        if re.match("^\d{7}(-\d{7})?$", zip_code):
            print("マッチしました！")
        else:
            print("マッチしませんでした！")
            return render(request, "regex_app/index.html", {"zip_code": ""})

        if re.match("^\d{11}(-\d{11})?$", cell_phone):
            print("マッチしました！")
        else:
            print("マッチしませんでした！")
            return render(request, "regex_app/index.html", {"cell_phone": ""})

        form_data = {
            "name": name,
            "age": age,
            "zip_code": zip_code,
            "cell_phone": cell_phone,
        }

        return render(request, "regex_app/confirm.html", {"form_data": form_data})

    return render(request, "regex_app/confirm.html")
