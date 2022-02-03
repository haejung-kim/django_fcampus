from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름",
                               error_messages={'required': "아이디를 입력해주세요"})
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호",
                               error_messages={'required': "비밀번호 입력해주세요"})

    def clean(self):
        cleaned_data = super().clean()  # super() 해당 클래스의 부모 class 호출
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:  # id/pw입력했을때
            # 예외처리(해당 ID 없는 계정으로 login시)
            try:
                fcuser = Fcuser.objects.get(username=username)

            except Fcuser.DoesNotExist:
                self.add_error("username", 'ID가 없습니다')
                return  # 이ㄸ는 더 체크하면 안되니 return

            # 예외처리(패스워드 체크)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
                # 특정필드에 에러넣는 함수
            else:
                self.user_id = fcuser.id   # sessiog key위해 여기에 이것사용
