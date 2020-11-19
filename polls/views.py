from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Question

def index(request):
    myname = "tran huong"
    taisan1 = ["dien thoại", "máy tính", "mỹ", "nhiều tiền"]
    context = {"name": myname, "taisan": taisan1}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q=Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("loi khong co choice")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q": q})