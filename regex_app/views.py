from django.shortcuts import render
import re

def index(request):
    return render(request, 'regex_app/index.html')

def confirm(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        age = request.POST.get("age", "")
        zip_code = request.POST.get("zip_code", "")
        cell_phone = request.POST.get("cell_phone", "")

        name = name.replace(" ", "")

        if not re.match(r"^\d+$", age):
            return render(request, "regex_app/confirm.html")

        if not re.match(r"^\d{3}-?\d{4}$", zip_code):
            return render(request, "regex_app/confirm.html")

        if not re.match(r"^\d{3}-?\d{4}-?\d{4}$", cell_phone):
             return render(request, "regex_app/confirm.html")


    return render(request, "regex_app/confirm.html")

