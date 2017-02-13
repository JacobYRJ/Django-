from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book
from django.core.mail import send_mail
from django.template import RequestContext
from books.forms import ContactForm
# Create your views here.
#--a search form --
def search_form(request):
	return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else :
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors':errors})

# ==  Contact---
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','yrj123741@163.com'),
                ['yrj123741@163.com'], fail_silently=True
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
	    form = ContactForm()
    return render_to_response('contact_form.html', {'form': form}, context_instance=RequestContext(request))

def thanks(request):
	html = '<html><body>Thanks</html></body>'
	return HttpResponse(html)
