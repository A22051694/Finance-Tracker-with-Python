
# 💰 Finance Tracker with Python

A web-based personal finance tracker built using **Python**, **Django**, and **Vanilla CSS/JS**, with a clean UI, month-wise summaries, and CSV import/export features.

---

## 🚀 Features

- 🔍 Add, edit, and delete income/expense transactions
- 📅 Month-wise summaries
- 🗃️ Categorization by income or expense types
- 📤 Export transactions to CSV
- 📥 Import transactions from CSV (bulk upload)
- 💅 Dark theme with smooth, modern styling
- 🔧 Bug report form for user feedback

---

## 🖼️ Demo Screenshots

> _[Screenshots to be added soon]_  
(Include homepage, tracker page, and month summary when ready.)

---

## 📂 Project Structure

```
finance-tracker/
│
├── tracker/              # Django app
│   ├── migrations/       # Database migrations
│   ├── __init__.py
│   ├── admin.py          # Django admin configuration
│   ├── apps.py           # Django app configuration
│   ├── models.py         # Database models
│   ├── tests.py          # Unit tests
│   └── views.py          # View logic
│
├── templates/            # HTML templates (home, tracker, etc.)
│   ├── base.html         # Base layout
│   ├── home.html         # Home page template
│   └── tracker.html      # Tracker page template
│
├── static/               # CSS, JS, animations
│   ├── css/              # Stylesheets
│   │   ├── base.css      # Global styles
│   │   └── tracker.css   # Tracker page styles
│   └── js/               # JavaScript files
│       └── app.js        # JS functionality
│
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── .gitignore            # Git ignore rules
```

---

## 🧪 Local Setup

```bash
# Clone the repo
git clone https://github.com/A22051694/Finance-Tracker-with-Python.git
cd Finance-Tracker-with-Python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts ctivate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver
```

---

## 🐳 Docker Setup (Coming Soon)

> Dockerfile and containerization instructions will be added soon.
> Docker Image: `xoxoi/finance-tracker:latest`

---

## ☁️ Azure Deployment

> This section will be updated once the project is deployed on Azure Web App (free tier).
> Azure URL: `finance-trackers.azurewebsites.net`

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Want to Contribute?

Pull requests and suggestions are welcome!  
Feel free to open an issue or submit a PR for improvements or bug fixes.

---

## 👨‍💻 Author

Made with ❤️ by [@A22051694](https://github.com/A22051694)
