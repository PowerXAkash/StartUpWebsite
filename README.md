# FastAPI Project

A minimal FastAPI project scaffold.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000` in your browser.

## API endpoints

- `GET /` – health check message
- `GET /items/{item_id}` – read item
- `POST /items/` – create item using JSON body
