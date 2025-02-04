from fpdf import FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')

pdf.set_font("Arial", size=10)
pdf.cell(30, 10, "Shop", 1)
pdf.cell(30, 10, "Date", 1)
pdf.cell(30, 10, "Amount", 1)
pdf.cell(30, 10, "Commission", 1)
pdf.cell(30, 10, "Advance", 1)
pdf.cell(30, 10, "Net Balance", 1)
pdf.cell(20, 10, "Settled", 1)
pdf.ln()