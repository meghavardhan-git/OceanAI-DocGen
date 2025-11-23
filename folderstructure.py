import os

# Root folder
root = "backend"

# Sub-folders
folders = [
    f"{root}",
    f"{root}/services",
    f"{root}/routes"
]

# Files to create with empty or template content
files = {
    f"{root}/app.py": "",
    f"{root}/database.py": "",
    f"{root}/models.py": "",
    f"{root}/auth.py": "",
    
    f"{root}/services/llm_service.py": "",
    f"{root}/services/project_service.py": "",
    f"{root}/services/refine_service.py": "",
    
    f"{root}/routes/project_routes.py": "",
    f"{root}/routes/refine_routes.py": "",
    
    f"{root}/requirements.txt": "",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("Backend folder structure created successfully!")
