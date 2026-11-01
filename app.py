import streamlit as st

# ==========================================================
# PRO-LEVEL TECH INTEGRATION: MY NANI'S SECRET & AGNIHOTRI CONSULTANCY
# ==========================================================

st.set_page_config(page_title="My Nani's Secret Portal", layout="wide")

st.title("My Nani's Secret ®")
st.subheader("Proprietary Automated Batching & Industrial Reference Platform")

# 1. AUTHENTICATION MODULE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.markdown("### 🔐 Secure Consultant Access Portal")
    user = st.text_input("Enterprise User ID")
    pas = st.text_input("Cryptographic Secret Password", type="password")
    if st.button("Authenticate Portal"):
        if user == "nani" and pas == "secret":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Authentication Failed: Invalid ID or Password.")
else:
    st.success("🔒 Authorization Successful! Welcome to Ayush Consultancy Dashboard.")
    
    # NAVIGATION TABS FOR DEEP ANALYSIS
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧮 Smart Batching Calculator", 
        "🏭 Advanced Industrial Machinery", 
        "📦 High-Barrier Packaging Specs", 
        "⚖️ FSSAI Regulatory Compliance"
    ])
    
    # ------------------------------------------------------
    # TAB 1: SMART BATCHING CALCULATOR
    # ------------------------------------------------------
    with tab1:
        st.markdown("### 🎯 Automated Precision Recipe Formulation")
        salt_type = st.selectbox("Select Target Blend Profile:", ["Nani Namak", "Buknu", "Sheetal Namak"])
        weight = st.number_input("Enter Desired Total Batch Yield (kg):", min_value=1.0, value=100.0, step=10.0)
        
        st.markdown("#### ⚖️ Exact Ingredient Dispensing Breakdown (Gram-Level Precision)")
        
        if salt_type == "Nani Namak":
            st.info("Formulation Profile: Premium Aromatic Blended Salt")
            st.write(f"✔ White Vacuum Salt (45.0%): **{weight * 0.450:.3f} kg**")
            st.write(f"✔ Sendha Namak / Rock Salt (25.0%): **{weight * 0.250:.3f} kg**")
            st.write(f"✔ Kala Namak / Black Salt (15.0%): **{weight * 0.150:.3f} kg**")
            st.write(f"✔ Roasted Cumin / Jeera (5.0%): **{weight * 0.050:.3f} kg**")
            st.write(f"✔ Black Pepper / Kali Mirch (4.0%): **{weight * 0.040:.3f} kg**")
            st.write(f"✔ Red Chili Powder (3.0%): **{weight * 0.030:.3f} kg**")
            st.write(f"✔ Proprietary Garam Masala Blend (2.0%): **{weight * 0.020:.3f} kg** (Clove, Cardamom, Cinnamon, Bay Leaf)")
            st.write(f"✔ Compounded Asafoetida / Hing (1.0%): **{weight * 0.010:.3f} kg**")
            
        elif salt_type == "Buknu":
            st.info("Formulation Profile: Traditional Therapeutic Spice-Infused Salt")
            st.write(f"✔ Base Salt Matrix (50.0%): **{weight * 0.500:.3f} kg** (Triple Refined, Sendha, Kala)")
            st.write(f"✔ Badi & Chhoti Harad Blend (15.0%): **{weight * 0.150:.3f} kg** (Digestive Catalyst)")
            st.write(f"✔ Dry Amla Powder (10.0%): **{weight * 0.100:.3f} kg** (Natural Vitamin C)")
            st.write(f"✔ Pure Turmeric / Haldi (8.0%): **{weight * 0.080:.3f} kg** (Antimicrobial & Color Agent)")
            st.write(f"✔ Digestive Herb Blend (8.0%): **{weight * 0.080:.3f} kg** (Jeera, Ajwain, Saunf)")
            st.write(f"✔ Pungent Bio-Enhancers (5.0%): **{weight * 0.050:.3f} kg** (Kali Mirch, Long Pippali)")
            st.write(f"✔ Cold-Pressed Mustard Oil (2.0%): **{weight * 0.020:.3f} kg** (Binding & Aroma Locking)")
            st.write(f"✔ Premium Asafoetida / Hing (1.0%): **{weight * 0.010:.3f} kg**")
            st.warning("⚠️ Critical FSSAI Restricted Ingredients Below:")
            st.write(f"💥 Ammonium Chloride / Pure Naushadar (0.5%): **{weight * 0.005:.3f} kg** [FSSAI Max Cap Permitted]")
            st.write(f"💥 Sour Aamzhor Salt Mix (0.5%): **{weight * 0.005:.3f} kg**")
            
        elif salt_type == "Sheetal Namak":
            st.info("Formulation Profile: Cooling Mint & Summer Refreshing Salt")
            st.write(f"✔ Sendha Namak Base (50.0%): **{weight * 0.500:.3f} kg**")
            st.write(f"✔ Regular & Black Salt Mix (20.0%): **{weight * 0.200:.3f} kg**")
            st.write(f"✔ Dehydrated Mint / Pudina Powder (12.0%): **{weight * 0.120:.3f} kg**")
            st.write(f"✔ Fennel Seeds / Saunf Powder (6.0%): **{weight * 0.060:.3f} kg**")
            st.write(f"✔ Refined Candy Sugar / Mishri Powder (5.0%): **{weight * 0.050:.3f} kg**")
            st.write(f"✔ Tangy Dry Blend (4.0%): **{weight * 0.040:.3f} kg** (Pomegranate Seeds & Aamzhor)")
            st.write(f"✔ Refreshing Jaljeera Concentrate (2.5%): **{weight * 0.025:.3f} kg**")
            st.warning("⚠️ Critical FSSAI Restricted Ingredients Below:")
            st.write(f"💥 Ammonium Chloride / Pure Naushadar (0.5%): **{weight * 0.005:.3f} kg**")

    # ------------------------------------------------------
    # TAB 2: ADVANCED INDUSTRIAL MACHINERY
    # ------------------------------------------------------
    with tab2:
        st.markdown("### 🏭 Factory Equipment Fleet & Technical Specifications")
        st.write("This standardized machinery layout ensures structural consistency, hygiene compliance, and efficient bulk processing.")
        
        machinery_data = [
            {"Equipment Name": "SS 304 Impact Pulverizer (1-2 HP)", "Operational Role": "Cool-grinding of raw whole spices to protect volatile organic essential oils.", "Key Parameter": "2880 RPM / No Heat Generation"},
            {"Equipment Name": "SS 304 Ribbon Blender", "Operational Role": "Homogeneous mixing of dense salts with lighter herbal extracts.", "Key Parameter": "8-10 Minutes Mix Cycle Limit"},
            {"Equipment Name": "Industrial Dehumidifier Units", "Operational Role": "Prevents environmental ambient moisture from causing salt lump formation.", "Key Parameter": "Maintains <40% Relative Humidity"},
            {"Equipment Name": "Halogen Moisture Analyzer", "Operational Role": "Instant QA lab validation of moisture content before authorizing packaging.", "Key Parameter": "Critical Control Cap <0.40% Moisture"},
            {"Equipment Name": "Continuous Band Sealer (FR-900)", "Operational Role": "Automated high-speed airtight sealing of filled pouches.", "Key Parameter": "8-12 mm Extra-Wide Industrial Seal"},
            {"Equipment Name": "Inline Vibratory Sifter", "Operational Role": "Filters out foreign elements and coarse crystals before packing line.", "Key Parameter": "40-Mesh Safety Screen"},
            {"Equipment Name": "Air Compressor & Form-Fill-Seal", "Operational Role": "Pneumatic filling line for high-volume automated production.", "Key Parameter": "6 Bar Constant Pressure"},
            {"Equipment Name": "Rare-Earth Pouch Magnet Separator", "Operational Role": "Inline magnetic filtration to capture zero trace metal particles.", "Key Parameter": "12,000 Gauss Surface Intensity"}
        ]
        st.table(machinery_data)

    # ------------------------------------------------------
    # TAB 3: HIGH-BARRIER PACKAGING SPECS
    # ------------------------------------------------------
    with tab3:
        st.markdown("### 📦 Commercial Packaging Material Architecture (200g Packs)")
        st.error("🚨 Salt Blends are Highly Hygroscopic. Standard Plastics Will Cause Product Failure.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔬 Structural Engineering")
            st.write("• **Composite Matrix:** 3-Layer Solid Laminate Architecture")
            st.write("• **Layer Breakup:** Matte PET (Outer Aesthetic) / Aluminium Foil (Core Vapor Barrier) / Food-Grade LDPE (Inner Heat Sealant Layer)")
            st.write("• **Total Structural Thickness:** **110 to 120 Microns** (High burst and puncture score)")
        with col2:
            st.markdown("#### 🎯 Functional Performance")
            st.write("• **Moisture & Oxygen Barrier:** 100% Hermetic Block (Guarantees 12 months shelf-life without clumping)")
            st.write("• **Closure Mechanism:** Heavy-Duty Interlocking Reclosable Zip-Lock Profile")
            st.write("• **Surface Optics:** Premium Matte Coating to fit the organic branding of 'My Nani's Secret'")

    # ------------------------------------------------------
    # TAB 4: FSSAI REGULATORY COMPLIANCE
    # ------------------------------------------------------
    with tab4:
        st.markdown("### ⚖️ Legal FSSAI Compliance & Toxicity Control Rules")
        st.info("Compliance Audit Parameters for Agnihotri Food Consultancy Projects")
        
        st.markdown("#### 📑 Crucial Legal Standards for Blended Salts:")
        st.error("1. **Ammonium Chloride (Naushadar Limits):** As per FSSAI regulations, industrial food-grade Ammonium Chloride in proprietary spice salts cannot cross **0.5% of total batch mass**. Exceeding this limit constitutes a legal offense and causes computational taste rejection.")
        st.warning("2. **Heavy Metal Maximum Permissible Caps:** Arsenic < 0.1 ppm, Lead < 2.0 ppm, Cadmium < 0.1 ppm. Annual compliance lab testing through NABL accredited labs is mandatory.")
        st.write("3. **Mandatory Labeling Declarations (FSSAI 2026 Guidelines):** The CDR packaging graphics block must strictly maintain a designated 20% window on the rear panel for Font-Size 8 Nutritional Facts Panel, Batch Numbering, MFG Date, Best Before Timeline, and explicit Veg Logo.")
