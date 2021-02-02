from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def add(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        result = request.POST['indicator']
        firstNum = int(request.POST['fNum'])
        secondNum = int(request.POST['lNum'])
        if result == '+':
            sum = firstNum + secondNum
            context = {
                'sum': sum,
                'sum1': 'sum'
            }
            return render(request, 'result.html', context)
        elif result == '-':

            sub = firstNum - secondNum
            context = {
                'sub': sub,
                'sub1': 'subtraction'
            }
            return render(request, 'result.html', context)

        elif result == '*':
            mul = firstNum * secondNum
            context = {
                'multi': mul,
                'multi1': 'multiplication',
            }
            return render(request, 'result.html', context)
        else:
            div = firstNum/secondNum
        context = {

            'div': div,
            'div1': 'Devision'
        }
        return render(request, 'result.html', context)
