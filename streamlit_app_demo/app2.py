import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------------------------------
# Page config
# -------------------------------------------------------
st.set_page_config(
    page_title="Aadhaar Enrolment Analytics Dashboard",
    layout="wide"
)

st.title("📊 Aadhaar Enrolment Analytics & Insights Dashboard")
st.markdown("""
This dashboard provides **multi-level Aadhaar enrolment analysis** with:
- Temporal trends
- Demographic distribution
- Regional contribution
- Statistical anomalies

Designed for **clarity, interpretability, and decision-making**.
""")

# -------------------------------------------------------
# File selection
# -------------------------------------------------------
st.subheader("📁 Select Dataset")

csv_files = {
    "Aadhaar Enrolment Data": "DF_ENROLMENT_CLEANED.csv",
    "Demographic Data": "DF_DEMOGRAPHIC_CLEANED.csv",
    "Biometric Data": "DF_BIOMETRIC_CLEANED.csv"
}

selected_file_name = st.selectbox(
    "Choose a dataset to analyze:",
    list(csv_files.keys())
)

# -------------------------------------------------------
# Load data safely
# -------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", csv_files[selected_file_name])

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.to_period("M").astype(str)
    return df

df = load_data(DATA_PATH)

# -------------------------------------------------------
# Sidebar controls
# -------------------------------------------------------
st.sidebar.header("🔍 Analysis Controls")

level = st.sidebar.selectbox(
    "Select Analysis Level",
    ["National", "State", "District"]
)

state = district = None

if level in ["State", "District"]:
    state = st.sidebar.selectbox(
        "Select State",
        sorted(df["state"].dropna().unique())
    )

if level == "District":
    district = st.sidebar.selectbox(
        "Select District",
        sorted(df[df["state"] == state]["district"].dropna().unique())
    )

# -------------------------------------------------------
# Start plotting button
# -------------------------------------------------------
st.sidebar.markdown("---")
plot_button = st.sidebar.button("📊 Generate Plots", key="plot_button", use_container_width=True)

# -------------------------------------------------------
# Filter data
# -------------------------------------------------------
df_region = df.copy()
title_suffix = "India (National Level)"

if level == "State":
    df_region = df_region[df_region["state"] == state]
    title_suffix = f"{state} (State Level)"

elif level == "District":
    df_region = df_region[
        (df_region["state"] == state) &
        (df_region["district"] == district)
    ]
    title_suffix = f"{district}, {state} (District Level)"

if plot_button:
    if df_region.empty:
        st.warning("No data available for selected filters.")
        st.stop()

    # =======================================================
    # 1️⃣ Registrations in each month
    # =======================================================
    st.subheader(f"📅 Monthly Registrations — {title_suffix}")

    monthly_total = (
        df_region.groupby("month")[["age_0_5", "age_5_17", "age_18_greater"]]
        .sum()
        .sum(axis=1)
        .reset_index(name="registrations")
    )

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.barplot(data=monthly_total, x="month", y="registrations", ax=ax1)

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Total Registrations")
    ax1.set_title("Total Registrations per Month")
    ax1.bar_label(ax1.containers[0], padding=3)

    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # =======================================================
    # 2️⃣ Registrations by month across age groups
    # =======================================================
    st.subheader("👥 Monthly Registrations by Age Group")

    monthly_age = (
        df_region.groupby("month")[["age_0_5", "age_5_17", "age_18_greater"]]
        .sum()
        .reset_index()
        .melt(id_vars="month", var_name="age_group", value_name="registrations")
    )

    fig2, ax2 = plt.subplots(figsize=(16, 6))
    sns.barplot(
        data=monthly_age,
        y="month",
        x="registrations",
        hue="age_group",
        ax=ax2
    )

    ax2.set_ylabel("Month")
    ax2.set_xlabel("Registrations")
    ax2.set_title("Monthly Registrations Across Age Groups")
    plt.xticks(rotation=45)
    ax2.legend(title="Age Group")

    for container in ax2.containers:
        ax2.bar_label(container, padding=2)

    st.pyplot(fig2)

    # =======================================================
    # 3️⃣ Sub-territory registrations
    # =======================================================
    st.subheader("🗺️ Sub-Territory Registrations")

    if level == "District":
        st.info("Pincode-level data is best viewed as a table due to high cardinality.")

        pincode_table = (
            df_region.groupby("pincode")[["age_0_5", "age_5_17", "age_18_greater"]]
            .sum()
            .sum(axis=1)
            .reset_index(name="total_registrations")
            .sort_values("total_registrations", ascending=False)
        )

        st.dataframe(pincode_table, height=400)

    else:
        sub_col = "state" if level == "National" else "district"

        sub_total = (
            df_region.groupby(sub_col)[["age_0_5", "age_5_17", "age_18_greater"]]
            .sum()
            .sum(axis=1)
            .reset_index(name="registrations")
            .sort_values("registrations", ascending=False)
        )

        fig3, ax3 = plt.subplots(figsize=(14, df_region[sub_col].nunique() * 0.5 + 2))
        sns.barplot(data=sub_total, y=sub_col, x="registrations", ax=ax3)

        ax3.set_ylabel(sub_col.title())
        ax3.set_xlabel("Registrations")
        ax3.set_title(f"Registrations by {sub_col.title()}")
        plt.xticks(rotation=90)
        ax3.bar_label(ax3.containers[0], padding=3)

        st.pyplot(fig3)

    # =======================================================
    # 4️⃣ Sub-territory across age groups
    # =======================================================
    if level != "District":
        st.subheader("👶🧑 Sub-Territory Registrations by Age Group")

        sub_age = (
            df_region.groupby(sub_col)[["age_0_5", "age_5_17", "age_18_greater"]]
            .sum()
            .reset_index()
            .melt(id_vars=sub_col, var_name="age_group", value_name="registrations")
        )

        fig4, ax4 = plt.subplots(figsize=(16, df_region[sub_col].nunique() * 0.5 + 2))

        sns.barplot(
            data=sub_age,
            y=sub_col,                  # <-- categories on Y-axis
            x="registrations",          # <-- values on X-axis
            hue="age_group",
            ax=ax4
        )

        ax4.set_ylabel(sub_col.title())
        ax4.set_xlabel("Registrations")
        ax4.set_title("Registrations by Sub-Territory and Age Group")
        ax4.legend(title="Age Group")

        # Add value labels to the right of each bar
        for container in ax4.containers:
            ax4.bar_label(
                container,
                padding=3,
                fmt="%.0f"
            )

        st.pyplot(fig4)

    # =======================================================
    # 🔹 A. Cumulative registrations over time
    # =======================================================
    st.subheader("📈 Cumulative Registrations Over Time")

    daily_total = (
        df_region.groupby("date")[["age_0_5", "age_5_17", "age_18_greater"]]
        .sum()
        .sum(axis=1)
        .cumsum()
        .reset_index(name="cumulative_registrations")
    )

    fig5, ax5 = plt.subplots(figsize=(12, 5))
    ax5.plot(daily_total["date"], daily_total["cumulative_registrations"], linewidth=2)
    ax5.set_xlabel("Date")
    ax5.set_ylabel("Cumulative Registrations")
    ax5.set_title("Cumulative Registration Growth")
    st.pyplot(fig5)

    # =======================================================
    # 🔹 B. Age-group percentage share over time
    # =======================================================
    st.subheader("📊 Age Group Percentage Share Over Time")

    monthly_pct = (
        df_region.groupby("month")[["age_0_5", "age_5_17", "age_18_greater"]]
        .sum()
    )

    monthly_pct = monthly_pct.div(monthly_pct.sum(axis=1), axis=0) * 100
    monthly_pct = monthly_pct.reset_index().melt(
        id_vars="month",
        var_name="age_group",
        value_name="percentage"
    )

    fig6, ax6 = plt.subplots(figsize=(14, 6))
    sns.lineplot(
        data=monthly_pct,
        x="month",
        y="percentage",
        hue="age_group",
        marker="o",
        ax=ax6
    )

    ax6.set_xlabel("Month")
    ax6.set_ylabel("Percentage Share (%)")
    ax6.set_title("Age Group Contribution Over Time")
    plt.xticks(rotation=45)
    ax6.legend(title="Age Group")
    st.pyplot(fig6)

