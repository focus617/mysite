from django.db import models
from django.template.defaultfilters import default
from django.conf import  settings
#from django_pandas.managers import DataFrameManager

# Create your models here.

class Classfication(models.Model):
    pass


class Author(models.Model):
    first_name = models.CharField('名', max_length=30)
    last_name = models.CharField('姓氏', max_length=40)
    email = models.EmailField('邮箱', blank=True)
    pseudonym = models.CharField('笔名', max_length=30, blank=True)
    headshot = models.ImageField('相片', upload_to='author_headshots', blank=True, null=True)
    sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女'),),default=0)

    def __str__(self):
        if self.pseudonym:
            return u'%s %s  (笔名：%s)' % (self.first_name, self.last_name, self.pseudonym)
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    # 对于使用Django自带的通用视图非常重要
    # def get_absolute_url(self):
    #     # return reverse('pic_upload:pic_detail', args=[str(self.id)])
    #     return (settings.MEDIA_URL+'author_headshots/'+str(self.id)+'.png')

    class Meta:
        ordering = ['last_name']


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state_province = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


def file_dir_path(instance, filename=None):
    # file will be uploaded to MEDIA_ROOT/books/<book.id>.txt
    return 'books/{0}.txt'.format(instance.id)


class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    book_cover = models.ImageField('封面', upload_to='books', blank=True, null=True)
    authors = models.ManyToManyField(Author)
    classfication = models.ForeignKey(Classfication, on_delete=models.SET_NULL, null=True,  blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    filepath = models.FileField(upload_to=file_dir_path, null=True)
    abstract = models.CharField('摘要', max_length= 300, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


# class Securities(models.Model):
#     code = models.CharField(max_length=16)
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.code
#
#
# class TransactionData_Day(models.Model):
#     code = models.ForeignKey(Securities)
#     date = models.DateField()
#     open = models.FloatField()
#     close = models.FloatField()
#     high = models.FloatField()
#     low = models.FloatField()
#     volume = models.FloatField()
#     adjclose = models.FloatField(default=0)
# #     ma5 = models.FloatField()
# #     v_ma5 = models.FloatField()
# #     ma10 = models.FloatField()
# #     v_ma10 = models.FloatField()
# #     ma20 = models.FloatField()
# #     v_ma20 = models.FloatField()
#
#     objects = DataFrameManager()
#
#     def __str__(self):
#         return u'%s %s' % (self.code, self.date)
#
#     class Meta:
#         ordering = ['date']

