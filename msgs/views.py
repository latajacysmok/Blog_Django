from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User
from datetime import datetime

@login_required(login_url='/login/')
def send_message(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.sender = request.user
			message.message_date = datetime.now()
			message.save()
			return redirect('/')
	else:
		form = MessageForm()
		context = {
			"form": form
		}
		return render(request, 'msgs/sendmessage.html', context)

@login_required(login_url='/login/')
def inbox(request):
	u = User.objects.get(pk=request.user.id)
	logindate = u.last_login
	messages = Message.objects.filter(recipient=request.user, message_date__gte=logindate)
	
	context =  {'messages':messages,
				'logindate':logindate}
	return render(request, 'msgs/inbox.html',context)