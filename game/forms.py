from django import forms

from .models import Player


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nickname']

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if len(nickname) <=2:
            raise forms.ValidationError("Nickname을 2자 이상으로 입력해 주십시오.")
        return nickname

        
