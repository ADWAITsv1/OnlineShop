from flask import Flask, render_template, request, redirect, url_for, session, flash
import json, os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")  # set in .env for production

DATA_FILE = os.path.join("data", "products.json")

def load_products():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    products = load_products()
    cart_count = sum(item["qty"] for item in session.get("cart", []))
    return render_template("index.html", products=products, cart_count=cart_count)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        session["user"] = email or "guest@example.com"
        flash(f"Logged in as {session['user']}")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    products_by_id = {p["id"]: p for p in load_products()}
    # enrich items for display
    for item in cart:
        p = products_by_id.get(item["id"])
        if p:
            item["name"] = p["name"]
            item["price"] = p["price"]
            item["image"] = p.get("image", "")
            item["subtotal"] = round(item["qty"] * item["price"], 2)
    total = round(sum(i.get("subtotal", 0) for i in cart), 2)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/add/<pid>", methods=["POST"])
def add_to_cart(pid):
    cart = session.get("cart", [])
    for it in cart:
        if it["id"] == pid:
            it["qty"] += 1
            break
    else:
        cart.append({"id": pid, "qty": 1})
    session["cart"] = cart
    flash("Added to cart")
    return redirect(url_for("home"))

@app.route("/clear-cart", methods=["POST"])
def clear_cart():
    session.pop("cart", None)
    flash("Cart cleared")
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(port=8502, debug=True)
