from rest_framework import serializers

from . import models


class TrySerializer(serializers.ModelSerializer):
    # user will be able to post these fields and we will collect them
    # in view.py no need of any other thing, not even models
    minCells = serializers.IntegerField()
    minGenes = serializers.IntegerField()


    class Meta:
        model = models.Try
        fields = ('checkIt','minCells','minGenes')
        # here user_profile will be an id, as it is a foreign key

        # we will make it read_only because we donot want the user to be able
        # to post feeds with other user's user_profile id
        extra_kwargs = {'checkIt' : {'read_only': True}}