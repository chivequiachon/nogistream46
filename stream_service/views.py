from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

import requests

from .models import MvInfo

import json

def retrieve_view_count(videos):
    url = settings.VIEW_COUNT_URL
    char = '?'
    for video in videos:
        url += "%cid=%s" % (char, video.mv_id)
        char = '&'

    response = requests.get(url)
    json_data = response.json()

    success = json_data['success']
    if success:
        for video in videos:
            video.view_count = json_data[video.mv_id]

    return success

def retrieve_view_count_of_video(video):
    url = settings.VIEW_COUNT_URL + "?id=" + video.mv_id
    response = requests.get(url)
    json_data = response.json()

    success = json_data['success']
    if success:
        video.view_count = json_data[video.mv_id]

    return success


def homepage(request):
    return redirect(reverse('list_page'))

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
