# 🌸 Iris Predictor

A Django web application that predicts the species of an Iris flower based on its measurements, using a trained Random Forest model.

---

## 📋 Description

This project exposes a web form and a REST API endpoint to classify Iris flowers into one of three species:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

It uses a **RandomForestClassifier** trained on the classic Iris dataset from scikit-learn.

---

## 💻 Local Installation

### 1. Clone the repository
```bash
git clone https://github.com/Kenkyoo/django-iris-predictor.git
cd mlapp
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train and save the model
```bash
python train.py
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

---

## 🐳 Docker

### Build the image
```bash
docker build -t mlapp .
```

### Run the container
```bash
docker run -p 8000:8000 mlapp
```

Visit `http://localhost:8000` in your browser.

---

## 🚀 Deploy on Render

1. Push your code to **GitHub** (make sure `predictor/model/iris_rf.joblib` is included).
2. Go to [render.com](https://render.com) and create a new **Web Service**.
3. Connect your GitHub repository.
4. Render will detect the `Dockerfile` automatically.
5. Click **Deploy**.

---

## 🔌 API Usage

**Endpoint:** `POST /api/predict/`

**Content-Type:** `application/json`

### Request
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Response
```json
{
  "class_index": 0,
  "class_name": "setosa",
  "probabilities": {
    "setosa": 0.980,
    "versicolor": 0.015,
    "virginica": 0.005
  }
}
```

### Example with curl
```bash
curl -X POST http://localhost:8000/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

---

## 🛠 Tech Stack

- Python 3.12
- Django
- scikit-learn
- Gunicorn
- Docker
- Bulma CSS
