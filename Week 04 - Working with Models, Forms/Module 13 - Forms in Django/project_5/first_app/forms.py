from django import forms 
from django.core import validators

# widgets == field to html input 
class contactForm(forms.Form):
    name = forms.CharField(
        label="Full Name: ",  
        help_text="Total lenght must be within 70 characters",
        required=False, 
        disabled=False,
        
        widget= forms.Textarea(attrs= {
            'id' : 'textName', 
            'class' : 'class1',
            'placeholder' : 'Enter your name', 
            })

    
    ) 


    file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)

    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
 

    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form): 
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput) 

#     way 2   
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 10:
#             raise forms.ValidationError("Name have to be minimum 10 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError('Email must contain .com')

    # way 1 
    # clean_(fieldName)

    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     print(valName) 
    #     if len(valName) < 10:
    #         raise forms.ValidationError("Name have to be minimum 10 characters") 
    #     return valName

    # def clean_email(self):
    #     valEmail = self.cleaned_data['email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("this is not an valid email") 
    #     return valEmail


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")

class StudentData(forms.Form): 
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name at least 10 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),  validators.MinValueValidator(24, message="age at least 24")]) 
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])]) 

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])


class PasswordCheck(forms.Form):
     password = forms.CharField(widget=forms.PasswordInput)
     confirm_password = forms.CharField(widget=forms.PasswordInput)
    
     def clean(self):
        cleaned_data = super().clean() 
        pass_1 = self.cleaned_data['password']
        pass_2 = self.cleaned_data['confirm_password']

        if pass_1 != pass_2:
            raise forms.ValidationError("Passwords are not same")