from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class Index(generic.ListView):
    template_name='polls/index.html'
    context_object_name='qlist'

    def get_queryset(self):
        return Question.objects.all()

class Detail(generic.DetailView):
    template_name='polls/detail.html'
    context_object_name = 'q'
    model=Question

def vote(request,id):
    q=get_object_or_404(Question,pk=id)
    try:
        selectedc=Choice.objects.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'em':'You did not select a valid choice','q':q})

    else:
        selectedc.votes+=1
        selectedc.save()
        return HttpResponseRedirect(reverse('polls:results',args=(id,selectedc.choice_text)))

def results(request,id,c):
    return render(request,'polls/results.html',{'q':Question.objects.get(id=id),'c':c})

def create(request):
    global c,q
    q = request.POST.get('ques')
    c = request.POST.get('number')
    if q==None:
        return render(request,'polls/create.html')

    if q=='':
        return render(request,'polls/create.html',{'sub':'This field is required'})

    date=request.POST.get('date')
    global newid, newq
    # Create the new question object
    if date:
        newq=Question(question_text=q,pub_date=date)
    else:
        newq=Question(question_text=q,pub_date=timezone.now())

    newq.save()
    newid=newq.id

    if c=='':
        return render(request, 'polls/proceed/ques_added.html', {'q':q})
    t=[1]*int(c)
    return render(request,'polls/proceed/ques_added.html',{'q':q,'list':[1]*int(c)})

def choice_form(request):
    global c,q,newq,newid
    c=int(c)
    choice_set = []
    validc = 0
    for i in range(1, c + 1):
        choice = request.POST.get('choice' + str(i))
        if choice:
            choice_set.append(choice)
            validc += 1
    if validc == c:
        for choice in choice_set:
            newq.choice_set.create(choice_text=choice)
        return render(request, 'polls/proceed/choice_created.html', {'q': q})
    return render(request, 'polls/proceed/ques_added.html', {'q': q, 'list': [1] * c, 'less': c - validc})

