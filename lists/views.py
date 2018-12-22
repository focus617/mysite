from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.core.exceptions import ValidationError

import datetime

# Create your views here.
# from lists.models import Item, List
# from lists.forms import ItemForm, ExistingListItemForm


def lists_homepage(request):
    """
    # R1:
    return render(request, 'lists/home.html')
    """
    # R1.1:
    return render(request, 'lists/home.html',
                  {'new_item_text': request.POST.get('item_text','')})

    """
    # R2:
    #     if request.method == 'POST':
    #         Item.objects.create(text=request.POST['text'])
    #         return redirect('/lists/the-only-list-in-the-world/')
    #     else:
    #        return render(request, 'home.html')
    # R3: migrates POST to new_list view,
    #     via home.html: <form method="POST" action="lists/new">
    # return render(request, 'home.html', {'form': ItemForm()})
    """

# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     error = None
#
#     if request.method == 'POST':
#         try:
#             item = Item(text=request.POST['text'], list=list_)
#             item.full_clean()
#             item.save()
#             # return redirect('/lists/%d/' % (list_.id,))
#             return redirect(list_)
#         except ValidationError:
#             error = "You can't have an empty list item"
#
# return render(request, 'list.html', {'form': ItemForm(), 'list': list_,
# 'error': error})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            #item = Item.objects.create(text=request.POST['text'], list=list_)
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'form': form, 'list': list_, })


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        #Item.objects.create(text=request.POST['text'], list=list_)
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})
