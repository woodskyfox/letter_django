from django.shortcuts import render, redirect

# Create your views here.

from . models import Message
from django.contrib.auth.decorators import login_required
from . forms import MessageForm
# from django.http import Http404

# My additional functions.

# def check_owner(request, message):
#     """Check owner of topic."""
#     if message.owner != request.user:
#         raise Http404

# letter_app views.

@login_required
def index(request):
	"""The home page for letter_app."""
	return render(request, 'letter_app/index.html')

@login_required
def messages(request):
	"""The message page for letter_app. For all messages."""
	messages = Message.objects.order_by('-date_added')
	request_user = request.user
	messages_number = len(messages)
	context = {'messages': messages, 'request_user': request_user, 'messages_number': messages_number}
	return render(request, 'letter_app/messages.html', context)

@login_required
def input_messages(request):
	"""The input messages page."""
	input_message = Message.objects.exclude(owner=request.user).order_by('-date_added')
	input_number = len(input_message)
	context = {"input_message": input_message, "input_number": input_number}
	return render(request, 'letter_app/inputmessages.html', context)

@login_required
def output_messages(request):
	"""The input messages page."""
	output_messages = Message.objects.filter(owner=request.user).order_by('-date_added')
	output_number = len(output_messages)
	context = {'output_messages': output_messages, "output_number": output_number}
	return render(request, 'letter_app/outputmessages.html', context)

@login_required
def write_message(request):
	"""Write a message."""

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = MessageForm()
	else:
		# POST data submitted: process data.
		form = MessageForm(data=request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.owner = request.user
			message.save()
			return redirect('letter_app:output_messages')

	# Display a blank or invalid form.
	context = {"form": form}
	return render(request, 'letter_app/write_message.html', context)

# def new_entry(request, topic_id):
#     """Add a new entry for a particular topic."""
#     # topic = Topic.objects.get(id=topic_id)
#     topic = get_object_or_404(Topic, id=topic_id)
#     check_topic_owner(request, topic)
    
#     if request.method != 'POST':
#         # No data submitted; create a blank form.
#         form = EntryForm()
#     else:
#         # POST data submitted: process data.
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.topic = topic
#             new_entry.save()
#             return redirect('learning_logs:topic', topic_id=topic_id)

#     # Display a blank or invalid form.
#     context = {'topic': topic, 'form': form}
#     return render(request, 'learning_logs/new_entry.html', context)

# def index(request):
# 	"""The home page for letter_app."""
# 	messages = Message.objects.order_by('-date_added')
# 	context = {'messages': messages}
# 	return render(request, 'letter_app/index.html', context)
