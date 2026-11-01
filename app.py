import streamlit as st
import pandas as pd

# ==========================================================
# WORLD-CLASS MOBILE NATIVE UI INTEGRATION (WHATSAPP/INSTA FEEL)
# Developed by: Ayush Kumar Agnihotri (Food Technologist)
# ==========================================================

st.set_page_config(page_title="My Nani's Secret Portal", layout="centered", page_icon="🌶️")

# जादुई मोबाइल स्टाइलिंग (CSS Updates)
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none;} 
    .reportview-container .main .block-container { padding-top: 0.5rem; }
    div.block-container { padding-top: 1rem; max-width: 450px !important; margin: 0 auto; } 
    
    /* बटन और कार्ड्स को ऐप जैसा लुक देने के लिए */
    .stButton>button {
        border-radius: 12px;
        font-weight: bold;
    }
    div[data-testid="stNotification"] {
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# ऐप का मुख्य हेडर
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🌶️ My Nani's Secret ®</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>Food Tech & Tradition Combined</p>", unsafe_allow_html=True)

# 1. AUTHENTICATION MODULE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown("### 🔐 Secure Login")
    with st.container(border=True):
        user = st.text_input("User ID", placeholder="Enter ID")
        pas = st.text_input("Password", type="password", placeholder="••••••••")
        
        if st.button("Authenticate Portal 🚀", use_container_width=True, type="primary"):
            if user == "nani" and pas == "secret":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("❌ Invalid ID or Password.")
else:
    # --- WHATSAPP / INSTAGRAM STYLE NATIVE MENU BUTTONS ---
    menu_selection = st.radio(
        "📱 APP MENU",
        ["🧮 Calculator", "🏭 Machinery", "📦 Packaging", "⚖️ FSSAI Rules"],
        horizontal=True
    )
    st.markdown("---")
    
    # ------------------------------------------------------
    # MENU 1: CALCULATOR (WITH COSTING & CSV EXPORT)
    # ------------------------------------------------------
    if menu_selection == "🧮 Calculator":
        st.subheader("🎯 Batch Formulation")
        
        with st.container(border=True):
            salt_type = st.selectbox("Select Blend Profile:", ["Nani Namak", "Buknu", "Sheetal Namak"])
            weight = st.number_input("Enter Batch Weight (kg):", min_value=1.0, value=100.0, step=10.0)
        
        # रेसिपी डेटा स्ट्रक्चर
        recipes = {
            "Nani Namak": [
                ("White Salt", 0.45, "✔"), ("Sendha Namak", 0.25, "✔"), ("Kala Namak", 0.15, "✔"),
                ("Jeera", 0.05, "✔"), ("Kali Mirch", 0.04, "✔"), ("Lal Mirch", 0.03, "✔"),
                ("Garam Masala", 0.02, "✔"), ("Hing", 0.01, "✔")
            ],
            "Buknu": [
                ("Base Salt Mix", 0.50, "✔"), ("Badi & Chhoti Harad Blend", 0.15, "✔"), ("Dry Amla Powder", 0.10, "✔"),
                ("Pure Turmeric / Haldi", 0.08, "✔"), ("Digestive Herb Blend", 0.08, "✔"), ("Pungent Bio-Enhancers", 0.05, "✔"),
                ("Mustard Oil", 0.02, "✔"), ("Hing", 0.01, "✔"), ("Naushadar [Food-Grade]", 0.005, "💥 [FSSAI Max Cap]"),
                ("Aamzhor Namak Mix", 0.005, "💥")
            ],
            "Sheetal Namak": [
                ("Sendha Base", 0.50, "✔"), ("Regular/Black Salt", 0.20, "✔"), ("Pudina Powder", 0.12, "✔"),
                ("Saunf Powder", 0.06, "✔"), ("Mishri Powder", 0.05, "✔"), ("Sour Blend", 0.04, "✔"),
                ("Jaljeera", 0.025, "✔"), ("Naushadar", 0.005, "💥")
            ]
        }
        
        # 💰 COST ESTIMATOR INTERFACE
        st.markdown("### 💰 Ingredient Costing (per kg)")
        report_data = []
        total_cost = 0.0
        
        with st.expander("📊 Click to adjust Ingredient Prices (₹/kg)", expanded=False):
            st.caption("Enter the market rate for each ingredient to calculate total batch cost:")
            price_dict = {}
            for ing, pct, _ in recipes[salt_type]:
                # डिफॉल्ट प्राइस ₹50 रखी है, जिसे यूजर बदल सकता है
                price_dict[ing] = st.number_input(f"{ing} (₹/kg):", min_value=0.0, value=50.0, step=5.0, key=f"price_{ing}")

        # गणना और डिस्प्ले
        st.markdown("### ⚖️ Ingredients Breakdown & Costs")
        with st.container(border=True):
            for ing, pct, status in recipes[salt_type]:
                calc_wt = weight * pct
                item_price = price_dict[ing]
                item_cost = calc_wt * item_price
                total_cost += item_cost
                
                wt_str = f"{calc_wt:.3f}" if pct < 0.01 else f"{calc_wt:.2f}"
                st.write(f"{status} **{ing}** ({pct*100}%): {wt_str} kg | Cost: ₹{item_cost:.2f}")
                
                # CSV के लिए डेटा इकट्ठा करना
                report_data.append({
                    "Ingredient": ing,
                    "Percentage (%)": pct * 100,
                    "Weight (kg)": float(wt_str),
                    "Rate (₹/kg)": item_price,
                    "Total Cost (₹)": round(item_cost, 2)
                })
        
        # कुल लागत कार्ड
        st.metric(label="💵 Total Batch Production Cost", value=f"₹{total_cost:,.2f}")
        
        # 📦 CSV EXPORT MODULE
        df_report = pd.DataFrame(report_data)
        csv_data = df_report.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="📥 Download Batch Report (CSV)",
            data=csv_data,
            file_name=f"{salt_type.lower().replace(' ', '_')}_batch_report.csv",
            mime="text/csv",
            use_container_width=True,
            type="secondary"
        )

    # ------------------------------------------------------
    # MENU 2: MACHINERY
    # ------------------------------------------------------
    elif menu_selection == "🏭 Machinery":
        st.subheader("🏭 Factory Equipment Setup")
        machinery_data = [
            {"Equipment Name": "Impact Pulverizer", "Critical Parameter": "2880 RPM / Cool Grind"},
            {"Equipment Name": "Ribbon Blender", "Critical Parameter": "8-10 Mins Max Mix"},
            {"Equipment Name": "Dehumidifier", "Critical Parameter": "Maintains <40% RH"},
            {"Equipment Name": "Moisture Analyzer", "Critical Parameter": "Critical Lock <0.40%"},
            {"Equipment Name": "Band Sealer", "Critical Parameter": "8-12 mm Extra-Wide Seal"}
        ]
        st.dataframe(pd.DataFrame(machinery_data), hide_index=True, use_container_width=True)

    # ------------------------------------------------------
    # MENU 3: PACKAGING
    # ------------------------------------------------------
    elif menu_selection == "📦 Packaging":
        st.subheader("📦 Pouch Architecture")
        st.info("🧬 **3-Layer Composite Laminate Matrix**")
        
        with st.container(border=True):
            st.markdown("""
            * 🛡️ **Layers:** Matte PET / Aluminium Foil / Food-Grade LDPE
            * 📏 **Thickness:** 110 to 120 Microns (Puncture Resistant)
            * 🛑 **Barrier:** 100% Moisture Block (No Clumping Guarantee)
            """)

    # ------------------------------------------------------
    # MENU 4: FSSAI RULES
    # ------------------------------------------------------
    elif menu_selection == "⚖️ FSSAI Rules":
        st.subheader("⚖️ Regulatory Mandates")
        st.error("🚨 **Naushadar (Ammonium Chloride):** Cap strictly limited to **0.5% max** by weight.")
        st.warning("📋 **Labeling Rule:** Rear packaging panel must allocate **20% surface area** for Nutritional Panel (Font Size 8).")

    # --- LOGOUT BUTTON ---
    st.markdown("---")
    if st.button("🚪 Logout From Portal", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
