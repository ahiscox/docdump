from django.db import models
from frontend.help.taconite import Taconite

class Topic(models.Model):
    """
        Manages various help topics.
    """

    def tac_load_page(self):
        tac = Taconite()
        tac.replace('#help #help_content', str(self.content))
        return tac

    content = models.TextField()
    slug = models.CharField(max_length=20)

