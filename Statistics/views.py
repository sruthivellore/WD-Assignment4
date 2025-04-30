import statistics
from django.shortcuts import render, redirect
import math

def home(request):
     context = {}
     return render(request, 'home.html', context)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

def results(request):
    if request.method == 'POST':
        numbers = []

        text_input = request.POST.get('numbers', '')
        if text_input:
            numbers = text_input.split(',')

        elif 'file' in request.FILES:
            file = request.FILES['file']
            file_content = file.read().decode('utf-8')
            numbers += file_content.split(',')

        numbers = [int(n.strip()) for n in numbers if n.strip().isdigit()]

        if not numbers:
            return render(request, 'home.html', {'error': 'Please enter a valid comma-separated list of numbers.'})

        num_sum = sum(numbers)
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        try:
            mode = statistics.mode(numbers)
        except statistics.StatisticsError:
            mode = 'No unique mode'
        num_range = max(numbers) - min(numbers)
        primes = [n for n in numbers if is_prime(n)]
        armstrongs = [n for n in numbers if is_armstrong(n)]

        context = {
            'numbers': numbers,
            'sum': num_sum,
            'mean': mean,
            'median': median,
            'mode': mode,
            'range': num_range,
            'primes': primes,
            'armstrongs': armstrongs,
            'unique_count': len(numbers)
        }

        return render(request, 'result.html', context)

    return redirect('home')

