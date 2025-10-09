from fastapi import FastAPI

app = FastAPI(title="ExpenseTracker")


@app.get("/")
def root():
    return {"message": "Expense Tracker API działa!"}

