from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    """
    Hello World页面，显示姓名和学号
    """
    context = {
        'title': 'Hello World应用',
        'message': 'Hello World!',
        'name': '张宇',
        'student_id': '20231201085',
        'welcome_message': '欢迎访问我的第一个Hello World应用'
    }
    return render(request, 'helloworld/hello.html', context)

def simple_hello(request):
    """
    简单的Hello World文本响应
    """
    return HttpResponse("Hello World! 我是张宇，学号20231201085")

def json_data(request):
    """
    JSON格式的Hello World数据
    """
    from django.http import JsonResponse
    data = {
        'app_name': 'Hello World应用',
        'message': 'Hello World!',
        'developer': {
            'name': '张宇',
            'student_id': '20231201085'
        },
        'timestamp': '2025年',
        'status': 'success'
    }
    return JsonResponse(data)