from django import forms

from users.models import User


class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(
            attrs={'id': 'file-input',
                   'accept': 'image/*',
                   'onchange': 'preview_image(event)'}), 
            required=False)


    class Meta:
        model = User
        fields = ['profile_picture']

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        if commit:
            user.save()
        return user