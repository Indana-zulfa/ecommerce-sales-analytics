from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "processed"

COLORS = {
    "navy": "#0F172A",       # Slate 900
    "blue": "#3B82F6",       # Blue 500
    "teal": "#14B8A6",       # Teal 500
    "purple": "#8B5CF6",     # Purple 500
    "orange": "#F59E0B",     # Amber 500
    "cyan": "#06B6D4",       # Cyan 500
    "red": "#EF4444",        # Red 500
    "background": "#F8FAFC", # Slate 50
    "card_bg": "#FFFFFF",
    "text": "#334155",       # Slate 700
    "muted": "#64748B",      # Slate 500
    "border": "#E2E8F0",     # Slate 200
}


# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Main Background */
    .stApp {
        background-color: #F8FAFC;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #0F172A;
        border-right: none;
        box-shadow: 4px 0 24px rgba(0,0,0,0.1);
    }

    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #1E293B;
        border-color: #334155;
        border-radius: 8px;
    }

    [data-testid="stSidebar"] [data-testid="stDateInput"] > div > div {
        background-color: #1E293B;
        border-color: #334155;
        border-radius: 8px;
    }

    [data-testid="stSidebar"] hr {
        border-color: #334155;
        margin: 2rem 0;
    }

    /* Metric Cards */
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: #CBD5E1;
    }

    [data-testid="stMetricLabel"] {
        color: #64748B;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    [data-testid="stMetricValue"] {
        color: #0F172A;
        font-size: 26px;
        font-weight: 800;
        margin-top: 4px;
    }

    /* Typography */
    h1, h2, h3 {
        color: #0F172A;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
        padding: 40px 45px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    /* Hero Decorative Circle */
    .hero::after {
        content: '';
        position: absolute;
        top: -50px;
        right: -50px;
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, rgba(59,130,246,0.3) 0%, rgba(59,130,246,0) 70%);
        border-radius: 50%;
    }

    .hero h1 {
        color: white !important;
        font-size: 34px;
        margin: 0 0 10px 0;
        font-weight: 800;
        z-index: 1;
        position: relative;
    }

    .hero p {
        color: #93C5FD !important;
        font-size: 16px;
        margin: 0;
        font-weight: 500;
        z-index: 1;
        position: relative;
    }

    /* Section Description */
    .section-description {
        color: #64748B;
        font-size: 14px;
        margin-top: -10px;
        margin-bottom: 25px;
        font-weight: 500;
    }

    /* Plotly Chart Container */
    div[data-testid="stPlotlyChart"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    /* Tabs Styling */
    div[data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        padding-bottom: 0;
    }

    div[data-testid="stTabs"] [data-baseweb="tab"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 10px 20px;
        color: #64748B;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
    }

    div[data-testid="stTabs"] [data-baseweb="tab"]:hover {
        border-color: #CBD5E1;
        color: #0F172A;
    }

    div[data-testid="stTabs"] [aria-selected="true"] {
        background-color: #EFF6FF;
        border-color: #3B82F6;
        color: #1D4ED8;
        border-bottom: none;
    }

    div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        display: none;
    }

    /* Sidebar Text Styling */
    .sidebar-title {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .sidebar-subtitle {
        color: #94A3B8;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1.5px;
        margin-bottom: 32px;
        text-transform: uppercase;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94A3B8;
        font-size: 13px;
        padding: 40px 0 10px 0;
        border-top: 1px solid #E2E8F0;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    files = {
        "orders": "orders_cleaned.csv",
        "order_items": "order_items_cleaned.csv",
        "customers": "customers_cleaned.csv",
        "payments": "payments_cleaned.csv",
        "reviews": "reviews_cleaned.csv",
        "products": "products_cleaned.csv",
        "sellers": "sellers_cleaned.csv",
        "category_translation": "category_translation_cleaned.csv",
    }

    data = {}

    for name, filename in files.items():

        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Missing data file: {file_path}"
            )

        data[name] = pd.read_csv(file_path)

    return data


try:

    data = load_data()

    orders = data["orders"].copy()
    order_items = data["order_items"].copy()
    customers = data["customers"].copy()
    payments = data["payments"].copy()
    reviews = data["reviews"].copy()
    products = data["products"].copy()
    sellers = data["sellers"].copy()
    category_translation = data["category_translation"].copy()

except Exception as error:

    st.error(f"Unable to load project data: {error}")
    st.stop()


# ============================================================
# 4. DATA PREPARATION
# ============================================================

date_columns = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

for column in date_columns:

    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )


# Merge order items with order information
sales_data = order_items.merge(
    orders[
        [
            "order_id",
            "order_purchase_timestamp",
            "order_status",
        ]
    ],
    on="order_id",
    how="left"
)

# Merge product categories
sales_data = sales_data.merge(
    products[
        ["product_id", "product_category_name"]
    ],
    on="product_id",
    how="left"
)

sales_data = sales_data.merge(
    category_translation,
    on="product_category_name",
    how="left"
)

sales_data["category"] = (
    sales_data["product_category_name_english"]
    .fillna("Unknown")
)

# Merge customer information
customer_orders = orders.merge(
    customers[
        [
            "customer_id",
            "customer_unique_id",
            "customer_state",
        ]
    ],
    on="customer_id",
    how="left"
)


# ============================================================
# 5. SIDEBAR AND FILTERS
# ============================================================

st.sidebar.markdown(
    '<div class="sidebar-title">📊 E-Commerce</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-subtitle">Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("**Dashboard Filters**")

valid_dates = orders["order_purchase_timestamp"].dropna()

if valid_dates.empty:
    st.error("No valid purchase dates found.")
    st.stop()

min_date = valid_dates.min().date()
max_date = valid_dates.max().date()

date_range = st.sidebar.date_input(
    "Purchase Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:

    start_date, end_date = date_range

elif isinstance(date_range, (tuple, list)) and len(date_range) == 1:

    start_date = date_range[0]
    end_date = date_range[0]

else:

    start_date = min_date
    end_date = max_date


category_options = sorted(
    sales_data["category"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "Product Categories",
    options=category_options,
    default=[]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Dataset: Brazilian E-Commerce Public Dataset by Olist"
)


# ============================================================
# 6. APPLY FILTERS
# ============================================================

date_mask = (
    sales_data["order_purchase_timestamp"].dt.date.between(
        start_date,
        end_date
    )
)

filtered_sales = sales_data[date_mask].copy()

if selected_categories:

    filtered_sales = filtered_sales[
        filtered_sales["category"].isin(selected_categories)
    ]

# Use selected sales order IDs to keep related metrics consistent
filtered_order_ids = filtered_sales["order_id"].dropna().unique()

filtered_orders = orders[
    orders["order_id"].isin(filtered_order_ids)
].copy()

filtered_payments = payments[
    payments["order_id"].isin(filtered_order_ids)
].copy()

filtered_customers = customer_orders[
    customer_orders["order_id"].isin(filtered_order_ids)
].copy()


# ============================================================
# 7. HELPER FUNCTIONS
# ============================================================

def style_chart(fig, height=420):

    fig.update_layout(
        template="plotly_white",
        height=height,
        font=dict(
            family="Plus Jakarta Sans, sans-serif",
            color=COLORS["text"],
            size=12
        ),
        title=dict(
            font=dict(
                size=16,
                color=COLORS["navy"],
                weight="bold"
            ),
            x=0.02,
            xanchor="left",
            y=0.95
        ),
        margin=dict(
            l=10,
            r=20,
            t=60,
            b=20
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            bgcolor="rgba(255,255,255,0)",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hoverlabel=dict(
            bgcolor="#0F172A",
            font_color="#FFFFFF",
            font_family="Plus Jakarta Sans"
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#F1F5F9",
        zeroline=False,
        tickfont=dict(color="#64748B")
    )

    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(color="#64748B")
    )

    return fig


# ============================================================
# 8. HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <h1>E-Commerce Sales Analytics</h1>
    <p>Business performance, customer behavior, product trends, payments, delivery, and seller insights.</p>
</div>
""", unsafe_allow_html=True)

st.caption(
    f"📅 Analysis period: **{start_date}** — **{end_date}**"
)

# ============================================================
# 9. EXECUTIVE OVERVIEW / KPI CARDS
# ============================================================

total_sales = filtered_sales["price"].sum()
total_orders = filtered_orders["order_id"].nunique()
total_items = len(filtered_sales)
total_customers = (filtered_customers["customer_unique_id"].nunique())
average_order_value = (total_sales / total_orders if total_orders > 0 else 0)

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("TOTAL SALES", f"R$ {total_sales:,.2f}")
k2.metric("TOTAL ORDERS", f"{total_orders:,}")
k3.metric("ITEMS SOLD", f"{total_items:,}")
k4.metric("CUSTOMERS", f"{total_customers:,}")
k5.metric("AVG ORDER VALUE", f"R$ {average_order_value:,.2f}")

st.caption(
    "*Sales represents recorded item prices across all order statuses "
    "and excludes freight. It is not net or realized revenue.*"
)

st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# 10. TABS
# ============================================================

tab_overview, tab_sales, tab_customer, tab_delivery = st.tabs(
    [
        "📈 Executive Overview",
        "📦 Sales & Products",
        "👥 Customers & Payments",
        "🚚 Delivery & Sellers",
    ]
)


# ============================================================
# TAB 1: EXECUTIVE OVERVIEW
# ============================================================

with tab_overview:

    st.subheader("Monthly Sales Performance")

    monthly_sales = (
        filtered_sales
        .dropna(subset=["order_purchase_timestamp"])
        .assign(
            month=lambda df: (
                df["order_purchase_timestamp"]
                .dt.to_period("M")
                .astype(str)
            )
        )
        .groupby("month", as_index=False)
        .agg(
            total_sales=("price", "sum")
        )
    )

    fig_monthly = px.line(
        monthly_sales,
        x="month",
        y="total_sales",
        markers=True,
        title="Monthly Sales Trend",
        labels={
            "month": "",
            "total_sales": "Sales Value (R$)"
        }
    )

    fig_monthly.update_traces(
        line=dict(
            color=COLORS["blue"],
            width=3.5
        ),
        marker=dict(
            size=8,
            color="#FFFFFF",
            line=dict(width=2, color=COLORS["blue"])
        ),
        fill="tozeroy",
        fillcolor="rgba(59, 130, 246, 0.08)"
    )

    fig_monthly = style_chart(fig_monthly, 430)

    st.plotly_chart(
        fig_monthly,
        use_container_width=True
    )


# ============================================================
# TAB 2: SALES & PRODUCT ANALYSIS
# ============================================================

with tab_sales:

    st.subheader("Sales & Product Analysis")

    left, right = st.columns(2)

    # Top categories by sales
    category_sales = (
        filtered_sales
        .groupby("category", as_index=False)
        .agg(
            total_sales=("price", "sum")
        )
        .sort_values(
            "total_sales",
            ascending=False
        )
        .head(10)
    )

    with left:

        fig_category = px.bar(
            category_sales.sort_values("total_sales"),
            x="total_sales",
            y="category",
            orientation="h",
            text="total_sales",
            title="Top 10 Product Categories by Sales",
            labels={
                "total_sales": "Sales Value (R$)",
                "category": ""
            }
        )

        fig_category.update_traces(
            marker_color=COLORS["blue"],
            marker_line_color="rgba(0,0,0,0)",
            texttemplate="R$ %{x:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_category = style_chart(fig_category, 480)

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )

    # Order status distribution
    with right:

        order_status = (
            filtered_orders["order_status"]
            .value_counts()
            .rename_axis("status")
            .reset_index(name="total_orders")
            .sort_values("total_orders")
        )

        fig_status = px.bar(
            order_status,
            x="total_orders",
            y="status",
            orientation="h",
            text="total_orders",
            title="Order Status Distribution",
            labels={
                "total_orders": "Number of Orders",
                "status": ""
            }
        )

        fig_status.update_traces(
            marker_color=COLORS["teal"],
            marker_line_color="rgba(0,0,0,0)",
            texttemplate="%{x:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_status.update_xaxes(
            type="log",
            title="Number of Orders (Log Scale)"
        )

        fig_status = style_chart(fig_status, 480)

        st.plotly_chart(
            fig_status,
            use_container_width=True
        )


# ============================================================
# TAB 3: CUSTOMER & PAYMENT ANALYSIS
# ============================================================

with tab_customer:

    st.subheader("Customer & Payment Analysis")

    left, right = st.columns(2)

    # Customer distribution by state
    customer_state = (
        filtered_customers
        .groupby("customer_state", as_index=False)
        .agg(
            total_customers=(
                "customer_unique_id",
                "nunique"
            )
        )
        .sort_values(
            "total_customers",
            ascending=False
        )
        .head(10)
    )

    with left:

        fig_customer = px.bar(
            customer_state.sort_values("total_customers"),
            x="total_customers",
            y="customer_state",
            orientation="h",
            text="total_customers",
            title="Top 10 Customer States",
            labels={
                "total_customers": "Customers",
                "customer_state": ""
            }
        )

        fig_customer.update_traces(
            marker_color=COLORS["cyan"],
            marker_line_color="rgba(0,0,0,0)",
            texttemplate="%{x:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_customer = style_chart(fig_customer, 440)

        st.plotly_chart(
            fig_customer,
            use_container_width=True
        )

    # Payment method analysis
    with right:

        payment_summary = (
            filtered_payments
            .groupby("payment_type", as_index=False)
            .agg(
                total_payment=("payment_value", "sum"),
                total_transactions=("payment_type", "count")
            )
            .sort_values(
                "total_payment",
                ascending=False
            )
        )

        fig_payment = px.bar(
            payment_summary,
            x="payment_type",
            y="total_payment",
            text="total_payment",
            title="Payment Methods by Transaction Value",
            labels={
                "payment_type": "",
                "total_payment": "Payment Value (R$)"
            }
        )

        fig_payment.update_traces(
            marker_color=COLORS["teal"],
            marker_line_color="rgba(0,0,0,0)",
            texttemplate="R$ %{y:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_payment = style_chart(fig_payment, 440)

        st.plotly_chart(
            fig_payment,
            use_container_width=True
        )

    st.divider()

    # Customer purchase frequency
    st.subheader("Customer Purchase Frequency")

    purchase_frequency = (
        filtered_customers
        .groupby("customer_unique_id")
        .agg(
            total_orders=("order_id", "nunique")
        )
        .reset_index()
    )

    purchase_frequency["customer_type"] = np.where(
        purchase_frequency["total_orders"] > 1,
        "Repeat Customer",
        "One-Time Customer"
    )

    customer_type = (
        purchase_frequency["customer_type"]
        .value_counts()
        .rename_axis("customer_type")
        .reset_index(name="total_customers")
    )

    fig_repeat = px.pie(
        customer_type,
        names="customer_type",
        values="total_customers",
        hole=0.6,
        title="One-Time vs Repeat Customers",
        color="customer_type",
        color_discrete_map={
            "One-Time Customer": COLORS["blue"],
            "Repeat Customer": COLORS["orange"]
        }
    )

    fig_repeat.update_traces(
        textposition="inside",
        textinfo="percent+label",
        marker=dict(line=dict(color='#FFFFFF', width=2))
    )

    fig_repeat = style_chart(fig_repeat, 430)

    st.plotly_chart(
        fig_repeat,
        use_container_width=True
    )


# ============================================================
# TAB 4: DELIVERY & SELLER ANALYSIS
# ============================================================

with tab_delivery:

    st.subheader("Delivery Performance")

    delivery = filtered_orders[
        filtered_orders["order_status"].eq("delivered")
    ].dropna(
        subset=[
            "order_purchase_timestamp",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ).copy()

    delivery["actual_delivery_days"] = (
        delivery["order_delivered_customer_date"]
        - delivery["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    delivery["estimated_delivery_days"] = (
        delivery["order_estimated_delivery_date"]
        - delivery["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    delivery["delivery_status"] = np.where(
        delivery["order_delivered_customer_date"]
        <= delivery["order_estimated_delivery_date"],
        "On-Time",
        "Late"
    )

    delivery_summary = (
        delivery["delivery_status"]
        .value_counts()
        .rename_axis("delivery_status")
        .reset_index(name="total_orders")
    )

    left, right = st.columns(2)

    with left:

        fig_delivery = px.pie(
            delivery_summary,
            names="delivery_status",
            values="total_orders",
            hole=0.6,
            title="On-Time vs Late Delivery",
            color="delivery_status",
            color_discrete_map={
                "On-Time": COLORS["teal"],
                "Late": COLORS["red"]
            }
        )

        fig_delivery.update_traces(
            textposition="inside",
            textinfo="percent+label",
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )

        fig_delivery = style_chart(fig_delivery, 430)

        st.plotly_chart(
            fig_delivery,
            use_container_width=True
        )

    with right:

        review_analysis = reviews.merge(
            delivery[
                ["order_id", "delivery_status"]
            ],
            on="order_id",
            how="inner"
        )

        review_summary = (
            review_analysis
            .groupby("delivery_status", as_index=False)
            .agg(
                total_reviews=("review_score", "count"),
                average_score=("review_score", "mean")
            )
        )

        review_summary["average_score"] = (
            review_summary["average_score"].round(2)
        )

        fig_review = px.bar(
            review_summary,
            x="delivery_status",
            y="average_score",
            text="average_score",
            title="Average Review Score by Delivery Performance",
            labels={
                "delivery_status": "",
                "average_score": "Average Review Score"
            },
            range_y=[0, 5],
            color="delivery_status",
            color_discrete_map={
                "On-Time": COLORS["teal"],
                "Late": COLORS["red"]
            }
        )

        fig_review.update_traces(
            texttemplate="%{y:.2f}",
            textposition="outside",
            marker_line_color="rgba(0,0,0,0)",
            cliponaxis=False
        )

        fig_review = style_chart(fig_review, 430)

        st.plotly_chart(
            fig_review,
            use_container_width=True
        )

    # Delivery KPIs
    average_actual_delivery = (
        delivery["actual_delivery_days"].mean()
        if not delivery.empty
        else 0
    )

    average_estimated_delivery = (
        delivery["estimated_delivery_days"].mean()
        if not delivery.empty
        else 0
    )

    st.markdown("<br>", unsafe_allow_html=True)
    d1, d2, d3 = st.columns(3)

    d1.metric(
        "AVG ACTUAL DELIVERY",
        f"{average_actual_delivery:.2f} days"
    )

    d2.metric(
        "AVG ESTIMATED DELIVERY",
        f"{average_estimated_delivery:.2f} days"
    )

    d3.metric(
        "DELIVERED ORDERS ANALYZED",
        f"{len(delivery):,}"
    )

    st.divider()

    # Seller analysis
    st.subheader("Seller Performance")

    seller_sales = filtered_sales.merge(
        sellers[
            ["seller_id", "seller_state"]
        ],
        on="seller_id",
        how="left"
    )

    seller_performance = (
        seller_sales
        .groupby(
            ["seller_id", "seller_state"],
            as_index=False
        )
        .agg(
            total_orders=("order_id", "nunique"),
            total_items=("order_id", "count"),
            total_sales=("price", "sum")
        )
        .sort_values(
            "total_sales",
            ascending=False
        )
    )

    left, right = st.columns(2)

    with left:

        top_sellers = seller_performance.head(10)

        fig_seller = px.bar(
            top_sellers.sort_values("total_sales"),
            x="total_sales",
            y="seller_id",
            orientation="h",
            text="total_sales",
            title="Top 10 Sellers by Sales Value",
            labels={
                "total_sales": "Sales Value (R$)",
                "seller_id": ""
            }
        )

        fig_seller.update_traces(
            marker_color=COLORS["purple"],
            marker_line_color="rgba(0,0,0,0)",
            texttemplate="R$ %{x:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_seller = style_chart(fig_seller, 530)

        st.plotly_chart(
            fig_seller,
            use_container_width=True
        )

    with right:

        seller_state = (
            seller_sales
            .groupby("seller_state", as_index=False)
            .agg(
                total_sellers=("seller_id", "nunique"),
                total_sales=("price", "sum")
            )
            .sort_values(
                "total_sales",
                ascending=False
            )
            .head(10)
        )

        fig_seller_state = px.bar(
            seller_state.sort_values("total_sales"),
            x="total_sales",
            y="seller_state",
            orientation="h",
            text="total_sales",
            title="Top 10 Seller States by Sales",
            labels={
                "total_sales": "Sales Value (R$)",
                "seller_state": ""
            }
        )

        fig_seller_state.update_traces(
            marker_color=COLORS["teal"],
            marker_line_color="rgba(0,0,0,0)",
            texttemplate="R$ %{x:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_seller_state = style_chart(
            fig_seller_state,
            530
        )

        st.plotly_chart(
            fig_seller_state,
            use_container_width=True
        )


# ============================================================
# 11. FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <b>E-Commerce Sales Analytics</b> &copy; 2023<br>
    Brazilian E-Commerce Public Dataset by Olist<br>
    <span style="color: #CBD5E1;">Data Analytics Portfolio Project</span>
</div>
""", unsafe_allow_html=True)