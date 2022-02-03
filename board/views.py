from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from fcuser.models import Fcuser  # session위해
from django.http import Http404
from django.core.paginator import Paginator
from tag.models import Tag


def board_detail(request, pk):  # pk
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')

    return render(request, 'board_detail.html', {"board": board})


def board_write(request):
    # method 확인전 사용자 확인
    if not request.session.get("user"):
        return redirect('/fcuser/login/')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():

            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            tags = form.cleaned_data["tags"].split(',')  # list만듬
            board = Board()  # model instance 생성
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser  # session 값 넣기
            board.save()
            # 위에서 ID 생성이 먼저필요 saveㅁㄴ저함
            for tag in tags:
                # 있으면 가져오고, 없으면 생성 (get_or_create)
                if not tag:
                    continue
                # 2개반환 앞인자(생성된 class객체), 뒤인자(새로 생성된지 아닌지여부)
                _tag, created = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')  # 다가져오고 (id역순정렬 -
    page = int(request.GET.get('p', 1))  # page번호를 (p변수로) GET방식으로 받기 , get없으면 1
    paginator = Paginator(all_boards, 3)  # 2개씩 나오게

    boards = paginator.get_page(page)
    return render(request, "board_list.html", {'boards': boards})
