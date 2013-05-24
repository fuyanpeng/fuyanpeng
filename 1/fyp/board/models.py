# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Board(models.Model):
    
    name = models.CharField(max_length=64, verbose_name=_(u"姓名"))
    email = models.EmailField(blank=True, verbose_name=_(u"邮箱"))
    content = models.TextField(verbose_name=_(u"留言"))
    reply = models.TextField(blank=True, verbose_name=_(u"回复"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _(u"留言板")
        verbose_name_plural = _(u"留言板")

    def __unicode__(self):
        return u"%s--%s" % (self.name, self.email)
