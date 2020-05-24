from fpdf import FPDF
from flask import Flask, render_template, redirect, Response, request
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
import os

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def main():
    return redirect("/admin")


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        name = request.form.get('name')  # запрос к данным формы
        address = request.form.get('address')
        data = request.form.get('data')
        print(name, data, address)

        if os.path.exists("message.txt"):
            os.remove("message.txt")
        else:
            print("The file does not exist")

        f = open("message.txt", "a+")
        f.write("{:>75}".format(name) + "\n")
        f.write("{:>75}".format(address) + "\n")

        f.write("{:>50}".format("Уважаемый Иван Иванович!\n"))
        f.write(
            "Убедительно прошу Вас сообщить будете ли и впредь пользоваться\nуслугами нашей видеотеки, поскольку в последний раз Вы посещали\nнас с ")

        f.write(data + "\n")
        f.write("{:>75}".format("Заранее спасибо\n"))
        f.write("{:>75}".format("Подпись\n"))
        f.write("{:>75}".format("Дата"))

        f.close()

    return render_template('message.html')


db = SQLAlchemy(app)
from models import *


@app.route('/download/report/pdf')
def download_report():
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
        pdf.cell(col_width - 35, th, str(row['id']), border=1)
        pdf.cell(col_width + 20, th, row['name'], border=1)
        pdf.cell(col_width, th, row['data'], border=1)
        pdf.cell(col_width + 20, th, row['film'], border=1)
        pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Times', '', 10.0)
    pdf.cell(page_width, 0.0, '- end of report -', align='C')

    pdf.output('list_debtors.pdf', 'F')

    # import subprocess
    # lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    # lpr.stdin.write("list_debtors.pdf")

    # import os, tempfile
    # filename = tempfile.mkdtemp('list_debtors.pdf')
    # os.startfile(filename, 'print')
    # subprocess.call(["xdg-open", 'list_debtors.pdf'])

    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf',
                    headers={'Content-Disposition': 'attachment;filename=list_debtors.pdf'})


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='VideoLib', template_mode='bootstrap3')

admin.add_view(UserAdmin(User, db.session))
admin.add_view(FilmInfoAdmin(FilmInfo, db.session))
admin.add_view(GivenAdmin(Given, db.session))
