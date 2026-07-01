import streamlit as st

st.set_page_config(
    page_title="Property Vision ",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:15px 0;">
        <h2 style="color:white;margin-bottom:5px;">🏠 Property Vision </h2>
        
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("Pages/1_Price_Predictor.py", label="Price Predictor", icon="💰")
    st.page_link("Pages/2_Analaysis_app.py", label="Market Analysis", icon="📈")
    st.page_link("Pages/3_Recommender_Appartments.py", label="Apartment Recommender", icon="🏢")

    st.markdown("---")

    st.info("Select a module to begin.")

# ---------------- Hero ---------------- #

st.markdown("""
<div style="text-align:center; padding-top:40px;">


<div class="main-title">
Property <span>Vision </span>
</div>

<p class="subtitle">

Predict • Analyze • Discover Smarter Real Estate Decisions

</p>

<p class="small-text">

Use the sidebar to explore tools for price prediction,
market analysis and apartment recommendations.

</p>

</div>
""", unsafe_allow_html=True
)

st.markdown("""
<div class="features">

<div class="feature-card">

<div class="feature-icon">
💰
</div>

<div class="feature-title">
Price Predictor
</div>

<div class="feature-desc">
Estimate property prices using our Machine Learning model with high accuracy.
</div>

</div>

<div class="feature-card">

<div class="feature-icon">
📈
</div>

<div class="feature-title">
Market Analysis
</div>

<div class="feature-desc">
Visualize trends, locality insights, price distribution and uncover hidden patterns.
</div>

</div>

<div class="feature-card">

<div class="feature-icon">
🏢
</div>

<div class="feature-title">
Apartment Finder
</div>

<div class="feature-desc">
Discover the best apartments based on amenities, budget and your preferences.
</div>

</div>

</div>
""", unsafe_allow_html=True)

    
st.write("")
st.write("")
st.write("")

st.markdown(
"""
<h2 style='text-align:center;color:white;'>

Platform Statistics

</h2>

""",
unsafe_allow_html=True
)

st.write("")

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""

<div class="stat-card">

<div class="stat-number">

25K+

</div>

<div class="stat-title">

Properties

</div>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="stat-card">

<div class="stat-number">

200+

</div>

<div class="stat-title">

Localities

</div>

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class="stat-card">

<div class="stat-number">

95%

</div>

<div class="stat-title">

Prediction Accuracy

</div>

</div>

""",unsafe_allow_html=True)


st.write("")
st.write("")

st.write("")
st.write("")

st.markdown(
"""
<hr style="
border:.5px solid rgba(255,255,255,.08);
">
""",
unsafe_allow_html=True
)

st.markdown("""

<div class="footer">

Made by Sandeep Singh | Property Vision  © 2026

</div>

""",unsafe_allow_html=True)