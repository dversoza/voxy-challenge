from django import forms


class TextForm(forms.Form):
    text_input = forms.CharField(
        label="Text Input", widget=forms.Textarea(attrs={"placeholder": "Enter text to count words"}), required=True
    )
