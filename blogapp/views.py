from django.http import JsonResponse
from .models import BlogPost

def blogs(request):
    posts = BlogPost.objects.all()
    data = {
        'blogs': [{
            'category': 'empty',
            'title': post.title,
            'content': post.content,
            'short_description': post.short_description,
            'created_at': post.created_at.strftime('%d %B, %H:%M'),
            'updated_at': post.updated_at.strftime('%d %B, %H:%M'),
        } for post in posts]
    }
    return JsonResponse(data)

def ck_editor_5_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        return JsonResponse({'uploaded': True, 'url': 'URL_TO_UPLOADED_FILE'})
    return JsonResponse({'uploaded': False, 'error': 'Invalid request'})
