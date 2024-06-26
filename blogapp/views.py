from django.http import JsonResponse
from .models import BlogPost

<<<<<<< HEAD
=======

>>>>>>> 0d8e3ba2b3687abcdae31d00e282f9998a43988f
def blogs(request):
    posts = BlogPost.objects.all()
    data = {
        'blogs': [{
<<<<<<< HEAD
            'category': 'empty',
            'title': post.title,
            'content': post.content,
            'short_description': post.short_description,
            'created_at': post.created_at.strftime('%d %B, %H:%M'),
            'updated_at': post.updated_at.strftime('%d %B, %H:%M'),
=======
            'title': post.title,
            'content': post.content,
            'short_description': post.short_description,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': post.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
>>>>>>> 0d8e3ba2b3687abcdae31d00e282f9998a43988f
        } for post in posts]
    }
    return JsonResponse(data)

<<<<<<< HEAD
=======

>>>>>>> 0d8e3ba2b3687abcdae31d00e282f9998a43988f
def ck_editor_5_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        return JsonResponse({'uploaded': True, 'url': 'URL_TO_UPLOADED_FILE'})
    return JsonResponse({'uploaded': False, 'error': 'Invalid request'})
