# 🎲 BoardRadar

**BoardRadar** is a web-based board game collection tracker built to help users browse, manage, and discover board games. It provides features such as rating games, adding them to a wishlist, downloading rule PDFs, and more. Designed to be responsive and user-friendly, BoardRadar brings your board game library to your fingertips.

---

## 📌 Table of Contents

- [Features](#features)
- [Screens](#screens)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

---

## ✅ Features

- 🏠 **Homepage** displaying all games as cards with:
  - Game title
  - Game image
  - Game rating
  - "View Details" button

- 🔐 **Authentication System**
  - User Signup
  - User Login
  - Session management

- 📄 **Game Details Page**
  - Detailed description
  - Game image
  - 1–5 star rating system
  - "Add to Wishlist" functionality
  - PDF download for rulebook

- 📝 **Wishlist**
  - Logged-in users can save games to their wishlist

- 📱 **Responsive Design**
  - Fully functional across all screen sizes

---

## 🖥️ Screens

1. `index.html`: Homepage with game listing and search bar
2. `login.html`: Login form with validation
3. `signup.html`: Signup form with validation
4. `details.html`: Game details page

---

## 🛠️ Tech Stack

### Frontend:
- HTML5
- CSS3
- JavaScript (Vanilla)
- Jinja2 Templating (via Flask)

### Backend:
- Python (Flask Framework)
- SQLite (for local development DB)

### Other Tools:
- Git & GitHub (team collaboration)
- Bootstrap (for some UI components)
- PDF files for rule downloads
- Flask-Login (for user sessions)

---

## 📁 Project Structure

BoardRadar/ │ ├── static/ │ ├── css/ │ ├── js/ │ └── images/ │ ├── templates/ │ ├── index.html │ ├── login.html │ ├── signup.html │ └── details.html │ ├── app.py ├── models.py ├── database.db ├── README.md └── requirements.txt

yaml
Copy
Edit

---

## 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/BoardRadar.git
cd BoardRadar


---









