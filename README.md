# 学生信息页面项目

## 项目描述
这是一个基于Django框架的学生信息展示页面，显示学号20231201085和姓名张宇。

## 功能特点
- 显示学生学号：20231201085
- 显示学生姓名：张宇
- 响应式网页设计
- 现代化的UI界面

## 技术栈
- Python 3.x
- Django 5.2.7
- HTML5 + CSS3

## 项目结构
```
20231201085-/
├── manage.py          # Django项目管理文件
├── mysite/            # Django项目配置
│   ├── settings.py    # 项目设置
│   ├── urls.py       # URL路由配置
│   └── wsgi.py       # WSGI配置
├── student_info/      # 学生信息应用
│   ├── views.py       # 视图函数
│   └── urls.py       # 应用路由
├── templates/         # 模板文件
│   └── student_info.html  # 学生信息页面模板
└── .gitignore        # Git忽略规则
```

## 安装和运行

### 环境要求
- Python 3.8+
- Django 5.2+

### 安装步骤
1. 克隆或下载项目
2. 创建虚拟环境：`python -m venv .venv`
3. 激活虚拟环境：`.venv\\Scripts\\activate` (Windows)
4. 安装依赖：`pip install django`
5. 运行迁移：`python manage.py migrate`
6. 启动服务器：`python manage.py runserver`
7. 访问：http://127.0.0.1:8000/

## 页面功能
访问首页即可看到学生信息卡片，包含：
- 学号：20231201085（蓝色显示）
- 姓名：张宇（绿色显示）

## 开发者信息
- 学号：20231201085
- 姓名：张宇
- 项目创建时间：2025年

## 许可证
本项目使用GNU Lesser General Public License v2.1。