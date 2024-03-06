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

        if not word2.startswith('http://youtube.com'):
            raise serializers.ValidationError("The value is uncorrected")
