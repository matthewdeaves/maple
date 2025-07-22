# Maple Django Blog

A simple Django blog application for learning Django fundamentals.

## Setup Commands (One-time)

I develop on Ubuntu, so this is tested on that environment.

### Initial Project Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Update pip
python3 -m pip install -U pip

# Install Django
python3 -m pip install Django

# Install Pillow (for ImageField support)
pip install Pillow

# Create Django project
django-admin startproject maple

# Create Django app
cd maple/
python3 manage.py startapp posts
```

### Initial Database Setup
```bash
# Run initial migrations
python3 manage.py migrate

# Create superuser for admin
python3 manage.py createsuperuser
```

## Daily Development Commands

### Starting Development
```bash
# Activate virtual environment (always do this first)
source .venv/bin/activate

# Start development server
cd maple/
python3 manage.py runserver
```

### Database Operations
```bash
# After model changes - generate migration files
python3 manage.py makemigrations

# Apply migrations to database
python3 manage.py migrate

# Open Django shell for database queries
python3 manage.py shell
```

### Package Management
```bash
# Update pip
python3 -m pip install -U pip

# Update Pillow
pip install -U Pillow

# Install new packages
pip install package_name

# See installed packages
pip list
```

### Creating New Projects/Apps
```bash
# Create new Django project (from parent directory)
django-admin startproject project_name

# Create new app within existing project (from project directory)
python3 manage.py startapp app_name

# Don't forget to add new apps to INSTALLED_APPS in settings.py
```

## Important Notes

- **Always activate the virtual environment** with `source .venv/bin/activate` before running any Python/Django commands
- **Run migrations** after any model changes: `makemigrations` then `migrate`
- **Server runs on** http://127.0.0.1:8000/ by default
- **Admin panel** available at http://127.0.0.1:8000/admin/
- **Stop server** with Ctrl+C
- **Deactivate virtual environment** with `deactivate`
- **Add new apps** to `INSTALLED_APPS` in `settings.py` after creating them

## Project Structure
- `maple/` - Main Django project directory
- `posts/` - Blog posts Django app
- `media/` - User uploaded files (images)
- `static/` - CSS, JavaScript files
- `.venv/` - Virtual environment (not in git)