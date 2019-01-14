from django import forms
# creating forms here
# what ever fieds are required into form that fields define here

class StudentForm(forms.Form):
    name = forms.CharField(max_length=30)
    marks = forms.IntegerField()
