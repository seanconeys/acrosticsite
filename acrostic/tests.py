from django.test import TestCase
from .models import Adjective, Acrostic
import json

class AcrosticModelTests(TestCase):

    def test_poem_create_method_single_root(self):
        root_word = "Sean"
        acrostic = Acrostic.create(root_word=root_word)
        assert acrostic.root_word == "Sean"

    def test_poem_create_method_double_root(self):
        root_word = "Sean Coneys"
        acrostic = Acrostic.create(root_word=root_word)
        assert acrostic.root_word == "Sean Coneys"

    def test_poem_create_method_single_poem(self):
        root_word = "Sean"
        acrostic = Acrostic.create(root_word=root_word)
        poem = json.decoder.JSONDecoder().decode(acrostic.poem)
        assert len(root_word) == len(poem)

    def test_poem_create_method_double_poem(self):
        root_word = "Sean Coneys"
        acrostic = Acrostic.create(root_word=root_word)
        poem = json.decoder.JSONDecoder().decode(acrostic.poem)
        assert len(root_word) == len(poem)
         
