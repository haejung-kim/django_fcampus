from django import forms
# from .models import Board/
# from django.contrib.auth.hashers import check_password


class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label="제목",
                            error_messages={'required': "제목을 입력해주세요"})
    contents = forms.CharField(widget=forms.Textarea, label="내용",
                               error_messages={'required': "내용을 입력해주세요"})
    tags = forms.CharField(label="태그",
                           required=False)

    # 주의) 모델에는 TextField있지만 form에는 Textfield하면 오류(CharField사용)

    # widget (textarea -> forms.Textarea)
