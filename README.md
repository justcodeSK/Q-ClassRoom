# Q CLASSROOM

## Project Overview
**Q CLASSROOM** is a Learning Management System (LMS) designed to make the teaching and learning process more efficient.  
It allows **students** to view their course syllabus, subjects, and assigned teachers, while **teachers** can upload video lessons and manage students.  
The platform was developed for **QUEST Innovative Solutions** to overcome the limitations of sharing study materials through platforms like Gmail Drive.  

This centralized system simplifies video sharing, syllabus management, and communication between **admins**, **staff**, **teachers**, and **students**.

---

## Features

### 1. **Admins**
- Approve new staff, teachers, and students.
- Delete teachers, students, staff, and uploaded videos.

### 2. **Staff**
- Add new syllabus content.
- Edit staff details.

### 3. **Teachers**
- Upload new video lessons.
- View assigned staff.
- Edit student and teacher details.

### 4. **Students**
- View syllabus.
- Watch video lessons.
- See assigned teachers and subjects.

---

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Backend:** Django (Python)  
- **Database:** SQLite3  
- **IDE:** VS Code

---

## System Requirements

### Hardware
- Processor: Minimum 2.0 GHz Pentium or higher
- RAM: 2 GB or higher
- Storage: 500 MB free space

### Software
- **VS Code** (or any Python IDE)
- **Python 3.8+**
- **SQLite3** (bundled with Python)
- **Git** (optional for version control)

---

## Setup & Installation Guide

To make running this project easier, a `requirements.txt` file has been included.  
This file was generated using `pip freeze` and contains all the **exact versions** of dependencies used in this Django project.  

Follow these steps:

### 1. Create Project Folder (Linux)
```bash
mkdir Qclassroom
cd Qclassroom
```
### 2. Create Virtual Environment (On Windows)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```
### On Linux / macOS
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```
### 3. Install Dependencies
- Once inside the virtual environment, install required packages:
```bash
pip install -r requirements.txt
```
### 4. Run the Project
- Navigate to the Django project folder (qproject) and run:
```bash
python manage.py runserver
```
### Notes
Always activate the virtual environment before running the project.
To deactivate:
```bash
deactivate
```
If any new packages are added, update requirements.txt with:
```bash
pip freeze > requirements.txt
```
