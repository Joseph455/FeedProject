from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "FeedApp/index.html", {})


def post(request):
    return render(request, "FeedApp/post.html", {})


def reports(request):
    return render(request, "FeedApp/report.html", {})