from django.db import models
import json
# Create your models here.

class Adjective(models.Model):
    adjective = models.CharField(max_length=50)

    @classmethod
    def create(cls, adjective):
        acrostic = cls(root_word=root_word)
        return acrostic

    def __str__(self):
        return self.adjective

class Acrostic(models.Model):
    root_word = models.TextField(max_length=50)
    poem = models.TextField(null=True)

    def __str__(self):
        return self.root_word

    def get_random_adjective(self, letter):
        word = Adjective.objects.filter(adjective__startswith=letter).order_by("?").first()
        return(word.adjective)

    @classmethod
    def create(cls, root_word):
        acrostic = cls(root_word=root_word)
        acrostic.save()
        poem = []
        for letter in root_word:
            poem.append(acrostic.get_random_adjective(letter))

        acrostic.poem = json.dumps(poem)
        acrostic.save()
        return acrostic
