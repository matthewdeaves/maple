# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 5.2.4 blog application called "Maple" with a simple post management system. The project uses SQLite as the database and includes basic static file handling for CSS/JS and media file uploads.

## Development Commands

### Server Management
- **Start development server**: `python maple/manage.py runserver`
- **Create migrations**: `python maple/manage.py makemigrations`
- **Apply migrations**: `python maple/manage.py migrate`
- **Create superuser**: `python maple/manage.py createsuperuser`
- **Django shell**: `python maple/manage.py shell`

### Testing
- **Run tests**: `python maple/manage.py test`
- **Run specific app tests**: `python maple/manage.py test posts`

## Project Structure

The project follows standard Django conventions with a nested directory structure:

```
maple/
├── maple/                    # Project root directory
│   ├── manage.py            # Django management script
│   ├── db.sqlite3          # SQLite database
│   ├── maple/              # Main Django project package
│   │   ├── settings.py     # Project settings
│   │   ├── urls.py         # Main URL configuration
│   │   ├── views.py        # Homepage and about views
│   │   └── wsgi.py/asgi.py # WSGI/ASGI applications
│   ├── posts/              # Posts Django app
│   │   ├── models.py       # Post model definition
│   │   ├── views.py        # Post list and detail views
│   │   ├── urls.py         # Posts URL patterns
│   │   └── templates/      # Post-specific templates
│   ├── templates/          # Global templates (home.html, about.html, layout.html)
│   └── static/             # Static files (CSS, JS)
└── media/                  # User-uploaded files
```

## Architecture Notes

### URL Structure
- Root (`/`): Homepage view
- `/about/`: About page
- `/posts/`: Post listing
- `/posts/<slug>/`: Individual post pages
- `/admin/`: Django admin interface

### Models
- **Post model** (`posts/models.py`): Main content model with title, body, slug, created timestamp, and banner image field

### Templates
- Uses Django template inheritance with `layout.html` as base template
- Post templates located in `posts/templates/posts/`
- Global templates in `templates/` directory

### Static Files
- CSS files in `static/css/`
- JavaScript files in `static/js/` 
- Media uploads stored in `media/` directory
- Static files served during development via `django.conf.urls.static.static()`

### Database
- Uses SQLite (`db.sqlite3`) for development
- Post model includes ImageField for banner images with `'fallback.png'` default

## Key Files to Understand

- `maple/settings.py`: Contains `INSTALLED_APPS` with 'posts' app, static/media file configuration
- `maple/urls.py`: Main URL routing including posts app via `include('posts.urls')`
- `posts/models.py`: Simple Post model with slug-based URLs
- `posts/views.py`: Function-based views for post listing and detail pages