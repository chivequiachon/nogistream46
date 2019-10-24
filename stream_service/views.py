from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests

from .models import MvInfo

import json

def retrieve_view_count(videos):
    url = settings.VIEW_COUNT_URL
    char = '?'
    should_fetch = False
    for video in videos:
        if video.should_update_view_count():
            url += "%cid=%s" % (char, video.mv_id)
            char = '&'
            should_fetch = True
    
    if should_fetch:
        response = requests.get(url)
        json_data = response.json()

        success = json_data.get('success', False)
        if success:
            for video in videos:
                if video.should_update_view_count():
                    video.update_view_count(json_data[video.mv_id])

        return success
    else:
        return True

def retrieve_view_count_of_video(video):
    url = settings.VIEW_COUNT_URL
    should_fetch = False
    if video.should_update_view_count():    
        url += "?id=%" + video.mv_id
        should_fetch = True

    if should_fetch:
        response = requests.get(url)
        json_data = response.json()

        success = json_data.get('success', False)
        if success:
            video.update_view_count(json_data[video.mv_id])

        return success
    else:
        return True


def homepage(request):
    return redirect(reverse('list_page'))

def music_list_lazy_load(request):
    if request.is_ajax():
        html_template = '''
<div>
    <a style="display: -webkit-flex; padding-top: 0px;" href="%s">
    <img src="%s/%s.jpg" alt="" />
    </a>
    <a href="%s">%s</a>
    <small>%s</small>

    <p>%s views</p>
</div>
        '''
        mv_list = []
        cloudinary_img_url = \
            "https://res.cloudinary.com/%s/image/upload/v1555853606/nogistream" % settings.CLOUDINARY_NAME

        retreived_mvs = MvInfo.objects.filter(is_disabled=False).order_by('published_date')

        paginator = Paginator(retreived_mvs, 8) # Allow only 4 pages for each page
        page = int(request.GET.get('page', 2))
        json_response = json.dumps({'status': 'error'}).encode('utf-8')
        try:
            mvs = paginator.page(page)
        except PageNotAnInteger:
            return HttpResponse(json_response)
        except EmptyPage:
            return HttpResponse(json_response)
    
        success = retrieve_view_count(mvs)
        
        if success:
            for i in mvs:
                link_to_view = reverse('view_page', kwargs={'name_in_code':i.name_in_code})
                x = html_template % (link_to_view, cloudinary_img_url, i.name_in_code, link_to_view, i.title, i.performer_name, i.view_count)
                mv_list.append(x)

            json_response = json.dumps({'status': 'success', 'data': ''.join(mv_list)})
            return HttpResponse(json_response.encode('utf-8'))
        else:
            return HttpResponse(status_code=503) # Service Unavailable
    else:
        return HttpResponse(status_code=503) # Service Unavailable

def music_list_page(request):
    # Retrieve available mvs
    mv_list = MvInfo.objects.filter(is_disabled=False).order_by('published_date')[:8]
    success = retrieve_view_count(mv_list)

    if success:
        # Create url for images stored in cloudinary
        cloudinary_img_url = \
            "https://res.cloudinary.com/%s/image/upload/v1555853606/nogistream" % settings.CLOUDINARY_NAME

        return render(request, "music.html", {'mvs': mv_list, 'cloudinary_img_url': cloudinary_img_url})
    else:
        return HttpResponse(status_code=503) # Service Unavailable

def list_page(request):
    # Retrieve available mvs
    mv_list = MvInfo.objects.filter(is_disabled=False).order_by('published_date')[:8]
    success = retrieve_view_count(mv_list)

    if success:
        # Create url for images stored in cloudinary
        cloudinary_img_url = \
            "https://res.cloudinary.com/%s/image/upload/v1555853606/nogistream" % settings.CLOUDINARY_NAME

        return render(request, "index.html", {'mvs': mv_list, 'cloudinary_img_url': cloudinary_img_url})
    else:
        return HttpResponse(status_code=503) # Service Unavailable

def sample_viewpage(request, name_in_code):
    video = get_object_or_404(MvInfo, name_in_code=name_in_code)
    success = retrieve_view_count_of_video(video)
    
    if success:
        cloudinary_img_url = \
            "https://res.cloudinary.com/%s/image/upload/v1555853606/nogistream" % settings.CLOUDINARY_NAME
        other_videos = \
            MvInfo.objects.filter(is_disabled=False) \
                  .exclude(name_in_code=name_in_code) \
                  .order_by('published_date')[:6]
        success = retrieve_view_count(other_videos)
        if not success:
            return HttpResponse(status_code=503) # Service Unavailable    
        return render(request, "view.html", {'video': video, 'other_videos': other_videos, 'cloudinary_img_url': cloudinary_img_url})
    else:
        return HttpResponse(status_code=503) # Service Unavailable
