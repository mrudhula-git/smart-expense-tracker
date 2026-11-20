# Smart Expense Tracker

A clean, responsive expense tracking dashboard built with **Django**. Add your daily expenses, see where your money goes by category, and keep track of monthly spending at a glance.

<!-- Add a screenshot: save it as screenshot.png in the project root and uncomment the line below -->
<!-- ![Dashboard](screenshot.png) -->

## Features

- **Dashboard overview** with total spent, this month's spending, number of transactions and top spending category
- **Add expenses** with title, amount and category (Food, Travel, Shopping, Bills) and form validation
- **Category breakdown** with an interactive doughnut chart and per-category amounts and percentages
- **Transactions table** with colour-coded category badges, newest first
- **Live search** to filter expenses instantly
- **Safe delete** using a POST request with a confirmation prompt
- **Responsive design** that works on desktop and mobile

## Tech Stack

| Layer     | Technology                                  |
|-----------|---------------------------------------------|
| Backend   | Python 3, Django 6                          |
| Database  | SQLite                                      |
| Frontend  | HTML, CSS, Bootstrap 5, Bootstrap Icons     |
| Charts    | Chart.js                                    |

## Project Structure

```
expense_tracker/
├── manage.py
├── expense_tracker/        # Project settings and root URLs
│   ├── settings.py
│   └── urls.py
└── tracker/                # Main app
    ├── models.py           # Expense model
    ├── forms.py            # Expense form and validation
    ├── views.py            # Dashboard and delete views
    ├── urls.py
    └── templates/
        └── dashboard.html  # Dashboard UI
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/mrudhula-git/smart-expense-tracker.git
cd smart-expense-tracker

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install Django
pip install django

# 4. Create the database
python manage.py migrate

# 5. Start the server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

> The page loads Bootstrap, Chart.js and fonts from a CDN, so an internet connection is needed for the full design.

### Admin panel (optional)

```bash
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/.

## Usage

1. Fill in the **Add expense** form (title, amount, category) and click **Add expense**.
2. Watch the summary cards and the category chart update.
3. Use the search box to find a transaction, or click the bin icon to delete one.

## Future Improvements

- Edit existing expenses
- Choose the expense date and filter by month
- User login so each person sees only their own expenses
- Export to CSV
- Monthly trend chart and budget limits

## License

This project is for learning and personal use.
