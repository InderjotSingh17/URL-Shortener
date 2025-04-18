import random
import string
from django.shortcuts import render, redirect
shortened_urls = {}
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        short_code = generate_short_code()
        shortened_urls[short_code] = original_url

        return render(request, "result.html", {"short_code": short_code})
    
    return render(request, "index.html")

def redirect_url(request, short_code):
    original_url = shortened_urls.get(short_code)

    if original_url:
        return redirect(original_url)
    else:
        return render(request, "not_found.html", {"short_code": short_code})
