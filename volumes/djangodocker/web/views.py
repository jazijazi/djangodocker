from django.http import HttpResponse
from django.views.generic.edit import FormView
from .tasks import add
from .forms import EmailForm
from celery.result import AsyncResult

def home(req):
    return HttpResponse("<h1> Hello From Django </h1>")

def add_task(req):
    a = int(req.GET.get('a' , '2'))
    b = int(req.GET.get('b' , '2'))
    wait = int(req.GET.get('wait' , '2'))

    res = add.apply_async([a,b] , countdown=wait)
    res = res.get()

    return HttpResponse(f"<h2> a is {a} / b is {b} / wait time is {wait} seconds</h2> <h1>result is {res}</h1>")


class EmailView(FormView):
    template_name = 'review.html'
    form_class = EmailForm

    def form_valid(self, form):
        res = form.send_email()
        res = AsyncResult(res.task_id)
        #print(res , res.state , res.result , res.status)
        try:
            x = res.get() #wait until get result of this task
            print(x)
            return HttpResponse("<h1> Email Sent Successfully </h1>")
        except Exception as e:
            print(f"Exception in Email Task : {e} , state : {res.state}")
            return HttpResponse("<h1> Email Not Sent Try Again</h1>")


