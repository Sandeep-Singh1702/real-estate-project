import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Plotting Demo")

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)
# st.dataframe(df)

st.header("Enter your Input ")
# selecting property
property_type = st.selectbox("Property Type",["flat","house"])
# selecting sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bathroom = float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))

bedroom = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input("Enter Built up area "))

servant_room = float(st.selectbox('Servant Room',[0.0,1.0]))

store_room = float(st.selectbox('Store Room',[0.0,1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Type ',sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):
    data = [[
    property_type,
    sector,
    bedroom,
    bathroom,
    balcony,
    property_age,
    built_up_area,
    servant_room,
    store_room,
    furnishing_type,
    luxury_category,
    floor_category
]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # st.dataframe(one_df)
    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22
    
    #display
    st.text("Price of the mentioned Property is between {:.2f} Cr and {:.2f} Cr".format(low, high))




