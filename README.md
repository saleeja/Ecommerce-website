# Ecommerce Website (JustClick)

Django storefront with admin (Jazzmin), categories, products, and media uploads.

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ — admin at `/admin/`.

## Deploy on Render (free)

Hosting needs an account on your side; this repo is set up for [Render](https://render.com).

1. Push this repo to GitHub (`saleeja/Ecommerce-website`).
2. Sign up at [render.com](https://render.com) and connect GitHub.
3. **New → Blueprint** → select this repo (uses `render.yaml`), or **New → Web Service**:
   - **Build command:** `./build.sh`
   - **Start command:** `gunicorn ecomsite.wsgi:application --bind 0.0.0.0:$PORT`
   - **Environment:** `DJANGO_DEBUG=false`, `SECRET_KEY` (generate a random value), `ALLOWED_HOSTS=.onrender.com`
4. After deploy, open the `*.onrender.com` URL.

**Notes**

- Product images in `media/` are in git and deploy with the app.
- SQLite is fine for a demo; for a live store, add a Render PostgreSQL database and set `DATABASE_URL` (migrations run in `build.sh`).
- New admin uploads on the free tier may not persist across redeploys unless you use Postgres + object storage.
