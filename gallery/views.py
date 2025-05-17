from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import Photo

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('images')
    else:
        form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})

@login_required
def view_images(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'gallery/images.html', {'photos': photos})


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
from .models import Photo, Like, Comment


def feed(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'feed.html', {'photos': photos})

@login_required
def like_photo(request):
    if request.method == 'POST':
        photo_id = request.POST.get('photo_id')
        photo = get_object_or_404(Photo, id=photo_id)
        liked = Like.objects.filter(photo=photo, user=request.user).exists()

        if liked:
            Like.objects.filter(photo=photo, user=request.user).delete()
            action = 'unliked'
        else:
            Like.objects.create(photo=photo, user=request.user)
            action = 'liked'

        return JsonResponse({'action': action, 'likes': photo.total_likes()})

@login_required
def add_comment(request):
    if request.method == 'POST':
        photo_id = request.POST.get('photo_id')
        text = request.POST.get('text')
        photo = get_object_or_404(Photo, id=photo_id)
        comment = Comment.objects.create(photo=photo, user=request.user, text=text)
        return JsonResponse({
            'username': request.user.username,
            'text': comment.text
        })
