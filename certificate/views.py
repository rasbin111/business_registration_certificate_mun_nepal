import os
from django.http import FileResponse
from django.shortcuts import render
from docx import Document
from docx.shared import Pt
from nepali.datetime import parser, nepalidate

from certificate.forms import BusinessCertificateForm


def date_font_nepali(date_in_bs):
    np_date = nepalidate.strptime(date_in_bs, format='%Y-%m-%d')
    return np_date.strftime_ne("%Y-%m-%d")


def create_certificate(data_dict):
    current_dir = os.getcwd()
    template_path = os.path.join(current_dir, 'static', 'certificates', 'certificate_template.docx')

    word_file = Document(template_path)

    place_holders = list(data_dict.keys())

    for paragraph in word_file.paragraphs:
        for run in paragraph.runs:
            for i in range(len(place_holders)):
                if place_holders[i] in run.text:
                    run.text = run.text.replace(place_holders[i], data_dict[place_holders[i]])

    file_name = "certificate.docx"
    saving_dir = os.path.join(current_dir, 'static', 'certificates')
    word_file.save(os.path.join(saving_dir, file_name))


def home_view(request):
    form = BusinessCertificateForm()
    return render(request, 'home.html', {'form': form})
        

def generate_certificate(request):
    if request.method == "POST":
        form = BusinessCertificateForm(request.POST)
        
        if form.is_valid():
            fiscal_year = form.cleaned_data["fiscal_year"]
            certificate_date = date_font_nepali(str(form.cleaned_data["certificate_date"]))
            certificate_num = form.cleaned_data["certificate_num"]
            business_name = form.cleaned_data["business_name"]
            business_start_date = date_font_nepali(str(form.cleaned_data["business_start_date"]))
            proprietor_name = form.cleaned_data["proprietor_name"]
            father_or_husband_name = form.cleaned_data["father_or_husband_name"]
            grandfather_or_fil_name = form.cleaned_data["grandfather_or_fil_name"]
            citizenship_number = form.cleaned_data["citizenship_number"]
            citizenship_issue_date = date_font_nepali(str(form.cleaned_data["citizenship_issue_date"]))
            citizenship_issue_district = form.cleaned_data["citizenship_issue_district"]
            permanent_address = form.cleaned_data["permanent_address"]
            business_address = form.cleaned_data["business_address"]
            investment_amount = form.cleaned_data["investment_amount"]
            business_type = form.cleaned_data["business_type"]

            create_certificate({
                "fiscal_year": fiscal_year,
                "cert_date": str(certificate_date),
                "certificate_num": certificate_num,
                "business_name": business_name,
                "business_start_date": str(business_start_date),
                "proprietor_name": proprietor_name,
                "father_or_husband_name": father_or_husband_name,
                "grandparent_or_father_in_law_name": grandfather_or_fil_name,
                "citizenship_no_and_issue_date_and_district": f"{citizenship_number}, {citizenship_issue_date}, {citizenship_issue_district}",
                "permanent_address": permanent_address,
                "business_address": business_address,
                "investment_amount": investment_amount,
                "business_type": business_type
            })
            file_path = os.path.join('static', 'certificates', 'certificate.docx')
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = 'attachment; filename="certificate.docx"'
            return response
        return render(request, 'home.html', {'form': form})

    else:
        form = BusinessCertificateForm()
        return render(request, 'home.html', {'form': form})

    