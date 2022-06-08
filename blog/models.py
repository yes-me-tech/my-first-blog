from django.conf import settings            #他のファイルから必要な行のみを追加
from django.db import models
from django.utils import timezone



class Post(models.Model):                   #Object モデルの定義.名前は大文字から付ける.ポストがDjango Modelという意味.データベースに保存
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)      #プロパティ
    title = models.CharField(max_length=200)        #文字数が制限されたテキストを定義する
    text = models.TextField()                       #制限なしの長いテキスト
    created_date = models.DateTimeField(default=timezone.now)        #日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)    #他のモデルへのリンク


    def publish(self):      #method  英小文字とアンダーバーのみしか名前に使えない
        self.published_date = timezone.now()
        self.save()

    def __str__(self):      #method  戻り値ポストのタイトルのテキスト(string)が返ってくる
        return self.title