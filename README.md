# 🚀 Interactive Portfolio Website

Современный full-stack сайт-портфолио с анимированным интерфейсом, dark/light темой и REST API.

## ⚡ Технологии

| Технология | Описание |
|------------|----------|
| **Python 3.11+** | Backend логика |
| **Flask** | Web-фреймворк |
| **HTML5** | Структура страниц |
| **CSS3** | Стили, анимации, переменные |
| **JavaScript** | Интерактивность, API запросы |

## 🏗 Структура проекта

```
portfolio-project/
├── app.py                  # Flask приложение + API
├── requirements.txt        # Зависимости Python
├── .env.example           # Пример переменных окружения
├── .gitignore             # Игнорируемые файлы
├── static/
│   ├── css/
│   │   └── style.css      # Все стили (1000+ строк)
│   ├── js/
│   │   └── main.js        # Frontend логика
│   └── images/            # Изображения
└── templates/
    └── index.html         # Jinja2 шаблон
```

## 🚀 Запуск

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/yourusername/portfolio.git
cd portfolio

# 2. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Запустите сервер
python app.py
```

Откройте http://localhost:5000 в браузере.

## 🎨 Возможности

### Frontend
- ✅ **Анимированный курсор** с эффектом следования
- ✅ **Dark/Light тема** с сохранением в localStorage
- ✅ **Typed-эффект** для имени в Hero секции
- ✅ **Анимированные счётчики** статистики
- ✅ **Фильтрация навыков** по категориям
- ✅ **Scroll-анимации** элементов
- ✅ **Кастомные курсоры** при наведении
- ✅ **Адаптивный дизайн** для всех устройств

### Backend API
```
GET  /                    # Главная страница
GET  /api/portfolio       # Все данные портфолио
GET  /api/projects        # Список проектов
GET  /api/projects/<id>   # Детали проекта
GET  /api/skills          # Навыки (фильтр: ?category=frontend)
POST /api/contact         # Форма обратной связи
GET  /api/stats           # Статистика
```

### Пример запроса
```bash
curl http://localhost:5000/api/projects
```

## 🎯 Что здесь изучено

- **Python**: Flask роутинг, JSON API, шаблонизатор Jinja2
- **HTML**: Семантическая разметка, доступность
- **CSS**: CSS переменные, Grid/Flexbox, анимации, backdrop-filter
- **JS**: Intersection Observer, Fetch API, localStorage,事件委托

## 📝 Лицензия

MIT
