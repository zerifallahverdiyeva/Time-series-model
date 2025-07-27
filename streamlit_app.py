import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("🚗 Hyundai Elantra Qiymət Proqnozu")
st.markdown("Turbo.az məlumatlarına əsaslanan sadə model")

year = st.slider("Buraxılış ili", 2005, 2025, 2020)
engine = st.slider("Mühərrik həcmi (L)", 1.0, 3.0, 1.6, step=0.1)
mileage = st.number_input("Yürüş (km)", min_value=0, value=100000, step=1000)
color = st.selectbox("Rəng", ['ağ', 'qara', 'boz', 'gümüşü', 'mavi', 'qırmızı', 'bej', 'digər'])

ts_years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]).reshape(-1, 1)
avg_prices = np.array([9000, 11000, 12500, 13500, 14500, 16000, 17000, 18000])

reg_model = LinearRegression()
reg_model.fit(ts_years, avg_prices)

year_price = reg_model.predict(np.array([[year]]))[0]

engine_factor = (engine - 1.6) * 1000
mileage_factor = (150000 - mileage) * 0.02
color_bonus = {
    'ağ': 300, 'qara': 200, 'gümüşü': 100,
    'boz': 0, 'mavi': -200, 'qırmızı': -300,
    'bej': -100, 'digər': 0
}

final_price = year_price + engine_factor + mileage_factor + color_bonus.get(color, 0)

st.subheader("🔮 Proqnozlaşdırılmış Qiymət:")
st.success(f"Təxmini qiymət: **{int(final_price):,} AZN**")
