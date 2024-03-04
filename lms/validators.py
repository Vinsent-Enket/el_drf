from rest_framework import serializers
from rest_framework.serializers import ValidationError


class URLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        word = dict(value).get(self.field)
        if word == None:
            return
        word2 = word.lower()

        if word2.startswith('http://youtube.com') or word2.startswith('http://127.0.0.1:8000'):
            pass
        else:
            raise serializers.ValidationError("The value is uncorrected")
