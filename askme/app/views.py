from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def paginate(obj_list, req, per_page=4):
    paginator = Paginator(obj_list, per_page)
    page_number = req.GET.get('page', 1)

    try:
        page_number = int(page_number)
    except ValueError:
        page_number = 1

    try:
        return paginator.get_page(page_number), page_number
    except EmptyPage:
        return paginator.get_page(paginator.num_pages), paginator.page_number


def index(request):
    arr_questions = []

    CNT_Q = 7

    for i in range(CNT_Q):
        arr_questions.append({
            'likes': 5,
            'title': 'How to build a moon park ? ' + str(i + 1),
            'description': 'Guys, i have trouble with a moon park. Cant find th black-jack...',
            'cnt_answers': 3,
            'tags': ['black-jack', 'bender']
        })

    CNT_ON_PAGE = 4

    paginated_questions, cur_page = paginate(arr_questions, request, CNT_ON_PAGE)
    data = {
        'questions': paginated_questions,
        'cnt_pages': range(1, (CNT_Q + CNT_ON_PAGE - 1) // CNT_ON_PAGE + 1),
        'cur_page': cur_page
    }

    return render(request, 'app/index.html', data)

def ask(request):
    return render(request, 'app/ask.html')

def login(request):
    return render(request, 'app/login.html')

def signup(request):
    return render(request, 'app/signup.html')

def questions(request):
    return render(request, 'app/questions.html')