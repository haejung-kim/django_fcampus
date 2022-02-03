from django.shortcuts import render, redirect
from .models import Fcuser   # fcuser생성위해 필요
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
# make_password(암호화), check_password(비밀번호 비교)


def home(request):
    # views.py만든 session 가져오기
    # user_id = request.session.get('user')

    # if user_id:
    # fcuser = Fcuser.objects.get(pk=user_id)

    return render(request, 'home.html')
    # return HttpResponse('Home')  # 로그인 안하면 Home


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')  # 로그 off후  /이동


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # 받은 POST데이터 넣고
        if form.is_valid():  # form 검증(아무것도 입력안하면 )
            request.session["user"] = form.user_id          #
            return redirect('/')
    else:
        form = LoginForm()  # 빈 instance 만들면 됨
    return render(request, 'login.html', {'form': form})
    # dict형태로 전달 (그래서 key('form), value(instance넣엇 전달))


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # name값 연동 필요
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data = {}  # error메세지 담을 변수

        if not (username and password and re_password and useremail):
            res_data['error'] = "모든값을 입력해야 합니다 "
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:  # else일때 저장
            # 가지고 온 값으로 fcuser생성 필요
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            # 저장 필요
            fcuser.save()

        return render(request, 'register.html', res_data)  # dict(res_data)전달
