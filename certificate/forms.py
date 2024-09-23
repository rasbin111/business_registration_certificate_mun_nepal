from django import forms
from nepali_datetime import date

from nepali_datetime_field.forms import NepaliDateField

class BusinessCertificateForm(forms.Form):
    fiscal_year = forms.CharField(max_length=10, initial="०८१्/०८२", label="आ. व.")
    certificate_date = NepaliDateField(initial=date.today, 
                                          label="मिति")
    certificate_num = forms.CharField(max_length=10, required=True, label="प्रमाण पत्र नं")
    business_name = forms.CharField(max_length=100, required=True, label="व्यापार व्यवसायको नाम")
    business_start_date = NepaliDateField(initial=date.today, 
                                          label="व्यवसाय सुरु गरेको मिति")
    proprietor_name = forms.CharField(max_length=100, required=True, label="प्रोपाइटरको नाम")
    father_or_husband_name = forms.CharField(max_length=100, required=True, label="पिता / पतिको नाम")
    grandfather_or_fil_name = forms.CharField(max_length=100, required=True, label="बाजे / ससुराको नाम")
    citizenship_number = forms.CharField(max_length=20, required=True, label="नागरिकता नं.")
    citizenship_issue_date = NepaliDateField(initial=date.today, required=True, label="जारी मिति")
    citizenship_issue_district = forms.CharField(max_length=50, required=True, label="जारी जिल्ला")
    permanent_address = forms.CharField(max_length=100, required=True, label="स्थायी ठेगाना")
    business_address = forms.CharField(max_length=100, required=True, label="व्यवसाय सञ्चालनमा रहेको ठेगाना")
    investment_amount = forms.CharField(max_length=10, label="व्यवसायमा लगानी गरेको पुँजी रकम")
    business_type = forms.CharField(max_length=50, required=True, label="व्यवसायको किसिम")
