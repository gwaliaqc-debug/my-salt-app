import streamlit as st
import pandas as pd

# ==========================================================
# MY NANI'S SECRET - SAFE & PURE STREAMLIT NATIVE UI
# Developed by: Ayush Kumar Agnihotri (Food Technologist)
# ==========================================================

st.set_page_config(page_title="My Nani's Secret Portal", layout="centered", page_icon="🌿")

# ऐप का मुख्य हेडर और लोगो सेक्शन
st.markdown("<h1 style='text-align: center; color: #6CC551; font-family: sans-serif; margin-bottom: 0px;'>My Nani's Secret ®</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4A5568; font-size: 13px; font-weight: 500; letter-spacing: 1px; margin-top: 0px; text-align: center;'>PRISTINE FORMULATIONS & BLENDS</p>", unsafe_allow_html=True)
st.markdown("---")

# 1. AUTHENTICATION MODULE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.subheader("🔐 Secure Access")
    with st.container(border=True):
        user = st.text_input("User ID", placeholder="Enter official ID")
        pas = st.text_input("Password", type="password", placeholder="••••••••")
        
        if st.button("Authenticate Portal 🚀", use_container_width=True, type="primary"):
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
        st.subheader("💰 Ingredient Price Log (₹/kg)")
        report_data = []
        total_cost = 0.0
        
        with st.expander("🛠 Click to Adjust Raw Material Rates", expanded=False):
            st.caption("Customize market rates to evaluate live production expenses:")
            price_dict = {}
            for ing, pct, _ in recipes[salt_type]:
                price_dict[ing] = st.number_input(f"{ing} (₹/kg):", min_value=0.0, value=60.0, step=5.0, key=f"price_{ing}")

        # गणना और डिस्प्ले
        st.subheader("📋 Formula Breakdown & Live Costing")
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
            use_container_width=True,
            type="primary"
        )

    # ------------------------------------------------------
    # MENU 2: MACHINERY (DEEP INTEGRATION FROM OFFICIAL DOC)
    # ------------------------------------------------------
    elif menu_selection == "🏭 Machinery":
        st.subheader("🏭 Trial Production & QA Equipment List")
        st.caption("Detailed engineering specifications & authorized vendors:")
        
        with st.container(border=True):
            st.markdown("### 1. SS 304 Impact Pulverizer / Pin Mill (1 HP / 2 HP)")
            st.info("📍 Recommended Suppliers: Friends & Company, Shree Engineering Works, Jas Enterprise")
            st.write("• **Material:** SS 304 Food-Grade Stainless Steel")
            st.write("• **Capacity:** 10 to 20 Kg/Hr output")
            st.write("• **Technology:** Cool Grinding Technology to perfectly retain delicate herb aroma")
            st.write("• **Power:** Single Phase (Runs smoothly on domestic electricity)")
            
        with st.container(border=True):
            st.markdown("### 2. SS 304 Rectangular GMP Processing Tub / Mixing Vessel")
            st.write("• **Material:** Heavy-gauge SS 304 with Mirror Finish Inside")
            st.write("• **Volume Capacity:** 50 Liters to 100 Liters (Handles 20-40 Kg batch easily)")
            
        with st.container(border=True):
            st.markdown("### 3. SS 304 Food-Grade Handling Scraper / Mixing Paddle")
            st.write("• **Material:** Solid Stainless Steel 304 Construction")
            st.write("• **Length:** 2 to 3 Feet long handle tailored for deep tub mixing")
            
        with st.container(border=True):
            st.markdown("### 4. Halogen Moisture Analyzer")
            st.info("📍 Approved Models: Wensar LMB-1 / Labman LHS-10 / Shimadzu MOC63u")
            st.write("• **Capacity:** 50g to 110g sample capacity")
            st.write("• **Accuracy:** Ultra-precise 0.001g / 0.01% moisture detection level")
            st.write("• **Target Gate:** Powered by Halogen Lamp to strictly lock salt moisture below 0.40%")
            
        with st.container(border=True):
            st.markdown("### 5. Continuous Band Sealer FR-900 (Horizontal Type)")
            st.info("📍 Recommended Vendor: Continental Packaging")
            st.write("• **Sealing Width:** 8mm to 12mm heavy-duty airtight hermetic lock")
            st.write("• **Speed & Temp:** 0-12 meters/minute with precision temperature controller up to 300°C")
            
        with st.container(border=True):
            st.markdown("### 6. Laboratory Test Sieve Set (दानों का साइज एक बराबर करने के लिए)")
            st.info("📍 Recommended Supplier: Shanti Scientific Traders")
            st.write("• **Industry Standard:** SS 304 Standard Test Sieves (8-inch Diameter)")
            st.write("• **Material:** Food-Grade Stainless Steel 304")
            st.write("• **Mesh Sizes Grid:** 30 Mesh, 40 Mesh, 60 Mesh, and 80 Mesh for strict particle uniformity")
            
        with st.container(border=True):
            st.markdown("### 7. Analytical Balance")
            st.info("📍 Industry Approved: High-Precision Electronic Lab Balance (CAS / Wensar / Essae)")
            st.write("• **Max Capacity:** 200g to 600g range")
            st.write("• **Readability:** Milligram level precision (0.01g or 0.001g) for accurate expensive herb costing")
            
        with st.container(border=True):
            st.markdown("### 8. Room Dehumidifier")
            st.info("📍 Approved Equipment: Heavy-Duty Dehumidifier (White Westinghouse / Origin 15-20L)")
            st.write("• **Moisture Extraction:** 15 to 20 Liters condensation removal per day")
            st.write("• **Target Humidity:** Strict environmental control fixed at 40% RH to prevent salt clumping")

    # ------------------------------------------------------
    # MENU 3: PACKAGING
    # ------------------------------------------------------
    elif menu_selection == "📦 Packaging":
        st.subheader("📦 Advanced Pouch Architecture")
        st.success("🔬 **Laminate Matrix Specs Verified**")
        
        with st.container(border=True):
            st.markdown("""
            * 🛡️ **Composition:** Matte PET / Aluminium Foil / Food-Grade LDPE
            * 📏 **Thickness Parameter:** 110 to 120 Microns (High Puncture Resistance)
            * 🛑 **Barrier Efficiency:** 100% Hermetic Water-Vapor Block (Zero-Clumping Guarantee)
            """)

    # ------------------------------------------------------
    # MENU 4: FSSAI RULES
