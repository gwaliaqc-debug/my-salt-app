import streamlit as st

# ==========================================================
# WORLD-CLASS MOBILE NATIVE UI INTEGRATION (WHATSAPP/INSTA FEEL)
# ==========================================================

st.set_page_config(page_title="My Nani's Secret Portal", layout="centered")

# जादुई मोबाइल स्टाइलिंग (CSS) - यह ब्राउज़र के टैब्स को छुपाकर असली ऐप जैसा लुक देता है
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none;} /* ऊपर की फालतू पट्टी गायब */
    .reportview-container .main .block-container { padding-top: 1rem; }
    div.block-container { padding-top: 1rem; max-width: 450px !important; } /* मोबाइल स्क्रीन साइज लॉक */
    </style>
    """, unsafe_allow_html=True)

st.title("My Nani's Secret ®")

# 1. AUTHENTICATION MODULE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown("### 🔐 Secure Login")
    user = st.text_input("User ID")
    pas = st.text_input("Password", type="password")
    if st.button("Authenticate Portal", use_container_width=True):
        if user == "nani" and pas == "secret":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid ID or Password.")
else:
    # --- WHATSAPP / INSTAGRAM STYLE NATIVE MENU BUTTONS ---
    # स्क्रीन के टॉप या बॉटम पर सुंदर मेनू बटन
    st.markdown("---")
    menu_selection = st.radio(
        "📱 APP MENU",
        ["🧮 Calculator", "🏭 Machinery", "📦 Packaging", "⚖️ FSSAI Rules"],
        horizontal=True
    )
    st.markdown("---")
    
    # ------------------------------------------------------
    # MENU 1: CALCULATOR
    # ------------------------------------------------------
    if menu_selection == "🧮 Calculator":
        st.subheader("🎯 Batch Formulation")
        salt_type = st.selectbox("Select Blend Profile:", ["Nani Namak", "Buknu", "Sheetal Namak"])
        weight = st.number_input("Enter Batch Weight (kg):", min_value=1.0, value=100.0, step=10.0)
        
        st.markdown("#### ⚖️ Ingredients Breakdown")
        if salt_type == "Nani Namak":
            st.write(f"✔ White Salt (45%): **{weight * 0.45:.2f} kg**")
            st.write(f"✔ Sendha Namak (25%): **{weight * 0.25:.2f} kg**")
            st.write(f"✔ Kala Namak (15%): **{weight * 0.15:.2f} kg**")
            st.write(f"✔ Jeera (5%): **{weight * 0.05:.2f} kg**")
            st.write(f"✔ Kali Mirch (4%): **{weight * 0.04:.2f} kg**")
            st.write(f"✔ Lal Mirch (3%): **{weight * 0.03:.2f} kg**")
            st.write(f"✔ Garam Masala (2%): **{weight * 0.02:.2f} kg**")
            st.write(f"✔ Hing (1%): **{weight * 0.01:.2f} kg**")
            
        elif salt_type == "Buknu":
            st.write(f"✔ Base Salt Mix (50%): **{weight * 0.50:.2f} kg**")
            st.write(f"✔ Harad Blend (15%): **{weight * 0.15:.2f} kg**")
            st.write(f"✔ Amla Powder (10%): **{weight * 0.10:.2f} kg**")
            st.write(f"✔ Haldi (8%): **{weight * 0.08:.2f} kg**")
            st.write(f"✔ Spice Blend (8%): **{weight * 0.08:.2f} kg**")
            st.write(f"✔ Pungent Boost (5%): **{weight * 0.05:.2f} kg**")
            st.write(f"✔ Mustard Oil (2%): **{weight * 0.02:.2f} kg**")
            st.write(f"✔ Hing (1%): **{weight * 0.01:.2f} kg**")
            st.write(f"💥 Naushadar (0.5%): **{weight * 0.005:.3f} kg** [FSSAI Max Cap]")
            st.write(f"💥 Aamzhor Mix (0.5%): **{weight * 0.005:.3f} kg**")
            
        elif salt_type == "Sheetal Namak":
            st.write(f"✔ Sendha Base (50%): **{weight * 0.50:.2f} kg**")
            st.write(f"✔ Regular/Black Salt (20%): **{weight * 0.20:.2f} kg**")
            st.write(f"✔ Pudina Powder (12%): **{weight * 0.12:.2f} kg**")
            st.write(f"✔ Saunf Powder (6%): **{weight * 0.06:.2f} kg**")
            st.write(f"✔ Mishri Powder (5%): **{weight * 0.05:.2f} kg**")
            st.write(f"✔ Sour Blend (4%): **{weight * 0.04:.2f} kg**")
            st.write(f"✔ Jaljeera (2.5%): **{weight * 0.025:.2f} kg**")
            st.write(f"💥 Naushadar (0.5%): **{weight * 0.005:.3f} kg**")

    # ------------------------------------------------------
    # MENU 2: MACHINERY
    # ------------------------------------------------------
    elif menu_selection == "🏭 Machinery":
        st.subheader("🏭 Factory Equipment Setup")
        machinery_data = [
            {"Name": "Impact Pulverizer", "Parameter": "2880 RPM / Cool Grind"},
            {"Name": "Ribbon Blender", "Parameter": "8-10 Mins Max Mix"},
            {"Name": "Dehumidifier", "Parameter": "Maintains <40% RH"},
            {"Name": "Moisture Analyzer", "Parameter": "Critical Lock <0.40%"},
            {"Name": "Band Sealer", "Parameter": "8-12 mm Extra-Wide Industrial Seal"}
        ]
        st.table(machinery_data)

    # ------------------------------------------------------
    # MENU 3: PACKAGING
    # ------------------------------------------------------
    elif menu_selection == "📦 Packaging":
        st.subheader("📦 Pouch Architecture")
        st.info("3-Layer Composite Laminate Matrix")
        st.write("• **Layers:** Matte PET / Aluminium Foil / Food-Grade LDPE")
        st.write("• **Thickness:** 110 to 120 Microns (Puncture Resistant)")
        st.write("• **Barrier:** 100% Moisture Block (No Clumping Guarantee)")

    # ------------------------------------------------------
    # MENU 4: FSSAI RULES
    # ------------------------------------------------------
    elif menu_selection == "⚖️ FSSAI Rules":
        st.subheader("⚖️ Regulatory Mandates")
        st.error("🚨 Naushadar (Ammonium Chloride) Cap strictly limited to 0.5% max by weight.")
        st.warning("🚨 Rear packaging panel must allocate 20% surface area for Nutritional Panel (Font Size 8).")
