import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# ======================
# LOAD DATA (FROM DASHBOARD FOLDER)
# ======================
@st.cache_data
def load_data():
    day_df = pd.read_csv("dashboard/main_data.csv")
    hour_df = pd.read_csv("dashboard/hour_data.csv")

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    return day_df, hour_df

day_df, hour_df = load_data()

# ======================
# SIDEBAR FILTER
# ======================
st.sidebar.title("🔎 Filter Data")

min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date]
)

season_order = ["Spring", "Summer", "Fall", "Winter"]

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    season_order,
    default=season_order
)

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    sorted(day_df['weathersit'].unique()),
    default=sorted(day_df['weathersit'].unique())
)

# Apply filter
filtered_df = day_df[
    (day_df['dteday'] >= pd.to_datetime(date_range[0])) &
    (day_df['dteday'] <= pd.to_datetime(date_range[1])) &
    (day_df['season'].isin(selected_season)) &
    (day_df['weathersit'].isin(selected_weather))
]

# ======================
# HEADER
# ======================
st.title("🚲 Bike Sharing Interactive Dashboard")
st.markdown("### Advanced Analysis of Seasonal & Weather Impact on Bike Rentals")
st.markdown("---")

# ======================
# KPI SECTION
# ======================
col1, col2, col3 = st.columns(3)

total_days = len(filtered_df)
avg_rent = filtered_df['cnt'].mean()
total_rent = filtered_df['cnt'].sum()
overall_avg = day_df['cnt'].mean()

col1.metric("📅 Total Hari", total_days)
col2.metric(
    "📊 Rata-rata Penyewaan",
    f"{avg_rent:,.2f}",
    delta=f"{avg_rent - overall_avg:,.2f}"
)
col3.metric("🚲 Total Penyewaan", f"{total_rent:,}")

st.markdown("---")

# ======================
# VISUALISASI MUSIM
# ======================
st.subheader("📈 Rata-rata Penyewaan per Musim")

season_avg = (
    filtered_df.groupby("season")["cnt"]
    .mean()
    .reindex(season_order)
    .reset_index()
)

fig_season = px.bar(
    season_avg,
    x="season",
    y="cnt",
    color="season",
    text_auto=True
)

st.plotly_chart(fig_season, use_container_width=True)

# ======================
# VISUALISASI CUACA
# ======================
st.subheader("🌤 Rata-rata Penyewaan Berdasarkan Cuaca")

weather_avg = (
    filtered_df.groupby("weathersit")["cnt"]
    .mean()
    .reset_index()
)

fig_weather = px.bar(
    weather_avg,
    x="weathersit",
    y="cnt",
    color="weathersit",
    text_auto=True
)

st.plotly_chart(fig_weather, use_container_width=True)

# ======================
# POLA JAM
# ======================
st.subheader("⏰ Pola Penyewaan per Jam")

hour_avg = hour_df.groupby("hr")["cnt"].mean().reset_index()

fig_hour = px.line(
    hour_avg,
    x="hr",
    y="cnt",
    markers=True
)

st.plotly_chart(fig_hour, use_container_width=True)

st.markdown("---")

# ======================
# HEATMAP KORELASI
# ======================
st.subheader("🔥 Correlation Heatmap")

corr_matrix = day_df.corr(numeric_only=True)

fig_heatmap = px.imshow(
    corr_matrix,
    aspect="auto",
    color_continuous_scale="RdBu_r"
)

st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")

# ======================
# DYNAMIC INSIGHT
# ======================
st.subheader("🔎 Insight Otomatis")

if not season_avg.empty and not weather_avg.empty:
    top_season = season_avg.loc[season_avg['cnt'].idxmax(), 'season']
    top_weather = weather_avg.loc[weather_avg['cnt'].idxmax(), 'weathersit']

    st.success(f"""
    Musim dengan performa terbaik dalam rentang waktu ini adalah **{top_season}**.

    Kondisi cuaca paling mendukung adalah **{top_weather}**.

    Terdapat pola penggunaan komuter yang kuat pada pagi dan sore hari.
    """)

st.markdown("---")
st.caption("Proyek Analisis Data - Linda Putriani | Data Scientist")
