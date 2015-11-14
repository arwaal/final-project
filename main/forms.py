from django import forms 
from main.models import Users, Recommendation, BusinessSubmission, Category, Comment
from django.contrib.auth.models import User

from django.core import exceptions
from django.core.validators import RegexValidator

from django.core import exceptions
from django.utils.six.moves.urllib.parse import urlsplit, urlunsplit
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

import re

from django.core.exceptions import ValidationError

class KuwaitMobileField(forms.Field):
    def validate(self, value):
        if value != "":
            kuwait_mobile = re.compile('^(9|6|5)(\d{7})$')
            kuwait_mobile_match = kuwait_mobile.match(value)
            if kuwait_mobile_match == None:
                raise exceptions.ValidationError(_('Invalid Number: %(value)s'),
                    code='invalid',
                    params={'value': 'Please enter a Kuwaiti Mobile number'},
                )
            else:
                return value
        else:
            return value
        # else:
        #     raise exceptions.ValidationError(_('Invalid Number: %(value)s'),
        #             code='invalid',
        #             params={'value': 'Please enter a Kuwaiti Mobile number'},
        #         )    


class KuwaitLandPhoneField(forms.Field):
    def validate(self, value):
        print '%s the value of land phone' % value
        if value != "":
            kuwait_phone = re.compile('^(2)(\d{7})$')
            kuwait_phone_match = kuwait_phone.match(value)
            if kuwait_phone_match == None:
                raise exceptions.ValidationError(_('Invalid Phone: %(value)s'), 
                    code= 'invalid',
                    params={'value': 'Please enter a Kuwaiti Land number'},
                )
            else:
                return value
        else:
            return value
        # else:
        #     raise exceptions.ValidationError(_('Invalid Phone: %(value)s'),
        #         code='invalid',
        #         params={'value': "Please enter a Kuwaiti Land Number"},
        #         )

class UserSignUp(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(max_length=255, required=True)
    confirm_email = forms.EmailField(max_length=255, required=True)
    
    def clean(self):
        if (self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
            raise ValidationError('Email addresses do not match')
        return self.cleaned_data
    # terms_of_use=forms.CharField(widget=CheckboxInput(), required=True)


class BusinessSignUp(forms.Form):
    business_name = forms.CharField(max_length=255, required=True)
    company = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=250, required=True)
    confirm_email = forms.EmailField(max_length=250, required=True)

    def clean(self):
        if (self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
            raise ValidationError('Email addresses do not match')
        return self.cleaned_data

    mobile=KuwaitMobileField(help_text='Please enter a valid Kuwaiti mobile number', required=False)
    phone=KuwaitLandPhoneField(help_text='Please enter a Kuwaiti land phone number', required=False)
    password=forms.CharField(widget=forms.PasswordInput(), required=True)
    # terms_of_use=forms.CharField(widget=CheckboxInput(), required=True)


class BusinessSubmissionForm(forms.Form):
    business_user = forms.CharField(widget=forms.HiddenInput(), max_length=255, required=True)
    image1 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=True, help_text='You Must Upload atleast One picture and Max. ten')
    image2 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image3 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image4 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image5 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image6 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image7 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image8 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image9 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    image10 = forms.FileField(widget=forms.FileInput(attrs={'class': 'image_input'}), required=False)
    mobile = forms.CharField(max_length=255, required=False)
    address = forms.CharField(widget=forms.TextInput(), max_length=255, required=True)
    email = forms.EmailField(max_length=250, required=True)
    category = forms.CharField(required=False)
    info = forms.CharField(max_length=255, widget=forms.Textarea())
    longitude = forms.FloatField(required=False)
    latitude = forms.FloatField(required=False)


class UserLogin(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class BusinessLogin(forms.Form):
    business_name = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class Comments(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(), required=False)
    class Meta:
        model = Comment
        fields = ('reply', 'recomendation')











