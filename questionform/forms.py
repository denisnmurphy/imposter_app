from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from . models import QuestionOne, QuestionTwo, QuestionThree


class QuestionOneForm(forms.ModelForm):

    class Meta:
        model = QuestionOne
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(

        'text',
        Submit('submit', 'Submit', css_class='btn-success'),

        )


class QuestionTwoForm(forms.ModelForm):

    class Meta:
        model = QuestionTwo
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(

        'text',
        Submit('submit', 'Submit', css_class='btn-success')

        )


class QuestionThreeForm(forms.ModelForm):

    class Meta:
        model = QuestionThree
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(

        'text',
        Submit('submit', 'Submit', css_class='btn-success')

        )
