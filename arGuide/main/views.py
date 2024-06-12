from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainPage(request):
    # 检查用户是否已经访问过网站
    has_visited = request.COOKIES.get('hasVisited')
    if has_visited == 'True':
        visit_status = "Welcome back! You have visited this site before."
    else:
        visit_status = "Welcome! This is your first visit to this site."
        # 设置 'hasVisited' cookie
        response = render(request, 'index.html', {'visit_status': visit_status})
        response.set_cookie('hasVisited', 'True')
        return response

    return render(request, 'index.html', {'visit_status': visit_status})