# AI Hub Portal

A skeletal Django application illustrating the foundations of a modular AI-enabled portal. It features secure authentication, a dashboard for departments, and hooks for future AI assistants.

## Setup

```bash
# Clone repository
$ git clone <repo-url>
$ cd myfirstbot

# Create virtual environment
$ python -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run database migrations
$ python manage.py migrate

# Start development server
$ python manage.py runserver
```

## Usage

1. Visit `http://127.0.0.1:8000/login/` and sign in using a superuser account.
2. Create departments from `/departments/new/`.
3. Extend AI settings and OAuth providers via `portal/settings.py` and future configuration modules.

## Documentation

To build HTML documentation from docstrings:

```bash
make docs
```
Generated files appear under `docs/build/html`.

## Contributing

Pull requests are welcome. Please ensure code is well-tested and documented. For major changes, open an issue to discuss the proposed feature.

## Deployment

- **Local**: use `python manage.py runserver`.
- **Docker**: build using the provided `Dockerfile` (TODO).
- **Azure**: deploy to Azure Web Apps or Azure Static Web Apps with the included configurations (TODO).

## License

MIT
