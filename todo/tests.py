from django.test import TestCase
from models import (
    TTodo,
    TDo,
)

# Create your tests here.
class TodoTest(TestCase):
    # modelについて
    def module_test(self):
        todo = TTodo()
        do = TDo()


