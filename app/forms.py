from django import forms


from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class DisplayQuestionsForm(forms.ModelForm):
    class Meta:
        model = DisplayQuestions
        fields = ['title', 'description']
        widgets={'address':forms.Textarea()}

class DisplayAnswersForm(forms.ModelForm):
    class Meta:
        model = DisplayAnswers
        fields = ['question','description']
        widgets={'address':forms.Textarea()}