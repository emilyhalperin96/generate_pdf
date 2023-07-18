from fpdf import FPDF 
import pandas as pd 



pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')


pdf.add_page()

pdf.set_font(family='Times', size=12)
pdf.cell(w=0, h=12, txt='Hello there', align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt='Hi there', align="L", ln=1, border=1)

pdf.add_page()

pdf.set_font(family='Times', size=12)
pdf.cell(w=0, h=12, txt='Hello there', align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt='Hi there', align="L", ln=1, border=1)

pdf.output('output.pdf')