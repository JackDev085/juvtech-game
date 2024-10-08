from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Question, Alternative
from django.shortcuts import render, get_object_or_404
import random
def login_view(request):
    if request.method == "POST":
        apelido = request.POST.get("jogo")
        
        if str(apelido).lower() == "jogo":
            return redirect(reverse('saudacao'))
        else:
            messages.error(request, "Digite a palavra certa. Tente novamente.")
            return redirect(reverse('login'))
    return render(request, "pages/index.html")

def quiz_view(request, id):
   
    if id == 11:
        return redirect('mario')
    quiz_question = get_object_or_404(Question, pk=id)
    quiz_alternatives = quiz_question.alternatives.all()
    return render(request, 'pages/quiz.html', {'quiz': quiz_question,"id":id,'alternatives': quiz_alternatives})

def quiz_submit(request, id):
    if request.method == "POST":
        alternativa_correta = Alternative.objects.filter(question=id, is_correct=True).first()
        alternativa_enviada = request.POST.get('resposta')
        print(alternativa_correta, alternativa_enviada)
        if str(alternativa_correta) == str(alternativa_enviada):
            return redirect('quiz', id+1)
        else:
           messages.error(request, "Você errou!")
           return redirect('quiz', 1)
    return redirect('quiz', 1)
         

def saudacao(request):
    return render(request, 'pages/saudacao.html')

def mario(request):
    return render(request, 'pages/mario.html')

def premio(request):
    return render(request, 'pages/premio.html')


