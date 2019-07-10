from django.db import models

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
    root_word = models.CharField(max_length=50)
    poem = []

    def __str__(self):
        return self.root_word

    def get_random_adjective(self, letter):
        word = Adjective.objects.filter(adjective__startswith=letter).order_by("?").first()
        self.poem.append(word)

    @classmethod
    def create(cls, root_word):
        acrostic = cls(root_word=root_word, poem=[])
        acrostic.save()
        for letter in root_word:
            acrostic.get_random_adjective(letter)
        acrostic.save()
        return acrostic
