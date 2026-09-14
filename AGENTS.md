# AGENTS.md

Django 5.2 (Python 3.11) "Learning Journal" app — a beginner Learning-Log-style tutorial project. The Django project package is `config`; the single app is `mypett`. Managed with **uv** (`uv.lock` is the source of truth; `requirements.txt` exists only for the PythonAnywhere deployment and is regenerated with `uv export --format requirements-txt -o requirements.txt`).

## Commands

Run everything through uv's venv (never bare `python`/`manage.py`):

```sh
uv run python manage.py runserver      # dev server
uv run python manage.py check          # quick sanity check; catches broken URL config
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py test           # tests use unittest, NOT pytest
```

## Gotchas

- **`mypett/urls.py` currently defines `urlpetterns` (misspelled) instead of `urlpatterns`.** This breaks the whole app: `manage.py check` and `runserver` fail with `ImproperlyConfigured: The included URLconf does not appear to have any patterns in it`. Rename the variable to `urlpatterns` before doing anything else.
- **No pytest installed.** `.vscode/settings.json` sets the `unittest` runner (`python.testing.pytestEnabled: false`). Write discovery-style `*test.py` files and use the unittest runner.
- **`db.sqlite3` is committed to git** (verified via `git ls-files`). Don't store secrets there and be cautious about committing dev-data / schema churn.
- **Two ignore files exist**: `.gitignore` (authoritative) and `.gitignore-2`. `.venv` and `.vscode` are ignored. The working tree currently has a modified `.gitignore` and untracked `.gitignore-2`, `.vscode/`.
- **`mypett/models.py` `Entry.__str__`** slices the text (`self.text[:50]...`) and always appends an ellipsis. `research+howToos_django.md` records a refinement (append the ellipsis only when >50 chars) and a past `'>' not supported between 'str' and 'int'` bug — read that file before editing the model.
- **No CI, no lint/format config.** `manage.py check` is the primary verification path.

## Notes

- Root `.md` files (`research+howToos_django.md`, `issues_django.md`) are tracked learning/scratch notes, not authoritative docs. `README.md` is empty. `main.py` is a stub.
