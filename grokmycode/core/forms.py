from django import forms


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField()
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['message'] = forms.CharField(widget=forms.Textarea)
        self.fields['message'].widget.attrs['placeholder'] = 'Message...'
        self.fields['message'].widget.attrs['required'] = 'required'
