from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect  #,HttpResponse,Http404,
from .models import Question,Choice
#from django.template import loader
from django.views import generic
from django.urls import reverse

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Test! Last 5 items!"""
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    try:        
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # ����choiceδ�ҵ��쳣ʱ�����·��ر�ҳ�棬��������ʾ��Ϣ
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # �ɹ��������ݺ��Զ���ת�����ҳ�棬��ֹ�û���������ύ��
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))        