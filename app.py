import streamlit as st
from streamlit.components.v1 import html
from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

    if remaining_amount < 5000:
        save_percentage = 60
        sip_percentage = 25
        bonds_percentage = 15
        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Save in a savings account: {remaining_amount * save_percentage / 100} ({save_percentage}%)</li>"
        report += f"<li>Invest in SIP mutual funds: {remaining_amount * sip_percentage / 100} ({sip_percentage}%)</li>"
        report += f"<li>Invest in bonds to diversify the portfolio: {remaining_amount * bonds_percentage / 100} ({bonds_percentage}%)</li>"
        report += "</ul>"

    elif 5000 < remaining_amount < 20000:
        direct_equities_percentage = 25
        rbi_bonds_percentage = 45
        corporate_bonds_percentage = 30
        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Invest in direct equities: {remaining_amount * direct_equities_percentage / 100} ({direct_equities_percentage}%)</li>"
        report += f"<li>Invest in RBI bonds: {remaining_amount * rbi_bonds_percentage / 100} ({rbi_bonds_percentage}%)</li>"
        report += f"<li>Invest in corporate bonds: {remaining_amount * corporate_bonds_percentage / 100} ({corporate_bonds_percentage}%)</li>"
        report += "</ul>"

    elif 20000 < remaining_amount < 100000:
        fixed_deposits_percentage = 40
        gold_percentage = 30
        gold_bonds_percentage = 10
        
        stocks_upper_percentage = 70
        stocks_middle_percentage = 18
        stocks_lower_percentage = 12

        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Invest in fixed deposits: {remaining_amount * fixed_deposits_percentage / 100} ({fixed_deposits_percentage}%)</li>"
        report += f"<li>Invest in gold: {remaining_amount * gold_percentage / 100} ({gold_percentage}%)</li>"
        report += f"<li>Invest in gold bonds: {remaining_amount * gold_bonds_percentage / 100} ({gold_bonds_percentage}%)</li>"
        report += f"<li>Invest in stocks (Upper): {remaining_amount * stocks_upper_percentage / 100} ({stocks_upper_percentage}%)</li>"
        report += f"<li>Invest in stocks (Middle): {remaining_amount * stocks_middle_percentage / 100} ({stocks_middle_percentage}%)</li>"
        report += f"<li>Invest in stocks (Lower): {remaining_amount * stocks_lower_percentage / 100} ({stocks_lower_percentage}%)</li>"
        report += "</ul>"

    elif remaining_amount >= 100000:
        real_estate_percentage = 40
        gold_percentage = 12
        mutual_funds_percentage = 18
        direct_equities_upper_percentage = 30
        direct_equities_middle_percentage = 45
        direct_equities_lower_percentage = 25

        report += "<h3>Investment Recommendations:</h3>"
        report += f"<ul>"
        report += f"<li>Invest in real estate: {remaining_amount * real_estate_percentage / 100} ({real_estate_percentage}%)</li>"
        report += f"<li>Invest in gold: {remaining_amount * gold_percentage / 100} ({gold_percentage}%)</li>"
        report += f"<li>Invest in mutual funds: {remaining_amount * mutual_funds_percentage / 100} ({mutual_funds_percentage}%)</li>"
        report += f"<li>Invest in direct equities (Upper): {remaining_amount * direct_equities_upper_percentage / 100} ({direct_equities_upper_percentage}%)</li>"
        report += f"<li>Invest in direct equities (Middle): {remaining_amount * direct_equities_middle_percentage / 100} ({direct_equities_middle_percentage}%)</li>"
        report += f"<li>Invest in direct equities (Lower): {remaining_amount * direct_equities_lower_percentage / 100} ({direct_equities_lower_percentage}%)</li>"
        report += "</ul>"

    report += "</body>"
    report += "</html>"
    return report


def generate_pdf_report(remaining_amount, monthly_income):
    # Set up the canvas for the PDF document
    pdf_file = "MIA_Report.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # Add content to the PDF document
    c.setFont("Helvetica", 16)
    c.drawString(100, height - 100, "Monthly Income Analysis Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, f"Remaining Amount after Expenses: {remaining_amount}")

    if monthly_income <= 0:
        c.setFont("Helvetica", 14)
        c.drawString(100, height - 200, "Please enter your income and other expenses!")
    else:
        if remaining_amount < 5000:
            save_percentage = 60
            sip_percentage = 25
            bonds_percentage = 15

            c.setFont("Helvetica", 14)
            c.drawString(100, height - 200, "Investment Recommendations:")
            c.setFont("Helvetica", 12)
            c.drawString(120, height - 230, f"Save in a savings account: {remaining_amount * save_percentage / 100} ({save_percentage}%)")
            c.drawString(120, height - 250, f"Invest in SIP mutual funds: {remaining_amount * sip_percentage / 100} ({sip_percentage}%)")
            c.drawString(120, height - 270, f"Invest in bonds to diversify the portfolio: {remaining_amount * bonds_percentage / 100} ({bonds_percentage}%)")

        elif 5000 < remaining_amount < 20000:
            direct_equities_percentage = 25
            rbi_bonds_percentage = 45
            corporate_bonds_percentage = 30
        
            c.setFont("Helvetica", 14)
            c.drawString(100, height - 200, "Investment Recommendations:")
            c.setFont("Helvetica", 12)
            c.drawString(120, height - 230, f"Invest in direct equities: {remaining_amount * direct_equities_percentage / 100} ({direct_equities_percentage}%)")
            c.drawString(120, height - 250, f"Invest in RBI bonds: {remaining_amount * rbi_bonds_percentage / 100} ({rbi_bonds_percentage}%)")
            c.drawString(120, height - 270, f"Invest in corporate bonds: {remaining_amount * corporate_bonds_percentage / 100} ({corporate_bonds_percentage}%)")
        
        
        elif 20000 < remaining_amount < 100000:
            fixed_deposits_percentage = 40
            gold_percentage = 30
            gold_bonds_percentage = 10

            remaining_after_gold_bonds = remaining_amount - remaining_amount * ((fixed_deposits_percentage + gold_percentage + gold_bonds_percentage) / 100)
            stocks_upper_percentage = 70
            stocks_middle_percentage = 18
            stocks_lower_percentage = 12
        
            c.setFont("Helvetica", 14)
            c.drawString(100, height - 200, "Investment Recommendations:")
            c.setFont("Helvetica", 12)
            c.drawString(120, height - 230, f"Invest in fixed deposits: {remaining_amount * fixed_deposits_percentage / 100} ({fixed_deposits_percentage}%)")
            c.drawString(120, height - 250, f"Invest in gold: {remaining_after_fixed_deposits * gold_percentage / 100} ({gold_percentage}%)")
            c.drawString(120, height - 270, f"Invest in gold bonds: {remaining_after_gold * gold_bonds_percentage / 100} ({gold_bonds_percentage}%)")
            c.drawString(120, height - 290, f"Invest in stocks (Upper): {remaining_after_gold_bonds * stocks_upper_percentage / 100} ({stocks_upper_percentage}%)")
            c.drawString(120, height - 310, f"Invest in stocks (Middle): {remaining_after_gold_bonds * stocks_middle_percentage / 100} ({stocks_middle_percentage}%)")
            c.drawString(120, height - 330, f"Invest in stocks (Lower): {remaining_after_gold_bonds * stocks_lower_percentage / 100} ({stocks_lower_percentage}%)")
        
        elif remaining_amount >= 100000:
            fixed_deposits_percentage = 40
            gold_percentage = 12
            mutual_funds_percentage = 18

            remaining_after_gold_bonds = remaining_amount - remaining_amount * ((fixed_deposits_percentage + gold_percentage + gold_bonds_percentage) / 100)
            direct_equities_upper_percentage = 30
            direct_equities_middle_percentage = 45
            direct_equities_lower_percentage = 25
        
            c.setFont("Helvetica", 14)
            c.drawString(100, height - 200, "Investment Recommendations:")
            c.setFont("Helvetica", 12)
            c.drawString(120, height - 230, f"Invest in fixed deposits: {remaining_amount * fixed_deposits_percentage / 100} ({fixed_deposits_percentage}%)")
            c.drawString(120, height - 250, f"Invest in gold: {remaining_after_fixed_deposits * gold_percentage / 100} ({gold_percentage}%)")
            c.drawString(120, height - 270, f"Invest in mutual funds: {remaining_after_gold * mutual_funds_percentage / 100} ({mutual_funds_percentage}%)")
            c.drawString(120, height - 290, f"Invest in direct equities (Upper): {remaining_after_mutual_funds * direct_equities_upper_percentage / 100} ({direct_equities_upper_percentage}%)")
            c.drawString(120, height - 310, f"Invest in direct equities (Middle): {remaining_after_mutual_funds * direct_equities_middle_percentage / 100} ({direct_equities_middle_percentage}%)")
            c.drawString(120, height - 330, f"Invest in direct equities (Lower): {remaining_after_mutual_funds * direct_equities_lower_percentage / 100} ({direct_equities_lower_percentage}%)")


    # Save and close the PDF document
    c.save()
    return pdf_file

    

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
        st.write(html_report, unsafe_allow_html=True)

        pdf_report_data = generate_pdf_report(remaining_amount, monthly_income)

        with st.expander("Download Report"):
            # Provide the option to download the report as a PDF
            st.write("Click the button below to download the report as a PDF file.")
            st.download_button(
                label="Download PDF Report",
                data=pdf_report_data,
                file_name="MIA_Report.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
