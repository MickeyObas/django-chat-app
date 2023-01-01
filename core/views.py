from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import RegistrationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import RoomCreationForm
from .models import Room, Message

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            new_room = form.save(commit=False)
            new_room.creator = request.user
            new_room.save()
            return redirect('room', new_room.id)
    q = request.GET.get('search')
    rooms = Room.objects.filter(title__icontains=q) if q != None else ""
    form = RoomCreationForm() 

    context = {
        "form": form,
        "rooms": rooms
    }

    return render(request, "core\index.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = new_user.email.lower()
            new_user.save()
            return redirect('login')
    
    return render(request, "accounts/register.html", {"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials!!!")
            return redirect('login')

    return render(request, "accounts/login.html")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request, "accounts/logout.html")

def room(request, pk):
    room = get_object_or_404(Room, id=pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        print(body)
        new_message = Message.objects.create(sender=request.user, room=room, body=body)
        new_message.save()
        return redirect('room', pk)

    context = {
        "messages": Message.objects.filter(room=room).order_by('date_created'),
        "room": room
    }

    return render(request, "core/room.html", context)
