from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    #if request.method == 'POST':
        #return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    return render(request, 'home.html', {
            'new_item_text': request.POST.get('item_text', '')                        
        })