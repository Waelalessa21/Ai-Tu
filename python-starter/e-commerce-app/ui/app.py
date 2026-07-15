import uuid
from pathlib import Path

import streamlit as st

from models.cart import Cart
from models.product import Product
from payments.credit_card import CreditCard
from payments.paypal import PayPal
from services.catalog import ProductCatalog
from services.order_service import OrderService
from storage.json_storage import JsonStorage

BASE_DIR = Path(__file__).parent.parent

catalog = ProductCatalog(JsonStorage(BASE_DIR / "data" / "products.json"))
order_service = OrderService(JsonStorage(BASE_DIR / "data" / "orders.json"))

if "cart" not in st.session_state:
    st.session_state.cart = Cart()

st.title("Online Store")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Shop", "Cart", "Checkout", "Orders", "Admin"]
)

with tab1:
    st.subheader("Products")
    products = catalog.get_all()
    if not products:
        st.write("No products yet. Add some in the Admin tab.")
    for product in products:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(
                f"**{product.name}** — ${product.price:.2f} ({product.stock} in stock)"
            )
        with col2:
            if st.button("Add", key=f"add_{product.id}"):
                st.session_state.cart.add(product)
                st.success(f"Added {product.name}")

with tab2:
    st.subheader("Your Cart")
    if not st.session_state.cart.items:
        st.write("Cart is empty.")
    else:
        for item in st.session_state.cart.items:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(
                    f"{item.product.name} x{item.quantity} — ${item.subtotal():.2f}"
                )
            with col2:
                if st.button("Remove", key=f"remove_{item.product.id}"):
                    st.session_state.cart.remove(item.product.id)
                    st.rerun()
        st.write(f"**Total: ${st.session_state.cart.total():.2f}**")

with tab3:
    st.subheader("Checkout")
    if not st.session_state.cart.items:
        st.write("Cart is empty.")
    else:
        st.write(f"Total: ${st.session_state.cart.total():.2f}")
        payment_type = st.selectbox("Payment method", ["Credit Card", "PayPal"])
        if st.button("Place Order"):
            if payment_type == "Credit Card":
                payment = CreditCard("4111111111111111")
            else:
                payment = PayPal("user@email.com")
            order = order_service.create_order(st.session_state.cart, payment)
            if order:
                st.success(f"Order #{order.id} placed!")
            else:
                st.error("Payment failed.")

with tab4:
    st.subheader("Order History")
    orders = order_service.get_all()
    if not orders:
        st.write("No orders yet.")
    for order in orders:
        st.write(f"Order #{order.id} — ${order.total:.2f} — {order.status}")

with tab5:
    st.subheader("Add Product")
    name = st.text_input("Name")
    price = st.number_input("Price", min_value=0.01, format="%.2f")
    stock = st.number_input("Stock", min_value=0, step=1)
    if st.button("Add Product"):
        product = Product(str(uuid.uuid4())[:8], name, price, int(stock))
        catalog.add_product(product)
        st.success(f"Added {name}")
