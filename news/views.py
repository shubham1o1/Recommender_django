from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News
from django.views.generic import DetailView
from users.models import Profile, KeyVal


@login_required
def home(request):

    current_user = request.user

    # find category and score for user
    keyval = KeyVal.objects.filter(name = current_user.username).order_by('-value')
    news = News.objects.all()

    # for user find the total tag list:

    if keyval.exists():
        user_tag_list=[]
        # Get list of all keys in that username.
        for kvi in keyval:
            user_tag_list.append(kvi.key)
    
        #if tag list is present in news then collect the news to show in the post:
        news_to_recommend = []
        for n in news:
            for user_tag in user_tag_list:
                if user_tag in n.tags and n not in news_to_recommend:
                    news_to_recommend.append(n)
                
        '''TODO:        
        # Sort the news list according to the value of the tag
        '''
        context = {
            'news_context': News.objects.all(),
            'recommended_context' : news_to_recommend
        }

    else:
        context = {
            'news_context': News.objects.all()
        }
    return render(request, 'news/home.html', context)

def login(request):
    return render(request, 'news/login.html')

def detail(request, tags, username):
    context = {
        'this_user': username,
        'tags': tags
    }
    current_user = request.user

    kv = KeyVal.objects.filter(name = current_user.username)

    kv_keys_list=[]
    if kv.exists():
        li = list(tags.split(","))
        # Get list of all keys of that username.
        for kvi in kv:
            kv_keys_list.append(kvi.key)
       
        # for each list passed through link, compare the key in the list
        for item in li:

            # if list has the key then increment the value
            if item in kv_keys_list:
                kv_buf = KeyVal.objects.get(name = current_user.username, key = item)
                kv_buf.value = kv_buf.value + 1 
                kv_buf.save()
            
            # if list doesn't have the key then add the key and value = 1
            else :
                KeyVal.objects.create(name = current_user.username, key = item, value = 1)

    # If there is not keyvalue pair at all for the user, create one and add value 1 to each key
    else :
        li = list(tags.split(","))
        for item in li:
            KeyVal.objects.create(name = current_user.username, key = item, value = 1)


    
    return render(request, 'news/news_detail.html', context)