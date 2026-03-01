import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Closed-Loop Generative Structural Intelligence System", layout="wide")

# --------------------------------------------------
# DARK FUTURISTIC STYLE
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.block-container {
    padding-top: 2rem;
}
.metric-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1e293b;
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("Closed-Loop Generative Structural Intelligence System")
st.markdown("### Real-Time Closed-Loop Generative + IoT + Adaptive Correction Platform")

tabs = st.tabs([
    "Generative Design",
    "Analytical Validation",
    "Performance Monitoring",
    "Design Recommendation Engine",
    "Deviation Analysis & Model Sync"
])

# =====================================================
# 1️⃣ GENERATIVE DESIGN
# =====================================================
with tabs[0]:
    st.header("🔹 Generative Design Engine")

    col1, col2 = st.columns(2)

    with col1:
        plot_size = st.number_input("Plot Size (sqm)", 100, 1000, 300)
        load_req = st.number_input("Load Requirement (kN)", 100, 2000, 600)
        budget = st.number_input("Budget (Lakhs)", 10, 500, 100)
        material = st.selectbox("Material", ["Concrete", "Steel", "Composite"])

    with col2:
        columns = int(plot_size / 40)
        beam_thickness = round(load_req / 120, 2)
        score = round(100 - beam_thickness * 2, 2)

        st.markdown(f"""
        <div class="metric-box">
        <h4>Optimized Layout</h4>
        Columns: {columns}<br>
        Beam Thickness: {beam_thickness} m<br>
        Optimization Score: {score}%
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# 2️⃣ PREDICTIVE SIMULATION
# =====================================================
with tabs[1]:
    st.header("🔹 Predictive Simulation")

    depth = st.slider("Foundation Depth (m)", 1, 15, 5)
    soil = st.slider("Soil Stability Factor", 1, 10, 5)
    load = st.slider("Applied Load (kN)", 100, 2000, 700)

    risk = load / (depth * soil)

    if risk < 20:
        st.success("🟢 SAFE ZONE")
    elif risk < 35:
        st.warning("🟡 WARNING ZONE")
    else:
        st.error("🔴 HIGH RISK ZONE")

    x = np.linspace(0, 10, 200)
    y = np.sin(x * 2) * load/500 + risk

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
    fig.update_layout(template="plotly_dark", height=350)
    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# 3️⃣ LIVE IOT FEED (ANIMATED)
# =====================================================
with tabs[2]:
    st.header("🔹 Live IoT Sensor Feed")

    placeholder = st.empty()

    load_history = []

    for _ in range(20):  # animation loop
        expected = 600
        actual = expected + random.randint(-40, 180)
        deviation = ((actual - expected)/expected) * 100
        tilt = round(random.uniform(0, 5), 2)

        load_history.append(actual)

        with placeholder.container():
            col1, col2, col3 = st.columns(3)
            col1.metric("Expected Load", expected)
            col2.metric("Actual Load", actual)
            col3.metric("Deviation %", round(deviation,2))

            fig_live = go.Figure()
            fig_live.add_trace(go.Scatter(
                y=load_history,
                mode='lines+markers'
            ))
            fig_live.update_layout(template="plotly_dark", height=300)
            st.plotly_chart(fig_live, use_container_width=True)

            if deviation > 20:
                st.error("🔴 CRITICAL LOAD DEVIATION")
            else:
                st.success("🟢 LOAD STABLE")

        time.sleep(0.5)

# =====================================================
# 4️⃣ AI CORRECTION ENGINE
# =====================================================
with tabs[3]:
    st.header("🔹 AI Adaptive Correction Engine")

    expected = 600
    actual = expected + random.randint(-40, 180)
    deviation = ((actual - expected)/expected) * 100

    st.write(f"Deviation Detected: {round(deviation,2)} %")

    if deviation > 20:
        st.error("AI Triggered Structural Adaptation")
        st.write("• Increase Beam Thickness by 15%")
        st.write("• Add Additional Support Column")
        st.write("• Reinforce Foundation Layer")
    else:
        st.success("System Within Adaptive Limits")

# =====================================================
# 5️⃣ DIGITAL TWIN (DYNAMIC COLOR)
# =====================================================
with tabs[4]:
    st.header("🔹 Digital Twin Visualization")

    risk_dynamic = random.randint(10, 50)

    if risk_dynamic < 25:
        color = "green"
        st.success("🟢 STRUCTURE STABLE")
    else:
        color = "red"
        st.error("🔴 STRUCTURAL STRESS DETECTED")

    fig2 = go.Figure()
    fig2.add_shape(type="rect",
                   x0=0, y0=0, x1=3, y1=6,
                   line=dict(color=color),
                   fillcolor=color)

    fig2.update_layout(template="plotly_dark",
                       height=350,
                       xaxis=dict(visible=False),
                       yaxis=dict(visible=False))

    st.plotly_chart(fig2, use_container_width=True)

