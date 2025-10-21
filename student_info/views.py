from django.shortcuts import render

def student_info(request):
    """显示学生信息的视图函数"""
    student_data = {
        'student_id': '20231201085',
        'student_name': '张宇'
    }
    return render(request, 'student_info.html', student_data)