# Created by Naman Gupta (00512693)
# Created on 12-12-2018 at 10:42
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import datetime

from reportlab.platypus import TableStyle, Table, Paragraph

now = datetime.datetime.now()
pageWidth = A4[1]
pageWidthMod = pageWidth
pageHeight = A4[0]
pageTop = 205
canvas = canvas.Canvas("TEST.pdf", pagesize=landscape(A4))
canvas.setLineWidth(.3)
canvas.setFont('Courier', 8)

consPadY = 4

def string_center_pos(string, pady):
    global pageTop
    text_width = stringWidth(string, 'Courier', 8)
    canvas.drawString(((pageWidth - text_width) / 2.0), pageTop * mm, string)
    pageTop -= pady


def string_left_pos(string, pady=9999, padx=10 * mm):
    global pageWidth, pageWidthMod, pageTop
    text_width = stringWidth(string, 'Courier', 8)
    x = pageWidth - pageWidthMod + padx / 2
    canvas.drawString(x, pageTop * mm, string)
    pageWidthMod -= (text_width + padx / 2)
    if pady != 9999:
        pageTop -= pady
        pageWidthMod = pageWidth


def string_right_pos(string, pady=9999, padx=10 * mm):
    global pageWidth, pageWidthMod, pageTop
    text_width = stringWidth(string, 'Courier', 8)
    canvas.drawString((pageWidth - text_width - padx / 2), pageTop * mm, string)
    pageWidthMod -= (text_width + padx / 2)
    if pady != 9999:
        pageTop -= pady
        pageWidthMod = pageWidth


string_center_pos("INDIAN OIL CORPORATION LIMITED", consPadY)
string_center_pos("JAYANT DEPOT", consPadY*2)
canvas.setFont('Courier-Bold', 8)
string_center_pos("ESTIMATE", consPadY)
canvas.setFont('Courier', 8)
string_left_pos("Name of work:")
string_left_pos("Internal & External repainting of building facilities at Jayant Depot")
string_right_pos("JD/OPS/M&I/Building", consPadY)
string_left_pos("Location: Jayant Depot")
string_right_pos("Dated: " + now.strftime("%d-%m-%Y"), consPadY/2)

elements = []

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Font', fontName ='Courier',fontSize=8))
styleN = styles["Font"]
styleN.alignment = TA_LEFT
styleBH = styles["Font"]
styleBH.alignment = TA_CENTER
# Headers
hdescrpcion = Paragraph('''<b>S. No.</b>''', styleBH)
hpartida = Paragraph('''<b>Description of works</b>''', styleBH)
hcandidad = Paragraph('''<b>Qty</b>''', styleBH)
hprecio_unitario = Paragraph('''<b>Unit</b>''', styleBH)
hprecio_total = Paragraph('''<b>Rate</b>''', styleBH)
hprecio_total1 = Paragraph('''<b>Amount</b>''', styleBH)

# Texts
candidad = Paragraph('Demolishing brick work manually/mechanical means including stacking of serviceable material & disposal of unserviceable material outside site at unobjectionable place & as/direction of Engineer-in-charge.', styleN)
partida = Paragraph('MPLCL021XX', styleN)
descrpcion = Paragraph('30000.00', styleN)
precio_unitario = Paragraph('kg', styleN)
precio_total = Paragraph('5631.00', styleN)
precio_total1 = Paragraph('721000.00', styleN)

data1= [[hdescrpcion, hpartida,hcandidad, hprecio_unitario, hprecio_total, hprecio_total1],
       [partida, candidad, descrpcion, precio_unitario, precio_total, precio_total1]]
t1 = Table(data1, colWidths=[25*mm, 185*mm, 20*mm, 15*mm, 17*mm, 25*mm])
t1.setStyle(TableStyle([('ALIGN', (0, -1), (-1, -1), 'CENTER'), ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black), ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
w1, h1 = t1.wrapOn(canvas, 0, 0)
t1.drawOn(canvas,(pageWidth - w1) / 2.0,pageTop*mm-h1)

# Headers
hdescrpcio = Paragraph('''<b>Sub Total</b>''', styleBH)
hpartid = Paragraph('''<b>Discount @ 27.28%</b>''', styleBH)
hcandida = Paragraph('''<b>Sub Total</b>''', styleBH)
hprecio_unitari = Paragraph('''<b>GST @ 18%</b>''', styleBH)
hprecio_tota = Paragraph('''<b>Total</b>''', styleBH)

# Texts
candida = Paragraph('1868020.00', styleN)
partid = Paragraph('509689.26', styleN)
descrpcio = Paragraph('1358330.74', styleN)
precio_unitari = Paragraph('244499.53', styleN)
precio_tota = Paragraph('1602830.00', styleN)

data2= [[hdescrpcio,candida],[hpartid,partid],[hcandida, descrpcio],[hprecio_unitari, precio_unitari],[hprecio_tota, precio_tota]]
t2 = Table(data2, colWidths=[52*mm, 25*mm])
t2.setStyle(TableStyle([('ALIGN', (0, -1), (-1, -1), 'CENTER'), ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black), ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
w2, h2 = t2.wrapOn(canvas, 0, 0)
t2.drawOn(canvas,(pageWidth + w1 - 2*w2) / 2.0,pageTop*mm-h2-h1)
temp = pageTop-h2/mm-h1/mm-consPadY
pageTop = temp
string_left_pos("Note:", consPadY)
string_left_pos("1. The estimate has been prepared as per cat-II SOR Rate contract of Jabalpur DO with contract discount of 27.285%.", consPadY)
string_left_pos("2. The estimate has been prepared based upon the additional recommendation by M&I Deptt  vide its Inspection report no. IW00068.(Annexure-I)", consPadY)
string_left_pos("3. The Job is of Revenue nature.", consPadY)
string_left_pos("4. As per engineering circular-ENG/20/276 estimates upto Rs.2 crore can be approved by Chief Managers & above.", consPadY)

# Headers
hdescrpci = Paragraph('''<b>Prepared by</b>''', styleBH)
hparti = Paragraph('''<b>Checked by</b>''', styleBH)
hcandid = Paragraph('''<b>Vetted by</b>''', styleBH)
hprecio_unitar = Paragraph('''<b>Approved by</b>''', styleBH)

# Texts
candid = Paragraph('AM (Ops-M&I)', styleN)
parti = Paragraph('Sr. Depot Manager', styleN)
descrpci = Paragraph('Manager (E)', styleN)
precio_unitar = Paragraph('(DGM(O)', styleN)

# Texts
candi = Paragraph('Jayant Depot', styleN)
part = Paragraph('Jayant Depot', styleN)
descrpc = Paragraph('MPSO', styleN)
precio_unita = Paragraph('MPSO', styleN)

data3= [[hdescrpci, hparti,hcandid, hprecio_unitar],
       [candid, parti, descrpci, precio_unitar],
       [candi, part, descrpc, precio_unita]]
t3 = Table(data3, colWidths=[50*mm, 50*mm, 50*mm, 137*mm])
t3.setStyle(TableStyle([('ALIGN', (0, -1), (-2, -1), 'CENTER'), ('VALIGN', (0, -1), (-2, -1), 'MIDDLE'),('ALIGN', (-1, -1), (-1, -1), 'RIGHT'), ('VALIGN', (-1, -1), (-1, -2), 'MIDDLE')]))
w3, h3 = t3.wrapOn(canvas, 0, 0)
t3.drawOn(canvas,(pageWidth - w3) / 2.0 , pageTop*mm-h3 - 100)

canvas.save()