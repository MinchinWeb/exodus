from django.shortcuts import render, HttpResponse

def index(request):
    # replace with links to the indices
    return HttpResponse(
        "Welcome! You're at the <em>exodus</em> homepage. You might "
        "want to replace this."
    )
