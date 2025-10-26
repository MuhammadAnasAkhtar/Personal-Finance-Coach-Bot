from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Dict, List, TypedDict
from langgraph.graph import StateGraph, END
import os

app = FastAPI(title="Personal Finance Coach API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (for the frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic models for request/response
class Transaction(BaseModel):
    description: str
    amount: float
    category: str

class FinanceRequest(BaseModel):
    transactions: List[Transaction]

class FinanceResponse(BaseModel):
    total_spent: float
    spending_patterns: Dict
    savings_recommendations: List[str]
    weekly_budget: Dict
    alerts: List[str]

# Finance Coach Logic
class FinanceState(TypedDict):
    transactions: List[Dict]
    spending_patterns: Dict
    savings_recommendations: List[str]
    weekly_budget: Dict
    alerts: List[str]
    total_spent: float

def spending_analyzer(state: FinanceState):
    transactions = state["transactions"]
    
    categories = {}
    total = 0
    
    for transaction in transactions:
        category = transaction.get("category", "other")
        amount = transaction.get("amount", 0)
        categories[category] = categories.get(category, 0) + amount
        total += amount
    
    patterns = {
        "total_spent": total,
        "category_breakdown": categories,
        "highest_spending": max(categories.items(), key=lambda x: x[1])[0] if categories else "None"
    }
    
    return {"spending_patterns": patterns, "total_spent": total}

def savings_advisor(state: FinanceState):
    patterns = state["spending_patterns"]
    categories = patterns["category_breakdown"]
    
    recommendations = []
    alerts = []
    
    if categories.get("dining", 0) > 200:
        recommendations.append("Reduce dining out expenses by cooking at home more")
        alerts.append("High dining expenses detected")
    
    if categories.get("entertainment", 0) > 150:
        recommendations.append("Consider free entertainment options")
    
    if patterns["total_spent"] > 1000:
        recommendations.append("Create emergency fund with 20% of monthly income")
        alerts.append("Monthly spending exceeds $1000")
    
    if not recommendations:
        recommendations.append("Good spending habits! Consider increasing investments")
    
    return {"savings_recommendations": recommendations, "alerts": alerts}

def budget_planner(state: FinanceState):
    total_spent = state["total_spent"]
    
    weekly_budget = {
        "groceries": 150,
        "dining": 75,
        "entertainment": 50,
        "transportation": 100,
        "savings": 200,
        "total_weekly": 575
    }
    
    if total_spent > 1200:
        weekly_budget["savings"] += 50
        weekly_budget["dining"] = max(50, weekly_budget["dining"] - 25)
    
    return {"weekly_budget": weekly_budget}

# Build graph
finance_builder = StateGraph(FinanceState)
finance_builder.add_node("analyze_spending", spending_analyzer)
finance_builder.add_node("provide_advice", savings_advisor)
finance_builder.add_node("plan_budget", budget_planner)
finance_builder.set_entry_point("analyze_spending")
finance_builder.add_edge("analyze_spending", "provide_advice")
finance_builder.add_edge("provide_advice", "plan_budget")
finance_builder.add_edge("plan_budget", END)
finance_graph = finance_builder.compile()

# API Routes
@app.get("/")
async def serve_frontend():
    return FileResponse('static/index.html')

@app.get("/api/")
async def root():
    return {"message": "Personal Finance Coach API"}

@app.post("/api/analyze-finances", response_model=FinanceResponse)
async def analyze_finances(request: FinanceRequest):
    try:
        # Convert Pydantic transactions to dict
        transactions_dict = [transaction.dict() for transaction in request.transactions]
        
        result = finance_graph.invoke({
            "transactions": transactions_dict,
            "spending_patterns": {},
            "savings_recommendations": [],
            "weekly_budget": {},
            "alerts": [],
            "total_spent": 0.0
        })
        
        return FinanceResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

# Sample data endpoint
@app.get("/api/sample-transactions")
async def get_sample_transactions():
    return {
        "transactions": [
            {"description": "Grocery Store", "amount": 85, "category": "groceries"},
            {"description": "Restaurant", "amount": 65, "category": "dining"},
            {"description": "Movie Tickets", "amount": 40, "category": "entertainment"},
            {"description": "Gas Station", "amount": 55, "category": "transportation"},
            {"description": "Online Shopping", "amount": 120, "category": "shopping"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)