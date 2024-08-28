from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Question, Alternative, Answer
from django.shortcuts import render, get_object_or_404


def login_view(request):
    if request.method == "POST":
        apelido = request.POST.get("jogo")
        
        if str(apelido).lower() == "jogo":
            return redirect(reverse('saudacao'))
        else:
            messages.error(request, "Digite a palavra certa. Tente novamente.")
            return redirect(reverse('login'))  # Substitua 'login' pelo nome da sua URL de login
    return render(request, "index.html")

def quiz_view(request, id):
    quiz_question = get_object_or_404(Question, pk=id)
    quiz_alternatives = quiz_question.alternatives.all()
    return render(request, 'quiz.html', {'quiz': quiz_question, 'id': id, 'alternatives': quiz_alternatives})


def quiz_submit(request, id):
    if id == 10:
        return redirect('mario')
    
    if request.method == "POST":
        alternativa_correta = Alternative.objects.filter(question=id, is_correct=True).first()
        alternativa_enviada = request.POST.get('resposta')
        
        print(alternativa_correta, alternativa_enviada)
        
        if str(alternativa_correta) == str(alternativa_enviada):
            return redirect('quiz', id+1)
        
        else:
           messages.error(request, "Você errou!")
           return redirect('quiz', id=1)

def saudacao(request):
    return render(request, 'saudacao.html')

def mario(request):
    return render(request, 'mario.html')

def premio(request):
    return render(request, 'premio.html')
