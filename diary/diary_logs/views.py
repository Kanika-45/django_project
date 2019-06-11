from django.shortcuts import render
from .models import Log
from django.shortcuts import render, get_object_or_404
from .forms import LogForm
from django.shortcuts import redirect

# Create your views here.
def log_list(request):
    logs = Log.objects.all()
    return render(request, 'diary/log_list.html',{'logs':logs})


def log_details(request, primary_key):
   # log = get_object_or_404(Log, pk=pk)
   try:
       log = Log.objects.get(pk=primary_key)
   except Log.DoesNotExist:
       raise Http404
   return render(request, 'diary/log_detail.html', {'log': log})

def log_new(request):
    if request.method=="POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit = False)
            log.author = request.user
            log.published_date = timezone.now()
            log.save()
            return redirect('log_detail', pk = post.pk)
    else:
        form = LogForm()
    return render(request, 'diary/log_new.html',{'form': form})
