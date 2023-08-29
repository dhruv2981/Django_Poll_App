from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
#we are also having get_list function
from .models import Question,Choice
from django.http import Http404
from django.urls import reverse
from django.db.models import F
# from django.template import loader




# Create your views here.

# def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request,question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question dont exist")
    question=get_object_or_404(Question,pk=question_id)
    context={
        "question":question
    }
    return render(request,"polls/detail.html",context)

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={
        "question":question
    }
    return render(request,"polls/results.html",context)

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    # if (request.method="post"):
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
            "question":question,
            "error_message":"You did not select a choice"
        },
        )        #agar ek hi chiz chaiye hoti to value attribute pe vo de dena tha
    else:
        selected_choice.votes=F('votes') + 1
        selected_choice.save()
        #avoid racing condition
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # return render(request,"polls/results.html",{
        #     'question':question
        # })
    
