from django.http import HttpResponse
from .scraper import scrap_recipe
import os
# Create your views here.
def parse(request):
    if request.method == "POST":
        url = request.GET.get("url", None)
        if url is not None:
            temp = scrap_recipe(url)
            if type(temp) is not str:
                return HttpResponse("Error")
            file_data = None
            with open(temp, 'r') as f:
                file_data = f.read()
            os.remove(temp)
            return HttpResponse(file_data, content_type="text/markdown")

    return HttpResponse("Couldn't find it bro")
