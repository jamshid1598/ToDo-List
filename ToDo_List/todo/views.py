from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import ToDo_List
from .forms import ToDo_List_Form


# Create your views here.

def homepage(request):
    if request.POST:
        form=ToDo_List_Form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                ('Item Has Been Added To List!')
            )
            object_list = ToDo_List.objects.all()
            return render(
                request=request,
                template_name='todo/home-page.html',
                context={
                    'object_list' : object_list
                }
            )
    else:
        object_list = ToDo_List.objects.all()
        return render(
            request=request,
            template_name='todo/home-page.html',
            context={
                'object_list' : object_list
            }
        )


def Item_Delete(request, id):
    obj=get_object_or_404(ToDo_List, id=id)
    if obj:
        obj.delete()
    messages.success(
        request,
        ('It Has Been Deleted!')
    )
    return redirect('todo:home')


def cross_off(request, id):
    obj=get_object_or_404(ToDo_List, id=id)
    if obj:
        obj.complated=True
        obj.save()
    # messages.success(
    #     request,
    #     ('It Has Been Deleted!')
    # )
    return redirect('todo:home')

def uncross(request, id):
    obj=get_object_or_404(ToDo_List, id=id)
    if obj:
        obj.complated=False
        obj.save()
    # messages.success(
    #     request,
    #     ('It Has Been Deleted!')
    # )
    return redirect('todo:home')


def edit_view(request, id):
    if request.method == 'POST':
        obj=get_object_or_404(ToDo_List, id=id)
        form=ToDo_List_Form(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                ('Item Has Been Edited!')
            )
            return redirect('todo:home')
            # object_list = ToDo_List.objects.all()
            # return render(
            #     request=request,
            #     template_name='todo/home-page.html',
            #     context={
            #         'object_list' : object_list
            #     }
            # )
    else:
        obj=get_object_or_404(ToDo_List, id=id)
        return render(
            request=request,
            template_name='todo/edit-page.html',
            context={
                'object' : obj
            }
        )