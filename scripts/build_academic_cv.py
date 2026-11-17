"""Build the downloadable CV from the editable Markdown source (reportlab required)."""
from pathlib import Path
import re
from html import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import subprocess

for name, pattern in [('Helvetica', 'Liberation Sans'), ('Helvetica-Bold', 'Liberation Sans:style=Bold')]:
    font_path = subprocess.check_output(['fc-match', pattern, '-f', '%{file}'], text=True).strip()
    pdfmetrics.registerFont(TTFont(name, font_path))
pdfmetrics.registerFontFamily('Helvetica', normal='Helvetica', bold='Helvetica-Bold')

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'static/uploads/academic-cv.md'
OUTPUT = ROOT / 'static/uploads/resume.pdf'
styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=19, leading=23, alignment=TA_CENTER, spaceAfter=5),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=8.5, leading=11, alignment=TA_CENTER, spaceAfter=2),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=colors.HexColor('#15334d'), spaceBefore=10, spaceAfter=5, keepWithNext=True),
    'entry': ParagraphStyle('entry', fontName='Helvetica-Bold', fontSize=9.6, leading=12, spaceBefore=5, spaceAfter=2, keepWithNext=True),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.2, leading=12, spaceAfter=3),
    'project': ParagraphStyle('project', fontName='Helvetica', fontSize=9.2, leading=12, spaceBefore=3, spaceAfter=3, keepWithNext=True),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.2, leading=12, leftIndent=10, firstLineIndent=-7, spaceAfter=3),
}
def markup(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escape(text))

story=[]
header=True
for line in SOURCE.read_text().splitlines():
    if not line.strip():
        continue
    if line == '<!-- pagebreak -->':
        story.append(PageBreak())
        continue
    if line.startswith('# '):
        style, text = 'title', line[2:]
    elif line.startswith('## '):
        header=False
        style, text='section', line[3:]
    elif line.startswith('### '):
        style, text='entry', line[4:]
    elif line.startswith('- '):
        style, text='bullet', '- ' + line[2:]
    else:
        style='contact' if header else ('project' if line.startswith('**') and line.endswith('**') else 'body')
        text=line
    story.append(Paragraph(markup(text), styles[style]))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica',8)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawString(40,25,'Chencheng Qi')
    canvas.drawRightString(letter[0]-40,25,str(doc.page))
    canvas.restoreState()

SimpleDocTemplate(str(OUTPUT), pagesize=letter, rightMargin=40, leftMargin=40,
                  topMargin=32, bottomMargin=40, title='Chencheng Qi - Academic CV',
                  author='Chencheng Qi').build(story,onFirstPage=footer,onLaterPages=footer)
print(OUTPUT)
