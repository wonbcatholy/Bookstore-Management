# Bookstore Management System – Django Starter

Project Django dùng chung cho nhóm. Frontend được render bằng Django Templates và backend xử lý trong cùng một Django project; **không tách thành hai project FE/BE**.

## 1. Công nghệ

- Python 3.10 trở lên
- Django 5.2.x (dải phiên bản trong `requirements.txt`)
- SQLite cho môi trường phát triển ban đầu
- Django Templates, CSS
- Git

## 2. Cấu trúc thư mục

```text
bookstore_django_starter/
├── apps/
│   └── common/          # App dùng chung: trang chủ, health check
├── config/              # Cấu hình project Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
│   └── css/style.css    # CSS, ảnh, JavaScript tĩnh
├── templates/           # HTML templates dùng chung
├── .env.example         # Mẫu biến môi trường, không chứa secret thật
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## 3. Cài đặt lần đầu trên máy Windows

Mở Terminal/PowerShell tại thư mục project.

### Bước 1 – Kiểm tra Python và Git

```powershell
python --version
git --version
```

Khuyến nghị Python 3.10 trở lên. Nếu lệnh `python` không hoạt động, cài Python và bật tùy chọn Add Python to PATH.

### Bước 2 – Tạo môi trường ảo

```powershell
python -m venv .venv
```

Kích hoạt:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn script, có thể dùng Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Khi thành công, đầu dòng terminal thường có tiền tố `(.venv)`.

### Bước 3 – Cài thư viện

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Bước 4 – Tạo file môi trường `.env`

PowerShell:

```powershell
Copy-Item .env.example .env
```

Command Prompt:

```cmd
copy .env.example .env
```

`.env` chứa cấu hình riêng của máy và secret; không commit file này lên Git.

### Bước 5 – Tạo bảng dữ liệu ban đầu

```powershell
python manage.py migrate
```

Lệnh này tạo các bảng mặc định mà Django cần (người dùng, phiên đăng nhập, quyền, admin...).

### Bước 6 – Chạy server

```powershell
python manage.py runserver
```

Mở trình duyệt tại:

- Trang chủ: http://127.0.0.1:8000/
- Kiểm tra server: http://127.0.0.1:8000/health/
- Trang quản trị: http://127.0.0.1:8000/admin/

Dừng server bằng `Ctrl + C`.

### Bước 7 – (Tùy chọn) Tạo tài khoản quản trị

```powershell
python manage.py createsuperuser
```

Làm theo hướng dẫn trong terminal để tạo username, email và password.

## 4. Cài đặt trên macOS / Linux

Tại thư mục project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Mở http://127.0.0.1:8000/.

## 5. Quy trình khi thành viên mới nhận project từ Git

Thành viên chỉ cần làm các bước sau, không cần tạo project Django mới:

```bash
git clone <URL_REPOSITORY>
cd <TEN_THU_MUC_REPOSITORY>
python -m venv .venv
```

Kích hoạt venv theo hệ điều hành, sau đó:

```bash
pip install -r requirements.txt
```

Tạo `.env` từ `.env.example` (Windows dùng `Copy-Item .env.example .env`; macOS/Linux dùng `cp .env.example .env`), rồi chạy:

```bash
python manage.py migrate
python manage.py runserver
```

**Lưu ý:** `venv` và `.env` không được đẩy lên Git. Mỗi thành viên tự tạo chúng trên máy của mình. `requirements.txt` là danh sách thư viện để mọi người cài cùng bộ dependency.

## 6. Quy tắc Git đề xuất cho nhóm

### Nhánh

- `main`: phiên bản ổn định, đủ điều kiện demo/nộp.
- `develop`: nhánh tích hợp công việc đang phát triển.
- `feature/<ten-chuc-nang>`: phát triển chức năng, ví dụ `feature/book-management`.
- `fix/<ten-loi>`: sửa lỗi, ví dụ `fix/login-validation`.
- `docs/<noi-dung>`: cập nhật tài liệu, ví dụ `docs/update-readme`.

Không commit trực tiếp lên `main`. Thành viên tạo nhánh từ `develop`, làm việc và push lên remote, sau đó tạo Pull Request/Merge Request vào `develop`. Chỉ merge `develop` vào `main` khi nhóm kiểm tra và thống nhất.

### Lệnh Git khởi tạo (người quản lý repository thực hiện)

```bash
git init
git add .
git commit -m "chore: initialize Django project structure"
git branch -M main
git switch -c develop
```

Tạo repository trống trên GitHub, sau đó liên kết và push:

```bash
git remote add origin <URL_REPOSITORY>
git push -u origin main
git push -u origin develop
```

### Quy trình làm một chức năng

```bash
git switch develop
git pull origin develop
git switch -c feature/book-management

# chỉnh sửa code
git status
git add .
git commit -m "feat: add book management scaffold"
git push -u origin feature/book-management
```

Sau đó mở Pull Request từ `feature/book-management` vào `develop`.

### Quy tắc đặt commit

Dùng dạng:

```text
<type>: <mô tả ngắn bằng tiếng Anh>
```

Các type nên dùng:

- `feat`: thêm chức năng
- `fix`: sửa lỗi
- `docs`: tài liệu
- `style`: định dạng code, không đổi logic
- `refactor`: tái cấu trúc code
- `test`: thêm/sửa kiểm thử
- `chore`: công việc cấu hình, công cụ, dependency

Ví dụ:

```text
feat: add book search page
fix: prevent negative stock quantity
docs: update installation guide
chore: add Django environment configuration
```

Một commit nên tập trung vào một mục đích nhỏ, dễ đọc và dễ xem lại.

## 7. Quy ước phát triển Django trong nhóm

- Tất cả thành viên làm trên **một repository và một Django project**.
- Mỗi phân hệ nghiệp vụ được tạo thành một Django app riêng bên trong `apps/`, ví dụ `apps/accounts`, `apps/books`, `apps/inventory`, `apps/sales`.
- Tạo app bằng lệnh từ thư mục gốc, ví dụ:

```bash
python manage.py startapp books apps/books
```

Sau đó chỉnh `apps/books/apps.py` để `name = "apps.books"` và thêm `"apps.books.apps.BooksConfig"` vào `INSTALLED_APPS` trong `config/settings.py`.
- URL từng app có thể được khai báo trong `apps/<app_name>/urls.py`, sau đó include từ `config/urls.py`.
- Khi thay đổi model: chạy `python manage.py makemigrations`, xem lại migration, commit migration cùng code; thành viên khác chạy `python manage.py migrate`.
- Không commit `.env`, `.venv/`, `db.sqlite3`, mật khẩu hoặc secret.
- Trước khi tạo Pull Request: chạy `python manage.py check` và `python manage.py test`.

## 8. Các lệnh kiểm tra quan trọng

```bash
python manage.py check
python manage.py test
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate
```

## 9. Sự cố thường gặp

- `No module named django`: chưa kích hoạt `.venv` hoặc chưa chạy `pip install -r requirements.txt`.
- `python is not recognized`: Python chưa được cài hoặc chưa thêm vào PATH.
- `TemplateDoesNotExist`: kiểm tra tên file trong `templates/` và `DIRS` trong `config/settings.py`.
- `Port is already in use`: chạy `python manage.py runserver 8001`.
- Máy mới không có dữ liệu SQLite cũ: đây là bình thường vì database local không được commit; chạy `migrate` để tạo database mới. Nếu cần dữ liệu mẫu chung, nhóm nên tạo fixture hoặc seed data riêng.

## 10. Phạm vi của bộ khung này

Bộ khung cung cấp project Django chạy được, cấu hình cơ bản, trang chủ mẫu, health-check, static CSS, SQLite và quy trình làm việc nhóm. Nó **chưa triển khai** các nghiệp vụ quản lý tài khoản, sách, kho, khách hàng, bán hàng, hóa đơn hoặc phân quyền theo yêu cầu nghiệp vụ. Những phần đó sẽ được phát triển trong các Django app tiếp theo.
