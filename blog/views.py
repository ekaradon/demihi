from django.shortcuts import render, get_object_or_404
from blog.models import Entry
# Create your views here.

def index(request):
	latest_entry_list = Entry.objects.order_by('-pub_date')[:5]
	context = {'latest_entry_list': latest_entry_list}
	return render(request, 'blog/index.jade', context)


def entry(request, entry_id):
	e = get_object_or_404(Entry, pk=entry_id)
	return render(request, "blog/entry.jade", {"entry": e})