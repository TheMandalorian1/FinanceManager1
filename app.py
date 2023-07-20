import streamlit as st
from streamlit.components.v1 import html
from fpdf import FPDF

def calculate_remaining_income(monthly_income, education, food, rent, transport, general_expenses):
    total_expenses = education + food + rent + transport + general_expenses
    remaining_income = monthly_income - total_expenses
    remaining_after_deduction = remaining_income - (0.3 * remaining_income)
    return remaining_after_deduction

def check_income_interval(remaining_amount):
    if remaining_amount < 10000:
        return "Your remaining amount is less than 10000."
    elif remaining_amount < 50000:
        return "Your remaining amount is between 10000 and 50000."
    else:
        return "Your remaining amount is above 100000."

def generate_html_report(remaining_amount, interval_result):
    report = f"<h2>Monthly Income Analysis Report</h2>"
    report += f"<p>Remaining Amount after Expenses: {remaining_amount}</p>"
    report += f"<p>{interval_result}</p>"
    return report

def generate_pdf_report(remaining_amount, interval_result):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="Monthly Income Analysis Report", ln=True)
    pdf.cell(0, 10, txt=f"Remaining Amount after Expenses: {remaining_amount}", ln=True)
    pdf.cell(0, 10, txt=interval_result, ln=True)
    return pdf

def main():
    st.title("Monthly Income Analysis")
    st.write("Enter your monthly income and expenses:")

    monthly_income = st.number_input("Monthly Income", min_value=0.0, step=1000.0)
    education = st.number_input("Education Expenses", min_value=0.0, step=100.0)
    food = st.number_input("Food Expenses", min_value=0.0, step=100.0)
    rent = st.number_input("Rent Expenses", min_value=0.0, step=100.0)
    transport = st.number_input("Transport Expenses", min_value=0.0, step=100.0)
    general_expenses = st.number_input("General Expenses/Others", min_value=0.0, step=100.0)

    if st.button("Generate Report"):
        remaining_amount = calculate_remaining_income(monthly_income, education, food, rent, transport, general_expenses)
        interval_result = check_income_interval(remaining_amount)
        
        report = generate_html_report(remaining_amount, interval_result)
        html_report = f"<div>{report}</div>"
        html(html_report, height=500)

        pdf_report = generate_pdf_report(remaining_amount, interval_result)
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
