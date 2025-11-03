# 🛍️ OnlineShop  
**A Minimal Flask E-Commerce Web App**

OnlineShop is a full-stack mini e-commerce prototype built using **Flask**, featuring a clean dark UI, dynamic cart system, and JSON-based product catalog.  
It demonstrates essential web architecture: templating, session handling, and static asset management — perfect for learning or portfolio showcase.

---

## ✨ Features

- 🗂️ Dynamic product catalog loaded from `products.json`  
- 🖼️ Local image assets under `/static/images/`  
- 🛒 Add-to-cart and session-based storage  
- 🔐 Simple login demo (no DB yet — for UX demonstration)  
- ⚡ Responsive dark-theme design built with pure CSS  

---

## 📸 App Preview

### 🔐 Login Page
![Login Page](static/Screenshot%202025-11-03%20at%2017.14.06.png)

### 🏠 Product Catalog
![Product Catalog](static/Screenshot%202025-11-03%20at%2017.14.33.png)

### ➕ Add to Cart
![Add to Cart](static/Screenshot%202025-11-03%20at%2017.14.47.png)

### 🛒 Cart Page
![Cart Page](static/Screenshot%202025-11-03%20at%2017.15.02.png)

---

## 🧱 Tech Stack

| Layer | Technology |
|:------|:------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML, CSS, Jinja2 Templates |
| **Data Source** | JSON (`data/products.json`) |
| **Session Handling** | Flask `session` |
| **Styling** | Custom dark-theme CSS |

---

## ⚙️ Setup & Run

```bash
# 1️⃣ Clone this repository
git clone https://github.com/ADWAITsv1/OnlineShop.git
cd OnlineShop

# 2️⃣ Create virtual environment
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