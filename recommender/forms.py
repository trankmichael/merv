from django import forms

class RatingUpload(forms.Form):
    ratings_csv = forms.FileField(
        label='Select a ratings [.csv] file',
        help_text='max. 42 megabytes'
    )

