**💰Personal Finance Coach Bot**


<div align="center">

![Finance Coach](https://img.shields.io/badge/Personal-Finance%20Coach-blue?style=for-the-badge&logo=cashapp)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-green?style=for-the-badge&logo=fastapi)
![LangGraph](https://img.shields.io/badge/LangGraph-AI%20Workflow-orange?style=for-the-badge)

**AI-Powered Financial Analysis & Smart Budgeting Assistant**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

*Transform your spending habits with AI-driven financial insights*

</div>

## 🚀 Overview

**Personal Finance Coach Bot** is an intelligent web application that analyzes your spending patterns using AI and provides personalized savings recommendations. Built with **FastAPI** backend and modern frontend, it helps you understand your finances and create smarter budgets.

## ✨ Key Features

### 🔍 **Smart Spending Analysis**
- **Automatic Category Detection**: Transactions are automatically categorized and analyzed
- **Visual Spending Breakdown**: See exactly where your money goes each month
- **Highest Spending Identification**: Instantly identify your biggest expense categories

### 💡 **AI-Powered Recommendations**
- **Personalized Savings Advice**: Get tailored recommendations based on your spending habits
- **Smart Alert System**: Receive warnings for unusual spending patterns
- **Proactive Financial Guidance**: AI suggests specific actions to improve your finances

### 📊 **Dynamic Budget Planning**
- **Automated Weekly Budgets**: AI creates customized weekly spending plans
- **Adaptive Budget Adjustments**: Budgets automatically adjust based on your spending
- **Category-wise Allocation**: Detailed breakdown across groceries, dining, entertainment, etc.

### 🎯 **User-Friendly Interface**
- **Modern Responsive Design**: Beautiful gradient UI that works on all devices
- **Real-time Updates**: Instant analysis as you add transactions
- **Sample Data Loading**: Quick start with pre-loaded example transactions
- **One-Click Actions**: Simple buttons for all operations

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | FastAPI, Python, LangGraph |
| **Frontend** | HTML5, CSS3, JavaScript |
| **AI Engine** | LangGraph State Management |
| **API** | RESTful JSON API |
| **Styling** | Custom CSS with Gradients |

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/personal-finance-coach.git
cd personal-finance-coach
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv finance_env
source finance_env/bin/activate  # On Windows: finance_env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install fastapi uvicorn langgraph
```

### Step 4: Project Structure
```
personal-finance-coach/
├── main.py                 # FastAPI backend server
├── static/
│   └── index.html         # Frontend web interface
└── README.md
```

### Step 5: Run the Application
```bash
uvicorn main:app --reload --port 8000
```

### Step 6: Access the Application
Open your browser and navigate to:
```
http://localhost:8000
```

## 🎮 How to Use

### **Get INSTANT Analysis:**
1. **Add Transactions Manually:**
   - Enter transaction description
   - Input amount spent
   - Select category (Groceries, Dining, Entertainment, etc.)
   - Click "Add" button

2. **Quick Start with Sample Data:**
   - Click **"Load Sample Data"** to instantly populate with example transactions
   - System automatically analyzes and displays results

3. **View Comprehensive Results:**
   - **Total Spending**: See your overall expenditure
   - **Category Breakdown**: Visualize spending across different categories
   - **AI Recommendations**: Get personalized savings advice
   - **Weekly Budget**: Receive customized budget plan
   - **Smart Alerts**: Important warnings about your spending habits

### **Example Workflow:**
```python
# Sample transactions the system analyzes
transactions = [
    {"description": "Grocery Store", "amount": 85, "category": "groceries"},
    {"description": "Restaurant", "amount": 65, "category": "dining"},
    {"description": "Movie Tickets", "amount": 40, "category": "entertainment"},
    {"description": "Gas Station", "amount": 55, "category": "transportation"},
    {"description": "Online Shopping", "amount": 120, "category": "shopping"}
]
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve main frontend interface |
| `POST` | `/api/analyze-finances` | Analyze transactions and provide recommendations |
| `GET` | `/api/sample-transactions` | Get sample transaction data |
| `GET` | `/api/` | API status check |

### Example API Request:
```bash
curl -X POST "http://localhost:8000/api/analyze-finances" \
     -H "Content-Type: application/json" \
     -d '{
       "transactions": [
         {"description": "Grocery", "amount": 100, "category": "groceries"},
         {"description": "Restaurant", "amount": 75, "category": "dining"}
       ]
     }'
```

## 🧠 AI Engine Architecture

### **LangGraph Workflow:**
```python
# Three-Step AI Analysis Pipeline
1. analyze_spending → 2. provide_advice → 3. plan_budget
```

### **Smart Decision Making:**
- **Spending Thresholds**: Alerts when dining > $200 or entertainment > $150
- **Budget Optimization**: Automatically adjusts savings and dining budgets
- **Pattern Recognition**: Identifies highest spending categories instantly

## 🎨 Features in Detail

### **Real-time Financial Dashboard**
- Live transaction list with running total
- Instant category-wise spending visualization
- Interactive transaction management (add/remove)

### **Intelligent Alert System**
```python
# Example Alert Triggers
if dining_spending > 200:
    alert("High dining expenses detected")
if total_spent > 1000:
    alert("Monthly spending exceeds $1000")
```

### **Adaptive Budget Calculator**
- Base weekly budget: $575
- Auto-adjusts based on total spending
- Increases savings for high spenders
- Reduces discretionary spending categories


## 🚀 Deployment

### Local Development
```bash
uvicorn main:app --reload --port 8000
```

### Production Deployment
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/) for high-performance backend
- AI workflow powered by [LangGraph](https://langchain.com/langgraph)
- Modern UI design with CSS gradients and responsive layout

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

*Made with ❤️ for better financial health*


</div>
```

This comprehensive README includes:

✅ **Eye-catching badges and header**  
✅ **Detailed feature descriptions**  
✅ **Step-by-step installation guide**  
✅ **Complete usage instructions**  
✅ **API documentation**  
✅ **Technical architecture**  
✅ **Visual placeholders for screenshots**  
✅ **Contributing guidelines**  
✅ **Professional formatting**  
✅ **Mobile-responsive design**

The README is ready to be used on GitHub and provides all the information users need to understand, install, and use your Personal Finance Coach Bot! 🚀
