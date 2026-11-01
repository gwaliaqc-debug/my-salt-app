import streamlit as st
import pandas as pd

# ==========================================================
# MY NANI'S SECRET - ULTRA PREMIUM FOOD-TECH NATIVE UI
# Developed by: Ayush Kumar Agnihotri (Food Technologist)
# ==========================================================

st.set_page_config(page_title="My Nani's Secret Portal", layout="centered", page_icon="🌿")

# जादुई मोबाइल स्टाइलिंग (CSS Updates)
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none;} 
    .reportview-container .main .block-container { padding-top: 0.5rem; }
    div.block-container { padding-top: 1rem; max-width: 450px !important; margin: 0 auto; } 
    
    /* बटन और कार्ड्स को प्रीमियम ऐप लुक देने के लिए */
    .stButton>button {
        border-radius: 14px;
        font-weight: bold;
        background-color: #6CC551 !important;
        color: white !important;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #5ab340 !important;
        transform: scale(1.02);
    }
    div[data-testid="stNotification"] {
        border-radius: 14px;
    }
    
    /* कस्टमाइज़्ड सब-हेडिंग्स */
    h3 {
        color: #4A9C30;
        font-weight: 700;
    }
    
    /* मशीनरी कार्ड स्टाइलिंग */
    .machinery-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
    }
    .machine-title {
        color: #2D3748;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 4px;
    }
    .machine-supplier {
        color: #4A9C30;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .machine-detail {
        color: #4A5568;
        font-size: 13px;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. ऐप का मुख्य हेडर और लोगो सेक्शन
st.markdown("<h1 style='text-align: center; color: #6CC551; font-family: sans-serif; margin-bottom: 0px;'>My Nani's Secret ®</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4A5568; font-size: 13px; font-weight: 500; letter-spacing: 1px; margin-top: 0px;'>PRISTINE FORMULATIONS & BLENDS</p>", unsafe_allow_html=True)

# 2. AUTHENTICATION MODULE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown("### 🔐 Secure Access")
    with st.container(border=True):
        user = st.text_input("User ID", placeholder="Enter official ID")
        pas = st.text_input("Password", type="password", placeholder="••••••••")
        
        if st.button("Authenticate Portal 🚀", use_container_width=True):
            if user == "nani" and pas == "secret":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("❌ Invalid Credentials. Please try again.")
else:
    # --- WHATSAPP / INSTAGRAM STYLE NATIVE MENU BUTTONS ---
    menu_selection = st.radio(
        "📱 PORTAL SECTIONS",
        ["🧮 Calculator", "🏭 Machinery", "📦 Packaging", "⚖️ FSSAI Rules"],
        horizontal=True
    )
    st.markdown("---")
    
    # ------------------------------------------------------
    # MENU 1: CALCULATOR (WITH DYNAMIC COSTING & REPORT)
    # ------------------------------------------------------
    if menu_selection == "🧮 Calculator":
        st.subheader("🎯 Batch Formulation Panel")
        
        with st.container(border=True):
            salt_type = st.selectbox("Select Blend Profile:", ["Nani Namak", "Buknu", "Sheetal Namak"])
            weight = st.number_input("Enter Batch Weight (kg):", min_value=1.0, value=100.0, step=10.0)
        
        # मास्टर रेसिपी मैट्रिक्स
        recipes = {
            "Nani Namak": [
                ("White Salt", 0.45, "🌿"), ("Sendha Namak", 0.25, "🌿"), ("Kala Namak", 0.15, "🌿"),
                ("Jeera", 0.05, "🌿"), ("Kali Mirch", 0.04, "🌿"), ("Lal Mirch", 0.03, "🌿"),
                ("Garam Masala", 0.02, "🌿"), ("Hing", 0.01, "🌿")
            ],
            "Buknu": [
                ("Base Salt Mix", 0.50, "🌿"), ("Badi & Chhoti Harad Blend", 0.15, "🌿"), ("Dry Amla Powder", 0.10, "🌿"),
                ("Pure Turmeric / Haldi", 0.08, "🌿"), ("Digestive Herb Blend", 0.08, "🌿"), ("Pungent Bio-Enhancers", 0.05, "🌿"),
                ("Mustard Oil", 0.02, "🌿"), ("Hing", 0.01, "🌿"), ("Naushadar [Food-Grade]", 0.005, "💥 [FSSAI Max Cap]"),
                ("Aamzhor Namak Mix", 0.005, "💥")
            ],
            "Sheetal Namak": [
                ("Sendha Base", 0.50, "🌿"), ("Regular/Black Salt", 0.20, "🌿"), ("Pudina Powder", 0.12, "🌿"),
                ("Saunf Powder", 0.06, "🌿"), ("Mishri Powder", 0.05, "🌿"), ("Sour Blend", 0.04, "🌿"),
                ("Jaljeera", 0.025, "🌿"), ("Naushadar", 0.005, "💥")
            ]
        }
        
        # 💰 COST ESTIMATOR INTERFACE
        st.markdown("### 💰 Ingredient Price Log (₹/kg)")
        report_data = []
        total_cost = 0.0
        
        with st.expander("🛠 Click to Adjust Raw Material Rates", expanded=False):
            st.caption("Customize market rates to evaluate live production expenses:")
            price_dict = {}
            for ing, pct, _ in recipes[salt_type]:
                price_dict[ing] = st.number_input(f"{ing} (₹/kg):", min_value=0.0, value=60.0, step=5.0, key=f"price_{ing}")

        # गणना और डिस्प्ले
        st.markdown("### 📋 Formula Breakdown & Live Costing")
        with st.container(border=True):
            for ing, pct, status in recipes[salt_type]:
                calc_wt = weight * pct
                item_price = price_dict[ing]
                item_cost = calc_wt * item_price
                total_cost += item_cost
                
                wt_str = f"{calc_wt:.3f}" if pct < 0.01 else f"{calc_wt:.2f}"
                st.write(f"{status} **{ing}** ({pct*100}%): {wt_str} kg | `₹{item_cost:.2f}`")
                
                report_data.append({
                    "Ingredient": ing,
                    "Percentage (%)": pct * 100,
                    "Weight (kg)": float(wt_str),
                    "Rate (₹/kg)": item_price,
                    "Total Cost (₹)": round(item_cost, 2)
                })
        
        # कुल लागत डिस्प्ले
        st.metric(label="💵 Grand Production Cost for Batch", value=f"₹{total_cost:,.2f}")
        
        # 📦 CSV EXPORT MODULE
        df_report = pd.DataFrame(report_data)
        csv_data = df_report.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="📥 Export Batch Sheet (CSV)",
            data=csv_data,
            file_name=f"{salt_type.lower().replace(' ', '_')}_batch_sheet.csv",
            mime="text/csv",
            use_container_width=True
        )

    # ------------------------------------------------------
    # MENU 2: MACHINERY (DEEP INTEGRATION FROM OFFICIAL DOC)
    # ------------------------------------------------------
    elif menu_selection == "🏭 Machinery":
        st.subheader("🏭 Trial Production & QA Equipment List")
        st.caption("Detailed engineering specifications & authorized vendors:")
        
        # 1. Impact Pulverizer
        st.markdown("""
        <div class="machinery-card">
            <div class="machine-title">1. SS 304 Impact Pulverizer / Pin Mill (1 HP / 2 HP)</div>
            <div class="machine-supplier">📍 Recommended Suppliers: Friends & Company, Shree Engineering Works, Jas Enterprise</div>
            <div class="machine-detail">
                • <b>Material:</b> SS 304 Food-Grade Stainless Steel<br>
                • <b>Capacity:</b> 10 to 20 Kg/Hr output<br>
                • <b>Technology:</b> Cool Grinding Technology to perfectly retain delicate herb aroma<br>
                • <b>Power:</b> Single Phase (Runs smoothly on domestic electricity)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. Mixing Vessel
        st.markdown("""
        <div class="machinery-card">
            <div class="machine-title">2. SS 304 Rectangular GMP Processing Tub / Mixing Vessel</div>
            <div class="machine-detail">
                • <b>Material:</b> Heavy-gauge SS 304 with Mirror Finish Inside<br>
                • <b>Volume Capacity:</b> 50 Liters to 100 Liters (Handles 20-40 Kg batch easily)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 3. Handling Scraper
        st.markdown("""
        <div class="machinery-card">
            <div class="machine-title">3. SS 304 Food-Grade Handling Scraper / Mixing Paddle</div>
            <div class="machine-detail">
                • <b>Material:</b> Solid Stainless Steel 304 Construction<br>
                • <b>Length:</b> 2 to 3 Feet long handle tailored for deep tub mixing
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 4. Moisture Analyzer
        st.markdown("""
        <div class="machinery-card">
            <div class="machine-title">4. Halogen Moisture Analyzer</div>
            <div class="machine-supplier">📍 Approved Models: Wensar LMB-1 / Labman LHS-10 / Shimadzu MOC63u</div>
            <div class="machine-detail">
                • <b>Capacity:</b> 50g to 110g sample capacity<br>
                • <b>Accuracy:</b> Ultra-precise 0.001g / 0.01% moisture detection level<br>
                • <b>Target Gate:</b> Powered by Halogen Lamp to strictly lock salt moisture below 0.40%
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 5. Continuous Band Sealer
        st.markdown("""
        <div class="machinery-card">
            <div class="machine-title">5. Continuous Band Sealer FR-900 (Horizontal Type)</div>
            <div class="machine-supplier">📍 Recommended Vendor: Continental Packaging</div>
            <div class="machine-detail">
