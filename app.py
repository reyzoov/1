from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from datetime import datetime
import json
import os
import hashlib
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'portfolio_data.json')

ADMIN_PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

DEFAULT_DATA = {
    "personal": {
        "name": "Reyizoov",
        "title": "Full-Stack Developer",
        "bio": "Создаю современные веб-приложения с чистым кодом и отличным UX",
        "email": "testingnurali@gmail.com",
        "github": "https://github.com/reyzoov",
        "telegram": "@reeizoov",
        "location": "Russian, Abakan"
    },
    "skills": [
        {"name": "Python", "level": 90, "category": "backend", "icon": "🐍"},
        {"name": "JavaScript", "level": 85, "category": "frontend", "icon": "⚡"},
        {"name": "React", "level": 80, "category": "frontend", "icon": "⚛️"},
        {"name": "Node.js", "level": 75, "category": "backend", "icon": "🟢"},
        {"name": "PostgreSQL", "level": 70, "category": "database", "icon": "🐘"},
        {"name": "Docker", "level": 65, "category": "devops", "icon": "🐳"},
        {"name": "CSS/SASS", "level": 85, "category": "frontend", "icon": "🎨"},
        {"name": "Git", "level": 80, "category": "tools", "icon": "📦"},
        {"name": "Linux", "level": 70, "category": "devops", "icon": "🐧"},
        {"name": "TypeScript", "level": 75, "category": "frontend", "icon": "📘"}
    ],
    "projects": [
        {
            "id": 1,
            "title": "Task Manager Pro",
            "description": "Полнофункциональный менеджер задач с авторизацией, drag-and-drop интерфейсом и уведомлениями",
            "tech": ["Python", "Flask", "PostgreSQL", "Redis", "WebSocket"],
            "demo_url": "#",
            "github_url": "#",
            "features": ["JWT авторизация", "Real-time обновления", "Канбан-доска", "Фильтры и поиск"]
        },
        {
            "id": 2,
            "title": "E-Commerce Platform",
            "description": "Интернет-магазин с платёжной системой, админ-панелью и аналитикой продаж",
            "tech": ["React", "Node.js", "MongoDB", "Stripe", "Docker"],
            "demo_url": "#",
            "github_url": "#",
            "features": ["Stripe интеграция", "Дашборд аналитики", "Управление товарами", "SEO оптимизация"]
        },
        {
            "id": 3,
            "title": "Chat Application",
            "description": "Мессенджер с поддержкой групповых чатов, отправки файлов и видеозвонков",
            "tech": ["Vue.js", "Socket.io", "Express", "MongoDB", "WebRTC"],
            "demo_url": "#",
            "github_url": "#",
            "features": ["Групповые чаты", "Video/Voice calls", "Шифрование E2E", "Обмен файлами"]
        }
    ],
    "experience": [
        {
            "company": "Freelance",
            "position": "Full-Stack Developer",
            "period": "2023 - настоящее время",
            "description": "Разработка веб-приложений, работа с клиентами по всему миру"
        },
        {
            "company": "StartupHub",
            "position": "Developer",
            "period": "2021 - 2023",
            "description": "Создание MVP продуктов, работа с React и Python бэкендом"
        }
    ],
    "stats": {
        "projects_completed": 15,
        "years_experience": 3,
        "happy_clients": 10,
        "code_commits": 800
    }
}


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return DEFAULT_DATA.copy()


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


PORTFOLIO_DATA = load_data()


def is_admin():
    return session.get('is_admin', False)


@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form.get('password', '')
        if hashlib.sha256(password.encode()).hexdigest() == ADMIN_PASSWORD_HASH:
            session['is_admin'] = True
            return redirect(url_for('admin_panel'))
        return render_template('admin_login.html', error='Неверный пароль')
    return render_template('admin_login.html', error=None)


@app.route('/admin/logout')
def admin_logout():
    session.pop('is_admin', None)
    return redirect(url_for('index'))


@app.route('/admin')
def admin_panel():
    if not is_admin():
        return redirect(url_for('admin_login'))
    return render_template('admin.html', data=PORTFOLIO_DATA)


@app.route('/admin/save', methods=['POST'])
def admin_save():
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 401

    new_data = request.get_json()
    PORTFOLIO_DATA.update(new_data)
    save_data(PORTFOLIO_DATA)
    return jsonify({"status": "success", "message": "Данные сохранены"})


@app.route('/admin/save/personal', methods=['POST'])
def admin_save_personal():
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    PORTFOLIO_DATA["personal"].update(data)
    save_data(PORTFOLIO_DATA)
    return jsonify({"status": "success"})


@app.route('/admin/save/skills', methods=['POST'])
def admin_save_skills():
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 401

    PORTFOLIO_DATA["skills"] = request.get_json()
    save_data(PORTFOLIO_DATA)
    return jsonify({"status": "success"})


@app.route('/admin/save/projects', methods=['POST'])
def admin_save_projects():
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 401

    PORTFOLIO_DATA["projects"] = request.get_json()
    save_data(PORTFOLIO_DATA)
    return jsonify({"status": "success"})


@app.route('/admin/save/experience', methods=['POST'])
def admin_save_experience():
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 401

    PORTFOLIO_DATA["experience"] = request.get_json()
    save_data(PORTFOLIO_DATA)
    return jsonify({"status": "success"})


@app.route('/admin/save/stats', methods=['POST'])
def admin_save_stats():
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 401

    PORTFOLIO_DATA["stats"].update(request.get_json())
    save_data(PORTFOLIO_DATA)
    return jsonify({"status": "success"})


@app.route('/api/portfolio')
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)


@app.route('/api/projects')
def get_projects():
    return jsonify(PORTFOLIO_DATA["projects"])


@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    project = next((p for p in PORTFOLIO_DATA["projects"] if p["id"] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({"error": "Project not found"}), 404


@app.route('/api/skills')
def get_skills():
    category = request.args.get('category')
    skills = PORTFOLIO_DATA["skills"]
    if category:
        skills = [s for s in skills if s["category"] == category]
    return jsonify(skills)


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')

    if not all([name, email, message]):
        return jsonify({"error": "All fields required"}), 400

    return jsonify({
        "status": "success",
        "message": f"Спасибо, {name}! Ваше сообщение получено.",
        "timestamp": datetime.now().isoformat()
    })


@app.route('/api/stats')
def get_stats():
    return jsonify(PORTFOLIO_DATA["stats"])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
