from __future__ import unicode_literals

from django.db import models


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    facebook_user_id = models.BigIntegerField(null=True)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter)

    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
