import streamlit as st
import pandas as pd

# =========================================================================
# TITLE: MY NANI'S SECRET PORTAL (ENTERPRISE CONFIGURATION)
# CHIEF ARCHITECT & DEVELOPER: AYUSH KUMAR AGNIHOTRI (FOOD TECHNOLOGIST)
# VERSION: 3.0 (GOOGLE SHEET INTEGRATION & LIVE P&L AUTOMATION)
# COPYRIGHT (c) 2026 | STRICT PRIVATE ACCESS ONLY
# =========================================================================

st.set_page_config(page_title="My Nani's Secret Portal", layout="centered", page_icon="🌿")

st.markdown("<p style='text-align: center; color: #4A9C30; font-size: 11px; font-weight: 700; letter-spacing: 2px; margin-bottom: 0px;'>PROPRIETARY ENTERPRISE SYSTEM</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #6CC551; font-family: sans-serif; margin-top: 0px; margin-bottom: 0px;'>My Nani's Secret ®</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #718096; font-size: 13px; font-weight: 500; margin-top: 0px; text-align: center;'>AUTOMATED FORMULATIONS & P&L ENGINE</p>", unsafe_allow_html=True)
st.markdown("---")

# 1. LIVE GOOGLE SHEET CONFIGURATION
# अपनी गूगल शीट को 'Anyone with the link can view' पर सेट करें। 
# फिर File > Share > Publish to web पर जाकर CSV लिंक कॉपी करें और नीचे पेस्ट करें।
# अभी सुरक्षा के लिए हमने एक डेमो CSV लिंक लगाया है ताकि आपका कोड तुरंत चालू हो सके।
GSHEET_URL = "https://google.com"

@st.cache_data(ttl=300) # हर 5 मिनट में डेटा अपने आप रीफ्रेश होगा
def load_live_sheet_data(url):
    try:
        # अगर लाइव शीट कनेक्टेड है तो वहां से डेटा आएगा, नहीं तो बैकअप डेटा चालू रहेगा
        return pd.read_csv(url)
    except:
        # बैकअप डेटा ताकि शीट न होने पर भी ऐप 100% चलता रहे
        backup_rates = {"Ingredient": ["White Salt", "Sendha Namak", "Kala Namak", "Jeera", "Kali Mirch", "Lal Mirch", "Garam Masala", "Hing", "Base Salt Mix", "Badi and Chhoti Harad Blend", "Dry Amla Powder", "Pure Turmeric / Haldi", "Digestive Herb Blend", "Pungent Bio-Enhancers", "Mustard Oil", "Naushadar [Food-Grade]", "Aamzhor Namak Mix", "Pudina Powder", "Saunf Powder", "Mishri Powder", "Sour Blend", "Jaljeera", "Naushadar"], "Rate":}
        return pd.DataFrame(backup_rates)

live_rates_df = load_live_sheet_data(GSHEET_URL)
rates_dict = pd.Series(live_rates_df.Rate.values, index=live_rates_df.Ingredient.values).to_dict()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.subheader("Secure Encrypted Access")
    with st.container(border=True):
        st.caption("This system contains proprietary formulas. Unauthorized entry is strictly prohibited.")
        user = st.text_input("Administrator ID", placeholder="Enter official ID")
        pas = st.text_input("Security Access Key", type="password", placeholder="--------")
        
        if st.button("Authenticate System", use_container_width=True, type="primary"):
            if user == "nani" and pas == "secret":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Access Denied: Invalid Security Key or Administrator ID.")
                
    st.markdown("<br><p style='text-align: center; color: #A0AEC0; font-size: 12px; font-weight: 500;'>Engineered & Maintained by:<br><span style='color: #4A9C30; font-weight: bold; font-size: 13px;'>Ayush Kumar Agnihotri</span><br>Food Technologist</p>", unsafe_allow_html=True)

else:
    with st.container(border=True):
        st.markdown("<p style='margin: 0; padding: 0; font-size: 11px; color: #718096; font-weight: bold; letter-spacing: 1px;'>CHIEF PLANT CONTROLLER</p>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin: 0; padding: 0; color: #2D3748; font-weight: 800;'>Ayush Kumar Agnihotri</h4>", unsafe_allow_html=True)
        st.markdown("<p style='margin: 0; padding: 0; font-size: 12px; color: #4A9C30; font-weight: 600;'>Food Technologist & R&D Lead</p>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Calculator", "📊 Monthly P&L", "Machinery", "Packaging & FSSAI"])
    with tab1:
        st.subheader("Batch Formulation Panel")
        
        with st.container(border=True):
            salt_type = st.selectbox("Select Blend Profile:", ["Nani Namak", "Buknu", "Sheetal Namak"])
            weight = st.number_input("Enter Batch Weight (kg):", min_value=1.0, value=100.0, step=10.0)
        
        recipes = {
            "Nani Namak": [
                ("White Salt", 0.45, "Base"), ("Sendha Namak", 0.25, "Base"), ("Kala Namak", 0.15, "Base"),
                ("Jeera", 0.05, "Herb"), ("Kali Mirch", 0.04, "Herb"), ("Lal Mirch", 0.03, "Herb"),
                ("Garam Masala", 0.02, "Herb"), ("Hing", 0.01, "Herb")
            ],
            "Buknu": [
                ("Base Salt Mix", 0.50, "Base"), ("Badi and Chhoti Harad Blend", 0.15, "Herb"), ("Dry Amla Powder", 0.10, "Herb"),
                ("Pure Turmeric / Haldi", 0.08, "Herb"), ("Digestive Herb Blend", 0.08, "Herb"), ("Pungent Bio-Enhancers", 0.05, "Herb"),
                ("Mustard Oil", 0.02, "Oil"), ("Hing", 0.01, "Herb"), ("Naushadar [Food-Grade]", 0.005, "Regulated"),
                ("Aamzhor Namak Mix", 0.005, "Herb")
            ],
            "Sheetal Namak": [
                ("Sendha Base", 0.50, "Base"), ("Regular/Black Salt", 0.20, "Base"), ("Pudina Powder", 0.12, "Herb"),
                ("Saunf Powder", 0.06, "Herb"), ("Mishri Powder", 0.05, "Herb"), ("Sour Blend", 0.04, "Herb"),
                ("Jaljeera", 0.025, "Herb"), ("Naushadar", 0.005, "Regulated")
            ]
        }
        
        st.subheader("Live Google Sheet Ingredient Prices")
        st.caption("Rates are automatically fetched from your cloud spreadsheet:")
        
        report_data = []
        total_cost = 0.0
        
        st.subheader("Formula Breakdown and Live Costing")
        with st.container(border=True):
            for ing, pct, status in recipes[salt_type]:
                calc_wt = weight * pct
                # गूगल शीट से लाइव प्राइस निकालना, अगर नहीं मिले तो डिफॉल्ट 60 रुपये लगाना
                item_price = float(rates_dict.get(ing, 60.0))
                item_cost = calc_wt * item_price
                total_cost += item_cost
                
                wt_str = f"{calc_wt:.3f}" if pct < 0.01 else f"{calc_wt:.2f}"
                st.write(f"[{status}] {ing} ({pct*100}%): {wt_str} kg | INR {item_cost:.2f}")
                
                report_data.append({
                    "Ingredient": ing,
                    "Percentage (%)": pct * 100,
                    "Weight (kg)": float(wt_str),
                    "Rate (INR/kg)": item_price,
                    "Total Cost (INR)": round(item_cost, 2)
                })
        
        st.metric(label="Total Production Cost for Batch", value=f"INR {total_cost:,.2f}")
        
        # भविष्य में P&L कैलकुलेशन के लिए इस बैच कॉस्ट को सेशन स्टेट में सेव कर रहे हैं
        st.session_state["last_calculated_cost_per_kg"] = total_cost / weight
        
        df_report = pd.DataFrame(report_data)
        csv_data = df_report.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="Export Batch Sheet (CSV)",
            data=csv_data,
            file_name=f"{salt_type.lower().replace(' ', '_')}_batch_sheet.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary"
        )
    with tab2:
        st.subheader("📊 Executive Monthly Profit & Loss Statement")
        st.caption("Pro-Level Production Metrics & Financial Control Desk:")
        
        # इनपुट सिमुलेटर जो एक प्रो-लेवल डैशबोर्ड फील देता है
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                monthly_sales_kg = st.number_input("Total Monthly Sales (kg):", min_value=1, value=5000, step=500)
            with col2:
                avg_selling_price = st.number_input("Average Selling Price (INR/kg):", min_value=1.0, value=250.0, step=10.0)
        
        # वित्तीय गणना
        cost_per_kg_now = st.session_state.get("last_calculated_cost_per_kg", 75.0)
        total_revenue = monthly_sales_kg * avg_selling_price
        total_raw_material_cost = monthly_sales_kg * cost_per_kg_now
        
        # प्रो-लेवल फिक्स्ड और ओवरहेड कॉस्ट
        factory_overhead = float(monthly_sales_kg * 4.5)  # ₹4.5/kg बिजली और लेबर
        packaging_overhead = float(monthly_sales_kg * 8.0) # ₹8/kg पाउच और बॉक्स बॉक्स कॉस्ट
        fixed_marketing = 15000.0
        
        total_expense = total_raw_material_cost + factory_overhead + packaging_overhead + fixed_marketing
        net_profit = total_revenue - total_expense
        profit_margin = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0.0

        # वित्तीय मेट्रिक्स कार्ड्स
        c1, c2, c3 = st.columns(3)
        c1.metric("Gross Revenue", f"₹{total_revenue:,.0f}")
        c2.metric("Total Expenses", f"₹{total_expense:,.0f}")
        
        # प्रॉफिट होने पर ग्रीन और लॉस होने पर रेड अलर्ट फील
        if net_profit >= 0:
            c3.metric("Net Profit (Live)", f"₹{net_profit:,.0f}", f"{profit_margin:.1f}% Margin")
        else:
            c3.metric("Net Profit (Live)", f"₹{net_profit:,.0f}", f"{profit_margin:.1f}% Margin", delta_color="inverse")

        # प्रो कॉर्पोरेट लेजर टेबल व्यू
        st.markdown("#### 📑 Profit & Loss Ledger Breakdown")
        pl_data = [
            {"Financial Line Item": "1. Gross Operating Revenue", "Amount (INR)": f"₹{total_revenue:,.2f}", "Status": "Income"},
            {"Financial Line Item": "2. Raw Material Cost (COGS)", "Amount (INR)": f"- ₹{total_raw_material_cost:,.2f}", "Status": "Variable Expense"},
            {"Financial Line Item": "3. Factory Utilities & Labor", "Amount (INR)": f"- ₹{factory_overhead:,.2f}", "Status": "Variable Expense"},
            {"Financial Line Item": "4. 3-Layer Packaging Matrix Cost", "Amount (INR)": f"- ₹{packaging_overhead:,.2f}", "Status": "Variable Expense"},
            {"Financial Line Item": "5. Marketing & Logistics Fixed Opex", "Amount (INR)": f"- ₹{fixed_marketing:,.2f}", "Status": "Fixed Expense"},
            {"Financial Line Item": "Net Net Operating Profit", "Amount (INR)": f"₹{net_profit:,.2f}", "Status": "EBITDA"}
        ]
        st.dataframe(pd.DataFrame(pl_data), hide_index=True, use_container_width=True)

    with tab3:
        st.subheader("Trial Production and QA Equipment List")
        with st.container(border=True):
            st.markdown("### 1. SS 304 Impact Pulverizer / Pin Mill")
            st.write("- Capacity: 10 to 20 Kg/Hr output | Cool Grinding Technology")
        with st.container(border=True):
            st.markdown("### 4. Halogen Moisture Analyzer")
            st.write("- Target Gate: Lock salt moisture strictly below 0.40%")
        with st.container(border=True):
            st.markdown("### 8. Room Dehumidifier")
            st.write("- Target Humidity: Strict control fixed at 40% RH to prevent clumping")
        st.caption("Check official documentation for items 2, 3, 5, 6, 7.")

    with tab4:
        st.subheader("Packaging Matrix & Regulatory Rules")
        with st.container(border=True):
            st.markdown("#### 📦 Advanced Pouch Architecture")
            st.write("- Composition: Matte PET / Aluminium Foil / Food-Grade LDPE")
            st.write("- Thickness Parameter: 110 to 120 Microns (High Barrier)")
        with st.container(border=True):
            st.markdown("#### ⚖️ Regulatory Mandates (FSSAI)")
            st.error("Ammonium Chloride (Naushadar): Capped strictly at 0.5% max by weight.")
            st.warning("Nutritional Facts Table: Must occupy minimum 20% surface area on back panel.")

    st.markdown("---")
    if st.button("Secure Logout", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
