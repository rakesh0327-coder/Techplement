import random
from django.http import JsonResponse
from django.shortcuts import render
from .models import Quote 

def home(request):
    return render(request, 'quotes/home.html')

def random_quote(request):
    """Return a random quote as JSON"""
    quotes = Quote.objects.all()
    if quotes.exists():
        quote = random.choice(quotes)
        return JsonResponse({"text": quote.text, "author": quote.author})
    else:
        return JsonResponse({"error": "No quotes found"}, status=404)

def search_quote(request):
    """Search quotes by author"""
    author = request.GET.get('author', '')
    if author:
        quotes = Quote.objects.filter(author__icontains=author)
        quotes_data = [{"text": q.text, "author": q.author} for q in quotes]
        return JsonResponse({"quotes": quotes_data})
    return JsonResponse({"quotes": []})

def quote_page(request):
    """Render the quote display page with a random quote."""
    quotes = Quote.objects.all()
    if quotes.exists():
        quote = random.choice(quotes)
        context = {"text": quote.text, "author": quote.author}
    else:
        context = {"text": "No quotes available", "author": ""}
    
    return render(request, 'quote.html', context)