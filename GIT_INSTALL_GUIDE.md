# Git命令行工具安装指南

## 当前状态
您的系统尚未安装Git命令行工具，但项目已经配置了Git仓库和远程连接。

## 安装方法

### 方法一：下载官方Git安装包（推荐）

#### 步骤1：下载Git
1. 打开浏览器，访问：https://git-scm.com/download/win
2. 点击 "Windows" 下载按钮
3. 保存 Git-2.xx.x-64-bit.exe 文件到您的电脑

#### 步骤2：安装Git
1. 双击运行下载的安装程序
2. 按照以下设置进行安装：

**重要设置选项：**
- ✅ **选择组件**：保持默认选择（全选）
- ✅ **PATH环境**：选择 "Git from the command line and also from 3rd-party software"
- ✅ **行尾转换**：选择 "Checkout Windows-style, commit Unix-style line endings"
- ✅ **终端模拟器**：选择 "Use Windows' default console window"
- ✅ **其他选项**：保持默认设置

#### 步骤3：验证安装
安装完成后，打开新的命令提示符或PowerShell窗口，输入：
```cmd
git --version
```
如果显示Git版本信息（如 `git version 2.xx.x`），说明安装成功。

### 方法二：使用GitHub Desktop（如果已安装）

如果您已经安装了GitHub Desktop，可以：
1. 打开GitHub Desktop
2. 点击菜单 File → Options → Git
3. 确保 "Use Git from Git Bash only" 或类似选项已配置
4. 重启命令行工具

## 安装后的项目推送步骤

Git安装成功后，在项目目录中执行以下命令：

### 1. 检查Git状态
```bash
git status
```

### 2. 添加所有文件到Git
```bash
git add .
```

### 3. 创建提交
```bash
git commit -m "添加学生信息页面项目 - 学号20231201085 姓名张宇"
```

### 4. 推送到GitHub
```bash
git push origin main
```

## 故障排除

### 如果Git命令仍然无法识别：
1. 重启计算机
2. 打开新的命令提示符窗口
3. 检查PATH环境变量是否包含Git路径

### 检查PATH环境变量：
在PowerShell中运行：
```powershell
echo $env:PATH
```
应该包含类似 `C:\\Program Files\\Git\\cmd` 的路径。

## 项目文件说明

您的项目已经包含以下重要文件：
- ✅ `.gitignore` - Git忽略规则
- ✅ `README.md` - 项目说明文档
- ✅ `DEPLOYMENT.md` - 部署指南
- ✅ `requirements.txt` - 依赖文件
- ✅ 完整的Django项目结构

## 技术支持

如果安装过程中遇到问题：
1. 检查网络连接
2. 确保以管理员身份运行安装程序
3. 查看Git官方文档：https://git-scm.com/doc

安装完成后，您就可以使用Git命令将项目推送到GitHub仓库了！