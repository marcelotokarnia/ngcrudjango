from django.db import models
import jsonfield
from rest_framework import serializers
from django.core.validators import RegexValidator


class Table(models.Model):
    entries = jsonfield.JSONField()

    def to_dict_json(self):
        return {
            'entries': self.entries
        }


class Client(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15)
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def to_dict_json(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'creation': self.creation,
            'update': self.update
        }


class ClientSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=250)
    phone = serializers.CharField(required=True, max_length=15)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
        model = Client
        fields = ('pk', 'name', 'phone', 'email', )