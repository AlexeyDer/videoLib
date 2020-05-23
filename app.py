import subprocess

from fpdf import FPDF
from flask import Flask, render_template, redirect, Response
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
import os

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def main():
    return redirect("/admin")


db = SQLAlchemy(app)
from models import *


@app.route('/download/report/pdf')
def download_report():
    result = {
        'id',
        'name',
        'data',
        'film'
    }
    result = []
    for instance in db.session.query(Given).order_by(Given.id):
        result.append({
            'id': instance.id,
            'name': instance.name,
            'data': instance.data,
            'film': instance.film
        })

    pdf = FPDF()
    pdf.add_page()

    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'List of debtors', align='C')
    pdf.ln(10)

    pdf.set_font('Courier', '', 12)

    col_width = page_width / 4

    pdf.ln(1)

    th = pdf.font_size

    for row in result:
        pdf.cell(col_width - 30, th, str(row['id']), border=1)
        pdf.cell(col_width + 20, th, row['name'], border=1)
        pdf.cell(col_width, th, row['data'], border=1)
        pdf.cell(col_width, th, row['film'], border=1)
        pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Times', '', 10.0)
    pdf.cell(page_width, 0.0, '- end of report -', align='C')

    pdf.output('list_debtors.pdf', 'F')

    # subprocess.call(["xdg-open", 'list_debtors.pdf'])

    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf',
                    headers={'Content-Disposition': 'attachment;filename=list_debtors.pdf'})


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='VideoLib', template_mode='bootstrap3')

admin.add_view(UserAdmin(User, db.session))
admin.add_view(FilmInfoAdmin(FilmInfo, db.session))
admin.add_view(GivenAdmin(Given, db.session))
