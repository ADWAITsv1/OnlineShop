# 🛍️ OnlineShop  
**A Minimal Flask E-Commerce Web App**

OnlineShop is a simple full-stack prototype built using **Flask**, featuring a responsive dark-theme UI, local image assets, and a dynamic shopping cart system.  
It demonstrates core web-app architecture — templates, routing, session storage, and JSON-based product management.

---

## 🧠 Features

- 🗂️ Product catalog loaded from local JSON  
- 🖼️ Local product images served via `/static/images`  
- 🛒 Add-to-cart functionality using Flask sessions  
- 🔐 Simple login form (demo only — no database yet)  
- ⚡ Responsive dark-theme UI  

---

## 📸 Preview

### 🏠 Product Catalog
![OnlineShop Catalog](static/Screenshot%202025-11-03%20at%2016.31.33.png)

### 🔐 Login Page
![OnlineShop Login](static/Screenshot%202025-11-03%20at%2016.36.55.png)

---

## 🧱 Tech Stack

| Layer | Technology |
|:------|:------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML, CSS, Jinja2 Templates |
| **Data** | JSON file (`data/products.json`) |
| **Session Handling** | Flask `session` |
| **Styling** | Custom dark-theme CSS |

---

## ⚙️ Setup & Run

```bash
# 1️⃣ Clone this repository
git clone https://github.com/ADWAITsv1/OnlineShop.git
cd OnlineShop

# 2️⃣ Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run Flask app
python app.py


Then open your browser → http://127.0.0.1:8502

🗂️ Project Structure
OnlineShop/
├── app.py
├── data/
│   ├── products.json
├── static/
│   ├── onlineshop.css
│   ├── images/
│   │   ├── bento.jpg
│   │   ├── onigiri.jpg
│   │   ├── sandwich.jpeg
│   │   └── milk.png
│   ├── Screenshot 2025-11-03 at 16.31.33.png
│   └── Screenshot 2025-11-03 at 16.36.55.png
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── cart.html
│   └── login.html
└── requirements.txt

🧩 Future Improvements

Integrate SQLite/MySQL for persistent users & products

Add checkout and order management

Include image uploads and user authentication

REST API for mobile integration

👤 Author

Adwait Varekar
📍 Tokyo, Japan
🌐 linkedin.com/in/adwait-varekar

💻 github.com/ADWAITsv1