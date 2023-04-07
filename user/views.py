from django.shortcuts import render,redirect
# render : views.py에서 수정한 html을 사용자에게 출력하기 위한 메소드
# redirect : 사용자에게 새로운 경로, url 을 안내하기 위한 메소드
from django.contrib.auth import get_user_model
#사용자가 데이터 베이스 안에 있는지 검사하는 함수
from django.contrib import auth
#Django의 인증 기능을 제공하는 헤더파일
from django.contrib.auth.decorators import login_required


from .models import UserModel
# user app에서 작성한 클래스 UserModel을 import

def sign_up(request):
    # form으로 데이터가 전송될때, 매개변수로 전달이 된다.
    # 변수 이름은 request로 지정하는것이 전통.

    user = request.user.is_authenticated
    # Django에 내장된 보안기능을 사용한다.
    # is_authenticated는 사용자가 로그인 했는지, 로그인 하지 않았는지 판별하며, 로그인을 했다면 True, 로그인 하지 않았다면 False를 반환한다.
    if request.method == 'GET':
        #데이터의 전달 방식이 GET방식이라면, 즉 사용자가 회원가입 페이지에 접속한다면 어떻게 처리할것인지 처리한다.

        if not user: #로그인을 하지 않았다면(Not False)
            return render(request, 'user/signup.html')

        #로그인을 했다면 사용자가 요청한 이전의 경로로 되돌아간다.
        return redirect('/')

    elif request.method == 'POST':
        #sign_up 함수를 POST방식으로 접근할때, 즉 어떤 데이터를 전송했을때 동작한다.

        #post형식으로 전달된 데이터를 저장하고
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        password2 = request.POST.get('confirm_password', '')

        #비밀번호 확인 절차가 올바른지 확인한다.
        if password2 != password:
            return render(request,'user/signup.html',{"error":"비밀번호를 확인해주세요."})

        # 이름이 빈 문자열일 경우
        if not username:
            return render(request,'user/signup.html',{"error":"이름을 입력해주세요."})

        exist_user = get_user_model().objects.filter(username=username)
        # filter를 통해, 똑같은 이름을 검색해서, 있다면 변수에 담는다.
        if exist_user:
            # 빈 문자열을 거짓을 반환하기에 조건문으로 사용 할 수 있다.
            return render(request, 'user/signup.html', {'error': '동일한 사용자가 존재합니다.'})
        else:
            #데이터베이스에 ORM형태로 저장한다, 이름과 비밀번호
            UserModel.objects.create_user(
                username=username, password=password
            )
            # 로그인 페이지로 이동
            return redirect('sign-in')


def sign_in(request):
    if request.method == 'POST':
        #POST방식으로 받은 데이터를 변수에 저장, 디폴트 값은 ''
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        me = auth.authenticate(request,username = username,password=password)
        # UserModel 클래스의 필드 username에, POST방식으로 저장한 username의 값이 있는지 확인한다.

        if me is not None:
            auth.login(request,me)
            return redirect('/')
        else:# 로그인에 실패할 경우 (비밀번호가 틀리거나 등등)
            return render(request,'user/signin.html',{'error':'아이디와 비밀번호를 확인 해 주세요.'})

        #로그인 성공 출력
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else :
            return render(request, 'user/signin.html')
        #GET이라면 화면에 HTML 출력

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')