import streamlit as st
from streamlit.components.v1 import html
from fpdf import FPDF

def calculate_remaining_income(monthly_income, education, food, rent, transport, general_expenses):
    total_expenses = education + food + rent + transport + general_expenses
    remaining_income = monthly_income - total_expenses
    remaining_after_deduction = remaining_income - (0.3 * remaining_income)
    return remaining_after_deduction

def generate_html_report(remaining_amount, monthly_income):
    report = "<html>"
    report += "<head>"
    report += "<style>"
    report += "body { font-family: Arial, sans-serif; }"
    report += "h2 { color: #007bff; }"
    report += "h3 { color: #28a745; }"
    report += "p { font-size: 16px; }"
    report += "ul { list-style-type: disc; margin-left: 20px; }"
    report += "li { margin-bottom: 8px; }"
    report += "</style>"
    report += "</head>"
    report += "<body>"

    report += f"<h2>Monthly Income Analysis Report</h2>"
    report += f"<p>Remaining Amount after Expenses: {remaining_amount}</p>"

    if monthly_income <= 0:
        report += "<h4>Please enter you income and other expenses!</h4>"

    elif remaining_amount < 5000:
        save_percentage = 60
        sip_percentage = 25
        bonds_percentage = 15
        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Save in a savings account upto: {remaining_amount * save_percentage / 100} Rs. ({save_percentage}%)</li>"
        report += f"<li>Invest in SIP mutual funds upto: {remaining_amount * sip_percentage / 100} Rs. ({sip_percentage}%)</li>"
        report += f"<li>Invest in bonds to diversify the portfolio upto: {remaining_amount * bonds_percentage / 100} Rs. ({bonds_percentage}%)</li>"
        report += "</ul>"

    elif 5000 < remaining_amount < 20000:
        direct_equities_percentage = 25
        rbi_bonds_percentage = 45
        corporate_bonds_percentage = 30
        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Invest in direct equities upto: {remaining_amount * direct_equities_percentage / 100} Rs. ({direct_equities_percentage}%)</li>"
        report += f"<li>Invest in RBI bonds upto: {remaining_amount * rbi_bonds_percentage / 100} Rs. ({rbi_bonds_percentage}%)</li>"
        report += f"<li>Invest in corporate bonds upto: {remaining_amount * corporate_bonds_percentage / 100} Rs. ({corporate_bonds_percentage}%)</li>"
        report += "</ul>"

    elif 20000 < remaining_amount < 100000:
        fixed_deposits_percentage = 40
        gold_percentage = 30
        gold_bonds_percentage = 10
        
        remaining_after_gold_bonds = remaining_amount - remaining_amount * ((fixed_deposits_percentage + gold_percentage + gold_bonds_percentage) / 100)
        
        stocks_upper_percentage = 70
        stocks_middle_percentage = 18
        stocks_lower_percentage = 12

        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Invest in fixed deposits upto: {remaining_amount * fixed_deposits_percentage / 100} Rs. ({fixed_deposits_percentage}%)</li>"
        report += f"<li>Invest in gold upto: {remaining_amount * gold_percentage / 100} Rs. ({gold_percentage}%)</li>"
        report += f"<li>Invest in gold bonds upto: {remaining_amount * gold_bonds_percentage / 100} Rs. ({gold_bonds_percentage}%)</li>"
        report += f"<li>Invest in stocks (Upper) upto: {remaining_after_gold_bonds * stocks_upper_percentage / 100} Rs. ({stocks_upper_percentage}%)</li>"
        report += f"<li>Invest in stocks (Middle) upto: {remaining_after_gold_bonds * stocks_middle_percentage / 100} Rs. ({stocks_middle_percentage}%)</li>"
        report += f"<li>Invest in stocks (Lower) upto: {remaining_after_gold_bonds * stocks_lower_percentage / 100} Rs. ({stocks_lower_percentage}%)</li>"
        report += "</ul>"

    elif remaining_amount >= 100000:
        real_estate_percentage = 40
        gold_percentage = 12
        mutual_funds_percentage = 18

        
        remaining_aftermutual_funds_percentage = remaining_amount - remaining_amount * ((real_estate_percentage + gold_percentage + mutual_funds_percentage) / 100)
        
        direct_equities_upper_percentage = 30
        direct_equities_middle_percentage = 45
        direct_equities_lower_percentage = 25

        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Invest in real estate upto: {remaining_amount * real_estate_percentage / 100} Rs. ({real_estate_percentage}%)</li>"
        report += f"<li>Invest in gold upto: {remaining_amount * gold_percentage / 100} Rs. ({gold_percentage}%)</li>"
        report += f"<li>Invest in mutual funds upto: {remaining_amount * mutual_funds_percentage / 100} Rs. ({mutual_funds_percentage}%)</li>"
        report += f"<li>Invest in direct equities (Upper) upto: {remaining_aftermutual_funds_percentage * direct_equities_upper_percentage / 100} Rs. ({direct_equities_upper_percentage}%)</li>"
        report += f"<li>Invest in direct equities (Middle) upto: {remaining_aftermutual_funds_percentage * direct_equities_middle_percentage / 100} Rs. ({direct_equities_middle_percentage}%)</li>"
        report += f"<li>Invest in direct equities (Lower) upto: {remaining_aftermutual_funds_percentage * direct_equities_lower_percentage / 100} Rs. ({direct_equities_lower_percentage}%)</li>"
        report += "</ul>"

    report += "</body>"
    report += "</html>"
    return report


def generate_pdf_report(remaining_amount, monthly_income):
    

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Monthly Income Analysis Report", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Remaining Amount after Expenses: {remaining_amount}", ln=True, align="L")

    if monthly_income <= 0:
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="Please enter your income and other expenses!", ln=True, align="L")
    else:

        if remaining_amount < 5000:
            save_percentage = 60
            sip_percentage = 25
            bonds_percentage = 15

            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt="Investment Recommendations:", ln=True, align="L")
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Save in a savings account upto: {remaining_amount * save_percentage / 100} Rs. ({save_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in SIP mutual funds upto: {remaining_amount * sip_percentage / 100} Rs. ({sip_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in bonds to diversify the portfolio upto: {remaining_amount * bonds_percentage / 100} Rs. ({bonds_percentage}%)", ln=True, align="L")


        elif 5000 < remaining_amount < 20000:
            direct_equities_percentage = 25
            rbi_bonds_percentage = 45
            corporate_bonds_percentage = 30

            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt="Investment Recommendations:", ln=True, align="L")
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Invest in direct equities upto: {remaining_amount * direct_equities_percentage / 100} Rs. ({direct_equities_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in RBI bonds upto: {remaining_amount * rbi_bonds_percentage / 100} Rs. ({rbi_bonds_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in corporate bonds upto: {remaining_amount * corporate_bonds_percentage / 100} Rs. ({corporate_bonds_percentage}%)", ln=True, align="L")
        
        
        elif 20000 < remaining_amount < 100000:
            fixed_deposits_percentage = 40
            gold_percentage = 30
            gold_bonds_percentage = 10

            remaining_after_gold_bonds = remaining_amount - remaining_amount * ((fixed_deposits_percentage + gold_percentage + gold_bonds_percentage) / 100)
            stocks_upper_percentage = 70
            stocks_middle_percentage = 18
            stocks_lower_percentage = 12

            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt="Investment Recommendations:", ln=True, align="L")
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Invest in fixed deposits upto: {remaining_amount * fixed_deposits_percentage / 100} Rs. ({fixed_deposits_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in gold upto: {remaining_amount * gold_percentage / 100} Rs. ({gold_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in gold bonds upto: {remaining_amount * gold_bonds_percentage / 100} Rs. ({gold_bonds_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in stocks (Upper) upto: {remaining_after_gold_bonds * stocks_upper_percentage / 100} Rs. ({stocks_upper_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in stocks (Middle) upto: {remaining_after_gold_bonds * stocks_middle_percentage / 100} Rs. ({stocks_middle_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in stocks (Lower) upto: {remaining_after_gold_bonds * stocks_lower_percentage / 100} Rs. ({stocks_lower_percentage}%)", ln=True, align="L")

        elif remaining_amount >= 100000:
            real_estate_percentage = 40
            gold_percentage = 12
            mutual_funds_percentage = 18

            remaining_after_gold_bonds = remaining_amount - remaining_amount * ((real_estate_percentage + gold_percentage + mutual_funds_percentage) / 100)
            
            direct_equities_upper_percentage = 30
            direct_equities_middle_percentage = 45
            direct_equities_lower_percentage = 25

            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt="Investment Recommendations:", ln=True, align="L")
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Invest in real state upto: {remaining_amount * real_estate_percentage / 100} Rs. ({real_estate_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in gold upto: {remaining_amount * gold_percentage / 100} Rs. ({gold_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in mutual funds upto: {remaining_amount * mutual_funds_percentage / 100} Rs. ({mutual_funds_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in direct equities (Upper) upto: {remaining_after_gold_bonds * direct_equities_upper_percentage / 100} Rs. ({direct_equities_upper_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in direct equities (Middle) upto: {remaining_after_gold_bonds * direct_equities_middle_percentage / 100} Rs. ({direct_equities_middle_percentage}%)", ln=True, align="L")
            pdf.cell(200, 10, txt=f"Invest in direct equities (Lower) upto: {remaining_after_gold_bonds * direct_equities_lower_percentage / 100} Rs. ({direct_equities_lower_percentage}%)", ln=True, align="L")
    return pdf

    

def main():
    # Center the title using CSS styling
    st.title("Monthly Income Analysis")

    # Show the input fields in a single line, half-split
    col1, col2 = st.columns(2)

    # First column with Monthly Income and Education Expenses
    with col1:
        monthly_income = st.number_input("Monthly Income", min_value=0.0, step=1000.0)
        education = st.number_input("Education Expenses", min_value=0.0, step=100.0)
        food = st.number_input("Food Expenses", min_value=0.0, step=100.0)

    # Second column with Food Expenses, Rent Expenses, and Transport Expenses
    with col2:
        rent = st.number_input("Rent Expenses", min_value=0.0, step=100.0)
        transport = st.number_input("Transport Expenses", min_value=0.0, step=100.0)
        general_expenses = st.number_input("General Expenses/Others", min_value=0.0, step=100.0)

    if st.button("Generate Report"):
        remaining_amount = calculate_remaining_income(monthly_income, education, food, rent, transport, general_expenses)
        
        report = generate_html_report(remaining_amount, monthly_income)
        html_report = f"<div>{report}</div>"
        html(html_report, height=500)
        
        pdf_report = generate_pdf_report(remaining_amount, monthly_income)
        
        with st.expander("Download Report"):
            st.write("Click the button below to download the report as a PDF file.")
            st.download_button(
                label="Download PDF Report",
                data=pdf_report.output(dest="S").encode("latin-1"),
                file_name="monthly_income_analysis_report.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
