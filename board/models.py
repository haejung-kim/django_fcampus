from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')  # Text길에제한없음
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                               verbose_name="작성자")
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    # Foreignkey ->  fcsuer.Fcuser(모델)을 가리킴
    # 사용자 정보가 삭제되면, 게시글도 삭제됨  (models.CASCADE)

    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name="등록시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = "패스트캠퍼스 게시글 "
        verbose_name_plural = "패스트캠퍼스 게시글"

   # verbose(관리페이지에서 영어가 아니라 그 이름으로 보임 )
   #registered_dttm : dttm (datetime약자)
   # auto_now_add  (객체 저장시점의 시간이 자동으로 저장됨 )
   # DB에 table명을 지정하고 싶다면 : Class Meta 활용
