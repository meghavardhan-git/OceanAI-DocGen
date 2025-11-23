🧠 OceanAI DocGen – AI Document & PPT Generator

OceanAI DocGen is a Flask-based intelligent document creation platform powered by Google Gemini (via LangChain). It lets you generate structured content section-by-section, refine content with custom instructions, store projects in a database, and export everything into clean DOCX and PPTX files. Built as a backend-focused project with a neat Bootstrap UI.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Version](https://img.shields.io/badge/version-1.0.0-orange)

✨ Features

- 🔐 User authentication (Login / Signup)
- 📁 Project creation with sections
- 🤖 AI content generation (Gemini + LangChain)
- ✨ Section refinement with custom instructions
- 📝 Feedback & comments per section
- 📤 Export entire project as DOCX or PPTX

⚙️ Setup & Installation

### 1️⃣ Clone the repository
git clone https://github.com/meghavardhan-git/OceanAI-DocGen.git

cd OceanAI-DocGen

### 2️⃣ Create a virtual environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4️⃣ Create .env file
Inside backend/: 

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

▶️ Running the App

From project root:

```bash
cd backend
python -m backend.app
```

or

```bash
python app.py
```

Visit:
- [http://127.0.0.1:5000](http://127.0.0.1:5000) → Login  
- /signup-page → Signup  
- /dashboard → After login
## 📸 Screenshots
# Signup Page
<img width="1915" height="1048" alt="signup" src="https://github.com/user-attachments/assets/b501dd18-803f-43a1-846c-f3970a6423a8" />
# Login Page
<img width="1915" height="1047" alt="login" src="https://github.com/user-attachments/assets/d4d09ed2-7d75-4a8c-adc1-0f8d3c81e262" />
# Dashboard
<img width="1913" height="1046" alt="dashboard" src="https://github.com/user-attachments/assets/87c78ca5-411b-4c71-a1d3-2c6b96dc929c" />
# Topic Based Content Generation
<img width="1919" height="1046" alt="generatedtopic" src="https://github.com/user-attachments/assets/fdc287ad-525b-4dd0-bc8a-4d3b67d584cf" />
# Content Refinement
<img width="1888" height="915" alt="refinedcontent" src="https://github.com/user-attachments/assets/81d5402b-e018-4fee-9cf8-429b89369894" />
# FeedBack For Like/Dislike 
<img width="1880" height="1042" alt="feedback" src="https://github.com/user-attachments/assets/31196910-9fd1-4cef-9453-93b19c62d9fa" />
# Comment
<img width="1919" height="845" alt="comment" src="https://github.com/user-attachments/assets/951a8e74-13eb-4a75-a886-30a35be11e3a" />
# Saved Comment
<img width="1620" height="465" alt="savedcomment" src="https://github.com/user-attachments/assets/03e73ec5-925b-47f1-8f81-9df5745f7c8e" />
# Download as Docx/PPT
<img width="1919" height="724" alt="downloaddocx" src="https://github.com/user-attachments/assets/73778863-a798-4998-8004-a1e0f965f1c2" />
# Downloaded Docx
<img width="1919" height="724" alt="downloaddocx" src="https://github.com/user-attachments/assets/bc7ff4d3-deb7-4c22-a202-0303ae23fbcd" />

## 🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

👤 Author

**Meghavardhan T**  
AI & Backend Developer  
GitHub: [meghavardhan-git](https://github.com/meghavardhan-git)
