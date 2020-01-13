from django.db import models

# Create your models here.

class Direaction(models.Model):
    name=models.CharField(max_length=32,verbose_name='名称')
    classfication=models.ManyToManyField('Classfication',verbose_name='分类')

    class Meta:
        verbose_name=verbose_name_plural='方向'

    def __str__(self):
        return self.name

class Classfication(models.Model):
    name=models.CharField(max_length=32,verbose_name='名称')

    class Meta:
        verbose_name=verbose_name_plural='分类'

    def __str__(self):
        return self.name

class Level(models.Model):
    name=models.CharField(max_length=32,verbose_name='名称')

    class Meta:
        verbose_name = verbose_name_plural = '级别'

    def __str__(self):
        return self.name


class Video(models.Model):
    STATUS_ITEM=(
        (0,'下线'),
        (1,'上线'),
    )
    status=models.IntegerField(choices=STATUS_ITEM,verbose_name='状态',default=1)
    title=models.CharField(max_length=64,verbose_name='标题')
    desc=models.CharField(max_length=128,verbose_name='简介')
    direaction=models.ForeignKey('Direaction',verbose_name='方向')
    classfication=models.ForeignKey('Classfication',verbose_name='分类')
    level=models.ForeignKey('Level',verbose_name='级别')
    weight=models.IntegerField(default=0,help_text='权重按照从大到小排列',verbose_name='权重（从大到小排列）')
    img=models.ImageField(upload_to='img',verbose_name='图片',null=True,blank=True)
    href=models.URLField(verbose_name='视频地址')

    class Meta:
        verbose_name= verbose_name_plural='视频'

    def __str__(self):
        return self.title




