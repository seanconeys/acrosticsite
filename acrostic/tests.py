from django.test import TestCase
from django.test.utils import setup_test_environment
from django.urls import reverse
from .models import Adjective, Acrostic
import json
import sys

class AcrosticModelTests(TestCase):
    fixtures = ['initial_data']

    def test_get_random_adj(self):
        acrostic = Acrostic()
        word = acrostic.get_random_adjective("a")
        assert isinstance(word, str) == True
        assert word[0] == 'A'

    def test_poem_create_method_root(self):
        root_word = "Sean"
        acrostic = Acrostic.create(root_word=root_word)
        assert acrostic.root_word == "Sean"

    def test_poem_create_method_with_space_root(self):
        root_word = "Sean Coneys"
        acrostic = Acrostic.create(root_word=root_word)
        assert acrostic.root_word == "Sean Coneys"

    def test_poem_create_method_poem(self):
        root_word = "Sean"
        acrostic = Acrostic.create(root_word=root_word)
        poem = json.decoder.JSONDecoder().decode(acrostic.poem)
        assert len(root_word) == len(poem)

    def test_poem_create_method_with_space_poem(self):
        root_word = "Sean Coneys"
        acrostic = Acrostic.create(root_word=root_word)
        poem = json.decoder.JSONDecoder().decode(acrostic.poem)
        assert len(root_word) == len(poem)

    def test_poem_create_pk_load_root(self):
        root_word = "Sean"
        acrostic = Acrostic.create(root_word=root_word)

        key = acrostic.id
        loaded_acrostic = Acrostic.objects.get(pk=key)

        assert acrostic.root_word == root_word == loaded_acrostic.root_word


    def test_poem_create_pk_load_poem(self):
        root_word = "Sean"
        acrostic = Acrostic.create(root_word=root_word)

        key = acrostic.id
        loaded_acrostic = Acrostic.objects.get(pk=key)

        poem = json.decoder.JSONDecoder().decode(acrostic.poem)
        loaded_poem = json.decoder.JSONDecoder().decode(loaded_acrostic.poem)
        assert poem == loaded_poem

    def test_poem_create_pk_load_with_space_root(self):
        root_word = "Sean Coneys"
        acrostic = Acrostic.create(root_word=root_word)
        key = acrostic.id
        loaded_acrostic = Acrostic.objects.get(pk=key)

        assert acrostic.root_word == root_word == loaded_acrostic.root_word

    def test_poem_create_pk_load_with_space_poem(self):
        root_word = "Sean Coneys"
        acrostic = Acrostic.create(root_word=root_word)

        key = acrostic.id
        loaded_acrostic = Acrostic.objects.get(pk=key)

        poem = json.decoder.JSONDecoder().decode(acrostic.poem)
        loaded_poem = json.decoder.JSONDecoder().decode(loaded_acrostic.poem)
        assert poem == loaded_poem

class IndexViewTests(TestCase):

    def test_load(self):
        response = self.client.get(reverse('acrostic:index'))
        self.assertEqual(response.status_code, 200)



class CreateViewTests(TestCase):
    fixtures = ['initial_data']

    def test_load(self):
        root_word = "Sean"
        response = self.client.post(reverse('acrostic:create'), {'Root Word': root_word}, follow=True)
        self.assertRedirects(response, reverse('acrostic:poem', args=(1,)))

    def test_load_with_special_chars(self):
        root_word = "$ean"
        response = self.client.post(reverse('acrostic:create'), {'Root Word': root_word})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No numbers or special characters are allowed")

    def test_load_with_space(self):
        root_word = "Sean Coneys"
        response = self.client.post(reverse('acrostic:create'), {'Root Word': root_word}, follow=True)
        self.assertRedirects(response, reverse('acrostic:poem', args=(1,)))


class PoemViewTests(TestCase):
    fixtures = ['initial_data']

    def test_load(self):
        root_word = "Sean"
        self.client.post(reverse('acrostic:create'), {'Root Word': root_word})
        response = self.client.get(reverse('acrostic:poem', args=(1,)))
        self.assertEqual(response.status_code, 200)
