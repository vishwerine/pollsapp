from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


from .models import ImgTxtPair , Choice

import random

def correct_img_paths(objs):

    for obj in objs:
        obj.image_src = obj.image_src[3:]
        obj.choice1_src = obj.choice1_src[3:]
        obj.choice2_src = obj.choice2_src[3:]
    return objs


def index(request):
    
    
    context = {
    }

    return render(request, 'polls/home.html', context)



def detail2(request):

    recipe_id_num = random.randint(0,99)
    objs = correct_img_paths(ImgTxtPair.objects.filter(recipe_id=str(recipe_id_num)+'.html'))
    context = {
        'pairs' : objs,
        'recipe_id': str(recipe_id_num),
        'userid': request.GET['id'],
    }

    return render(request, 'polls/index.html', context)




def detail(request, question_id):
    objs = correct_img_paths(ImgTxtPair.objects.filter(recipe_id=str(question_id)+'.html'))
    context = {
        'pairs' : objs,
        'recipe_id': str(question_id),
    }
    return render(request, 'polls/index.html', context)




def vote(request):
    recipe_id_num = random.randint(0,99)
    
    try:
        userid_val = request.GET['id']
    except:
        print('exception')
        userid_val = 'default'
    
    for key in request.GET.keys():
        if key!='id':
            Choice(imgtxtid=ImgTxtPair.objects.get(id=key), choice_text= request.GET[key], userid=userid_val).save()


    return detail2(request)


