from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):
    
    title = models.CharField(
        max_length=150,
    )
    slug = models.CharField(
        max_length=150,
        unique=True,
    )
    writer = models.ForeignKey(
        'myuser.MyUser',
    )
    content = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now,
    )
    class Meta:
        db_table = 'course'
        verbose_name = _('course')
        verbose_name_plural = _('courses')
    def __unicode__(self):
        return self.title
