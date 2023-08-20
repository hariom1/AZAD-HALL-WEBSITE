from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm, CommentForm
from django.core.mail import BadHeaderError, send_mail
from django.http import JsonResponse
from django.core import serializers

# def index(request):
#     return HttpResponse("Hello, world")

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')


def noticeboard(request):
    noticeboard = Notice.objects.all()
    return render(request, 'noticeboard.html', {'noticeboard': noticeboard})

def notice(request, noticeid):
    notice = Notice.objects.filter(id=noticeid)
    noticeboard = Notice.objects.all()
    return render(request, 'notice.html', {'notice': notice[0], 'noticeboard': noticeboard})


def achievements(request):
    achievements = Achievements.objects.all()
    return render(request, 'achievements.html', {'achievements': achievements})


def achievement(request, achievementid):
    achievement = Achievements.objects.filter(id=achievementid)
    achievements = Achievements.objects.all()
    return render(request, 'achievement.html', {'achievement': achievement[0], "achievements": achievements})

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def about(request):
    if (request.method == 'POST'):
        form = ContactForm(request.POST)
        form.save()
        subject = request.POST.get('subject', '')
        message = request.POST.get('msg', '')
        from_email = request.POST.get('email', '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email,
                          ['smarakdev@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/about')
        else:
            form = ContactForm()
            return render(request, 'about.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'about.html', {'form': form})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def postComment(request):
    # request should be ajax and method should be POST.
    print("hello")
    if is_ajax(request=request) and request.method == "POST":
        # get the form data
        form = CommentForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            print("saved")
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def event(request, eventid):
    id = eventid
    # print("message", eventid)
    event = Event.objects.filter(id=eventid)
    itemlist = []
    # print(event)
    # print(event[0].para_set.all())
    commentform = CommentForm()
    comments = event[0].comments.all()

    cover = ""
    for item in event[0].imagemodel_set.all():
        if item.caption == 'cover':
            cover = item
            continue
        itemlist.append(item)
    for item in event[0].para_set.all():
        itemlist.append(item)
    # print(itemlist)
    itemlist.sort(key=lambda x: x.date, reverse=True)
    # print(itemlist)
    # print(cover.caption)
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events, 'cover': cover, 'event': event[0], 'form': commentform, 'comments': comments})
