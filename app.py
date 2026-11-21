import streamlit as st
import io
import csv

# =========================================================================
# TITLE: MY NANI'S SECRET PORTAL (ENTERPRISE PRO V5.0 - ULTRA FAST ENGINE)
# CHIEF ARCHITECT: AYUSH KUMAR AGNIHOTRI (FOOD TECHNOLOGIST)
# =========================================================================

st.set_page_config(
    page_title="My Nani's Secret ® | Pro Portal",
    layout="centered",
    page_icon="🌿",
    initial_sidebar_state="collapsed"
)

# Custom Pro-Level UI Styling (Lightweight CSS for Instant Mobile & Desktop Render)
st.markdown("""
<style>
    .block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
    .brand-sub {text-align: center; color: #38A169; font-size: 11px; font-weight: 800; letter-spacing: 2px; margin-bottom: 0;}
    .brand-title {text-align: center; color: #2F855A; font-family: sans-serif; font-size: 2.2rem; font-weight: 900; margin: 0;}
    .brand-desc {text-align: center; color: #718096; font-size: 12px; font-weight: 600; margin-top: 2px; margin-bottom: 1rem;}
    .controller-card {background: linear-gradient(135deg, #F0FFF4 0%, #E6FFFA 100%); padding: 14px 18px; border-radius: 10px; border-left: 5px solid #38A169; margin-bottom: 15px;}
    .stButton>button {border-radius: 8px; font-weight: 700;}
</style>
<p class='brand-sub'>PROPRIETARY ENTERPRISE SYSTEM</p>
<h1 class='brand-title'>My Nani's Secret ®</h1>
<p class='brand-desc'>R&D FORMULATIONS • 5G STICK-PACK COSTING • LIVE P&L ENGINE</p>
""", unsafe_allow_html=True)

# 1. IN-MEMORY MASTER RATE DATABASE (INSTANT ACCESS - ZERO NETWORK LAG)
RATES_DB = {
    "White Salt": 20.0, "Sendha Namak": 60.0, "Sendha Base": 60.0,
    "Kala Namak": 50.0, "Regular/Black Salt": 35.0, "Base Salt Mix": 40.0,
    "Jeera (Cumin)": 320.0, "Kali Mirch (Black Pepper)": 680.0, "Lal Mirch (Red Chilli)": 280.0,
    "Garam Masala": 450.0, "Hing (Compounded)": 1500.0, "Haldi (Turmeric)": 210.0,
    "Dhaniya (Coriander)": 160.0, "Saunf (Fennel)": 240.0, "Methi (Fenugreek)": 140.0,
    "Elaichi (Green Cardamom)": 2600.0, "Badi & Chhoti Harad Blend": 350.0,
    "Dry Amla Powder": 200.0, "Digestive Herb Blend": 300.0, "Pungent Bio-Enhancers": 400.0,
    "Mustard Oil": 170.0, "Naushadar [Food-Grade]": 80.0, "Aamzhor Namak Mix": 120.0,
    "Pudina Powder": 250.0, "Mishri Powder": 100.0, "Sour Blend": 150.0, "Jaljeera": 180.0
}

RECIPES_DB = {
    "🌿 Nani Namak (Signature Blend)": [
        ("White Salt", 0.45, "Base"), ("Sendha Namak", 0.25, "Base"), ("Kala Namak", 0.15, "Base"),
        ("Jeera (Cumin)", 0.05, "Herb"), ("Kali Mirch (Black Pepper)", 0.04, "Herb"),
        ("Lal Mirch (Red Chilli)", 0.03, "Herb"), ("Garam Masala", 0.02, "Herb"), ("Hing (Compounded)", 0.01, "Herb")
    ],
    "🌿 Buknu (Ayurvedic Digestive)": [
        ("Base Salt Mix", 0.50, "Base"), ("Badi & Chhoti Harad Blend", 0.15, "Herb"), ("Dry Amla Powder", 0.10, "Herb"),
        ("Haldi (Turmeric)", 0.08, "Herb"), ("Digestive Herb Blend", 0.08, "Herb"), ("Pungent Bio-Enhancers", 0.05, "Herb"),
        ("Mustard Oil", 0.02, "Oil"), ("Hing (Compounded)", 0.01, "Herb"), ("Naushadar [Food-Grade]", 0.005, "Regulated"),
        ("Aamzhor Namak Mix", 0.005, "Herb")
    ],
    "🌿 Sheetal Namak (Cooling Blend)": [
        ("Sendha Base", 0.50, "Base"), ("Regular/Black Salt", 0.20, "Base"), ("Pudina Powder", 0.12, "Herb"),
        ("Saunf (Fennel)", 0.06, "Herb"), ("Mishri Powder", 0.05, "Herb"), ("Sour Blend", 0.04, "Herb"),
        ("Jaljeera", 0.025, "Herb"), ("Naushadar [Food-Grade]", 0.005, "Regulated")
    ],
    "🌶️ Sampler: Jeera Powder (100% Pure)": [("Jeera (Cumin)", 1.00, "Single Spice")],
    "🌶️ Sampler: Haldi Powder (100% Pure)": [("Haldi (Turmeric)", 1.00, "Single Spice")],
    "🌶️ Sampler: Garam Masala (Royal Blend)": [("Garam Masala", 1.00, "Spice Blend")],
    "🌶️ Sampler: Kali Mirch Powder": [("Kali Mirch (Black Pepper)", 1.00, "Single Spice")],
    "🌶️ Sampler: Elaichi Powder": [("Elaichi (Green Cardamom)", 1.00, "Single Spice")],
    "🌶️ Sampler: Lal Mirch Powder": [("Lal Mirch (Red Chilli)", 1.00, "Single Spice")],
    "🌶️ Sampler: Dhaniya Powder": [("Dhaniya (Coriander)", 1.00, "Single Spice")],
    "🌶️ Sampler: Saunf Powder": [("Saunf (Fennel)", 1.00, "Single Spice")],
    "🌶️ Sampler: Methi Powder": [("Methi (Fenugreek)", 1.00, "Single Spice")],
    "🌶️ Sampler: Hing Powder": [("Hing (Compounded)", 1.00, "Single Spice")]
}

# Authentication State
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    with st.container(border=True):
        st.subheader("🔐 Secure Client & Admin Login")
        st.caption("Authorized access only. Contains proprietary R&D formulations & vendor matrix.")
        user = st.text_input("Administrator ID", placeholder="Enter ID")
        pas = st.text_input("Security Access Key", type="default", placeholder="••••••••")

        
        if st.button("Authenticate & Launch Portal", use_container_width=True, type="primary"):
            if user.strip().lower() == "nani" and pas.strip() == "secret":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Access Denied: Invalid Credentials.")
                
    st.markdown("<p style='text-align: center; color: #718096; font-size: 12px; margin-top: 15px;'>Architected & Maintained by: <b style='color:#2F855A;'>Ayush Kumar Agnihotri</b> (Food Technologist)</p>", unsafe_allow_html=True)

else:
    # Top Executive Banner
    st.markdown("""
    <div class='controller-card'>
        <div style='font-size: 10px; color: #2F855A; font-weight: 800; letter-spacing: 1.5px;'>CHIEF FOOD TECHNOLOGIST & R&D ARCHITECT</div>
        <div style='font-size: 18px; color: #1A202C; font-weight: 800;'>Ayush Kumar Agnihotri</div>
        <div style='font-size: 12px; color: #4A5568;'>Product Formulation • Packaging Engineering • FSSAI Compliance</div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧮 Formulation & 5g Cost", "📊 Monthly P&L", "⚙️ Machinery", "📦 Packaging", "⚖️ FSSAI"])

    # TAB 1: FORMULATION & 5G STICK PACK COSTING
    with tab1:
        with st.container(border=True):
            c1, c2 = st.columns([2, 1])
            with c1:
                product = st.selectbox("Select SKU / Formulation:", list(RECIPES_DB.keys()))
            with c2:
                batch_kg = st.number_input("Batch Size (kg):", min_value=1.0, value=100.0, step=10.0)
            
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                stick_g = st.selectbox("Single-Serve Stick Weight (g):", [5.0, 2.0, 10.0], index=0)
            with col_s2:
                pack_cost_per_stick = st.number_input("Stick Laminate + Filling Cost (₹):", min_value=0.0, value=0.65, step=0.05)

        st.markdown("#### 📋 Bill of Materials (BOM) & Live Rate Matrix")
        rows = []
        total_rm_cost = 0.0

        with st.container(border=True):
            for ing, pct, tag in RECIPES_DB[product]:
                wt_kg = batch_kg * pct
                rate = RATES_DB.get(ing, 100.0)
                cost = wt_kg * rate
                total_rm_cost += cost
                wt_disp = f"{wt_kg:.3f}" if pct < 0.01 else f"{wt_kg:.2f}"
                st.write(f"**`[{tag}]` {ing}** ({pct*100:.1f}%) ➔ `{wt_disp} kg` | **₹{cost:,.2f}**")
                rows.append([ing, f"{pct*100:.1f}%", wt_disp, rate, round(cost, 2)])

        rm_per_kg = total_rm_cost / batch_kg
        rm_per_stick = (rm_per_kg / 1000.0) * stick_g
        finished_stick_cost = rm_per_stick + pack_cost_per_stick
        sampler_box_10_cost = (finished_stick_cost * 10) + 18.0  # ₹18 rigid box cost

        st.session_state["active_rm_per_kg"] = rm_per_kg

        m1, m2, m3 = st.columns(3)
        m1.metric("Raw Cost / Kg", f"₹{rm_per_kg:,.2f}")
        m2.metric(f"Finished {int(stick_g)}g Stick", f"₹{finished_stick_cost:.2f}", help="Includes Spice + Foil Stick + Filling")
        m3.metric("10-Stick Sampler Box", f"₹{sampler_box_10_cost:.2f}", help="10 Finished Sticks + Rigid Box")

        # Fast CSV Export without Pandas overhead
        csv_buffer = io.StringIO()
        writer = csv.writer(csv_buffer)
        writer.writerow(["Ingredient", "Percentage", "Weight (kg)", "Rate (INR/kg)", "Total Cost (INR)"])
        writer.writerows(rows)

        st.download_button(
            label="📥 Download Batch Sheet (CSV)",
            data=csv_buffer.getvalue(),
            file_name=f"Batch_Sheet_{batch_kg}kg.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary"
        )

    # TAB 2: MONTHLY P&L ENGINE
    with tab2:
        st.subheader("📊 Executive Monthly P&L Projection")
        with st.container(border=True):
            p1, p2 = st.columns(2)
            with p1:
                sales_kg = st.number_input("Monthly Volume (kg):", min_value=50, value=5000, step=250)
            with p2:
                sell_price = st.number_input("Selling Price (₹/kg):", min_value=50.0, value=350.0, step=10.0)

        rm_kg = st.session_state.get("active_rm_per_kg", 85.0)
        revenue = sales_kg * sell_price
        cogs = sales_kg * rm_kg
        utilities = sales_kg * 5.0
        packaging = sales_kg * 18.0
        marketing_fixed = 15000.0
        total_exp = cogs + utilities + packaging + marketing_fixed
        net_profit = revenue - total_exp
        margin = (net_profit / revenue * 100) if revenue > 0 else 0

        k1, k2, k3 = st.columns(3)
        k1.metric("Gross Revenue", f"₹{revenue:,.0f}")
        k2.metric("Total Opex + COGS", f"₹{total_exp:,.0f}")
        k3.metric("Net EBITDA Profit", f"₹{net_profit:,.0f}", f"{margin:.1f}% Margin")
        st.table([

            {"Particulars": "1. Gross Sales Revenue", "Amount (INR)": f"₹{revenue:,.2f}"},
            {"Particulars": "2. Raw Material Cost (COGS)", "Amount (INR)": f"- ₹{cogs:,.2f}"},
            {"Particulars": "3. Plant Utilities & Skilled Labor", "Amount (INR)": f"- ₹{utilities:,.2f}"},
            {"Particulars": "4. Stick-Pack & Rigid Box Packaging", "Amount (INR)": f"- ₹{packaging:,.2f}"},
            {"Particulars": "5. Fixed Marketing & Logistics", "Amount (INR)": f"- ₹{marketing_fixed:,.2f}"},
            {"Particulars": "NET OPERATING PROFIT", "Amount (INR)": f"₹{net_profit:,.2f}"}
        ])

    # TAB 3: MACHINERY & VENDORS
    with tab3:
        st.subheader("⚙️ Turnkey Plant & QA Machinery Matrix")
        machines = [
            ("1. Multi-Track Stick Pack FFS Machine (5g)", "Vendor: Nichrome India / Samarth Packaging | Output: 40-60 sticks/min | Nitrogen Flushing Enabled for aroma lock."),
            ("2. SS 304 Cool-Grinding Impact Pulverizer (2 HP)", "Vendor: Jas Enterprise / Friends & Co. | Capacity: 15-20 Kg/Hr | Single Phase | Zero volatile oil loss."),
            ("3. SS 304 GMP Ribbon Blender / Mixing Tub (50L)", "Mirror finish food-grade stainless steel for homogeneous spice & salt micro-blending."),
            ("4. Halogen Moisture Analyzer (0.01% Accuracy)", "Approved: Shimadzu MOC63u / Wensar LMB-1 | Strict moisture lock < 0.40% to prevent caking."),
            ("5. Continuous Band Sealer FR-900 + Batch Coder", "Vendor: Continental Packaging | 10mm hermetic seal with online MRP/Batch printing."),
            ("6. Room Dehumidifier (20L/Day)", "Approved: Origin / White Westinghouse | Maintains < 40% RH in packing room.")
        ]
        for title, desc in machines:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(desc)

    # TAB 4: PACKAGING ARCHITECTURE
    with tab4:
        st.subheader("📦 5g Stick-Pack & Sampler Box Specs")
        with st.container(border=True):
            st.success("✅ High-Barrier Aroma-Lock Laminate Verified")
            st.write("- **Stick Film Structure:** `12μ Matte PET / 9μ Aluminium Foil / 50μ Food-Grade LDPE` (Total ~110 Microns)")
            st.write("- **Stick Dimensions:** `25mm Width × 110mm Length` (5g Net Weight per stick)")
            st.write("- **Outer Sampler Box:** `350 GSM ITC Cyber XL Board` with Matte Lamination & Magnetic/Tuck Flap (Holds 10 Sticks = 50g)")
            st.write("- **Shelf Life:** 12 Months guaranteed under <40% RH storage.")

    # TAB 5: FSSAI COMPLIANCE
    with tab5:
        st.subheader("⚖️ FSSAI Regulatory & Labeling Mandates")
        with st.container(border=True):
            st.error("🚨 Ammonium Chloride (Naushadar): Strictly capped at 0.5% max by weight under FSSAI category rules.")
            st.warning("⚠️ Single-Serve Exemption: For packs under 10g (5g sticks), outer Sampler Box must carry complete Nutritional Table, FSSAI License, Batch No, and Allergen info.")

    if st.button("🔒 Secure Logout", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
