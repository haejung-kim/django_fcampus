from django.db import models


class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name="등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = "패스트캠퍼스 사용자"
        verbose_name_plural = "패스트캠퍼스 사용자"

   # verbose(관리페이지에서 영어가 아니라 그 이름으로 보임 )
   #registered_dttm : dttm (datetime약자)
   # auto_now_add  (객체 저장시점의 시간이 자동으로 저장됨 )
   # DB에 table명을 지정하고 싶다면 : Class Meta 활용
