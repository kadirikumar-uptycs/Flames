from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict

# Create your views here.

def home(request):
    return render(request, 'home.html')


def differentLettersCount(name1, name2):
    d1 = defaultdict(int)
    d2 = defaultdict(int)

    for letter in name1:
        d1[letter] += 1

    for letter in name2:
        d2[letter] += 1

    ans = 0
    for ascii in range(ord('a'), ord('z')+1):
        ans += abs(d1[chr(ascii)] - d2[chr(ascii)])
    return ans


def calculate(request):
    name1 = request.POST['name1']
    name2 = request.POST['name2']
    options = ['FriendShip', 'Love', 'Attraction', 'Marriage', 'Enemies', 'Sister']
    diff = differentLettersCount(name1.lower().replace(' ', ''), name2.lower().replace(' ', ''))
    start = 0
    while len(options) != 1:
        start += (diff - 1)
        start %= len(options)
        options.pop(start)
    relation = options[0]
    return render(request, 'home.html', {'name1': name1, 'name2': name2, 'relation': relation, 'image': relation+'.png'})