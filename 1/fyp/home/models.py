# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Links(models.Model):
    name = models.CharField(max_length=128, verbose_name=_(u'名称'))
    logo = models.ImageField(null=True, blank=True, upload_to="links", verbose_name=_(u'标识'))
    url = models.URLField(verbose_name=_(u"链接"))
    is_partner = models.BooleanField(default=False, verbose_name=_(u"合作伙伴"))

    class Meta:
        verbose_name = _(u"友情链接")
        verbose_name_plural = _(u"友情链接")
    
    def __unicode__(self):
        return self.name

    
