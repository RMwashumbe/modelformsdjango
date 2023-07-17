from django.shortcuts import render
from modelformsRobert.form import Name


def Home(request):
    name = Name
    return render(request, 'index.html', {'form': name})
