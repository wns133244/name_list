from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from name.models import Name


def insert(request):
    file = open('name/yob1880.txt', 'rt')
    for line in file.readlines():
        line = line.replace('\n', '')
        line = line.split(',')[0]
        n = Name(name=line)
        n.save()

    file.close()
    return HttpResponse('insert')

def list(request):
    page = request.GET['page']

    # 1. db 데이터 조회
    name_list = Name.objects.order_by('name')

    # paginator 이용해서 객체 이용. 페이지 정보 추출
    paginator = Paginator(name_list, 20)

    page_info = paginator.page(page)  # 내가 필요한 페이지 번호 입력, 상단의 페이지 변수와 연결

    start_page = (int(page) - 1) // 10 * 10 + 1
    end_page = start_page + 10
    page_range = range(start_page, end_page)

    return render(request, 'name/list.html',
                  {'page_info': page_info,
                   'page_range':page_range})
