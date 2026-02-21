
# Ниже примеры кода - они не выполняют всех требований!
# Вы можете использовать их в своей домашней работе для большего понимания происходящего.

# ==================================================
# Пример запуска FastAPI
# ==================================================
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "ok"}

# После в консоли вы должны прописать команду:
# uvicorn backend.main:app --reload

# ==================================================
# Чтение CSV файла (backend)
# ==================================================
import pandas as pd

def load_data():
    return pd.read_csv("data.csv")

def save_data(df):
    df.to_csv("data.csv", index=False)


# ==================================================
# Pydantic-модель для валидации данных
# ==================================================
from pydantic import BaseModel
from datetime import date

class RecordCreate(BaseModel):
    date: date
    category: str
    value: float
    comment: str | None = None


# ==================================================
# Пример GET эндпоинта
# ==================================================
@app.get("/records")
def get_records():
    df = load_data()
    return df.to_dict(orient="records")


# ==================================================
# Пример POST эндпоинта (добавление записи)
# ==================================================
@app.post("/records")
def add_record(record: RecordCreate):
    # загрузка CSV
    # генерация id
    # добавление строки
    # сохранение файла
    return record


# ==================================================
# Пример DELETE эндпоинта
# ==================================================
from fastapi import HTTPException

@app.delete("/records/{record_id}")
def delete_record(record_id: str):
    # найти запись по id
    # если нет — вернуть 404
    # удалить и сохранить CSV
    return {"deleted_id": record_id}


# ==================================================
# Streamlit: получение данных через API
# ==================================================
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

response = requests.get(f"{API_URL}/records")
data = response.json()


# ==================================================
# Streamlit: таблица
# ==================================================
import streamlit as st
import pandas as pd

df = pd.DataFrame(data)
st.dataframe(df)


# ==================================================
# Streamlit: форма добавления записи
# ==================================================
import streamlit as st
import pandas as pd

with st.form("add_record"):
    date = st.date_input("Date")
    category = st.text_input("Category")
    value = st.number_input("Value", min_value=0.0)
    submit = st.form_submit_button("Add")


# ==================================================
# Streamlit: удаление записи
# ==================================================
import streamlit as st
import requests

record_id = st.text_input("ID to delete")

if st.button("Delete"):
    r = requests.delete(f"{API_URL}/records/{record_id}")


# ==================================================
# Streamlit: простой график
# ==================================================
import streamlit as st
import pandas as pd

if not df.empty:
    st.line_chart(df, x="date", y="value")
