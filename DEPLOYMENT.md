# 项目部署指南

## GitHub手动上传步骤

由于Git命令行工具不可用，请按照以下步骤手动上传项目到GitHub：

### 步骤1：访问GitHub仓库
1. 打开浏览器，访问：https://github.com/Z4221/20231201085-
2. 确保您已登录到GitHub账户

### 步骤2：上传文件
1. 在仓库页面点击 "Add file" 按钮
2. 选择 "Upload files"
3. 将以下文件拖拽到上传区域：
   - `README.md` (项目说明文档)
   - `requirements.txt` (依赖文件)
   - `manage.py` (Django管理文件)
   - `mysite/` 目录下的所有文件
   - `student_info/` 目录下的所有文件
   - `templates/` 目录下的所有文件
   - `.gitignore` (Git忽略规则)

### 步骤3：排除的文件
**不要上传以下文件/目录：**
- `.venv/` (Python虚拟环境)
- `__pycache__/` (Python缓存文件)
- `db.sqlite3` (本地数据库文件)

### 步骤4：提交更改
1. 在提交信息框中输入："添加学生信息页面项目"
2. 点击 "Commit changes" 完成上传

## 项目验证

上传完成后，您的GitHub仓库应该包含以下文件结构：

```
20231201085-/
├── README.md
├── DEPLOYMENT.md
├── requirements.txt
├── manage.py
├── .gitignore
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── student_info/
│   ├── __init__.py
│   ├── urls.py
│   └── views.py
└── templates/
    └── student_info.html
```

## 项目功能验证

项目上传后，其他用户可以通过以下步骤运行项目：

1. 下载项目文件
2. 安装Python和Django依赖
3. 运行 `python manage.py runserver`
4. 访问 http://127.0.0.1:8000/ 查看学生信息页面

## 技术支持

如有问题，请联系项目开发者：
- 学号：20231201085
- 姓名：张宇