# 🧠 OceanAI DocGen – AI Document & PPT Generator

OceanAI DocGen is a Flask-based intelligent document creation platform powered by Google Gemini (via LangChain). It lets you generate structured content section-by-section, refine content with custom instructions, store projects in a database, and export everything into clean DOCX and PPTX files. Built as a backend-focused project with a neat Bootstrap UI.

---

## ✨ Features

- 🔐 User authentication (Login / Signup)
- 📁 Project creation with sections
- 🤖 AI content generation (Gemini + LangChain)
- ✨ Section refinement with custom instructions
- 📝 Feedback & comments per section
- 📤 Export entire project as DOCX or PPTX

---

## 🧱 Tech Stack

**Backend**
- Python 3, Flask, Flask-Login, Flask-CORS
- SQLAlchemy + SQLite
- LangChain + langchain_google_genai
- python-docx, python-pptx

**Frontend**
- HTML, Jinja2, Bootstrap 5
- Vanilla JavaScript (static/main.js)

**Other**
- .env for GOOGLE_API_KEY
- Cloudflare Tunnel (optional)

---

## 📁 Project Structure

oceanai/
├── backend/
│ ├── app.py # Main Flask application
│ ├── auth.py # Login / signup logic
│ ├── database.py # SQLAlchemy instance
│ ├── models.py # User, Project, Section models
│ ├── requirements.txt # Backend dependencies
│ │
│ ├── routes/
│ │ ├── project_routes.py # Create project, generate content, list sections
│ │ ├── refine_routes.py # Refining, comments, feedback
│ │ ├── export_routes.py # DOCX / PPTX download
│ │ └── setup_routes.py # Helper endpoints
│ │
│ ├── services/
│ │ ├── llm_service.py # Gemini + LangChain prompt logic
│ │ ├── project_service.py # Content generation & project logic
│ │ ├── refine_service.py # Refinement logic
│ │ └── export_service.py # DOCX / PPTX formatting
│ │
│ ├── templates/
│ │ ├── login.html
│ │ ├── signup.html
│ │ └── index.html # Dashboard
│ │
│ └── static/
│ └── main.js # Frontend JS
│
├── folderstructure.py # Automatically generates backend folder layout
├── requirements.txt
└── README.md


---

## 🔍 What folderstructure.py Does

`folderstructure.py` is a developer convenience utility that auto-creates the backend folder layout. It generates:

- backend/
- backend/routes/
- backend/services/
- backend/templates/
- backend/static/

And optional starter files like:
- app.py  
- database.py  
- models.py  
- routes/__init__.py  
- services/__init__.py  

It is only used during initial setup—not during runtime.

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
git clone https://github.com/meghavardhan-git/OceanAI-DocGen.git

cd OceanAI-DocGen


### 2️⃣ Create a virtual environment (Windows)


python -m venv venv
venv\Scripts\activate


macOS/Linux:


source venv/bin/activate


### 3️⃣ Install backend dependencies


cd backend
pip install -r requirements.txt


### 4️⃣ Create .env file
Inside backend/:


GOOGLE_API_KEY=your_gemini_api_key_here


---

## ▶️ Running the App

From project root:


cd backend
python -m backend.app


or


python app.py


Visit:
- http://127.0.0.1:5000 → Login  
- /signup-page → Signup  
- /dashboard → After login  

---

## 📝 Git Commands



git add .
git commit -m "Describe your change"
git push


---

## 👤 Author

**Meghavardhan T**  
AI & Backend Developer  
GitHub: https://github.com/meghavardhan-git
